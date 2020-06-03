###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits)

# Another hint:

# if (digit3[0] == guess[0]) and (digit3[1] == guess[1]) and (digit3[2] == guess[2]):
#     print('Complete')
# elif (digit3[0] == guess[0]) or (digit3[1] == guess[1]) or (digit3[2] == guess[2]):
#     print('Match')
# elif (guess[0] in digit3) or (guess[1] in digit3) or (guess[2] in digit3):
#     print('Close')
# else:
#     print('None')


def compare(num1, num2):
    if(num1 == num2):
        print('match')
        return 1
    elif(num2 in digit3):
        print('close')
        return 2
    else:
        return 0


while 1:
    guess = input("What is your guess? ")
    digit3 = [str(digits[0]), str(digits[1]), str(digits[2])]
    result = []
    for i in range(len(digit3)):
        result.append(compare(digit3[i], guess[i]))

    if (result[0] and result[1] and result[2]):
        print('complete')
        break
    elif ((result[0] == 0) and (result[1] == 0) and (result[2] == 0)):
        print('None')

    # Think about how you will compare the input to the random number, what format
    # should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
