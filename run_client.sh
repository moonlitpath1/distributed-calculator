#!/bin/bash
# run_client.sh - Compiles and starts the RMI Calculator Client
# Usage: ./run_client.sh

echo "=== Distributed Calculator RMI Client ==="
echo ""

# Step 1: Compile all Java files (ensures stubs are up to date)
echo "Compiling Java source files..."
javac *.java

if [ $? -ne 0 ]; then
    echo "Compilation failed. Check for errors above."
    exit 1
fi

echo "Compilation successful."
echo ""

# Step 2: Start the Client
echo "Starting the Calculator Client..."
echo "Make sure the Server is running before starting the Client."
echo ""

java Client

echo ""
echo "Client has been exited."