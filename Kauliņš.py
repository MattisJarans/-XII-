import random

number = random.randint(1,10)

guess = input("Uzmini ciparu no viens līdz desmit:")

guess = int(guess)

if guess == number:
    print("Uzminēji")
    
elif guess < number:
    print("Vairāk")
    
else:
    guess > number
    print("Mazāk")
   