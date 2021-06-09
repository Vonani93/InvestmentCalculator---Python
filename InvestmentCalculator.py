#COMPULSORY TASK 2

# Importing math

import math

# requesting the user to input financial information

P = float(input("write your deposit amount here: "))
i = float(input("write the interest rate, in percentage, here: "))
t = float(input("write the number of years you are willing to invest, here: "))
interest = input("do you want 'simple' or 'compound' interest? write your answer here: ").lower()

# Recognizing r as a formula

r = i/100

# calculating the return on investment, depending on user's choice

if(interest == "simple"):
    print(round(P*(1 + r * t), 2))   
elif(interest == "compound"):
    print(round(P*math.pow(1 + r, t), 2))
else:
    print(round(P*(1 + r * t), 2))
    print(round(P*math.pow(1 + r, t), 2))
