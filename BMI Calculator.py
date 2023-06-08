# This is a sample Python script.
import bmi as bmi


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def BMI():

    print('bmi')
#prompt the input
    height = int(input('Enter your height: ')) /100
    weight = int(input('Enter your weight: '))

    bmi = weight/(height**2)




    if (bmi < 18.5):
        print('underweight')
    elif (bmi >= 18.5 and bmi < 24.9):
        print('healthy range')
    elif (bmi >= 25 and bmi < 29.9):
         print('overweight')
    elif(bmi >= 30 and bmi < 39.9):
        print('obesity')
    elif (bmi >= 40):
        print('severe obesity')

BMI()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
