# Ferrin Senter (fas96) SW Testing and QA Assignment 2

from app import app

# main driver function
def main():
    # greeting
    print("Welcome to the BMI Calculator. Enter your height and weight.")
    ft = int(input("Feet: "))
    inch = int(input("Inches: "))
    weight = int(input("Weight(in pounds): "))

    # convert feet to inches and add to inches
    totalinches = inch + (ft*12)

    # function calls
    bmi = calc_bmi(totalinches, weight)
    display_bmi(bmi)

# calculates bmi and assigns appropriate category
def calc_bmi(totalinches, weight):
    # weight conversion
    weight = weight*0.45
    # height conversion and then squared
    totalinches = (totalinches*0.025)**2
    # final bmi
    bmi = float("{:.1f}".format(weight / totalinches))

    # dictionary
    category = ""

    # get category of bmi
    if(bmi <= 18.5):
        category = "underweight"
    # changed to greater than because one can not be underweight and normal simultaneously
    # boundary shift induced
    elif(bmi > 18.4 and bmi <= 24.9):
        category = "normal"
    elif(bmi >= 25 and bmi <= 29.9):
        category = "overweight"
    elif(bmi >= 30):
        category = "obese"
    else:
        print("Error occured.")

    # dictionary and return
    info = {"BMI" : bmi, "Category" : category}

    return info

def display_bmi(info):
    if info['Category'] == "underweight":
        print(f"BMI: {info['BMI']}, Classification: Underweight")
    elif info['Category'] == "normal":
        print(f"BMI: {info['BMI']}, Classification: Normal")
    elif info['Category'] == "overweight":
        print(f"BMI: {info['BMI']}, Classification: Overweight")
    elif info['Category'] == "obese":
        print(f"BMI: {info['BMI']}, Classification: Obese")
    else:
        print("An error occured.")


# call main function
main()
