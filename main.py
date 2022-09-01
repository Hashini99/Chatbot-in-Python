def welcome(bot_name,birth_year):
    print("Hello! I'm {0}.".format(bot_name))
    print("I was created in {0}. ".format(birth_year))

def guess_name():
    print('What is your name.')
    name=input()
    print("What a pretty name you have {0}!".format(name))

def guess_age():
    print('OK, Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {0}; that's a good time to start programming!".format(age))

def count():
        print('OK, shall we play a game. Tell me any number you want to count.')
        num = int(input())

        counter = 0
        while counter <= num:
            print("{0} !".format(counter))
            counter += 1

def test1():
        print("Let's test your python programming knowledge.")
        print("What will be the value of the following Python expression?")
        print("4 + 3 % 5")
        print("1.7")
        print("2.2")
        print("3.4")
        print("4.1")

        answer = 1
        guess = int(input())
        if (guess==answer):
            print("CORRECT!!")
        elif( guess != answer):
            print("WRONG!!Explanation: The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.")

def test2():

            print("Which of the following is used to define a block of code in Python language?")
            print("1.Indentation")
            print("2.Key")
            print("3.Brackets")
            print("4.All of the mentioned")

            answer = 1
            guess = int(input())
            if (guess == answer):
                print("CORRECT!!")
            elif (guess != answer):
                print("WRONG!!Explanation: The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.")


def test3():
    print("Which keyword is used for function in Python language?")
    print("1.Function")
    print("2.Def")
    print("3.Fun")
    print("4.Define")

    answer = 2
    guess = int(input())
    if (guess == answer):
        print("CORRECT!!")
    elif (guess != answer):
        print("WRONG!!Explanation: Answe is Def")

def test4():

            print("What is the order of precedence in python?")
            print("1.Exponential, Parentheses, Multiplication, Division, Addition, Subtraction")
            print("2.Exponential, Parentheses, Division, Multiplication, Addition, Subtraction")
            print("3.Parentheses, Exponential, Multiplication, Division, Subtraction, Addition")
            print("4.Parentheses, Exponential, Multiplication, Division, Addition, Subtraction")

            answer = 4
            guess = int(input())
            if (guess == answer):
                print("CORRECT!!")
            elif (guess != answer):
                print("WRONG!!Explanation: For order of precedence, just remember this PEMDAS (similar to BODMAS).")
def test5():

            print("Which of the following is not a core data type in Python programming?")
            print("1.Tuples")
            print("2.Lists")
            print("3.Class")
            print("4. Dictionary")

            answer = 3
            guess = int(input())
            if (guess == answer):
                print("CORRECT!!")
            elif (guess != answer):
                print("WRONG!!Explanation: Class is a user-defined data type.")


def end():
        print(' HAVE A NICE DAY!, KEEP PRACTICING!!!')
        print('.................................')
        print('.................................')
        print('.................................')
        input()


welcome('ABC','2022')
guess_name()
guess_age()
count()
test1()
test2()
test3()
test4()
test5()
end()
