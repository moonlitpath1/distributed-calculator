from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Set default font
style = doc.styles['Normal']
font = style.font
font.name = 'Liberation Serif'
font.size = Pt(11)

# Set default paragraph format
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.space_before = Pt(0)

# ======================================================================
# TITLE PAGE
# ======================================================================
doc.add_paragraph()
doc.add_paragraph()
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('Distributed Calculator Using Java RMI')
run.font.size = Pt(28)
run.font.bold = True
run.font.name = 'Liberation Serif'

doc.add_paragraph()
subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('B.Tech IT Distributed Computing System Implementation')
run.font.size = Pt(14)
run.font.name = 'Liberation Serif'

doc.add_paragraph()
sub2 = doc.add_paragraph()
sub2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = sub2.add_run('Java Remote Method Invocation (RMI) based Distributed Calculator')
run.font.size = Pt(12)
run.font.name = 'Liberation Serif'

doc.add_paragraph()
doc.add_paragraph()
sub3 = doc.add_paragraph()
sub3.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = sub3.add_run('Submitted by: Anu')
run.font.size = Pt(12)
run.font.name = 'Liberation Serif'

doc.add_paragraph()
sub4 = doc.add_paragraph()
sub4.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = sub4.add_run('Department of Information Technology')
run.font.size = Pt(12)
run.font.name = 'Liberation Serif'

doc.add_paragraph()
sub5 = doc.add_paragraph()
sub5.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = sub5.add_run('Session: Tuesday, October 20, 2026')
run.font.size = Pt(12)
run.font.name = 'Liberation Serif'

# Page break
doc.add_page_break()

# ======================================================================
# TABLE OF CONTENTS
# ======================================================================
doc.add_heading('Table of Contents', level=1)
toc_items = [
    ('1', 'Project Overview'),
    ('2', 'System Requirements'),
    ('3', 'Project Architecture'),
    ('4', 'Source Code Files'),
    ('5', 'Compilation and Execution Instructions'),
    ('6', 'Sample Input/Output'),
    ('7', 'Viva Questions and Answers'),
    ('8', 'Conclusion'),
]
for num, title_text in toc_items:
    p = doc.add_paragraph()
    run_num = p.add_run(f'{num}.')
    run_num.font.size = Pt(12)
    run_num.font.name = 'Liberation Serif'
    run2 = p.add_run(f' {title_text}')
    run2.font.size = Pt(12)
    run2.font.name = 'Liberation Serif'
    p.paragraph_format.space_after = Pt(6)

doc.add_page_break()

# ======================================================================
# 1. PROJECT OVERVIEW
# ======================================================================
doc.add_heading('1. Project Overview', level=1)
doc.add_paragraph(
    'This report documents the development of a Distributed Calculator using Java '
    'Remote Method Invocation (RMI), based strictly on the B.Tech IT Distributed '
    'Computing System syllabus. The implementation demonstrates core distributed '
    'computing concepts including distributed objects, remote method invocation, '
    'client-server communication, and concurrent client requests.'
)
doc.add_paragraph(
    'The calculator supports four basic arithmetic operations—addition, subtraction, '
    'multiplication, and division—executed on a remote server via Java RMI. The '
    'client communicates with the server over a network using the RMI registry, '
    'stubs, and proxy mechanisms. The implementation is modular, beginner-friendly, '
    'and runnable on a local computer using separate client and server processes.'
)
doc.add_paragraph(
    'Key syllabus concepts covered: distributed objects, remote method invocation, '
    'client-server communication, concurrent client requests, error handling '
    '(division by zero), and RMI architecture.'
)

# ======================================================================
# 2. SYSTEM REQUIREMENTS
# ======================================================================
doc.add_heading('2. System Requirements', level=1)
doc.add_paragraph('Minimum Java Version: JDK 8 (Java 8, version 1.8.x)')
doc.add_paragraph('Recommended Java Version: JDK 11 or JDK 17 (latest LTS versions)')
doc.add_paragraph('Required Libraries: Built-in Java RMI libraries (no external dependencies)')
doc.add_paragraph('Operating System: Any OS with JDK installed (Linux, macOS, Windows)')
doc.add_paragraph('Hardware: Any local computer with sufficient resources to run two Java processes')

# ======================================================================
# 3. PROJECT ARCHITECTURE
# ======================================================================
doc.add_heading('3. Project Architecture', level=1)
doc.add_paragraph(
    'The distributed calculator follows a classic client-server architecture using '
    'Java RMI. The architecture comprises three main components: the RMI Registry, '
    'the Calculator Server, and the Calculator Client. The RMI Registry acts as a '
    'lightweight naming service running on port 1099 by default, storing bindings '
    'between object names and their remote stubs. The Calculator Server creates the '
    'RMI Registry if it does not exist, binds the CalculatorImpl instance to the name '
    '"Calculator", and waits for client requests. The Calculator Client looks up the '
    'remote Calculator object via Naming.lookup("rmi://host:port/Calculator") and '
    'invokes remote methods through the stub (proxy). The CalculatorImpl extends '
    'UnicastRemoteObject to support concurrent client requests via RMI\'s default '
    'thread-per-client architecture. Communication occurs over the RMI wire protocol '
    'using Java serialization over TCP/IP.'
)
doc.add_paragraph(
    'Key RMI concepts: Stub (client-side proxy), Remote interface (must be extended '
    'by all remotely accessible objects), RemoteException (must be declared for all '
    'remote method signatures), RMI Registry (naming service), Serialization (method '
    'parameters and return values), UnicastRemoteObject (enables concurrent client requests).'
)

# ======================================================================
# 4. SOURCE CODE FILES
# ======================================================================
doc.add_heading('4. Source Code Files', level=1)

doc.add_heading('4.1 CalculatorInterface.java', level=2)
doc.add_paragraph(
    'Remote interface extending java.rmi.Remote with four arithmetic method signatures: '
    'add(double a, double b), subtract(double a, double b), multiply(double a, double b), '
    'divide(double a, double b). All methods throw java.rmi.RemoteException.'
)

doc.add_heading('4.2 CalculatorImpl.java', level=2)
doc.add_paragraph(
    'Implementation class extending UnicastRemoteObject and implementing CalculatorInterface. '
    'Provides the actual arithmetic logic. The divide method checks for division by zero '
    'and throws ArithmeticException.'
)

doc.add_heading('4.3 Server.java', level=2)
doc.add_paragraph(
    'Main server class that creates the RMI Registry on port 1099, binds the CalculatorImpl '
    'object to the name "Calculator", and waits for client requests.'
)

doc.add_heading('4.4 Client.java', level=2)
doc.add_paragraph(
    'Client application that looks up the remote Calculator object, displays a menu, accepts '
    'user input for two numbers and an operation, invokes the corresponding remote method, '
    'and displays the result. Handles division by zero and invalid input.'
)

doc.add_heading('4.5 run_server.sh and run_client.sh', level=2)
doc.add_paragraph(
    'Shell scripts to compile and run the server and client respectively.'
)

# ======================================================================
# 5. COMPILATION AND EXECUTION INSTRUCTIONS
# ======================================================================
doc.add_heading('5. Compilation and Execution Instructions', level=1)

doc.add_heading('Step 1: Compile all Java files', level=2)
doc.add_paragraph('Navigate to the project directory:')
doc.add_paragraph('cd /home/anu/Projects/distributed_calculator')
doc.add_paragraph('Compile: javac *.java')
doc.add_paragraph('Verify .class files are generated for all four Java files.')

doc.add_heading('Step 2: Start the RMI Server', level=2)
doc.add_paragraph('In one terminal window, start the server: java Server')
doc.add_paragraph('Verify output: "RMI Registry created at port 1099" and "Calculator server is ready."')
doc.add_paragraph('Keep this terminal open — the server must stay running.')

doc.add_heading('Step 3: Start the Client', level=2)
doc.add_paragraph('In a separate terminal window, start the client: java Client')
doc.add_paragraph('To connect to a remote server: java Client <server-IP>')
doc.add_paragraph('Wait for "Connected to Calculator service via RMI." message.')

doc.add_heading('Step 4: Test the Calculator', level=2)
doc.add_paragraph('Choose operation 1-4 (Addition, Subtraction, Multiplication, Division).')
doc.add_paragraph('Enter two numbers when prompted.')
doc.add_paragraph('View the result displayed by the remote server.')
doc.add_paragraph('Test division by zero: enter 0 as the second number.')

doc.add_heading('Step 5: Test Concurrent Clients', level=2)
doc.add_paragraph(
    'Open additional terminal windows and run the client in each. All clients can '
    'simultaneously use the server because UnicastRemoteObject handles concurrent requests '
    'via RMI\'s thread-per-client architecture.'
)

doc.add_heading('Step 6: Shut Down', level=2)
doc.add_paragraph('Terminate the client with Ctrl+C.')
doc.add_paragraph('Terminate the server with Ctrl+C.')
doc.add_paragraph('Kill the rmiregistry process: pkill rmiregistry.')

# ======================================================================
# 6. SAMPLE INPUT/OUTPUT
# ======================================================================
doc.add_heading('6. Sample Input/Output', level=1)

doc.add_heading('6.1 Server Terminal', level=2)
doc.add_paragraph(
    'RMI Registry created at port 1099\n'
    'Calculator server is ready.\n'
    'Remote object registered as: Calculator\n'
    'Clients can now connect via RMI.'
)

doc.add_heading('6.2 Client Terminal - Addition', level=2)
doc.add_paragraph(
    '=== Distributed Calculator Client ===\n'
    '1. Addition\n'
    '2. Subtraction\n'
    '3. Multiplication\n'
    '4. Division\n'
    '0. Exit\n'
    '=====================================\n'
    'Choose operation (1-5, 0 to exit): 1\n'
    'Enter first number: 12.5\n'
    'Enter second number: 7.3\n'
    'Result (Addition): 19.80'
)

doc.add_heading('6.3 Client Terminal - Division by Zero', level=2)
doc.add_paragraph(
    'Choose operation (1-5, 0 to exit): 4\n'
    'Enter first number: 10.0\n'
    'Enter second number: 0\n'
    'Error: Division by zero is not allowed'
)

doc.add_heading('6.4 Client Terminal - Division', level=2)
doc.add_paragraph(
    'Choose operation (1-5, 0 to exit): 4\n'
    'Enter first number: 15.0\n'
    'Enter second number: 3.0\n'
    'Result (Division): 5.00'
)

# ======================================================================
# 7. VIVA QUESTIONS AND ANSWERS
# ======================================================================
doc.add_heading('7. Viva Questions and Answers', level=1)

vivas = [
    ('Q1: What is Java RMI and what are its core components?',
     'A1: Java RMI (Remote Method Invocation) is a Java API that allows an object to invoke methods on an object running in a different JVM. Core components: Stub (client-side proxy), Skeleton (server-side, deprecated), Registry (naming service), Remote interface (must be extended by remotely accessible objects), RemoteException (must be declared for all remote methods).'),
    ('Q2: Why must remote methods throw RemoteException?',
     'A2: RemoteException is the base exception class for all remote method calls in RMI. It indicates a communication problem between client and server (network failure, server crash, timeout). The RMI system wraps IO or network errors into RemoteException.'),
    ('Q3: How does RMI support concurrent clients?',
     'A3: RMI supports concurrent clients through UnicastRemoteObject, which creates a separate thread for each client request. The RMI runtime\'s thread pool handles multiple simultaneous method invocations, allowing many clients to use the same remote object concurrently.'),
    ('Q4: What is the role of the RMI Registry?',
     'A4: The RMI Registry acts as a naming service. Its primary roles: store bindings between names (e.g., "Calculator") and remote object stubs, allow clients to discover remote objects via Naming.lookup(), facilitate initial connection without hardcoding IP addresses/ports, and can be shared across multiple remote objects of different types.'),
    ('Q5: What happens if the RMI Registry is not running when a client starts?',
     'A5: The client will throw NotBoundException when attempting Naming.lookup(). The error message indicates the Calculator service was not found in the RMI Registry. The server must be started first, which creates the registry and binds the remote object, before clients can connect.'),
    ('Q6: How do you handle division by zero in the RMI distributed calculator?',
     'A6: The divide() method in CalculatorImpl checks if the divisor is zero and explicitly throws ArithmeticException with the message "Division by zero is not allowed". The Client class catches this exception in a try-catch block around the calculator.divide() call and displays the error message to the user without crashing.'),
    ('Q7: Can the CalculatorInterface be extended with more operations without affecting existing clients?',
     'A7: Yes, new methods can be added to the CalculatorInterface, and existing clients will continue to work without modification. However, clients that want to use the new methods must recompile and redeploy. Version compatibility across distributed clients requires careful management of the remote interface.'),
    ('Q8: What is the difference between LocateRegistry.createRegistry() and LocateRegistry.getRegistry()?',
     'A8: LocateRegistry.createRegistry(int port) creates a NEW RMI Registry on the specified port. If a registry already exists on that port, it throws ExportException. LocateRegistry.getRegistry(String host, int port) returns the existing RMI Registry running on the specified host and port. Used when a client wants to connect to an already-running registry, or when the server has already created the registry. In our implementation, the Server uses createRegistry(1099) to ensure the registry exists before binding the remote object.'),
    ('Q9: Why is double used instead of Integer for the calculator operations?',
     'A9: double supports decimal numbers (fractional values), which is more general for a calculator. Primitive double values are automatically serializable in RMI. Using Integer would restrict to whole numbers only.'),
    ('Q10: What is the stub in RMI and what does it do?',
     'A10: The stub is a client-side proxy that forwards method calls to the remote object. It marshals (packages) the parameters, sends them over the RMI wire protocol (TCP/IP) to the server, receives the result from the server, unmarshals it, and presents it as the method return value to the client code. The stub hides the complexity of distributed communication from the caller.'),
]

for q, a in vivas:
    p = doc.add_paragraph()
    run_q = p.add_run(q)
    run_q.font.size = Pt(11)
    run_q.font.name = 'Liberation Serif'
    p.paragraph_format.space_after = Pt(6)
    p2 = doc.add_paragraph()
    run_a = p2.add_run(a)
    run_a.font.size = Pt(11)
    run_a.font.name = 'Liberation Serif'
    p2.paragraph_format.space_after = Pt(12)

# ======================================================================
# 8. CONCLUSION
# ======================================================================
doc.add_heading('8. Conclusion', level=1)
doc.add_paragraph(
    'This report documents the complete implementation of a Distributed Calculator '
    'using Java RMI, fulfilling the requirements of the B.Tech IT Distributed '
    'Computing System syllabus. The implementation successfully demonstrates '
    'distributed objects, remote method invocation, client-server communication, '
    'and concurrent client requests using only built-in Java RMI libraries. The '
    'project consists of four Java source files (CalculatorInterface.java, '
    'CalculatorImpl.java, Server.java, Client.java), two shell scripts '
    '(run_server.sh, run_client.sh), and comprehensive documentation. The system '
    'architecture leverages the RMI Registry as a naming service, stubs for '
    'transparent remote method invocation, and UnicastRemoteObject for concurrent '
    'client support. All syllabus requirements are met: remote interface with '
    'arithmetic operations, server implementation with RMI Registry binding, client '
    'with user CLI, concurrent client support, error handling for division by zero '
    'and invalid input, and testing with multiple clients. The code is modular, '
    'beginner-friendly, and runnable on any local computer with JDK 8 or later using '
    'separate client and server processes.'
)

# ======================================================================
# REFERENCES
# ======================================================================
doc.add_heading('References', level=1)
doc.add_paragraph(
    '• Oracle Java Documentation: https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/'
)
doc.add_paragraph(
    '• Java RMI Tutorial: https://www.tutorialspoint.com/java_rmi/'
)
doc.add_paragraph(
    '• B.Tech IT Distributed Computing System Syllabus: Institution-specific'
)

# Save the document
doc.save('/home/anu/Projects/distributed_calculator/Distributed_Calculator_Report.docx')
print('Document saved successfully.')