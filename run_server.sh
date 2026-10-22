#!/bin/bash
# run_server.sh - Compiles and starts the RMI Calculator Server
# Usage: ./run_server.sh

echo "=== Distributed Calculator RMI Server ==="
echo ""

# Step 1: Compile all Java files
echo "Compiling Java source files..."
javac *.java

if [ $? -ne 0 ]; then
    echo "Compilation failed. Check for errors above."
    exit 1
fi

echo "Compilation successful."
echo ""

# Step 2: Start the Server
echo "Starting the Calculator Server..."
java Server

echo ""
echo "Server has been stopped."