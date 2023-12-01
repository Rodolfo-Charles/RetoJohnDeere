using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cosechar : MonoBehaviour
{
    // Define the tag of the object you want to make disappear
    public string targetTag = "Maiz";

    // Use OnTriggerEnter for trigger events
    private void OnTriggerEnter(Collider other)
    {
        // Check if the triggering object has the specified tag
        if (other.gameObject.CompareTag(targetTag))
        {
            // Make the current object disappear
            Destroy(other.gameObject);
        }
    }
}
