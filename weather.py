degree =int(input("Enter the Degree:"))
if degree <=20:
    print("Cold Weather")
elif degree >20 and degree <=38:
    print("Normal Weather")
else:
    print("Hot! Weather")
fahrenheit=((degree*1.8)+32)
print("The Fahrenheit value is ",fahrenheit,"F")