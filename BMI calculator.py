#BMI Calculator
height=float(input("Enter your height in centimeters: "))
weight=float(input("Enter your weight in kg: "))
height=height/100
BMI=weight/(height*height)
print("Your Body Mass Index is: ", BMI)
if(BMI>0):
	if(BMI<=16):
		print("You are severely Underweight")
	elif(BMI<=18.5):
		print("You are Underweight")
	elif(BMI<=25):
		print("You are Healthy")
	elif(BMI<=30):
		print("You are Overweight")
	else:
		print("You are severely Overweight")
else:
	print("Enter valid Details !")
