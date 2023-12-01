using UnityEngine;

public class MoverObjeto : MonoBehaviour
{
    // Coordenadas a las que se moverá el objeto
    public Vector3 coordenadasObjetivo;

    // Velocidad de movimiento del objeto
    public float velocidad = 5f;

    void Update()
    {
        // Mover el objeto hacia las coordenadas objetivo
        transform.position = Vector3.MoveTowards(transform.position, coordenadasObjetivo, velocidad * Time.deltaTime);

        // Verificar si el objeto ha llegado a las coordenadas objetivo
        if (transform.position == coordenadasObjetivo)
        {
            Debug.Log("El objeto ha llegado a las coordenadas objetivo.");
        }
    }
}
