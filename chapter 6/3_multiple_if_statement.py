a=int(input("Enter your age: "))

#If statement no:1

if(a%2==0):
    print("a is even")
#End of if statement no:1

# If statement no:2
if(a>=18):
       print("You are above the age od consent")
       print("Good for you")

elif(a<0):
       print("You are entering an invalid negative age")
        

else:
    print("You are below the age od consent")
# End of if statement no:2    
print("End of program")
