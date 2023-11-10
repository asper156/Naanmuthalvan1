Certainly! Here's a simple Python program that determines whether a year entered by the user is a leap year or not using if-elif-else statements:

```python
# Get the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

This program takes a year as input from the user and checks the conditions for a leap year using if-elif-else statements. If the conditions are met, it prints that the year is a leap year; otherwise, it prints that it's not a leap year.
