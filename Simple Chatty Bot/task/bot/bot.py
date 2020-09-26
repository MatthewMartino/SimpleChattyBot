def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    x = 0
    stop = False
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    # age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    while x < 100000 and stop == False:
        if x % 3 == rem3 and x % 5 == rem5 and x % 7 == rem7:
            stop = True
        else:
            x += 1
    print("Your age is ", x, "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    ans = 0

    while ans != 2:
        ans = int(input())
        if ans == 2:
            print('Completed, have a nice day!')
        else:
            print("Please, try again.")

def end():
    print('Congratulations, have a nice day!')

greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
