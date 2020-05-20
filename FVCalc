# Simple Future Value Calculator

# This compounds at a fixed periodic rate and assumes there are no payments/coupons.

def calc(PV, r, n):
    FV = PV*((1+r)**n)
    return FV

def main():
    print("This is a simple future value calculator.")
    PresVal = float(input("Please enter a present value: "))
    rate = float(input("Please enter a compounding rate (stated as a decimal): "))
    per = float(input("Please enter the number of periods to compound over: "))
    FV = calc(PresVal, rate, per)
    print("The present value of ", PresVal, "compounded at a periodic rate of ", rate, "over ", per, "periods has a future value equal to: ", FV)

if __name__ == '__main__':
    main()
