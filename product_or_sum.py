#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

def product_or_sum(a,b):
    if a*b<=1000:
        c= a*b;
        return c;
    else:
        c= a+b
        return c

result=product_or_sum(a,b)
print(f"result is {result}")
