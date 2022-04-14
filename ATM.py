class ATM(object):
    def __init__(self):
        
        def CashWithdrawl(self):
            CN = input("Enter Your Card Number :")
            PN = input("Enter Your Pin Number :")
            Amount = input("Enter Your Amount :")
            if(Amount>=1,00,000):
                print("Amount Withdrawled")
            else:
                print("Amount is too high")
        
        def CashDeposit(self):
            CN = input("Enter Your Card Number :")
            PN = input("Enter Your Pin Number :")
            Amount = input("Enter Your Amount :")
            if(Amount>=1,00,000):
                print("Amount deposited")
            else:
                print("Amount is too high")

atm = ATM()
CWorCD = input("CashWithdrawl or CashDeposit :")
if(CWorCD == "CashWithdrawl"):
    atm.CashWithdrawl()
elif(CWorCD == "CashDeposit"):
    atm.CashDeposit()