# main driver function
def main():

    # greeting
    print("Welcome to the BMI Calculator. Input your height: ")
    ft = int(input("Feet: "))
    inch = int(input("Inches: "))
    weight = int(input("Weight(in pounds): "))

    # convert to inches
    totalinches = inch + (12 * inch)

# calculates bmi and assigns appropriate category
def calc_bmi(totalinches, weight):
    # weight conversion
    weight = weight*0.45
    # height conversion and then squared
    totalinches = (totalinches*0.025)**2
    # final bmi
    bmi = weight / totalinches
    return bmi

    # get category of bmi
    if(bmi <= 18.5):
        underweight = bmi
        return underweight
    # changed to greater than because one can not be underweight and normal simultaneously
    elif(bmi > 18.5 and bmi <= 24.9):
        normal = bmi
        return normal
    elif(bmi >= 25 and bmi <= 29.9):
        overweight = bmi
        return overweight
    elif(bmi >= 30):
        obese = bmi
        return obese
    else:
        print("Error occured.")

def display_bmi(underweight, normal, overweight, obese, bmi):
    if underweight:
        print("Your bmi is {bmi}, and you are underweight.")
    elif normal:
        print("Your bmi is {bmi}, and you are normal.")
    elif overweight:
        print("Your bmi is {bmi}, and you are overweight.")
    elif obese:
        print("Your bmi is {bmi}, and you are obese.")
    else:
        print("An error occured.")

