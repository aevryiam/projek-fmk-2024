# input
the_height = float(input("Enter the height in cm: "))  
the_weight = float(input("Enter the weight in kg: "))  

# function for BMI
the_BMI = the_weight / (the_height/100)**2  

# printing the BMI  
print("Your Body Mass Index is", the_BMI)  
# specifying the range of BMI  
if the_BMI <= 18.5:  
    print("underweight")  
elif the_BMI < 25:  
    print("healthy")  
elif the_BMI <= 29.9:  
    print("overweight")  
else:  
    print("obese")  