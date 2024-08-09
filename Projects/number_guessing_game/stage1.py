print("Welcome to the Number Guessing Game!")
print("I am Shreyas. Can you help me to guess a number between 1 to 10 :")
Number=int(input("Guess a number:"))

if Number == 7:
    print("You win! Congratulations.")
  
if Number < 7 and Number > 0:
    print("Its low.Try again.") 

if Number > 7 and Number < 10: 
    print("Its high. Try again.")

else:
    print("Not Applicable")

