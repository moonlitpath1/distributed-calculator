import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Remote interface for the Distributed Calculator.
 * Defines remote methods for arithmetic operations using Java RMI.
 */
public interface CalculatorInterface extends Remote {
    /**
     * Adds two numbers.
     *
     * @param a the first operand
     * @param b the second operand
     * @return the sum of a and b
     * @throws RemoteException if a communication error occurs
     */
    double add(double a, double b) throws RemoteException;

    /**
     * Subtracts the second number from the first.
     *
     * @param a the first operand
     * @param b the second operand
     * @return the difference of a and b
     * @throws RemoteException if a communication error occurs
     */
    double subtract(double a, double b) throws RemoteException;

    /**
     * Multiplies two numbers.
     *
     * @param a the first operand
     * @param b the second operand
     * @return the product of a and b
     * @throws RemoteException if a communication error occurs
     */
    double multiply(double a, double b) throws RemoteException;

    /**
     * Divides the first number by the second.
     *
     * @param a the dividend
     * @param b the divisor
     * @return the quotient of a divided by b
     * @throws RemoteException if a communication error occurs
     * @throws ArithmeticException if b is zero (division by zero)
     */
    double divide(double a, double b) throws RemoteException, ArithmeticException;
}