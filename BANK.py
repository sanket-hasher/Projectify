import pandas as pd
import random as rd
class Bank:
    __savings_rate=5.00
    __fixed_rate=7.00
    def __init__(self):
        print(' Welcome to SDBOI BANK ')
        print("------------------------")
        self.sacc=pd.DataFrame(columns=['NAME','DATE_of_Birth','AADHAR','PAN','BALANCE','ACC_NO'])
        self.facc=pd.DataFrame(columns=['NAME','DATE_of_Birth','AADHAR','PAN','Amount','PERIOD','FD_Number'])
        self.pin={}
    def create_acc(self):
        raw='1,2,3,4,5,6,7,8,9,0'
        raw=raw.split(',')
        acc_type=input(" What account you want to create Fixed Deposit Account (f) or SAvings Account(s) ")
        if acc_type=='s':
            print(" Enter the following details to create a new savings account  ")
            name=input(" NAME - ").upper()
            dob=input("Date of Birth in 'DD/MM/YYYY' format  - ")
            a_no=input(" AADHAR CARD NUMBER - ")
            p_no=input("PAN CARd NUMBER - ")
            amt=int(input("Initial Deposit (minimum 3000) "))
            if(amt<3000):
                print(" Account cannot be created ")
                return
            username=input("Username for app login ")
            acc_pin=input(" Pin for both bank and app login as well as for deposit and withdraw ")
            acc_num='SDBOIACNO'+''.join(rd.sample(raw,5))
            print(" Your account Number is : ",acc_num)
            self.pin[username]=acc_pin
            cus_details=(name,dob,a_no,p_no,amt,acc_num)
            self.sacc.loc[len(self.sacc)]=cus_details
            print("Account created Successfully")
        elif acc_type=='f':
           
            x=input("Do you have a Savings Account in our Bank (Y/N)")
            if x=='N':
                print(" No fixed Deposits Allowed without Savings Account ")
            else:
                print(" Enter the following details ")
                name=input(" NAME - ").upper()
                dob=input("Date of Birth in 'DD/MM/YYYY' format  - ")
                a_no=input(" AADHAR CARD NUMBER - ")
                if(a_no in self.sacc['AADHAR']):
                    print(" AADHAR NUMBER DID NOT MATCH WITH ACCOUNT DETAILS  ")
                    return
                p_no=input("PAN CARd NUMBER - ")
                if(p_no in self.sacc['PAN']):
                    print(" PAN NUMBER DID NOT MATCH WITH ACCOUNT DETAILS ")
                    return
                amt=int(input("FIXED  Deposit AMOUNT (minimum 10000) "))
                if(amt<10000):
                    print(" Fixed Deposit not allowed below 10000 ")
                    return
                period=int(input(" You can fix the amount for a minimum of 2 years and maximum of 15 years "))
                fd='FDNO'+''.join(rd.sample(raw,4))
                print(" FD NUMBER - ",fd)
                d=(name,dob,a_no,p_no,amt,period,fd)
                self.facc.loc[len(self.facc)]=d
                print("FIXED DEPOSIT created Successfully")
        else:
            print(" WRONG ACCOUNT TYPE ")
    def display(self,pin):
        
        acc_type=input(" What account you want to view Fixed Deposit Account (f) or SAvings Account(s)")
        if acc_type=='s':
            acc_num=input(" ENTER THE ACCOUNT NUMBER ")
            acc_pin=input(" ENTER THE PIN ")
            if acc_pin!=pin:
                print(" ACCESS DENIED PIN MISMATCH ")
                return
            cd=self.sacc[self.sacc['ACC_NO']==acc_num]
            print(cd)
            v=cd['BALANCE']
            final=v+Bank.__savings_rate/100*v
            print(" You will Receive an Annual Interest of = ",Bank.__savings_rate)
            print(" Your Amount is Likely to be {} after a year ".format(float(final)))
        elif acc_type=='f':
            f_num=input(" ENTER THE FD NUMBER ")
            acc_pin=input(" ENTER THE PIN ")
            if acc_pin!=pin:
                print(" ACCESS DENIED PIN MISMATCH ")
                return
            cd=self.facc[self.facc['FD_Number']==f_num]
            print(cd)
            final=float(cd['Amount'])
            p=int(cd['PERIOD'])
            for i in range(1,p+1):
                final=final+Bank.__fixed_rate/100*final
            print(" You will Receive an Annual Interest of = ",Bank.__fixed_rate)
            print(" Your Amount is Likely to be {} after {} years ".format(final,p))
        else:
            print(" INVALID ACCOUNT TYPE ")
    def deposit(self,pin):
        acc_num=input(" ENTER THE ACCOUNT NUMBER ")
        amt=int(input(" Enter the amount to deposit "))
        acc_pin=input(" ENTER THE PIN ")
        if acc_pin!=pin:
            print(" ACCESS DENIED PIN MISMATCH ")
            return
        cd=self.sacc[self.sacc['ACC_NO']==acc_num]
        upt_amt=cd['BALANCE']+amt
        self.sacc.loc[self.sacc['ACC_NO']==acc_num,'BALANCE']=upt_amt
        print(" UPDATED ")
        print(self.sacc[self.sacc['ACC_NO']==acc_num])
    def withdraw(self,pin):
        
        acc_num=input(" ENTER THE ACCOUNT NUMBER ")
        cd=self.sacc[self.sacc['ACC_NO']==acc_num]
        amt=float(input(" Enter the amount to withdraw "))
        b=float(cd['BALANCE'])
        if(amt>b):
            print(" WITHDRAW AMOUNT GREATER THAN BALANCE ")
            return
        acc_pin=input(" ENTER THE PIN ")
        if acc_pin!=pin:
            print(" ACCESS DENIED PIN MISMATCH ")
            return
        upt_amt=cd['BALANCE']-amt
        self.sacc.loc[self.sacc['ACC_NO']==acc_num,'BALANCE']=upt_amt
        print(" UPDATED ")
        print(self.sacc[self.sacc['ACC_NO']==acc_num])
b=Bank()
session=99
for i in range(1,session):
    stp=input(" ENTER 'end' to end session and PRESS ANY KEY TO CONTINUE ")
    if(stp=='end'):
        break
    customer=input(" ENTER 'new' for NEW CUSTOMER and 'old' for managing your existing account ")    
    if customer=='new':
        b.create_acc()
        username=input(" Enter your username ")
        pin=input(" Enter your pin ")
        if((username,pin) in b.pin.items()):
            b.display(pin)
        else:
            print(' RETRY ACCOUNT NOT CREATED ')
    elif customer=='old':
        username=input(" Enter your username ")
        pin=input(" Enter your pin ")
        if((username,pin) not in b.pin.items()):
            print(" WRONG PIN ")
        else:    
        
            print("----------------------------")
            print(" ********ACTIVITY******** ")
            print(" 1.Deposit ")
            print(" 2.Withdraw ")
            print(" 3.VIEW DETAILS ")
            print(" 4.CREATE FIXED DEPOSIT ")
            print(" 5.CREATE NEW ACCOUNT")
            print(' Enter your choice ')
            ch=int(input())
            if ch==1:
                b.deposit(pin)
            elif ch==2:
                b.withdraw(pin)
            elif ch==3:
                b.display(pin)
            elif ch==4:
                b.create_acc()
            elif ch==5:
                b.create_acc()
            else:
                print("Wrong Choice")
    else:
        print(" WRONG INPUT ")
            
                