# --------- Start with text
print("This tool will provide you with a suggested calories intake based on a few characteristics.")

# --------- Declare variables
bmr_const_men = 66
#bmr_const_women = 665
#weight_const_women = 9.6 #a constant used in calculations for women
weight_const_men = 13.7 #a constant used in calculations for men
#height_const_women = 1.8 #a constant used in calculations for women
height_const_men = 5 #a constant used in calculations for men
age_const_men = 6.8
#age_const_women = 4.7
activity = [1.2, 1.3, 1.5, 1.7, 2.1]

# --------- input a float for weight
while True:
    try:
        weight = float(input("How much do you weight? Please provide answer in kgs with up to 1 decimal point: e.g. 65.3"))
        break
    except ValueError:
        print("Please input a valid number corresponding to your weight")
        continue

# --------- input an int for height
while True:
    try:
        height = int(input("What is your height? Please provide answer in cms"))
        break
    except ValueError:
        print("Please input a valid number corresponding to your height")
        continue

# --------- input an int for age
while True:
    try:
        age = int(input("What is your age in years?"))
        break
    except ValueError:
        print("Please input a valid number corresponding to your age")
        continue

# --------- Select your gender
# --------- This feature is not implemented yet

# --------- Select your desired activity model
print("Please provide your activity model according to the provided information:")
print("1 - little to no activity + office work")
print("2 - low activity (1-2 trainings per week + office work)")
print("3 - medium activity (3-4 trainings per week + office work)")
print("4 - high activity (3-4 trainings per week + physical work)")
print("5 - very high activity (professional sportsperson with daily trainings)")
activity_input = int(input("Input a number from the list above."))

# --------- temp variable to avoid issues later on
BMR_temp = bmr_const_men + (weight_const_men * weight) + (height_const_men * height) - (age_const_men * age)

# --------- When user inputs activity in range between 1 and 5, the program outputs a valid calory intake
activity_input = 0
while 0 < activity_input or 5 < activity_input:
    try:
        activity_input = int(input("Input a number from the list above."))
    except ValueError:
        print("Incorrect value. Please select a value between 1-5")

# --------- obsolete
#while activity_input in range(1, 5):
#    try:
#        BMR_temp * activity[activity_input-1]
#        break
#    except ValueError:
#        print("Incorrect value. Please select a value between 1-5")
#        continue
print("Your desired calory input is:")
print(BMR_temp * activity[activity_input-1])