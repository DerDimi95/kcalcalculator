

#Calculate the BMR

#in KG
weight = float(input("Enter your weight in KG: "))
#in CM
height = float(input("Enter your height in CM: "))
#age
age = int(input("Enter your Age: "))
#BodyFat%
body_fat_percentage = float(input("Enter your Body Fat %:\n "))
#activity multiplier
print("| LIFESTYLE & TRAINING FREQUENCY        | EXAMPLE                                                                           | ACTIVITY MULTIPLIER |\n|---------------------------------------|-----------------------------------------------------------------------------------|---------------------|\n| Sedentary + Training 3-6x/wk          | Works a desk job, very little activity outside of lifting                         | 1.2 - 1.5           |\n| Lightly Active + Training 3-6x/wk     | Works a desk job, takes pet for a walk most days in addition to lifting           | 1.5 - 1.8           |\n| Moderately Active + Training 3-6x/ wk | Works as a full-time waitress, occa- sionally plays tennis in addition to lifting | 1.8 - 2.0           |\n| Highly Active + Training 3-6x/wk      | Works as a construction worker, reg- ular hiking in addition to lifting           | 2.0 - 2.2           |")
activity_multiplier = float(input("\nEnter your activity multiplier, refer to the table above: "))
#leanbodymassindex
lean_body_mass = 1.1 * weight - 128 * (weight / height)**2
#lbm multiplier to calculate protein
lbm_multiplier = float(input("Enter your protein multiplier, 1.2 - 1.6 (the leaner you are the closer you multiply by 1.6: "))



bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
maintaince_calories = bmr * activity_multiplier


#BMR * Activity Multiplier <-- to get the estimated maintaince calories while being active 
#protein intake -> LBM * 1.2 - 1.6 (the leaner you are the closer you multiply by 1.6)

protein = (lean_body_mass* 2.2) * lbm_multiplier

#calculate calories for fat loss
if body_fat_percentage > 25:
    maintaince_calories_deficit = maintaince_calories * 0.25
else:
    maintaince_calories_deficit = maintaince_calories * 0.20

maintaince_calories = maintaince_calories - maintaince_calories_deficit

print("You should eat: ", maintaince_calories, "Kcal and ", protein, "gr of protein\n Keep in mind to recalculate everything once a week !" )



