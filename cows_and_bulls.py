import random
def cow_bull(user_number, random_number):
    cows_bulls =[0,0]
    for i in range(len(random_number)):
        if user_number[i] == random_number[i]:
            cows_bulls[0] += 1
        elif user_number[i] in random_number:
            cows_bulls[1] += 1
    return cows_bulls

playing=True
random_number=str(random.randint(100,999))
guessed=0
while playing:
    guessed+=1
    print(random_number)
    user_number=input(str("Type number from 100 to 999: "))
    result = cow_bull(user_number,random_number)
    if result[0]<3:
        print("Cows: ", result[0], "Bulls:",result[1])
    else:
        if guessed==1:
             print("You guessed the number:",random_number, "from first time")
        else:
            print("You guessed the number:",random_number, "from", guessed, "times")
        playing=False
