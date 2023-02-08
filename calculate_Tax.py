'''
Calculate income tax for the given income by adhering to the below rules

Taxable Income	    Rate (in %)
First $10,000	    0
Next $10,000	    10
The remaining	    20

Expected Output:
For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.

'''
def cal_tax():
    salary=int(input('Enter your salary: '))
    first=int(10000)
    second=int(10000)
    remaining=salary-(first+second)
    tax=first*0+second*.1+remaining*.2
    print('Income tax is ',tax)

cal_tax()

