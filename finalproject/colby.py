#Front Menu

choice = float(input("Choose what you want to see--\n\nType 1 <--Your status of immigration \nType 2 <--For legal assistance in your surrounding area \nType 3 <-- For food assist., financial assist., religous, and therapy \nType 4 <-- For advocacy and representation\n"))
while choice >0 or choice <5:
    
    if choice == 1:
      print("status")
      break
    elif choice == 2:
      print("legal")
      break
    elif choice == 3:
      print("assistance")
      break
    elif choice == 4:
      print("representation")
      break
    else:
      print("~ only options: 1-4 ~")
      choice = int(input("Please enter a choice from 1 to 4"))
      
