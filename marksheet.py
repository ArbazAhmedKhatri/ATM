# getting bio from user
name = str(input("Enter name : "))
f_name = str(input("Enter Father's name : "))
clas = str(input("Enter Class : "))
rol_no = int(input("Enter roll number : "))

#getting marks from user
math = int(input("Enter Maths marks : "))
urdu = int(input("Enter Urdu marks : "))
eng = int(input("Enter English marks : "))
sci = int(input("Enter Science marks : "))

#calculate marks and percentage
total_marks = math+urdu+eng+sci
perentage = (total_marks*100)/400

#print Marksheet
print("=======================================")
print("           ANNUAL MARKSHEET            ")
print("=======================================")
print("Your name is : ",name)
print("Your Father's name : ",f_name)
print("Your class is : ",clas)
print("Your roll number is : ",rol_no)
print("=======================================")
print("                MARKS                  ")
print("=======================================")
print("  Subjects"+"   Total Marks"+"   Obtain Marks  ")
print("  English "+"       100    "+"     ",eng,"    ")
print("  Urdu    "+"       100    "+"     ",urdu,"    ")
print("  Maths   "+"       100    "+"     ",math,"    ")
print("  Science "+"       100    "+"     ",sci,"    ")
print("=======================================")
print("Total Marks : 400 "+"  Obtain Marks : ",total_marks)
print("Percentage  : ",perentage,"%")

#Grade Formula
if  perentage>79 : print("Your Grade is = A+")
elif perentage>69 : print("Your Grade is = A")
elif perentage>59 : print("Your Grade is = B")
elif perentage>49 : print("Your Grade is = C")
elif perentage>39 : print("Your Grade is = D")
else : print("Your are FAIL!")

#end marksheet
print("=======================================")