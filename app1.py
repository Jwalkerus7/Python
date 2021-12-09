"""MadLib game
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)"""

"""Basic calculator
num1 = input("First num: ")
num2 = input("Second num: ")
result = float(num1) + float(num2)
print(result)
"""

"""Lists uses []
friends = ["Jason", 44, "Heather", 44, "Mikey", 16, "Dakota", 9]
#friends[3] = 45
print(friends)
print(friends[0:2])"""

""""#List functions
lucky_nums = [3, 6, 7, 9, 44, 100]
friends = ["Jason", 44, "Heather", 44, "Mikey", 16, "Dakota", 9]
#friends.extend(lucky_nums)
#friends.append("Joey")
#friends.insert(8, "KK")
#friends.remove("KK")
#friends.clear()
#friends.pop()
#print(friends)
#print(friends.index("Joey"))
#print(friends.count("Mikey"))
#lucky_nums.sort() #Error,,, friends.sort() will not sort int and string, needs more info
#lucky_nums.reverse()
friends2 = friends.copy()
print(lucky_nums)
print(friends)"""

"""Tuples start here. Tuples can not be changed===immutable. Tuples use ()
coordinates = [(4, 44), (1, 2), (3, 4), (5, 6)]
print(coordinates[2])"""


"""Functions
def say_hi(name, age): #or sayhi()
    print("You da user learning code! " + name + ", you are " + str(age)) #or age and use str in call function
print("Top")
say_hi("jason", 44)
say_hi("walker", 45)
print("Bottom")"""

"""Return Statement
def cube(num):
    return num*num*num
print(cube(44))"""

"""If statements
I wake up 
if i am hungry
I eat breakfast
I leave my house
if it's cloudy
    I bring an umbrella
otherwise
    I bring sunglasses 
I'm at a restaurant
if I want meat
        I order a steak
otherwise if i want pasta
    I order spaghetti & meatballs
otherwise
    I order a salad.
is_male = True #False #can swith between the 2 to see differences of true and false
is_tall = True #False
if is_male or is_tall: #and
    print("Male, tall or both")
elif is_male and not(is_tall):
    print("Short male")
elif not(is_male) and is_male:
    print("Short male")
else:
    print("Not male nor tall")"""

"""If statements & comparisons #ie: also "dog" == "dog" "dog" != "cat"
def max_num(num1, num2, num3):
    if num1 >=(((== != > < <= >= different operators for different comparisions))) num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 44, 5))"""

"""Building a better Calculator
num1 = float(input("Enter first num: "))
op = input("Enter operator ")
num2 = float(input("Enter first num: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")"""

"""Dictionaries
Can use numbers as the key (((or 0: "January")))
monthConversions = {
    "Jan": "January", 
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Feb"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Luv", "Not a valid key"))"""


"""While Loop
j = 1
while j <= 44:
    print(j)
    j += 1 #<--shorthand #or j = j + 1
print("End of Loop")"""

"""Building A Guessing Game
secret_word = "Python"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses")
else:
    print("YOu guessed correct!")"""

"""For Loop
people_i_love = ["God", "Family", "Code"]
for pil in people_i_love:
    print(pil)


for index in range(3):
    print(index)


for index in range(5, 11):
    print(index)


people_i_love = ["God", "Family", "Code"]
for index in range(len(people_i_love)):
    print(people_i_love[index])


for index in range(len(people_i_love)):
    print(index)


for index in range(len(people_i_love)):
    print(index)

for index in range(7):
    if index == 0:
        print("7th Iteration")
    else:
        print("Not the first Iteration")"""


"""Exponent Function
#print(2**3)

def raise_up_num(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_up_num(3, 2))"""

"""2D Lists & Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)"""

"""Build a translator # j language
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "J"
            else:
                translation = translation + "j"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))"""

"""Comments
# Comments are cool
# This prints out a string
print("Comments are fun!")"""

"""Try Except"""



















