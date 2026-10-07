// Decompila le funzioni che chiamano (o referenziano) un indirizzo.  Args: fileUscita indirizzoHex [profondita']
// Con profondita' 2 decompila anche i chiamanti dei chiamanti.
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.*;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.Reference;
import java.io.PrintWriter;
import java.util.*;

public class Callers extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] a = getScriptArgs();
        PrintWriter out = new PrintWriter(a[0], "UTF-8");
        Address target = toAddr(a[1]);
        int depth = a.length > 2 ? Integer.parseInt(a[2]) : 1;
        DecompInterface dec = new DecompInterface();
        dec.openProgram(currentProgram);
        Set<Function> done = new HashSet<>();
        List<Address> level = new ArrayList<>(List.of(target));
        for (int d = 1; d <= depth; d++) {
            List<Address> next = new ArrayList<>();
            for (Address t : level) {
                for (Reference r : getReferencesTo(t)) {
                    Function f = getFunctionContaining(r.getFromAddress());
                    if (f == null || !done.add(f)) continue;
                    out.println("// ===== livello " + d + ": " + f.getName() + " @ " + f.getEntryPoint()
                        + "  (chiama " + t + " da " + r.getFromAddress() + ")");
                    DecompileResults res = dec.decompileFunction(f, 60, monitor);
                    out.println(res.decompileCompleted() ? res.getDecompiledFunction().getC() : "// decompilazione fallita");
                    next.add(f.getEntryPoint());
                }
            }
            level = next;
        }
        out.close();
        println("Funzioni chiamanti: " + done.size());
    }
}
