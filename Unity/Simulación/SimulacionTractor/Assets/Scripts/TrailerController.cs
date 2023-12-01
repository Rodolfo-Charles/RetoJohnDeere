using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class TrailerController : MonoBehaviour
{
    [SerializeField] WheelCollider backRight01;
    [SerializeField] WheelCollider backLeft01;
    [SerializeField] WheelCollider backRight02;
    [SerializeField] WheelCollider backLeft02;

    public float acceleration = 500f;
    public float breakingForce = 200f;
    public float maxTurnAngle = 20f;

    private float currentAcceleration = 0f;
    private float currentBreakForce = 0f;
    private float currentTurnAngle = 0f;

    private void FixedUpdate()
    {
        currentAcceleration = acceleration * Input.GetAxis("Vertical");

        if (Input.GetKey(KeyCode.Space))
        {
            currentBreakForce = breakingForce;
        }
        else
        {
            currentBreakForce = 0f;
        }

        backRight01.motorTorque = currentAcceleration;
        backLeft01.motorTorque = currentAcceleration;

        backRight02.brakeTorque = currentBreakForce;
        backLeft02.brakeTorque = currentBreakForce;
        backRight01.brakeTorque = currentBreakForce;
        backLeft01.brakeTorque = currentBreakForce;

        currentTurnAngle = maxTurnAngle * Input.GetAxis("Horizontal");

        backLeft02.steerAngle = currentTurnAngle;
        backRight02.steerAngle = currentTurnAngle;
    }

}