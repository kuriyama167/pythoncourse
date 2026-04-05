def divide (dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    return dividend / divisor

grades=[89, 92, 76, 85, 90]

print("welcome to the grade calculator!")
try:
    average = sum(grades) / len(grades)
except ZeroDivisionError as e:
    print("Error: No grades entered. Cannot calculate average.")
else:
    print(f"The average grade is: {average}")
finally: 
    print("Thank you for using the grade calculator!")