<<<<<<< HEAD
# distributed-calculator
=======
====================================================================
                     DISTRIBUTED CALCULATOR - RMI
====================================================================
Project Folder: /home/anu/Projects/distributed_calculator/

====================================================================
1. PROJECT FILE STRUCTURE
====================================================================
distributed_calculator/
│
├── CalculatorInterface.java    # Remote interface (extends Remote)
├── CalculatorImpl.java         # Implementation (extends UnicastRemoteObject)
├── Server.java                 # Server (creates Registry, binds remote object)
├── Client.java                 # Client (looks up remote object, invokes methods)
│
├── run_server.sh               # Shell script to compile and run the server
├── run_client.sh               # Shell script to compile and run the client
│
└── README.md                   # This file

====================================================================
2. COMPILATION AND EXECUTION INSTRUCTIONS
====================================================================

PREREQUISITES:
- Java Development Kit (JDK) version 8 or higher (Java 8+ recommended; JDK 11 or JDK 17 recommended)
- Java runtime must be on the system PATH
- Verify: java -version and javac -version
- On Termux (Android): `pkg install openjdk-17` or `pkg install openjdk-11`
- On Arch Linux: `pacman -Sy jdk11-openjdk`
- On Debian/Ubuntu: `apt-get install openjdk-11-jdk`
- On macOS: `brew install openjdk`

STEP 1: Compile all Java files
---------------------------
Open a terminal in the project directory:
  cd /home/anu/Projects/distributed_calculator
  javac *.java

This will generate .class files for all four files:
  CalculatorInterface.class
  CalculatorImpl.class
  Server.class
  Client.class

STEP 2: Start the RMI Registry and Server
------------------------------------------
In one terminal window:

# Option A: Using the run script (recommended)
./run_server.sh

# Option B: Manual startup
# First, start the RMI Registry:
rmiregistry &

# Then, start the server:
java Server

The RMI Registry will start on port 1099 by default.
You should see: "RMI Registry created at port 1099" and
                  "Calculator server is ready."

# DISTRIBUTED SETUP: Server on PC, Client on Phone (Termux)
# To run the server on one computer and the client on another device:
#
# 1. On the server computer, find its local IP address:
#    - Linux: ip addr show | grep 'inet ' | grep -v 127.0.0.1
#    - macOS: ifconfig | grep inet
#    - Windows: ipconfig
#    Example: 192.168.1.15 or 10.42.0.242
#
# 2. Start the server: java Server
#    Keep this terminal open — the server must stay running.
#
# 3. On the client device, install Termux and JDK:
#    pkg install openjdk-17 (Termux)
#
# 4. On the client device, navigate to the project and run:
#    java Client <server-IP>
#    Example: java Client 192.168.1.15
#
# 5. Test operations in the client terminal.
#
# Note: Both devices must be on the same WiFi network for this to work.

STEP 3: Start the Client
------------------------
In a SEPARATE terminal window (keep the server running):
  ./run_client.sh

# Or manually:
java Client

# To connect to a remote server:
java Client <server-IP>

The client will connect to the Calculator service via RMI.
You should see: "Connected to Calculator service via RMI."

STEP 4: Test the Calculator
----------------------------
Use the client's command-line interface:
  - Choose operation 1-4 (Addition, Subtraction, Multiplication, Division)
  - Enter two numbers when prompted
  - View the result displayed by the remote server

STEP 5: Test Concurrent Clients
--------------------------------
Open additional terminal windows and run the client in each one.
All clients can connect to and use the server simultaneously
because RMI's UnicastRemoteObject handles concurrent requests.

STEP 6: Shutdown
----------------
Terminate the client with Ctrl+C.
Terminate the server with Ctrl+C.
Kill the rmiregistry process: pkill rmiregistry

====================================================================
3. ARCHITECTURE OVERVIEW
====================================================================

    +---------------------+          +---------------------+
    |                     |          |                     |
    |      CLIENT 1       |  RMI --->|      SERVER         |
    | (runs java Client)  |          | (runs java Server)  |
    |                     |          |                     |
    +---------------------+          +--------+------------+
                                                |
                                                | Registry
    +---------------------+          +--------v------------+
    |                     |          |                   |
    |      CLIENT 2       |          | CalculatorImpl    |
    | (runs java Client)  |          | (remote object)   |
    |                     |          |                   |
    +---------------------+          +---------------------+

ARCHITECTURE DESCRIPTION:

1. RMI Registry (Port 1099)
   - Lightweight service that stores bindings between names and remote objects
   - Created by the Server using LocateRegistry.createRegistry(1099)
   - Clients use Naming.lookup() to find the remote object by name

2. Calculator Server
   - Creates the RMI Registry if it doesn't exist
   - Instantiates CalculatorImpl (the remote object)
   - Binds the object to the name "Calculator" in the registry
   - Extends UnicastRemoteObject to support concurrent client requests
   - Runs independently, waiting for client method invocations

3. Calculator Client
   - Looks up the remote Calculator object via Naming.lookup("rmi://host:port/Calculator")
   - Obtains a stub (proxy) for the remote object
   - Invokes remote methods as if they were local object methods
   - Handles user input, error display, and result output

4. CalculatorImpl (Remote Object)
   - Implements the CalculatorInterface
   - Extends UnicastRemoteObject for RMI infrastructure integration
   - Implements all arithmetic operations: add, subtract, multiply, divide
   - Handles division by zero with ArithmeticException
   - RMI automatically generates stubs and proxies

5. Communication Flow
   - Client → RMI Registry: Naming.lookup() to find the "Calculator" binding
   - RMI Registry → Server: Returns the stub/proxy for the remote object
   - Client → Server: Invokes remote methods through the stub
   - Server → Client: Returns the result of the computation
   - The wire protocol uses Java serialization (or optionally, binary protocols)

KEY RMI CONCEPTS:
- Stub: Client-side proxy that forwards method calls to the remote object
- Skeleton: Server-side stub (deprecated in newer Java versions, replaced by UnicastRemoteObject)
- Registry: Naming service for discovering remote objects
- RemoteException: Must be declared/thrown for all remote method calls
- Serialization: Objects/method parameters return values must be serializable

====================================================================
4. SAMPLE INPUT/OUTPUT
====================================================================

--- SERVER TERMINAL ---
$ java Server
RMI Registry created at port 1099
Calculator server is ready.
Remote object registered as: Calculator
Calculator server is ready.

--- CLIENT 1 TERMINAL (ADDITION) ---
$ java Client
Connected to Calculator service via RMI.
=== Distributed Calculator Client ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Exit
=====================================
Choose operation (1-5, 0 to exit): 1
Enter first number: 12.5
Enter second number: 7.3
Result (Addition): 19.80

--- CLIENT 2 TERMINAL (CONCURRENT TEST) ---
$ java Client
Connected to Calculator service via RMI.
=== Distributed Calculator Client ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Exit
=====================================
Choose operation (1-5, 0 to exit): 3
Enter first number: 4.0
Enter second number: 3.5
Result (Multiplication): 14.00

--- CLIENT 3 TERMINAL (CONCURRENT TEST) ---
$ java Client
Connected to Calculator service via RMI.
=== Distributed Calculator Client ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Exit
=====================================
Choose operation (1-5, 0 to exit): 4
Enter first number: 10.0
Enter second number: 0
Error: Division by zero is not allowed

Choose operation (1-5, 0 to exit): 4
Enter first number: 15.0
Enter second number: 3.0
Result (Division): 5.00

--- DIVISION BY ZERO HANDLING ---
The client properly catches the ArithmeticException from the server
and displays "Error: Division by zero is not allowed" instead of crashing.

====================================================================
5. ARCHITECTURE DIAGRAM
====================================================================
(Generated as text diagram - use any diagramming tool for SVG)

+---------------------------------------------------------------------------+
||                        DISTRIBUTED CALCULATOR RMI                         |
+===========================================================================+
||  +----------------------+                                                   |
||  |  +----------------+  |  RMI Protocol (stub/skeleton, serialization)    |
||  |  |   CLIENT 1     |  |                                                   |
||  |  | (runs java)    |  |                                                   |
||  |  +--------+-------+  |                                                   |
||  +------------+--------+           +-----------------+-----------------+  |
|  +----------------------+           |                 |                 |
||                              |         RMI Registry  |  Naming Service |
||                              |  (Port 1099)        |                 |
||                              +----------+----------+                 |
||                                       |  Naming.lookup("rmi://host:port/Calculator")|
||                                       v                 |
||                              +----------+----------+                 |
||                              |  +----------------+  |                 |
||                              |  |   CLIENT 2     |  |                 |
||                              |  | (runs java)   |  |                 |
||                              |  +--------+-------+  |                 |
||                              +------------+--------+                 |
||                                        |                 |
||               +---------------------+-----------------+-----------------|
||               |                                                 |                 |
|    +----------v--------+                        +-----v------+   +----v------+
|    |                   |                        |             |   |             |
|    |   +------------+   |                        |  RMI Registry|   |Calculator |
|    |   | Server     |   |  LocateRegistry    | (Port 1099)  |   |Impl       |
|    |   | (runs java) |   |  createRegistry  |              |   | (remote)  |
|    |   +-------+-------+                        +------------+   +----+------+
|    +----------+----------+                         |              |
||               |                                   |              |
||               |  rebind("Calculator", calculator)   |              |
||               v                                   v              v
||      +----------v--------+                +-----v------+  +-----v------+
||      |                   |                |            |  |            |
||      |   RMI Registry    |                |   Calculator|  |   Clients  |
||      |   (binds name)    |                |   Interface  |  | (stubs)    |
||      +-------------------+                +-------------+  +------------+

====================================================================
6. VIVA QUESTIONS AND ANSWERS
====================================================================

Q1: What is Java RMI and what are its core components?
A1: Java RMI (Remote Method Invocation) is a Java API that allows an object
    to invoke methods on an object running in a different Java Virtual Machine.
    Core components:
    - Stub: Client-side proxy that forwards method calls to the remote object
    - Skeleton: Server-side counterpart (deprecated in Java 2.x, replaced by
      UnicastRemoteObject) 
    - Registry: Naming service that binds remote object names to their stubs
    - Remote interface: Must be extended by all remotely accessible objects
    - RemoteException: Must be declared/thrown for all remote method signatures

Q2: Why must remote methods throw RemoteException?
A2: RemoteException is the base exception class for all remote method calls in
    RMI. It indicates that a communication problem has occurred between the
    client and server (network failure, server crash, timeout, etc.). The RMI
    system wraps any IO or network errors into RemoteException so the caller can
    detect and handle communication failures explicitly.

Q3: How does RMI support concurrent clients?
A3: RMI supports concurrent clients through the UnicastRemoteObject base class,
    which creates a separate thread for each client request. When a client invokes
    a remote method, the call is handled by the RMI runtime's thread pool, allowing
    multiple clients to make simultaneous requests. The CalculatorImpl extends
    UnicastRemoteObject, which automatically enables this concurrency support.

Q4: What is the role of the RMI Registry?
A4: The RMI Registry acts as a naming service or directory service. Its primary
    roles are:
    - Store bindings between names (e.g., "Calculator") and remote object stubs
    - Allow clients to discover remote objects via Naming.lookup()
    - Facilitate the initial connection without hardcoding IP addresses or ports
    - Can be shared across multiple remote objects of different types
    The registry itself is lightweight and does not process method invocations;
    it only routes clients to the appropriate remote objects.

Q5: What happens if the RMI Registry is not running when a client starts?
A5: If the RMI Registry is not running on the expected port (1099 by default),
    the client will throw a NotBoundException when attempting Naming.lookup().
    The error message will indicate that the Calculator service was not found in
    the RMI Registry. The client cannot connect to the server without a running
    registry. The server must be started first, which creates the registry and
    binds the remote object, before clients can connect.

Q6: How do you handle division by zero in the RMI distributed calculator?
A6: The divide() method in CalculatorImpl checks if the divisor (b) is zero
    and explicitly throws an ArithmeticException with the message "Division by
    zero is not allowed". The Client class catches this exception in a try-catch
    block around the calculator.divide() call and displays the error message to
    the user without crashing. This demonstrates proper error handling across the
    distributed boundary.

Q7: Can the CalculatorInterface be extended with more operations without
    affecting existing clients?
A7: Yes, new methods can be added to the CalculatorInterface, and existing
    clients will continue to work without modification. However, any client that
    wants to use the new methods must recompile and redeploy. Conversely, if a
    method is removed from the interface, existing clients that call that method
    will receive a ClassNotFound or NoSuchMethodError when trying to invoke it
    through the stub. Version compatibility across distributed clients requires
    careful management of the remote interface.

Q8: What is the difference between LocateRegistry.createRegistry() and
    LocateRegistry.getRegistry()?
A8: 
    - LocateRegistry.createRegistry(int port): Creates a NEW RMI Registry on the
      specified port. If a registry already exists on that port, it throws a
      java.rmi.server.ExportException. Used when starting the server for the first
      time or when ensuring a fresh registry.
    - LocateRegistry.getRegistry(String host, int port): Returns the existing RMI
      Registry running on the specified host and port. If no registry exists, it
      can optionally create one if called with specific parameters. Used when a
      client wants to connect to an already-running registry, or when the server
      has already created the registry.
    - In our implementation, the Server uses createRegistry(1099) to ensure the
      registry exists before binding the remote object.

Q8: Java Version Requirements
-----------------------------
- Minimum: JDK 8 (Java 8, version 1.8.x)
- Recommended: JDK 11 or JDK 17 (latest LTS versions)
- The code uses only standard Java RMI libraries (no external dependencies)
- All features used (extends UnicastRemoteObject, Naming.lookup, etc.) are
  available since Java 1.2 and remain fully supported in Java 8+

HOW TO CHECK YOUR JAVA VERSION:
  java -version

Expected output (example):
  openjdk version "11.0.2"  OpenJDK 64-Bit Server VM (build 11.0.2+9-LDebian)

If Java is not installed, install the JDK from:
  - Oracle: https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
  - OpenJDK: apt-get install openjdk-11-jdk (Linux) or brew install openjdk (macOS)

====================================================================
7. QUICK START COMMANDS SUMMARY
====================================================================

$ cd /home/anu/Projects/distributed_calculator
$ javac *.java                        # Compile all Java files
$ java Server &                       # Start server (background)
$ java Client                         # Start client in foreground
$ # In client interface:            # Try operations:
$ #   1. Addition with numbers      # $ java Client
$ #   2. Subtraction                #
$ #   3. Multiplication             #
$ #   4. Division by zero test      #
$ #   0. Exit                       #
$ pkill rmiregistry                   # Kill the registry when done

====================================================================
END OF README
====================================================================
>>>>>>> babd915 (1st commit)
