using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class MovObstaculos : MonoBehaviour
{
    // Velocidad de movimiento del objeto
    public float velocidad = 5f;

    public float tolerancia = 0.1f;

    public float rotationSpeed = 50f;

    private Vector3 destino1 = new Vector3(0.470000267f, 0.748251438f, -2f);
    private Vector3 destino2 = new Vector3(6.56165838f, 0.740282416f, -12.9999771f);
    private Vector3 destino3 = new Vector3(0.31547904f, 0.740289867f, -49f);
    private Vector3 destino4 = new Vector3(8.92264271f, 0.740289867f, 5f);
    private Vector3 destino5 = new Vector3(13.022462f, 0.740289927f, -49f);
    private Vector3 destino6 = new Vector3(21.7900486f, 0.740285456f, -33.3000145f);
    private Vector3 destino7 = new Vector3(28.1673203f, 0.740289807f, -21.0400009f);
    private Vector3 destino8 = new Vector3(21.5371971f, 0.740284741f, 5f);
    private Vector3 destino9 = new Vector3(25.6879158f, 0.740239024f, -49f);
    private Vector3 destino10 = new Vector3(34.1390915f, 0.740743339f, -5f);



    private int iteracion = 1;

    void Start()
    {
        switch (iteracion)
        {
            case 1:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino1));
                break;

            case 2:
                StartCoroutine(MoveLeft());
                break;

            case 3:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino2));
                break;

            case 4:
                StartCoroutine(MoveRight());
                break;

            case 5:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino3));
                break;

            case 6:
                StartCoroutine(RotateObjectRight());
                break;

            case 7:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino4));
                break;

            case 8:
                StartCoroutine(RotateObjectLeft());
                break;

            case 9:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino5));
                break;

            case 10:
                StartCoroutine(RotateObjectRight());
                break;
          
            case 11:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino6));
                break;

            case 12:
                StartCoroutine(MoveRightInv());
                break;

            case 13:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino7));
                break;

            case 14:
                StartCoroutine(MoveLeftInv());
                break;

            case 15:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino8));
                break;

            case 16:
                StartCoroutine(RotateObjectLeft());
                break;

            case 17:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino9));
                break;

            case 18:
                StartCoroutine(RotateObjectRight());
                break;

            case 19:
                StartCoroutine(MoverObjetoHaciaCoordenadas(destino10));
                break;

            case 20:
                StartCoroutine(RotateObjectLeft());
                break;
        }

    }

    void Update()
    {

    }

    IEnumerator MoveRight()
    {
        Vector3 targetPosition = transform.position + new Vector3(-6f, 0f, 0f);

        while (transform.position.x > targetPosition.x)
        {
            transform.Translate(Vector3.right * velocidad * Time.deltaTime);

            yield return null;
        }
        iteracion++;
        Start();
    }

    IEnumerator MoveRightInv()
    {
        Vector3 targetPosition = transform.position + new Vector3(6f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            transform.Translate(Vector3.right * velocidad * Time.deltaTime);

            yield return null;
        }
        iteracion++;
        Start();
    }

    IEnumerator MoveLeft()
    {
        Vector3 targetPosition = transform.position + new Vector3(6f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            transform.Translate(Vector3.left * velocidad * Time.deltaTime);

            yield return null;
        }
        iteracion++;
        Start();
    }

    IEnumerator MoveLeftInv()
    {
        Vector3 targetPosition = transform.position + new Vector3(-6f, 0f, 0f);

        while (transform.position.x > targetPosition.x)
        {
            transform.Translate(Vector3.left * velocidad * Time.deltaTime);

            yield return null;
        }
        iteracion++;
        Start();
    }

    IEnumerator MoverObjetoHaciaCoordenadas(Vector3 destino)
    {
        while (Vector3.Distance(transform.position, destino) > tolerancia)
        {
            transform.position = Vector3.MoveTowards(transform.position, destino, velocidad * Time.deltaTime);
            yield return null;
        }
        iteracion++;
        Start();


    }

    IEnumerator RotateObjectRight()
    {
        float totalRotation = 0f;

        while (totalRotation < 180f)
        {
            float rotationStep = Mathf.Min(rotationSpeed * Time.deltaTime, 180f - totalRotation);

            transform.Rotate(Vector3.down, rotationStep);

            totalRotation += rotationStep;

            yield return null;  // Yield to the next frame
        }

        Vector3 targetPosition = transform.position + new Vector3(8.2f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            transform.Translate(Vector3.right * velocidad * Time.deltaTime);

            yield return null;  // Yield to the next frame
        }

        iteracion++;
        Start();
    }

    IEnumerator RotateObjectLeft()
    {
        float totalRotation = 0f;

        while (totalRotation < 180f)
        {
            float rotationStep = Mathf.Min(rotationSpeed * Time.deltaTime, 180f - totalRotation);

            transform.Rotate(Vector3.up, rotationStep);

            totalRotation += rotationStep;

            yield return null;  // Yield to the next frame
        }

        Vector3 targetPosition = transform.position + new Vector3(3.8f, 0f, 0f);

        while (transform.position.x < targetPosition.x)
        {
            transform.Translate(Vector3.left * velocidad * Time.deltaTime);

            yield return null;  // Yield to the next frame
        }

        iteracion++;
        Start();
    }
}

