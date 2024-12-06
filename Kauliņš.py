import random
a = random.random()
print(a)
for i in range(0,5):
    a = random.randint(1,6)
    print(a)
    b = random.randint(1,6)
    print(b)
    c = a + b
    print(f"{a} | {b} | {a+b}")



import random

number = random.randint(1,10)

Attempts = 0

while True:

    Attempts += 1   
    guess = input("Uzmini ciparu no viens līdz desmit:")

    guess = int(guess)

    if guess == number:
        print("Uzminēji")
        print("Mēģinājumi:", Attempts)
    
    elif guess < number:
        print("Vairāk")
    
    else:
        guess > number
        print("Mazāk")
   
