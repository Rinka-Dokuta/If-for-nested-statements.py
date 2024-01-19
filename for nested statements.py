if choice == "winter":
    choice2 = input("Do you like sports or relaxing?")
    if choice2 == "sports":
        print("I recommend skiing!")
    elif choice2 == "relaxing":
        print("I recommend ice fishing!")
    else:
        print("That's not a choice")
elif choice == "summer":
      choice2 = input("Do you like sports or relaxing?")
      if choice2 == "sports":
          print("I recommend swimming!")
      elif choice2 == "relaxing":
          print("I recommend reading by the beach!")
      else:
          print("That's not a choice")
          
print()

for i in range(4): #rows
    for j in range(8): #columns 
        print("*", end = " ")
    print()
