# define a main function of the program.
def displayTable(purchasePrice, annualInterestRate):
# declare the required variables
#Holding interest rates
    downPaymentRate = 0
    annualInterestRate = annualInterestRate/100
    monthlyPayRate = 0.045
    print("\n");
# prompt the purcahse price from the user
#    purchasePrice = float(input(" Input Purchase Price: "));
#Calculate the down payment and store into the
# variable downpayment on annual interest rate
    downPayment = purchasePrice * downPaymentRate;
#Calculate the inital credit price and store into
    monthlyPayment=purchasePrice*monthlyPayRate
#Displaying credit information in a table
    month = 1
#Table Header
    print('\n Item Price: $%.2f | Down Payment: $%.2f' \
          % (purchasePrice, downPayment))
    head =' %5s %16s %16s %16s %9s %15s\n' % \
          ('Month','Starting Balance','Interest to pay',\
           'Principal to pay','Payment', 'Ending Balance')
#By the help of while loop check the current balance
    currentBalance = purchasePrice;
# until current balance is greater than zero
    table = head;
    while currentBalance > 0.00:
#Calculate the remaining balance and store into the
# variable balanceRemaing
        balanceRemaining = currentBalance-monthlyPayment
        monthlyInterest =(currentBalance*annualInterestRate)/12
        principalToPay = monthlyPayment-monthlyInterest

#Display a row of information with the calculated details
        line=' %3s %12.2f %17.2f %15.2f %15.2f %12.2f\n' % \
            (month, currentBalance, monthlyInterest, \
            principalToPay, monthlyPayment, balanceRemaining)   
        table +=line
#Compute the current balnce
        currentBalance = currentBalance - monthlyPayment
#increment for next month
        month += 1
    return table

def main():
    purchasePrice = float(input("Input Purchase Price: "))
    annualInterestRate = float(input("Input Annual Interest Rate:"))
    table = displayTable(purchasePrice, annualInterestRate)
    print(table)

if __name__ == "__main__":
    main();#call main function
