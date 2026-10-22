import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

/**
 * Server application for the Distributed Calculator using Java RMI.
 * Creates the RMI Registry if it doesn't exist, binds the CalculatorImpl
 * object to the name "Calculator", and waits for client requests.
 */
public class Server {
    private static final String CALCULATOR_NAME = "Calculator";
    private static final int RM_PORT = 1099; // Default RMI Registry port

    public static void main(String[] args) {
        try {
            // Create the RMI Registry on the default port (1099)
            // if it does not already exist
            Registry registry = LocateRegistry.createRegistry(RM_PORT);
            System.out.println("RMI Registry created at port " + RM_PORT);

            // Create the implementation instance
            CalculatorImpl calculator = new CalculatorImpl();

            // Bind the remote object to the registry with the name "Calculator"
            // This makes it accessible to clients via: "rmi://host:port/Calculator"
            registry.rebind(CALCULATOR_NAME, calculator);

            // Also try Naming.bind as a fallback if rebind fails
            try {
                Naming.bind("rmi://localhost:" + RM_PORT + "/" + CALCULATOR_NAME, calculator);
            } catch (Exception e) {
                // rebind already succeeded, ignore bind error
            }

            System.out.println("Calculator server is ready.");
            System.out.println("Remote object registered as: " + CALCULATOR_NAME);
            System.out.println("Clients can now connect via RMI.");

        } catch (Exception e) {
            System.err.println("Calculator server error:");
            e.printStackTrace();
            System.exit(1);
        }
    }
}
