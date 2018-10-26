low = input("please enter a low number ")
high = input("please enter a high number ")

low_int = int(low)
high_int = int(high)

counter = low_int

#while counter <= high_int :
    #if counter % 2 == 1:
       # print(counter)
    #counter += 1

for number in range (low_int, high_int + 1):
    if number % 2 == 1:
        print(number) 
