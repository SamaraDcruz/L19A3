num = int(input("Enter a number:"))

i = 1
while i <= num:   # outer loop
    print("Checking number:", i)

    if i % 2 == 0:   # if divisible by 2
        while True:  # inner infinite loop
            print("Bye Bye")   # keeps printing forever

    i += 1