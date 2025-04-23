import random

num = random.randint(1, 100)
print(num)  # optional: remove this for real guessing

while True:
    number = int(input('Guess the number between 1 to 100: '))

    if number > num:
        if number - num <= 10:
            print("You are close!")
        else:
            print('Too high')
                    

    elif number < num:
        if num - number <= 10:
            print("You are close!")
            
        else:
            print("Too low")

    else:
        print('You found it! 🎉')
        break
