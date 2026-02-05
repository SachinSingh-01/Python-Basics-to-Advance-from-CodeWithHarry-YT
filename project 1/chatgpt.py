import random

choices = ['snake', 'water', 'gun']
user = input("Choose snake, water or gun: ").lower()
comp = random.choice(choices)

print(f"Computer chose: {comp}")

if user == comp:
    print("It's a tie!")
elif (user == 'snake' and comp == 'water') or \
     (user == 'water' and comp == 'gun') or \
     (user == 'gun' and comp == 'snake'):
    print("You win!")
else:
    print("Computer wins!")
