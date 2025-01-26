# Ask for name
print(f"What is your name: ")
# We can use simple string for input here
name = input()
print(f"Hello", name,"!")

# Ask for age
print(f"What is your age: ")
age = input()

# Ask for years to add
print(f"How many years to add to your age: ")
varyAge = input()

#Here we need to convert the string to integer and use concatenation
print(f"In " + str(varyAge) +  " years you will be " + str(int(age) + int(varyAge)) + " years old")

print(f"Enter the number of hours worked: ")
hours = input()

print(f"Enter your hourly wage, without the $: ")
wage = input() 

#Calculate gross weekly pay
gross = float(hours) * float(wage)
print(f"Your gross pay is: " + str(gross)) 

#52 weeks are in a year
annual = gross * 52 
print(f"Your estimated annual gross pay is: $" + str(annual))
