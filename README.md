# Distributed Calculator using Java RMI

A simple distributed calculator built using **Java Remote Method Invocation (RMI)**. It allows clients to perform arithmetic operations by invoking methods on a remote calculator server.

## Features

- Addition, subtraction, multiplication, and division
- Client-server communication using Java RMI
- Remote method invocation through a shared remote interface
- Support for multiple concurrent clients
- Division-by-zero error handling
- Shell scripts for compiling and running the server and client
- Support for connecting clients from different devices on the same network

## Project Structure

```text
distributed_calculator/
├── CalculatorInterface.java   # Remote interface
├── CalculatorImpl.java        # Remote calculator implementation
├── Server.java                # RMI server and registry
├── Client.java                # Calculator client
├── run_server.sh              # Compile and start the server
├── run_client.sh              # Compile and start the client
├── .gitignore                 # Files excluded from Git
└── README.md                  # Project documentation
```

## Prerequisites

- Java Development Kit (JDK) 8 or later
- `java` and `javac` available on your system PATH
- A terminal or command-line environment

Verify your Java installation:

```bash
java -version
javac -version
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/moonlitpath1/distributed-calculator.git
cd distributed-calculator
```

Alternatively, navigate to your existing project directory.

### 2. Compile the project

```bash
javac *.java
```

This generates the `.class` files required to run the application.

### 3. Start the server

Open a terminal in the project directory and run:

```bash
chmod +x run_server.sh run_client.sh
./run_server.sh
```

The server should start the RMI registry, register the calculator service, and wait for client requests.

Keep the server running while using the client.

### 4. Start the client

Open a **separate terminal** in the project directory and run:

```bash
./run_client.sh
```

The client connects to the calculator service and displays a menu for performing arithmetic operations.

If the scripts are not configured to compile the Java files automatically, compile first using `javac *.java`.

## Usage

Choose an operation from the client menu:

1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Exit

Enter two numbers when prompted. The client sends the requested operation to the server and displays the returned result.

### Example

```text
=== Distributed Calculator Client ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
0. Exit

Choose operation: 1
Enter first number: 12.5
Enter second number: 7.3
Result (Addition): 19.80
```

Dividing by zero should display an appropriate error message rather than terminate the client unexpectedly.

## Running Across Different Devices

The server and client can run on separate devices connected to the same network.

1. Start the server on the host computer.
2. Find the host computer's local IP address.
3. Ensure the network firewall allows the required RMI connections.
4. On the client device, run:

   ```bash
   java Client <server-IP>
   ```

   Replace `<server-IP>` with the server computer's actual IP address.

For example:

```bash
java Client 192.168.1.15
```

The client implementation must support the optional server IP argument. Java RMI may also require appropriate server hostname configuration and firewall access for remote object connections.

## Architecture

```text
+------------------+        Java RMI        +------------------+
|                  | <--------------------> |                  |
|     Client       |                         |      Server      |
|                  |                         |                  |
| - User input     |                         | - RMI Registry   |
| - Remote calls   |                         | - Calculator     |
| - Display result |                         |   implementation |
+------------------+                         +------------------+
        |                                             |
        |              Remote Interface               |
        +---------------------------------------------+
```

### Main Components

- **CalculatorInterface:** Defines the remote arithmetic methods and extends `java.rmi.Remote`.
- **CalculatorImpl:** Implements the remote interface and performs the calculations.
- **Server:** Creates the RMI registry, exports the remote object, and registers the calculator service.
- **Client:** Looks up the remote calculator and invokes its methods.
- **RMI Registry:** Allows clients to locate the remote calculator by its registered name.

## Technologies Used

- Java
- Java RMI
- TCP/IP networking
- Shell scripting
- Git and GitHub

## Learning Objectives

This project demonstrates:

- Distributed computing fundamentals
- Remote method invocation
- Client-server architecture
- Remote interfaces and exceptions
- Service registration and discovery
- Basic concurrent request handling
- Network communication between Java applications

## Limitations

- Requires a reachable server and an active network connection.
- The default RMI registry port is `1099`.
- Remote connections may require firewall and hostname configuration.
- The application is intended for learning and demonstration, not production deployment.

## Future Improvements

- Add a graphical user interface.
- Support more mathematical operations.
- Add automated unit and integration tests.
- Improve network error handling.
- Introduce secure communication for remote connections.

## License

This project is available for educational and personal use. Add a license file if you intend to distribute it under a specific open-source license.
