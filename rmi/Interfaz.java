import java.rmi.Remote;
import java.rmi.RemoteException;

/*
	Declarar firma de métodos que serán sobrescritos
*/
public interface Interfaz extends Remote {
    int sumar(int numero1, int numero2) throws RemoteException;
    int restar(int numero1, int numero2) throws RemoteException;
    int multiplicar(int numero1, int numero2) throws RemoteException;
    float dividir(float numero1, float numero2) throws RemoteException;
    //Agregamos una nueva
}