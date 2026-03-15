
#!/usr/bin/env python3

'''
Prompt the user for first name and display output of result
'''

first_name = input("Enter first name: " )
print (f"Good day, {first_name}")


'''
Prompts the user for first operand and second operand and store the values as float
'''

first_operand = float(input("enter first operand:"))
float(first_operand)

second_operand = float(input("enter second operand:"))
float(second_operand)


'''
Performing basic arithmetics 
'''

addition = first_operand + second_operand
subtraction = first_operand - second_operand
multiplication = first_operand * second_operand
division = first_operand / second_operand

'''
Displaying basic arithimetics outputs
'''

print(f"Result of addition as float: {float(addition)}, as integer: {int(addition)}")
print(f"Result of subtraction as float: {float(subtraction)}, as integer: {int(subtraction)}")
print(f"Result of multiplication as float: {float(multiplication)}, as integer: {int(multiplication)}")
print(f"Result of division as float: {float(division)}, as integer: {int(division)}")



print(f"Thank you {first_name}")


