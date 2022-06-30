# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

response = input("EX 1: Please enter a letter from the alphabet (a-z or A-Z) ").lower()
    
if response == "a":
    print(f'The letter {response} is a vowel')
elif response == "e":
    print(f'The letter {response} is a vowel')
elif response == "i":
    print(f'The letter {response} is a vowel')
elif response == "o":
    print(f'The letter {response} is a vowel')
elif response == "u":
    print(f'The letter {response} is a vowel')
else:
    print(f'The letter {response} is a consonant')


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
while True:

    limit = 10
    response = input("EX 2: Please enter a word or phrase ")
    if response == "quit":
        break
    if len(response) > limit:
        print (f'The phrase is {len(response) - limit} too long.')
    else:
        print (f'What you entered is {len(response)} characters long.')
        


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

response = input("EX 3: Input a dog's age in human years. ")
human_years = int(response)
dog_years = 0

if human_years <= 2:
    dog_years = human_years * 10
else:
    dog_years = 20 + (human_years -2)*7

print(f"The dog's age in dog years is {dog_years}")
    


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print ("EX 4: Enter the lengths of three side of a triangle ")
side_1 = input("First side: ")
side_2 = input("Second side: ")
side_3 = input("Third side: ")
list = [side_1, side_2, side_3]

def has_duplicates(lst):
    return len(lst) != len(set(lst))

if side_1 == side_2 == side_3:
    print("equalateral")
elif has_duplicates(list):
    print("isosceles")
else:
    print("scalene")



# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
                        
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
zero = 0
one = 1
number = 0
number_list = [0,1]
print('EX 5')

for i in range(len(number_list)):
        number = i + i+1
        number_list.append(number)

a = 0
b = 1
n= 50

print(a,b,end=" ")
while(n-2):
    c=a+b
    a,b = b,c
    print(c,end=" ")
    n=n-1



# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):

month_bank = ["jan", "feb", "march", "april", "may", "june", "july", "aug", "sept","oct", "nov", "dec"]
month_input = input("EX 6: Enter the month of the season (Jan - Dec) ").lower()

def string_check (month):
    # if month != month_bank[2] and month != month_bank[3] and month != month_bank[4] and month != month_bank[5] and month != month_bank[6]:
    new_string = cut_string(month)
    print(new_string)
    return new_string

def cut_string (month_input): 
    return (month_input[:3])
    
month_input = string_check(month_input)
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:

print (month_input)
day_input = int(input("Enter a day of the month "))
# 3. Calculate what season it is based upon this chart:

if month_input in ('jan', 'feb', 'march'):
	season = 'winter'
elif month_input in ('april', 'may', 'june'):
	season = 'spring'
elif month_input in ('july', 'aug', 'sept'):
	season = 'summer'
else:
	season = 'autumn'

if (month_input == 'march') and (day_input > 19):
	season = 'spring'
elif (month_input == 'june') and (day_input > 20):
	season = 'summer'
elif (month_input == 'sept') and (day_input > 21):
	season = 'autumn'
elif (month_input == 'dec') and (day_input > 20):
	season = 'winter'


# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 
print(f"{month_input} {day_input} is in {season}")

    


