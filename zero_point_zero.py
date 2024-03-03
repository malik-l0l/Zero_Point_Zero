"""
This is my first personal project using python.
I did not know about Git/GitHub back then
so, I copy-pasted my code in this file again and again
until I get a satisfied result.
"""


# ========================================================================================
# TEST 6
# less code more function
# more terminal ui improvement
# eval function is used
# known exceptions handled

def calculator():
    last_num = 0.0

    print("choices = [ + , - , * , / , % , q ]\n")
    print(f"please type something like below:\n{last_num} + 5 or {last_num} - 5\n")

    # while (x := input(f" = {last_num} ")) != "q":
    while True:
        x = input(f" = {last_num} ")
        if x == "q":
            print(f" = {last_num} ")
            break

        try:
            last_num = eval(f"{last_num} {x}")
        except SyntaxError:
            print(f"\nplease type something like below:\n{last_num} + 5 or {last_num} / 5\n")
        except NameError:
            print(f"\nPlease type numbers!!\nplease type something like below:\n{last_num} + 5 or {last_num} / 5\n")
        except ZeroDivisionError:
            print(f"\n{last_num} / 0  => :| \n")


if __name__ == '__main__':
    calculator()

# =============================== VERSIONS ===============================================

# TEST 1
# find sum
"""
sum = 0
y = []

while True:
    a = int(input("Num: "))
    y.append(a)

    playagain = input('Enter (+/=): ').lower()

    if playagain != '+':
        break

for x in y:
    sum = sum + x
print("total = ", sum)
"""

# ========================================================================================

# TEST 2
# find +,-
'''
sum = 0
y = list()

while True:
    a = int(input("Num: "))
    y.append(a)

    if a == 0:
        break

b = input("(+/-): ")

if b == "+":
    for x in y:
        sum = sum + x
    print("total = ", sum)

elif b == "-":
    for x in y:
        sum = sum - x
    print("total = ", sum)
'''

# ========================================================================================

# Test 3
# find +,-,*
'''
import functools

sum = 0
y = list()

while True:
    x = input("Num : ")
    if x == "":
        break
    else:
        y.append(int(x))

b = input("(+/-/*): ")

if b == "+":
    for x in y:
        sum = sum + x
    print("total = ", sum)

elif b == "-":
    for x in y:
        sum = sum - x
    print("total = ", sum)

elif b == "*":
    function = lambda x, y: x * y
    factorial = functools.reduce(function, y)
    print("Results = ", factorial)
'''

# ========================================================================================

# Test 4
# multiplication works and ask for {+,-,*} infinitely
# used lambda fn

"""
import functools

def calculator():

    y = list()

    while True:
        x = input("Num : ")
        
        if x.isdigit():
            x = int(x)
            y.append(int(x))
        elif x == "":
            break
        else:
            print("Please enter a number :)")

    b = None

    choices = ["+", "-", "*"]
    while b not in choices:
        b = input("(+/-/*): ")

    if b == "+":
        function = lambda x, y: x + y
        add = functools.reduce(function, y)
        print("=================\nResult = ", add, "\n=================")

    elif b == "-":
        function = lambda x, y: x - y
        subtract = functools.reduce(function, y)
        print("=================\nResult = ", subtract, "\n=================")

    elif b == "*":
        function = lambda x, y: x * y
        factorial = functools.reduce(function, y)
        print("=================\nResult = ", factorial, "\n=================")

    play_again = input("Do you want to calculate(y/n):").lower()

    if play_again == "y":
        y.clear()
        calculator()
    else:
        print("thank you")


calculator()
"""

# ========================================================================================

# TEST 5
# add sign btw numbers 3+6*8/9

"""
def calculator():
    op_list = [0]
    choices = ["+", "-", "*", "/", "%", "q"]

    choice = None
    while True:
        print(f"last : {op_list[len(op_list) - 1]}")

        choice = input("('+','-','*','/','%','q')\n : ")
        
        if choice == "q":
            break
        elif choice in choices:
            num = input("num :")
            if num == "q":
                break
            elif num.isdigit():
                x = eval(f"{op_list[len(op_list) - 1]} {choice} {num}")
                op_list.append(x)
"""

# ========================================================================================
