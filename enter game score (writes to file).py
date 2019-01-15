Loop = True
file = open("CharacterStats.txt", "w")
print("")

while Loop == True:
  print("")
  name = input("Please enter your charater's name: ")
  print("")
  attack = int((input("Please enter your character's attack capability: ")))
  print("")
  defense = int((input("Please enter your character's defense capability: ")))
  print("")
  
  if attack >= 1 and attack <= 100 and defense >= 1 and defense <= 100:
    print("The results entered are valid.")
    file.write("")
    file.write("Name:" + name + "\n")
    file.write("Attack:" + str(attack) + "\n")
    file.write("Defense:" + str(defense) + "\n")
    print("Thank you.")
    print("")
    
  else:
    print("The results entered are invalid. Please only input a number between 0 and 100.")
    print("")
    
  confirm = input("Enter another? Y/N ")
  
  if confirm == "Y" or "y":
    Loop = True
    
  elif confirm == "N" or "n":
    Loop = False
    
  
