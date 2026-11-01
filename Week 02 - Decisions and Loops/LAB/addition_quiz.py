"""

step 1: generte two single digit integers for number1 (e.g, 4) and number2 (e.g, 5)
step 2: prompt the student to answer, "what is 4 + 5?" (usr input)
step 3: check wether the student answer is correct

"""

import random

while True:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("try again")
