using UnityEngine;

public class CameraSwitcher : MonoBehaviour
{
    public Camera[] cameras;
    private int currentCameraIndex = 0;

    void Start()
    {
        // Disable all cameras except the first one
        for (int i = 1; i < cameras.Length; i++)
        {
            cameras[i].gameObject.SetActive(false);
        }
    }

    void Update()
    {
        // Check for key input (1 to 5) to switch cameras
        for (int i = 0; i < cameras.Length; i++)
        {
            if (Input.GetKeyDown((i + 1).ToString()))
            {
                SwitchCamera(i);
            }
        }
    }

    void SwitchCamera(int newIndex)
    {
        if (newIndex == currentCameraIndex || newIndex < 0 || newIndex >= cameras.Length)
        {
            // No need to switch if the index is out of bounds or the same as the current index
            return;
        }

        // Disable the current camera
        cameras[currentCameraIndex].gameObject.SetActive(false);

        // Enable the new camera
        cameras[newIndex].gameObject.SetActive(true);

        // Update the current camera index
        currentCameraIndex = newIndex;
    }
}
