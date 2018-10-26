

counter = 1

while counter <= 18:
    par = int(input("Par of hole {0}: ".format(counter)))
    score = int(input("Score on hole {0}: ".format(counter)))
    if score - par == 0:
        print("par")
    elif score - par == 1:
        print("bogey")
    elif score - par == 2:
        print("dubble bogey")
    elif score - par == 3:
        print("tripple bogey")
    elif score - par > 3:
        print("bad hole")
    elif par - score == 3:
        print("birdie")
    elif par - score == 2:
        print("eagle")
    elif par - score == 3:
        print("albatross")
    elif par - score > 3:
        print("invalid score")    
counter += 1
