#!/bin/bash
# Uso: tools/ghidra/ghidra.sh <argomenti di analyzeHeadless...>
# Ghidra e JDK portatili stanno in _local/tools (fuori da git).
# analyzeHeadless.bat non regge gli spazi nel percorso: si usa il nome corto 8.3 (cygpath -d).
ROOT="$(cygpath -u "$(cygpath -d "$(cd "$(dirname "$0")/../.." && pwd)")")"
JDK="$ROOT/_local/tools/jdk21/jdk-21.0.12.1+1"
export JAVA_HOME="$(cygpath -w "$JDK")"
export PATH="$JDK/bin:$PATH"
cd "$ROOT/_local/tools/ghidra/ghidra_12.1.4_PUBLIC/support" && ./analyzeHeadless.bat "$@"
