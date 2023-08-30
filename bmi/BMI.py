
def calcu_bmi():
   height= float(input("enter your height in CM:"))
   weight= float(input("enter your weight in KG:")) 

   global BMI
   BMI= weight / (height/100)**2
   print(f"You BMI IS  {BMI}")
   
   
def interpetr_bmi(BM):
    if BMI <= 18.5:
      print("You are underweight.")
    elif 18.5 < BMI <= 24.9:
     print("Your weight is normal.")
    elif 25 < BMI <= 29.29:
     print("You are overweight.")
    else:
     print("You are obese.")

calcu_bmi()
interpetr_bmi(BMI) 




