print('welcome to the ATM')
restart=('Y')
chances=3
balance=999
while chances>=0:
    pin=int(input('Please Enter Your 4 Digit Pin: '))
    if pin==(1234):
        print('You Enter your Pin Correctly')
        print('Please Press 1 for your Balance')
        print('please press 2 to make a withdrawl')
        print('please enter 3 to pay in')
        print('press press 4 to return card \n')

        while restart not in ('n','No','no','N'):
            print('please press 1 for your balance')
            print('please press 2 to make a withdrawl')
            print('please press 3 to pay in')
            print('please 4 to return card')
            option=int(input('what would you like to choose?: '))
            if option==1:
                print('your balance is $',balance)
                restart=input('would you like to go back? ')
                if restart in('n','No','n','no','No'):
                    print('THANK YOU')
                break
            elif option==2:
                option2=('y')
                withdrawl=float(input('how much would you like to withdrawl? 10,20,40,60,80,100 for other enter 1:'))
            
                if withdrawl in [10,20,40,60,80,100]:   
                    balance=balance-withdrawl
                    print('\n your balance is now $',balance)
                    restart=input('would you like to go back?')
                    if restart in('n','no','NO','N'):
                        print('THANK YOU')
                    break
                elif withdrawl!=[10,20,40,60,80,100]:
                    print('INVALID AMOUNT,PLEASE ENTER AMOUNT AGAIN')
                    restart=('Y')
                elif withdrawl==1:
                    withdrawl=float(input('PLEASE ENTER DESIRED AMOUNT:'))
            elif option==3:
                pay_in=float(input('how much you like to pay in?'))
                balance=balance+pay_in
                print('\nyour balance is now $',balance)
                restart=input('would you like to go back?')
                if restart in('n','no','NO','N'):
                      print('THANK YOU')
                break
            elif option==4:
                print('please wait collect your card...\n')
                print('THANK YOU FOR YOUR SERVICE')
           
            else:
                print('enter a correct number.\n')
                restart('y')
        break

    elif pin !=('1234'):
        print('INCORRECT PASSWORD')
        chances=chances-1
        if chances==0:
            print('\n NO MORE TRIES')
        break
    break
  

