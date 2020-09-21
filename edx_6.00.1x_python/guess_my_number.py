#guess_my_number.py

ans = ''
high = 100
low = 0
guess = ((high - low)//2) + low

print("Please think of a number between 0 and 100!")

while guess:
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate guess is too high. Enter 'l' to indicate guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    elif ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
        continue
    
    guess = ((high - low)//2) + low
    #print(low, high, guess)
