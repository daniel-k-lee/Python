"""
File: tidbitwithgui.py
Project 8.7

GUI for tidbit program.

Inputs: purchase price and annual interest rate.
"""

from breezypythongui import EasyFrame

class TidbitGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title = "Tidbit Loan Scheduler")
        """Input fields"""
        self.addLabel(text="Purchase Price", row=0, column=0)
        self.priceField = self.addIntegerField(value=4900, row=0, column=1)
        self.addLabel(text="Annual Interest Rate", row=1, column=0)
        self.rateField = self.addFloatField(value=5.0, row=1, column=1)
        """Command button"""
        self.addButton(text="Compute", row=2, column=0, columnspan=2, command=self.computeSchedule)
        """Output text box"""
        self.outputArea = self.addTextArea(row=3, text=" ", column=0, columnspan=2, width=30, height=30)
        


    def computeSchedule(self):
        """Event handler for the Compute button."""
        # Write your code here
        table = displayTable(self.priceField.getNumber(), self.rateField.getNumber())
        self.outputArea.setText(table)

def displayTable(purchasePrice, annualInterestRate):
# declare the required variables
#Holding interest rates
    downPaymentRate = 0
    annualInterestRate = annualInterestRate/100
    monthlyPayRate = 0.045
    #print("\n");
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
    #print('\n Item Price: $%.2f | Down Payment: $%.2f' \
    #      % (purchasePrice, downPayment))
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
    """Instantiate and pop up the window."""
    TidbitGUI().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")

