# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#Eligibility for voting
age = int(input('Enter input: '))

if (age >= 18):
    print('Eligible to vote')
else:
    print('Not eligible to vote')

#Find the lowest number
print('Enter two numbers: ')
Number1 = int(input("Number 1: "))
Number2 = int(input('Number 2: '))

if(Number1 == Number2):
    print('Both numbers are equal: ')
elif (Number1 >= Number2):
    print('Number 1 is greater than Number2')
else:
    print('Number1 is the lowest number')

#Employee bonuses
Time =int(input('Enter your time of services: '))
Salary = int(input('Enter your salary: '))
if(Time>=10):
    Salary = Salary + Salary*10/100
    print(Salary)
elif (Time >= 6 and Time <= 10):
    Salary = Salary +Salary*8/100
    print(Salary)
elif (Time < 6):
    Salary = Salary + Salary*5/100
    print(Salary)
else:
    print('You did not enter your salary and time' + str(Salary))

# Program to give suggested footwear
num1 = float(input('Pick a number: '))
num2 = float(input('Pick a number: '))

if num1 <= num2:
    if num1 == num2:
        print('Num1 and Num2 are equal')
    else:
        print('Not equal')
elif num1 > num2:
        print('Greater!')
else:
        print('Less!!')

name = input('Enter your name: ')
friend_name = input('Enter your friends name: ')

if name == friend_name:
    friend = input("Do you and your friend really have the same name? Type yes or no: ")
    friend = str.lower(friend)
    if friend == "yes":
        print("Having the same name is cool!")
    elif friend == 'no':
        friend_name = input("Enter another name besides your own: ")
        print("Your friends name is: ", friend_name + ".")
    else:
        print("You did not enter yes or no.")
else:
    print("Your friend's name is", friend_name + ".")

name = ""

while True:
        name = input('Enter a one-word name, friends use to greet you: ')
        if name.isalpha():
            print("\nGood to see you: ", name.title())
            break #without this keyword it will run until kingdom comes
        else:
            print("\nSorry, enter one-word using letters only")

i = 1 #increment

while i < 6:
    print(i)
    i += 1

fruits =["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
