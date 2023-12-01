using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class MovimientoObjetosObstaculos : MonoBehaviour
{
    public TextAsset farmDataFile; // Asigna el archivo JSON desde el editor de Unity
    private FarmData farmData;
    // Velocidad de movimiento del objeto
    public float velocidad = 5f;
    private bool ajusteRealizado = false;
    private bool recorridoAcabado = false;
    private bool recorridoAcabado2 = true;
    public float targetRotation = 180f; // Adjust this value as needed
    public float rotationSpeed = 180f;
    private int iteracion = 1;
    private int iteracion2 = 1;

    public float distanciaMovimiento = 1.0f;
    public float distanciaMovimientoAdelante = 10.0f;
    


    void Start()
    {
        if (farmDataFile != null)
        {
            // Obtén el contenido del archivo JSON como una cadena
            string json = farmDataFile.text;

            // Deserializar el JSON a un objeto de tipo FarmData
            farmData = JsonUtility.FromJson<FarmData>(json);

            // Ahora puedes acceder a la información como antes
            Debug.Log("Step 0 - Container Load: " + farmData.step0.containerLoad);
            Debug.Log("Step 1 - Harvester Position: " + farmData.step98.harvesterPosition[0] + ", " + farmData.step98.harvesterPosition[1]);
            // ... (puedes seguir accediendo a la información según la estructura de tu JSON)
        }
        else
        {
            Debug.LogError("El archivo farmData.json no se ha asignado.");
        }
        //StartCoroutine(RotateObjectLeft());
    }

    void Update()
    {
        // Mueve el objeto hacia las coordenadas deseadas
        // MoverObjetoHaciaCoordenadas(farmData.step98.harvesterPosition[0], 0, farmData.step98.harvesterPosition[1]);
        switch (iteracion)
        {
            case 1:
                MoverObjetoHaciaAdelante1(0.47f, 0.74f, -1.7f);
                break;

            case 2:
                MoverObjetoHaciaAdelante2(6.27f, 0.74f, -12.3f);
                break;

                //case 3:
                //    MoverObjetoHaciaAdelante3(0.47f, 0.74f, -49);
                //    break;
        }

        //if (!recorridoAcabado2)
        //{

        //    switch (iteracion2)
        //    {
        //        case 1:
        //            MoverObjetoHaciaCoordenadasRegreso(9.04f, 0.74f, 6.02f);// -farmData.step98.harvesterPosition[1] + 40);
        //            break;

        //        case 2:
        //            MoverObjetoHaciaCoordenadasRegreso(21f, 0.74f, 6.02f);
        //            break;

        //        case 3:
        //            MoverObjetoHaciaCoordenadasRegreso(33f, 0.74f, 6.02f);
        //            break;
        //    }
        //}

    }

    IEnumerator RotateObjectRight()
    {
        float totalRotation = 0f;

        while (totalRotation < 180f)
        {
            // Calculate the rotation for each frame
            float rotationStep = Mathf.Min(rotationSpeed * Time.deltaTime, 180f - totalRotation);

            // Rotate the object around the down (Y) axis
            transform.Rotate(Vector3.down, rotationStep);



            // Update total rotation
            totalRotation += rotationStep;

            yield return null;  // Yield to the next frame
        }

        // Move the object left after rotation
        Vector3 targetPosition = transform.position + new Vector3(8.2f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            // Move the object left
            transform.Translate(Vector3.right * velocidad * Time.deltaTime);

            yield return null;  // Yield to the next frame
        }

        // Optional: Perform any actions when rotation and movement are completed
        Debug.Log("Rotation and movement completed!");
    }

    IEnumerator RotateObjectLeft()
    {
        float totalRotation = 0f;

        while (totalRotation < 180f)
        {
            // Calculate the rotation for each frame
            float rotationStep = Mathf.Min(rotationSpeed * Time.deltaTime, 180f - totalRotation);

            // Rotate the object around the up (Y) axis instead of down
            transform.Rotate(Vector3.up, rotationStep);

            // Update total rotation
            totalRotation += rotationStep;

            yield return null;  // Yield to the next frame
        }

        // Move the object right after rotation
        Vector3 targetPosition = transform.position + new Vector3(3.8f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            // Move the object right instead of left
            transform.Translate(Vector3.left * velocidad * Time.deltaTime);

            yield return null;  // Yield to the next frame
        }

        // Optional: Perform any actions when rotation and movement are completed
        Debug.Log("Rotation and movement completed!");
        recorridoAcabado = true;
    }

    IEnumerator MoveRight()
    {
        // Move the object left after rotation
        Vector3 targetPosition = transform.position + new Vector3(6f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            // Move the object left
            transform.Translate(Vector3.right * velocidad * Time.deltaTime);

            yield return null;  // Yield to the next frame
        }

        // Optional: Perform any actions when rotation and movement are completed
    }
    IEnumerator MoveLeft()
    {
        // Move the object right after rotation
        Vector3 targetPosition = transform.position + new Vector3(6f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            // Move the object right instead of left
            transform.Translate(Vector3.left * velocidad * Time.deltaTime);

            yield return null;  // Yield to the next frame
        }

        // Optional: Perform any actions when rotation and movement are completed
        iteracion++;
    }

    void MoverObjetoHaciaAdelante1(float x, float y, float z)
    {
        Vector3 coordenadasObjetivo = new Vector3(x, y, z);

        // Check if the adjustment has been made
        if (!ajusteRealizado)
        {
            Debug.Log(coordenadasObjetivo);
            coordenadasObjetivo += new Vector3(transform.position.x, transform.position.y, transform.position.z);
            ajusteRealizado = true;
            Debug.Log(coordenadasObjetivo);
        }

        // Mover el objeto hacia las coordenadas objetivo
        transform.position = Vector3.MoveTowards(transform.position, coordenadasObjetivo, velocidad * Time.deltaTime);

        // Verificar si el objeto ha llegado a las coordenadas objetivo
        if (transform.position == coordenadasObjetivo)
        {
            //recorridoAcabado = true;
            ajusteRealizado = false;
            StartCoroutine(MoveLeft());
            Debug.Log("MoverAdelante1");
        }
    }

    void MoverObjetoHaciaAdelante2(float x, float y, float z)
    {
        Vector3 coordenadasObjetivo = new Vector3(x, y, z);

        // Check if the adjustment has been made
        if (!ajusteRealizado)
        {
            Debug.Log(coordenadasObjetivo);
            coordenadasObjetivo += new Vector3(transform.position.x, transform.position.y, transform.position.z);
            ajusteRealizado = true;
            Debug.Log(coordenadasObjetivo);
        }

        // Mover el objeto hacia las coordenadas objetivo
        transform.position = Vector3.MoveTowards(transform.position, coordenadasObjetivo, velocidad * Time.deltaTime);

        // Verificar si el objeto ha llegado a las coordenadas objetivo
        if (transform.position == coordenadasObjetivo)
        {
            //recorridoAcabado = true;
            ajusteRealizado = false;
            StartCoroutine(MoveRight());
            iteracion++;
            Debug.Log("MoverAdelante2");
        }
    }

    void MoverObjetoHaciaAdelante3(float x, float y, float z)
    {
        Vector3 coordenadasObjetivo = new Vector3(x, y, z);

        // Check if the adjustment has been made
        if (!ajusteRealizado)
        {
            Debug.Log(coordenadasObjetivo);
            coordenadasObjetivo += new Vector3(transform.position.x, transform.position.y, transform.position.z);
            ajusteRealizado = true;
            Debug.Log(coordenadasObjetivo);
        }

        // Mover el objeto hacia las coordenadas objetivo
        transform.position = Vector3.MoveTowards(transform.position, coordenadasObjetivo, velocidad * Time.deltaTime);

        // Verificar si el objeto ha llegado a las coordenadas objetivo
        if (transform.position == coordenadasObjetivo)
        {
            recorridoAcabado = true;
            ajusteRealizado = false;
            StartCoroutine(RotateObjectRight());
            iteracion++;
            Debug.Log("MoverAdelante3");
        }
    }

    void MoverObjetoHaciaCoordenadasRegreso(float x, float y, float z)
    {
        Vector3 coordenadasObjetivo = new Vector3(x, y, z);

        // Check if the adjustment has been made
        if (!ajusteRealizado)
        {
            Debug.Log(coordenadasObjetivo);
            coordenadasObjetivo += new Vector3(transform.position.x, transform.position.y, transform.position.z);
            Debug.Log(coordenadasObjetivo);
            ajusteRealizado = true;
        }

        // Mover el objeto hacia las coordenadas objetivo
        transform.position = Vector3.MoveTowards(transform.position, coordenadasObjetivo, velocidad * Time.deltaTime);

        // Verificar si el objeto ha llegado a las coordenadas objetivo
        if (transform.position == coordenadasObjetivo)
        {
            recorridoAcabado2 = true;
            ajusteRealizado = false;
            StartCoroutine(RotateObjectLeft());
            Debug.Log("El objeto ha llegado a las coordenadas objetivo.");
            iteracion2++;
        }
    }
}
