# A very simple net present value (NPV) calculator.
# NPV is found by summing the discounted values of all future cashflows.

# User inputs the number of periods, a cash flow for each period, and the discount rate.

# For the purposes of calculating the discounted value (NPV):
#   Zero and negativbe values are acceptable.
#   The discount rate must be entered as a decimal, e.g. 9% == 0.09

# As Python lists start w/ index 0:
#   "Period 0" is t=0, e.g. the initial cashflow immeadiately at the start of the series.
#   A user that enters "5" for periods will need to enter 6 cashflows.
#   To correct for the indexing issue, periods += 1 has been included.

import math

cashflow = []
discountedvalue = []    

def main():
    welcome()
    periods = int(input('Number of Periods: '))
    periods += 1
    for i in range(periods):
        cf = float(input('Cashflow for Period ' + str(i) + ': '))
        cashflow.append(cf)
    rate = float(input('Discount Rate (as a decimal): '))
    calc(cashflow,rate)

def welcome():
    print('Welcome.')
    print('This is a simple Net Present Value Calculator.')

def calc(p,r):
    for cf in p:
        n = int(p.index(cf))
        fv = cf/((1+r)**n)
        discountedvalue.append(fv)
    npv = sum(discountedvalue)
    printout(cashflow, discountedvalue, npv)

def printout(cshflw, disval, netval):
    print("The cashflows are: ", cshflw)
    print("The discounted values are: ", disval)
    print("The net present value is: ", netval)

if __name__ == "__main__":
    main()

# Consider pandas
# CHANGE THE SIGNIFICANT DIGITS
