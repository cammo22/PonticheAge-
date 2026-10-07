# Elenca i file del game_pak (formato pak ArcheAge: intestazione "WIBO" cifrata AES-128-CBC in coda al file,
# tabella dei file (FAT) cifrata subito prima, una voce da 0x150 byte cifrata a se' con IV zero).
# Scrive un TSV: nome, offset, dimensione.  Uso: powershell -File tools\pak\pak_list.ps1 [-Pak ...] [-Out ...]
param(
  [string]$Pak = "$PSScriptRoot\..\..\_local\client\game_pak",
  [string]$Out = "$PSScriptRoot\..\..\_local\re\out\game_pak.files.tsv"
)
Add-Type -TypeDefinition @"
using System; using System.IO; using System.Text; using System.Security.Cryptography;
public static class AAPak {
  static readonly byte[] Key = {0x32,0x1F,0x2A,0xEE,0xAA,0x58,0x4A,0xB4,0x9A,0x6C,0x9E,0x09,0xD5,0x9E,0x9C,0x6F};
  static byte[] Dec(byte[] d, int off, int len) {
    using (var a = Aes.Create()) { a.Key = Key; a.IV = new byte[16]; a.Mode = CipherMode.CBC; a.Padding = PaddingMode.None;
      return a.CreateDecryptor().TransformFinalBlock(d, off, len); } }
  public static string List(string pak, string outTsv) {
    using (var fs = File.OpenRead(pak)) {
      long len = fs.Length; var hdr = new byte[32]; fs.Seek(len - 512, SeekOrigin.Begin); fs.Read(hdr, 0, 32);
      var h = Dec(hdr, 0, 32);
      if (Encoding.ASCII.GetString(h, 0, 4) != "WIBO") throw new Exception("intestazione non riconosciuta");
      uint files = BitConverter.ToUInt32(h, 8), extra = BitConverter.ToUInt32(h, 12);
      const int E = 0x150; long fatSize = (long)(files + extra) * E; long fatAligned = (fatSize + 511) / 512 * 512;
      fs.Seek(len - 512 - fatAligned, SeekOrigin.Begin);
      var entry = new byte[E];
      using (var w = new StreamWriter(outTsv, false, new UTF8Encoding(false))) {
        w.WriteLine("nome\toffset\tdimensione");
        for (uint i = 0; i < files; i++) {
          fs.Read(entry, 0, E); var p = Dec(entry, 0, E);
          int n = 0; while (n < 0x108 && p[n] != 0) n++;
          w.WriteLine(Encoding.UTF8.GetString(p, 0, n) + "\t" + BitConverter.ToInt64(p, 0x108) + "\t" + BitConverter.ToInt64(p, 0x110));
        }
      }
      return "file: " + files + "  extra: " + extra + "  FAT a " + (len - 512 - fatAligned);
    } } }
"@
[AAPak]::List((Resolve-Path $Pak).Path, [IO.Path]::GetFullPath($Out))
"scritto: $Out"
