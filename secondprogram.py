food= input ("Enter food : ")
eat= "yes" if food=="fruite" else "no"

print(eat)

food=input("food : ")
eat= "yes you can eat." if food== "fruite" or food == "meet" else "nooo you can't eat. leave it now."
print(eat)
food= input("food: ")
print("sweet") if food== "drinks" else print("no bro leave it pleace.")
"""
***Another example.***"""
   
age= int (input("age= "))
vote=("yes you are eligeble", "no you are not eligable")[age>=18]
print(vote)


