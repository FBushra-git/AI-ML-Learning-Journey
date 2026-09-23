salary = float(input("Enter salary : ")
)
if (salary < 30000):
    print("final_tax_rate = ", 5/100)
elif(salary <= 70000):
    print("final_tax_rate = ", 15/100)
elif(salary > 70000):
    print("final_tax_rate = ",25/100)
