import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * Implementation of the CalculatorInterface using Java RMI.
 * Extends UnicastRemoteObject to support remote method invocation.
 * Handles concurrent client requests automatically via RMI's default architecture.
 */
public class CalculatorImpl extends UnicastRemoteObject implements CalculatorInterface {

    private static final long serialVersionUID = 1L;

    /**
     * Default constructor. Calls the superclass constructor to register
     * this object with the RMI runtime's remote object infrastructure.
     *
     * @throws RemoteException if the remote object creation fails
     */
    public CalculatorImpl() throws RemoteException {
        super(5000);
    }

    /**
     * Adds two numbers.
     *
     * @param a the first operand
     * @param b the second operand
     * @return the sum of a and b
     * @throws RemoteException if a communication error occurs
     */
    @Override
    public double add(double a, double b) throws RemoteException {
        return a + b;
    }

    /**
     * Subtracts the second number from the first.
     *
     * @param a the first operand
     * @param b the second operand
     * @return the difference of a and b
     * @throws RemoteException if a communication error occurs
     */
    @Override
    public double subtract(double a, double b) throws RemoteException {
        return a - b;
    }

    /**
     * Multiplies two numbers.
     *
     * @param a the first operand
     * @param b the second operand
     * @return the product of a and b
     * @throws RemoteException if a communication error occurs
     */
    @Override
    public double multiply(double a, double b) throws RemoteException {
        return a * b;
    }

    /**
     * Divides the first number by the second.
     *
     * @param a the dividend
     * @param b the divisor
     * @return the quotient of a divided by b
     * @throws RemoteException if a communication error occurs
     * @throws ArithmeticException if b is zero (division by zero)
     */
    @Override
    public double divide(double a, double b) throws RemoteException, ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Division by zero is not allowed");
        }
        return a / b;
    }
}
