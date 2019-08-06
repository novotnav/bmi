print("Welcome to the Basal Energetic Expenditure calculator!")

sex = input("Select your sex: f for female, m for male: ")
weight = input("Insert your weight in kilograms: ")
height = input("Insert your height in centimetres: ")
age = input("Insert your age in years: ")

if sex is not "f" and sex is not "m":
    print("Please insert only letters f or m to select your sex!")
    quit()
try:
    val = int(weight)
    weight = int(weight)
except ValueError:
    print("Please use numbers to insert weight!")
    quit()
try:
    val = int(height)
    height = int(height)
except ValueError:
    print("Please use numbers to insert height!")
    quit()
try:
    val = int(age)
    age = int(age)
except ValueError:
    print("Please use numbers to insert age!")
    quit()

beef = 655 + (9.6 * weight + 1.7 * height) - (4.7 * age)
beem = 66 + (13.7 * weight + 5 * height) - (6.8 * age)

if sex is "f":
    print("Your BEE is " + str(beef) + " kilocalories per day.")
if sex is "m":
    print("Your BEE is " + str(beem) + " kilocalories per day.")

quest = input("Do you want to convert the result to kilojouls per day? Yes: type y, No: type n: ")

convf = beef * 4.184
convm = beem * 4.184

if quest is "y":
    if sex is "f":
        print("Your BEE is " + str(convf) + " kilojouls per day. ")
        print("Thank you for using this calculator!")
    if sex is "m":
        print("Your BEE is " + str(convm) + " kilojouls per day. ")
        print("Thank you for using this calculator!")
if quest is "n":
    print("Thank you for using this calculator!")
if quest is not "y" and quest is not "n":
    print("Please type only y or n to confirm or decline the conversion!")





