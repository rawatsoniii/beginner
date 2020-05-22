# A very simple net present value (NPV) calculator that graphs the inputs and the calculated discounted values.
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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cash_flow = []
discounted_value = []
period = []

df = pd.DataFrame(columns=['Period','Cashflow', 'Present Value'])

def main():
    welcome()
    input_periods = int(input('Number of Periods: '))
    input_periods += 1
    for i in range(input_periods):
        cf = float(input('Cashflow for Period ' + str(i) + ': '))
        cash_flow.append(cf)
        period.append(i)
    rate = float(input('Discount Rate (as a decimal): '))
    calc(cash_flow,rate)
    plot(input_periods)

def welcome():
    print('Welcome.')
    print('This is a simple Net Present Value Calculator.')
    print('______________________________________________________________________')

def calc(p,r):
    # main calculator that iterates over each item in the list cash_flow
    # to calculate separate discounted values
    # and then appends each discounted value to the list discounted_value
    df['Period'] = period
    for cf in p:
        n = period.pop(0)
        pv = cf/((1+r)**n)
        discounted_value.append(pv)
    npv = sum(discounted_value)
    data()
    printout(npv)

def data():
    # inserts items from the lists into the dataframe
    df['Cashflow'] = cash_flow
    df['Present Value'] = discounted_value
    df.to_csv('Cashflow.csv', index=False)

def printout(n):
    # prints dataframe and the value returned to npv in calc()
    print('______________________________________________________________________')
    print(df)
    print('______________________________________________________________________')
    print('The Net Present Value of your cashflow inputs is: ', n)
    print('______________________________________________________________________')

def plot(per):
    # configures settings for a line chart to be created with matplotlib
    # and styled with seaborn
    df2 = df[['Cashflow', 'Present Value']]
    sns.set(style="whitegrid")
    sns.set_style("ticks")
    graph = sns.lineplot(data=df2, palette="bright", linewidth=2.5)
    graph.set(xlabel='Period', ylabel='Dollar Values')
    plt.xticks(np.arange(0, per, step=1))
    plt.legend(loc = 'lower right')
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    main()

# An example:

# Cashflows over five full years (5 periods) would normally have 6 cashflows;
# An initial outflow (representing an investment), 
# followed by a series of inflows (representing the investment returns).

# -100, 100, 110, 121, 133.10, 146.41

# This file was actually the basis for NPVCalc_Basic.py, but grew to the above code. NPVCalc_Basic.py was reuploaded. 
