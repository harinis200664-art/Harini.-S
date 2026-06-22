'''print("******************")
print("ELIF STATEMENT")
print("******************")
un=input("Enter the User Name:")
p=input("Enter the Password:")
if un=="harini" and p=="642006":
  print("Login successfull")
  balance=5000     
  option=input("1.Debit \n2.Withdrawal \n3.Balance \n4.Exit")
  choice=int(input("Enter your choice:"))
  if choice==1:
    a=int(input("enter your ammount:"))
    if a>5000:
      print("can't debit ammount")
    if a<=5000:
      print("debit successfully")
      print("your balance ammount:",balance+a)
  elif choice==2:
    b=int(input("enter your withdrawal ammount:"))
    if b<=balance:
      print("withdrawal succefully")
      print("balance ammount:",balance)
  elif choice==3:
    print("account balance ammount is:",balance)
    if balance<5000:
      print("alert your balance is very low")
  elif choice==4:
    print("thank you")
else:
    print("check username and password")
'''    
'''print("********************")
print("HOTEL MANAGEMENT")
print("********************")
un=input("Enter the User Name:")
p=input("Enter the Password:")
if un=="harini" and p=="642006":
  print("Login successfull")
  option=input("choose the hotel... \n1.HOTEL1 \n2.HOTEL2 \n3.HOTEL3")
  choice=int(input("Enter your choice:"))
  if choice==1:
    print("welcome to HOTEL1")  
    tm=input("choose timing.. \n1.BREAKFAST \n2.LUNCH \n3.DINNER")
    choice=int(input("Enter your timing:"))
    if choice==1:
      option=input("choose the food item... \n1.IDLY \n2.POORI \n3.PONGAL")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=15
      elif food==2:
        rate=30
      elif food==3:
        rate=30
      else:
        print("inavalid menu")  
    elif choice==2:
      option=input("choose the food item... \n1.RICE \n2.PAROTTA \n3.BRIYANI")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=50
      elif food==2:
        rate=20
      elif food==3:
        rate=100
      else:
        print("inavalid menu")  
    elif choice==3:
      option=input("choose the food item... \n1.DOSA \n2.IDLY \n3.CHAPPATHI")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=30
      elif food==2:
        rate=20
      elif food==3:
        rate=30
      else:
        print("inavalid menu")
    else:
       print("invalid timing")  
    if choice==1 or choice==2 or choice==3: 
     qty=int(input("Enter the Quantity:"))
     t=rate*qty
     print("Total ammount:",t)
     print("Thank you,visit us agaain!")
  elif choice==2:
    print("welcome to HOTEL2")  
    tm=input("choose timing.. \n1.BREAKFAST \n2.LUNCH \n3.DINNER")
    choice=int(input("Enter your timing:"))
    if choice==1:
      option=input("choose the food item... \n1.CURD RICE \n2.IDLY \n3.PONGAL")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=30
      elif food==2:
        rate=20
      elif food==3:
        rate=30
      else:
        print("inavalid menu")  
    elif choice==2:
      option=input("choose the food item... \n1.VARIETY RICE \n2.MEALS \n3.FRIED RICE")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=50
      elif food==2:
        rate=60
      elif food==3:
        rate=50
      else:
        print("inavalid menu")  
    elif choice==3:
      option=input("choose the food item... \n1.SUSHI \n2.NOODLES \n3.NAAN")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=60
      elif food==2:
        rate=100
      elif food==3:
        rate=20
      else:
        print("inavalid menu")
    else:
       print("invalid timing")  
    if choice==1 or choice==2 or choice==3: 
     qty=int(input("Enter the Quantity:"))
     t=rate*qty
     print("Total ammount:",t)
     print("Thank you,visit us agaain!")
  elif choice==3:
    print("welcome to HOTEL3")  
    tm=input("choose timing.. \n1.BREAKFAST \n2.LUNCH \n3.DINNER")
    choice=int(input("Enter your timing:"))
    if choice==1:
      option=input("choose the food item... \n1.BREAD BUTTER JAM \n2.DESSERTS \n3.PONGAL")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=40
      elif food==2:
        rate=50
      elif food==3:
        rate=30
      else:
        print("inavalid menu")  
    elif choice==2:
      option=input("choose the food item... \n1.EGG RICE \n2.VEG RICE \n3.BRIYANI")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=70
      elif food==2:
        rate=50
      elif food==3:
        rate=100
      else:
        print("inavalid menu")  
    elif choice==3:
      option=input("choose the food item... \n1.FISH FRY \n2.CHICKEN RICE \n3.CHAPPATHI")
      food=int(input("Enter Your Food:"))
      if food==1:
        rate=40
      elif food==2:
        rate=60
      elif food==3:
        rate=30
      else:
        print("inavalid menu")
    else:
       print("invalid timing")  
    if choice==1 or choice==2 or choice==3: 
     qty=int(input("Enter the Quantity:"))
     t=rate*qty
     print("Total ammount:",t)
     print("Thank you,visit us agaain!")
  else:
    print("inavalid hotel")
else:
  print("check username and password")
'''





























    


    

    





      



























    


    

    





     
      



























    


    

    




