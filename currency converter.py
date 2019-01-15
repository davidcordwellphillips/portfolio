def EU():
  converted_money = money * 1.14
  print('€', converted_money)
  return(converted_money)
  
#------------------------------
  
def US():
  converted_money = money * 1.42
  print('$', converted_money)
  return(converted_money)
  
#------------------------------
  
print("Welcome to the Python Currency Converter.")
Loop = True
while Loop == True:
  print("")
  print("Enter 1 for GBP to USD")
  print("Enter 2 for GBP to EUR")
  print("")

  option = input()
  print("")

  money = int(input("Enter amount in GBP: £"))
  print("")

  if option == "1":
    US()
    
  else:
    EU()

  option = input("Convert again? Y/N ")

  if option == "Y":
    Loop = True

  else:
    Loop = False
