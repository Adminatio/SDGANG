Name=input("Enter the name:")
Emp_id=int(input("Enter the id:"))
basic_sal=int(input("Enter the basic salary:"))
DA=25
HRA=5
gross=basic_sal+((DA*basic_sal)/100)+((HRA*basic_sal)/100)
print("The Gross salary of an employee is:",gross)

