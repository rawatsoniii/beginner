# A very simple net present value (NPV) calculator.
# NPV is found by summing the discounted values of all future cashflows.

# User inputs the number of periods, a cash flow for each period, and the discount rate.
# Zero and negativbe values are acceptable.
# The discount rate must be entered as a decimal, e.g. 9% == 0.09

# As Python lists start w/ index 0:
#   "Period 0" is t=0, e.g. the initial cashflow immeadiately at the start of the series.
#   A user that enters "5" for periods will need to enter 6 cashflows.
#   To correct for the indexing issue, periods += 1 has been included.

# See the bottom for an example. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

cashflow = []
discountedvalue = []
period = []

df = pd.DataFrame(columns=['Period', 'Cashflow', 'Present Value'])
df2 = df

def main():
    welcome()
    periods = int(input('Number of Periods: '))
    periods += 1
    for i in range(periods):
        cf = float(input('Cashflow for Period ' + str(i) + ': '))
        cashflow.append(cf)
        period.append(i)
    rate = float(input('Discount Rate (as a decimal): '))
    calc(cashflow,rate)
    plot(period)

def welcome():
    print('Welcome.')
    print('This is a simple Net Present Value Calculator.')
    print('______________________________________________________________________')

def calc(p,r):
    for cf in p:
        n = int(p.index(cf))
        pv = cf/((1+r)**n)
        discountedvalue.append(pv)
    npv = sum(discountedvalue)
    data()
    printout(npv)

def data():
    df['Period'] = period
    df['Cashflow'] = cashflow
    df['Present Value'] = discountedvalue
    df.to_csv('Cashflow.csv', index=False)

def printout(n):
    print('______________________________________________________________________')
    print(df)
    print('______________________________________________________________________')
    print('The Net Present Value of your cashflow inputs is: ', n)
    print('______________________________________________________________________')

def plot(per):
    per -= 1
    df2 = df[['Cashflow', 'Present Value']]
    sns.lineplot(data=df2, palette="bright", linewidth=2.5)
    plt.xlim(0, per)
    plt.show()
    
if __name__ == "__main__":
    main()

# An example:

# Cashflows over five full years (5 periods) would normally have 6 cashflows;
# An initial outflow (representing an investment), 
# followed by a series of inflows (representing the investment returns).

# -100, 100, 110, 121, 133.10, 146.41
