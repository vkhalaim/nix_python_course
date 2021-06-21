from random import randint


counter = 0

while counter < 100:
    num = randint(0, 1000)

    print(num)

    if num == 777:
        print("There was number 777 in 100 tries!")
        break

    if counter == 99:
        raise ValueError("There was no 777 number in 100 tries :(")

    counter += 1
