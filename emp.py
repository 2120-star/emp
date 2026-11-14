basic_salary = int(input("Enter the basic salary: "))
HRA = basic_salary * 20/100
DA = basic_salary * 10/100

gross_salary = basic_salary + HRA + DA
print("Gross Salary:", gross_salary)   
