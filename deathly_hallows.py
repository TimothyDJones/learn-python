 # deathly_hallows.py
 # Draws the Harry Potter Deathly Hallows symbol
 # using Python Turtle graphics.

def deathly_hallows():
    import turtle

    bob = turtle.Turtle()
    # Draw square
    for i in range(4):
        bob.forward(200)
        bob.left(90)
    
    # Draw equilateral triangle
    for i in range(3):
        bob.forward(200)
        bob.left(120)

    bob.forward(95)

    # Draw an approximated circle
    for i in range(36):
        bob.forward(10)
        bob.left(10)

    # Draw vertical line
    bob.forward(6)
    bob.left(90)
    bob.forward(172)



if __name__ == "__main__":
    deathly_hallows()