a=input("Melanie Dental Clinic")
print("",a)
print("*.........................*")

Patient_name= input("Patient's name: ")
print("My name is",Patient_name)
visited_before = input("Has the patient been here before? (Yes/No): ")
print("",visited_before)
last_visit = input("How many days since your last vist:")
print(last_visit,"days")
height = int(input("What is the patient’s height (in cm)?: "))
print(height,"cm")
present_weight = float(input("What is the patient’s weight (in kg)?: "))
print("The patient's weight is",present_weight, "kg")
last_weighed = input("When was the patient last weighed in (1/1/2000 if never weighed)?: ")
print("The patient's was last weighed on",last_weighed)
previous_weight = float(input("What was the patient’s weight (in kg, -1 if never weighed)?: "))
print("The patient's previous weight was", previous_weight, "kg")
practitioner_assessment = int(input("Practitioner’s overall assessment of the patient’s health (-5 to +5)?: "))
print("Practitioner's assessment:", practitioner_assessment)

y=input("Return Report")
print("",y)

x=input("Melanie Dental Clinic")
print("",x)
print("*........................*")

BMI = (present_weight/ (height**2)) *10000

if BMI > 30:
    intermediate_score = 0
elif 25 <= BMI <= 29.9:
    intermediate_score = 3
elif 18.5 <= BMI <= 24.9:
    intermediate_score = 5
else:
    intermediate_score = 3





