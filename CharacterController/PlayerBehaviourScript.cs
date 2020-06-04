using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[RequireComponent(typeof(Rigidbody2D))]
public class PlayerBehaviourScript : MonoBehaviour
{

    private Rigidbody2D m_myRigidbody; //The rigidbody of this object
    private bool m_grounded; //boolean if the player touches the ground
    private int m_onWall; //-1 if the player touches a wall in -x direction, 1 if the player touches a wann in x direction, 0 otherwise
    private float m_horizontalInput;

    [SerializeField,Tooltip("the maximum hoizontal velocity the player can take on")]
    private float m_maxVelocity;
    [SerializeField, Tooltip("the acceleration of the player along the x-axis")]
    private float m_horizontalAccelerationForce;
    [SerializeField, Tooltip("the speed for jumping")]
    private float m_jumpVelocity;
    [SerializeField, Tooltip("the default gravity that applies to the player")]
    private float m_normalGravity;
    [SerializeField, Tooltip("gravity adjustment for descending to make jumping more enjoyable")]
    private float m_decendingGravity;
    [SerializeField, Tooltip("gravity adjustment for short hops")]
    private float m_shortJumpGravity; 


    // Start is called before the first frame update
    void Start()
    {
        m_myRigidbody = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        m_horizontalInput = Input.GetAxisRaw("Horizontal");

        if (Input.GetButtonDown("Jump") && m_grounded) 
        {
            Jump();
        }
        if (Input.GetKey("escape"))
        {
            Application.Quit();
        }
    }

    void FixedUpdate()
    {
        m_grounded = m_myRigidbody.IsTouchingLayers(LayerMask.GetMask("Ground"));
        WallCheck();
        Move();
        AdjustGrav();
    }
    
    /// <summary>
    /// checks if the player is attached to a wall and sets m_onWall apropriatly
    /// </summary>
    private void WallCheck()
    {
        if (Physics2D.Raycast(m_myRigidbody.position, Vector2.down, 2, LayerMask.GetMask("Ground")))
        {
            m_onWall = 0;
        }
        else if (Physics2D.Raycast(m_myRigidbody.position, Vector2.left, 2, LayerMask.GetMask("Ground")))
        {
            m_onWall = -1;
        } else if (Physics2D.Raycast(m_myRigidbody.position, Vector2.right, 2, LayerMask.GetMask("Ground")))
        {
            m_onWall = 1;
        }
        else
        {
            m_onWall = 0;
        }
    }

    /// <summary>
    /// accelerates, descelerates or stops the player depending on the input
    /// </summary>
    private void Move()
    {
        if (Mathf.Abs(m_myRigidbody.velocity.x) < m_maxVelocity)
        {
            m_myRigidbody.AddForce(new Vector2(m_horizontalInput * m_horizontalAccelerationForce, 0));
        }
        if (m_horizontalInput == 0 && m_grounded)
        {
            m_myRigidbody.velocity -= new Vector2(m_myRigidbody.velocity.x, 0);
        }
    }

    /// <summary>
    /// applies the jumpVelocity to the rigidbody
    /// </summary>
    private void Jump()
    {
        if (m_onWall == -1)
        {
            m_myRigidbody.velocity = Vector2.one*m_jumpVelocity;
        }
        else if (m_onWall == 1)
        {
            m_myRigidbody.velocity = (Vector2.up+Vector2.left)*m_jumpVelocity;
        }
        else
        { 
            m_myRigidbody.velocity = new Vector2(m_myRigidbody.velocity.x, m_jumpVelocity);
        }
    }

    /// <summary>
    /// adjusts the gravity while falling, jumping while holding the jump button for a high jump and while sliding alon a wall
    /// </summary>
    private void AdjustGrav()
    {
        if (m_myRigidbody.velocity.y < -0.001 && m_grounded) //player is sliding along a wall
        {
            m_myRigidbody.gravityScale = 1;
        }
        else if (m_myRigidbody.velocity.y < -0.001) //player is falling
        {
            m_myRigidbody.gravityScale = m_decendingGravity;
        }
        else if (m_myRigidbody.velocity.y > 0.001 && !Input.GetButton("Jump")) //player is not holding jump while ascending -> shorter jump
        {
            m_myRigidbody.gravityScale = m_shortJumpGravity;
        }
        else
        {
            m_myRigidbody.gravityScale = m_normalGravity;
        }
    }
}