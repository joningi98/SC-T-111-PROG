first_position = int(input("Input a position between 1 and 10: "))
current_position = first_position

def left():
    if current_position <= 1:
        return current_position
    c = current_position - 1
    return c

def right():
    if current_position >= 10:
        return current_position
    c = current_position + 1
    return c



while True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    r_or_l = input("Input your choice: ")
    if r_or_l == "l":
        current_position = left()
    elif r_or_l == "r":
        current_position = right()
    else:
        print("New position is:", current_position)
        break

    print("New position is:", current_position)