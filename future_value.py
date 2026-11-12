#Daniel E Salazar Gomez
#CMP-131-86520
#Week 9 
#Lab 01
#Assigment 9
#11/12/2026
def futureValue(presentValue, interestRate, months):
    future = presentValue * (1 + interestRate) ** months
    return future
def main():
    print("Savings Account Future Value Calculator")
    presentValue = float(input("Enter the present value: $"))
    if presentValue < 0:
        print("Error: Present value cannot be negative.")
        return
    interestRate = float(input("Enter the monthly interest rate (%): "))
    if interestRate < 0:
        print("Error: Interest rate cannot be negative.")
        return
    interestRate = interestRate / 100
    months = int(input("Enter the number of months: "))
    if months <= 0:
        print("Error: Number of months must be greater than zero.")
        return
    future = futureValue(presentValue, interestRate, months)
 
    print("Present Value: ${:.2f}".format(presentValue))
    print("Monthly Interest Rate: {:.2f}%".format(interestRate * 100))
    print("Number of Months:", months)
    print("Future Value: ${:.2f}".format(future))


main()
