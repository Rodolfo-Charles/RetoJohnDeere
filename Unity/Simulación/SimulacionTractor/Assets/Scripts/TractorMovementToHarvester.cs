using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class TractorMovementToHarvester : MonoBehaviour
{
    // Velocidad de movimiento del objeto
    public float velocidad = 5f;
    public float targetRotation = 90f; // Adjust this value as needed
    public float rotationSpeed = 180f;

    public float tolerancia = 0.1f;

    private Vector3 destino1 = new Vector3(-3.66f, 0.6f, 13f);
    private Vector3 destino2 = new Vector3(43.47f, 0.6f, 13f);
    //private Vector3 destino3 = new Vector3(43.47f, 0.6f, 3.04f);
    private Vector3 destino3 = new Vector3(43.47f, 0.6f, -9f);



    private int iteracion = 1;

    void Start()
    {
        switch (iteracion)
        {
            case 1:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino1));
                break;

            case 2:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino2));
                break;

            case 3:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino3));
                break;

            case 4:
                Debug.Log("ACABO");
                transform.position = destino3;
                break;
        }

    }

    void Update()
    {
        
    }

    IEnumerator RotateObjectRight()
    {
        float targetRotationY = transform.eulerAngles.y + targetRotation;

        while (transform.eulerAngles.y < targetRotationY)
        {
            float rotationStep = rotationSpeed * Time.deltaTime;

            // Rotate the object to the target rotation
            transform.rotation = Quaternion.RotateTowards(transform.rotation, Quaternion.Euler(0f, targetRotationY, 0f), rotationStep);

            yield return null;  // Yield to the next frame
        }

        // Optional: Perform any actions when rotation and movement are completed
        Debug.Log("Rotation and movement completed!");
    }


    IEnumerator MoverObjetoHaciaCoordenadas(Vector3 destino)
    {
        while (Vector3.Distance(transform.position, destino) > tolerancia)
        {
            transform.position = Vector3.MoveTowards(transform.position, destino, velocidad * Time.deltaTime);
            yield return null;
        }
        iteracion++;

        if (iteracion != 4)
        {
            StartCoroutine(RotateObjectRight());
        }
        Start();


    }
}
