#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# BMI Function
def bmi_calculator(weight, height):
    bmi = weight/ ((height/100) ** 2)
    return bmi 


# In[ ]:


weight = float(input('What is your weight (kgs) ?: '))
height = float(input('What is your height (cm)?: '))
bmi = bmi_calculator(weight, height)
print("Your BMI is {}".format(bmi))


if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You have a normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are Overweight")
else :
    print("You are Obese")


# In[ ]:




