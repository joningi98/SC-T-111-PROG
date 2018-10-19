top = 10
bottom = 1

while True:
    try:
        start = int(input("Enter a number between 1 and 10: "))
        current_pos = start
        break
    except ValueError:
        print("Please enter a integer")


def left():
    if current_pos <= bottom:
        return current_pos
    else:
        c = current_pos - 1
    return c


def right():
    if current_pos >= top:
        return current_pos
    else:
        c = current_pos + 1
    return c


def move():
    print("l - for moving left \n"
          "r - for moving right \n"
          "Any other letter for quitting")


while True:
    move()
    l_or_r = input("Input your choice: ")
    if l_or_r == "l":
        current_pos = left()
    elif l_or_r == "r":
        current_pos = right()
    else:
        print("New position is:", current_pos)
        break
    print("New position is:", current_pos)
