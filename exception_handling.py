try:
    age=int(input("Age: "))
    income=int(input("Income:"))
    risk = income/age
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid Value")