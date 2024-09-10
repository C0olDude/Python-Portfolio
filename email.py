#Question 3.

email = input("Enter your email: ")

#Check if email ends with @pdsb.net
if email[email.index("@"):] == "@pdsb.net": 

  #Checks email length, and if it has 6 numbers before @ symbol
  if len(email) == 15 and email[0:email.index("@")].isdigit(): 
    print("This is a pdsb student email")
  #Checks email length, if it starts with p, and has 7 number after
  elif len(email) == 17 and email[0] == "p" and email[1:7].isdigit:
    print("This is a pdsb staff email")
  
  else:
    print("This is not a pdsb email")
else:
  print("This is not a pdsb email")