# Prova diversi argomenti di avvio del client e registra cosa compare (titoli e testi delle finestre).
# Chiude solo i processi avviati da questo script.
param([int]$Secondi = 10)
$root = Resolve-Path "$PSScriptRoot\..\_local\client"
$exe  = Join-Path $root 'bin64\archeage.exe'
$prove = @(
  '-y',
  '-y -locale en_us -instant_token ponticheage-test',
  '-y -locale ko -instant_token ponticheage-test',
  '-y -locale ko_kr -instant_token ponticheage-test',
  '-StrUserName ponte -strUserToken test -serverId 1 -sIp 127.0.0.1 -sPort 1237 -gameId 1',
  '-t +auth_ip 127.0.0.1 +auth_port 1237 -lang en_us'
)
Add-Type @"
using System; using System.Text; using System.Runtime.InteropServices; using System.Collections.Generic;
public static class W {
  public delegate bool P(IntPtr h, IntPtr l);
  [DllImport("user32")] public static extern bool EnumWindows(P p, IntPtr l);
  [DllImport("user32")] public static extern bool EnumChildWindows(IntPtr h, P p, IntPtr l);
  [DllImport("user32")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32", CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr h, StringBuilder s, int n);
  public static List<string> Of(HashSet<uint> pids) {
    var r = new List<string>();
    EnumWindows((h, l) => { uint p; GetWindowThreadProcessId(h, out p);
      if (pids.Contains(p)) { var t = new StringBuilder(512); var c = new StringBuilder(256);
        GetWindowText(h, t, 512); GetClassName(h, c, 256); string line = c + " | " + t;
        EnumChildWindows(h, (k, m) => { var u = new StringBuilder(512); GetWindowText(k, u, 512); if (u.Length > 0) line += " || " + u; return true; }, IntPtr.Zero);
        r.Add(line); }
      return true; }, IntPtr.Zero);
    return r; } }
"@
foreach ($a in $prove) {
  $p = Start-Process -FilePath $exe -ArgumentList $a -WorkingDirectory $root -PassThru
  Start-Sleep -Seconds $Secondi
  $pids = New-Object 'System.Collections.Generic.HashSet[uint32]'
  [void]$pids.Add([uint32]$p.Id)
  Get-CimInstance Win32_Process | Where-Object { $_.ParentProcessId -eq $p.Id } | ForEach-Object { [void]$pids.Add([uint32]$_.ProcessId) }
  $figli = (Get-CimInstance Win32_Process | Where-Object { $pids.Contains([uint32]$_.ProcessId) } | ForEach-Object { $_.Name }) -join ', '
  $fin = [W]::Of($pids) -join ' ;; '
  "ARGOMENTI: $a"
  "  vivo: $(-not $p.HasExited)  processi: $figli"
  "  finestre: $fin"
  foreach ($id in $pids) { Stop-Process -Id $id -Force -ErrorAction SilentlyContinue }
  Start-Sleep -Seconds 2
}
