#!/bin/bash
# 1. Find the exact path to Java 21
JAVA_21_PATH=$(/usr/libexec/java_home -v 21)
FX_LIB="$(pwd)/javafx-sdk/lib"

echo "🚀 Using Java 21 from: $JAVA_21_PATH"

# 2. Compile using the specific Java 21 compiler
$JAVA_21_PATH/bin/javac --module-path "$FX_LIB" --add-modules javafx.controls SearchWindow.java

# 3. Run using the specific Java 21 runtime
$JAVA_21_PATH/bin/java --module-path "$FX_LIB" --add-modules javafx.controls SearchWindow
