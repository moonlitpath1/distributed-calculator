import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

/**
 * Client application for the Distributed Calculator using Java RMI.
 * Connects to the remote Calculator object via RMI, accepts user input for
 * two numbers and an arithmetic operation, invokes the corresponding remote
 * method, and displays the result.
 */
public class Client {
    private static CalculatorInterface calculator;
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    // RMI registry connection details
    private static final int RMI_PORT = 1099;
    private static final String CALCULATOR_NAME = "Calculator";

    public static void main(String[] args) {
        try {
            // Allow host to be specified as command-line argument,
            // otherwise default to "localhost"
            String rmiHost = args.length > 0 ? args[0] : "localhost";
            int rmiPort = args.length > 1 ? Integer.parseInt(args[1]) : RMI_PORT;

            // Look up the remote Calculator object from the RMI Registry
            String url = "rmi://" + rmiHost + ":" + rmiPort + "/" + CALCULATOR_NAME;
            calculator = (CalculatorInterface) Naming.lookup(url);
            System.out.println("Connected to Calculator service via RMI.\n");

            boolean exit = false;
            while (!exit) {
                displayMenu();
                int choice = getIntegerInput("Choose operation (1-5, 0 to exit): ");

                if (choice == 0) {
                    exit = true;
                    System.out.println("Exiting Client. Goodbye!");
                    continue;
                }

                if (choice >= 1 && choice <= 4) {
                    double num1 = getDoubleInput("Enter first number: ");
                    double num2 = getDoubleInput("Enter second number: ");

                    double result = 0;
                    String operation = "";

                    switch (choice) {
                        case 1:
                            result = calculator.add(num1, num2);
                            operation = "Addition";
                            break;
                        case 2:
                            result = calculator.subtract(num1, num2);
                            operation = "Subtraction";
                            break;
                        case 3:
                            result = calculator.multiply(num1, num2);
                            operation = "Multiplication";
                            break;
                        case 4:
                            try {
                                result = calculator.divide(num1, num2);
                                operation = "Division";
                            } catch (ArithmeticException e) {
                                System.out.println("Error: " + e.getMessage());
                                continue;
                            }
                            break;
                    }

                    System.out.printf("Result (%s): %.2f%n%n", operation, result);
                } else {
                    System.out.println("Invalid choice. Please try again.%n");
                }
            }
        } catch (NotBoundException e) {
            System.err.println("Error: Calculator service not found in RMI Registry.");
            System.err.println("Make sure the Server is running and the registry is available.");
            e.printStackTrace();
        } catch (RemoteException e) {
            System.err.println("Error: Communication failure with the Calculator service.");
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("Error: Input/output failure.");
            e.printStackTrace();
        }
    }

    /**
     * Displays the menu of available operations.
     */
    private static void displayMenu() {
        System.out.println("=== Distributed Calculator Client ===");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.println("0. Exit");
        System.out.println("=====================================");
    }

    /**
     * Reads an integer from user input using BufferedReader.
     *
     * @param prompt the display prompt
     * @return the integer entered by the user
     * @throws IOException if an I/O error occurs
     */
    private static int getIntegerInput(String prompt) throws IOException {
        System.out.print(prompt);
        String line = reader.readLine();
        if (line == null) {
            System.out.println("Exiting.");
            return 0;
        }
        try {
            return Integer.parseInt(line.trim());
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter an integer.");
            return getIntegerInput(prompt); // retry
        }
    }

    /**
     * Reads a double from user input using BufferedReader.
     *
     * @param prompt the display prompt
     * @return the double entered by the user
     * @throws IOException if an I/O error occurs
     */
    private static double getDoubleInput(String prompt) throws IOException {
        System.out.print(prompt);
        String line = reader.readLine();
        if (line == null) {
            System.out.println("Exiting.");
            return 0;
        }
        try {
            return Double.parseDouble(line.trim());
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a numeric value.");
            return getDoubleInput(prompt); // retry
        }
    }
}