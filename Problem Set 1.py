#!/usr/bin/env python
# coding: utf-8

# 
# 
# <h1><font color='#004b87'><center>BDAT1004-24W-20958- </center></font></h1>
# <h3><center>Data Programming - Problem Set 1 </center></h3>

# <h1><font color='#004b87'>Abdirahman Ahmed Hadi Ali   ID:200579531</font></h1>
# <p></p>
# <li>Late submission </li>

# <h3><font color='#004b87'>Question 1</font></h3>
# <p></p>
# 
# <li>What data type is each of the following (evaluate where necessary)?</li>
# 

# In[3]:


# integer
print(type(5))

#float
print(type(5.0))

#boolean
print(type(5 > 1))

#string
print(type('5'))

# integer
print(type(5 * 2))

#string
print(type('5' * 2))

#string
print(type('5' + '2'))

# float
print(type(5 / 2))

# integer
print(type(5 % 2))

# {5, 2, 1}
print(type({5, 2, 1}))

# boolean
print(type(5 == 3))

#float
import math
print(type(math.pi))


# <h3><font color='#004b87'>Question 2</font></h3>
# <p></p>
# Write (and evaluate) python expressions that answer these questions:
# a. How many letters are there in 'Supercalifragilisticexpialidocious'?
# b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? 
# c. Which of the following words is the longest:
# Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or
# Bababadalgharaghtakamminarronnkonn?
# d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian',
# 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?
# 
# 

# In[5]:


#(a)
word1 = 'Supercalifragilisticexpialidocious'
num_letters = len(word)
print("The number of letters in 'Supercalifragilisticexpialidocious' is: ", num_letters)


# In[11]:


#(b)
substring = 'ice'
contains_substring = substring in word
print("'Supercalifragilisticexpialidocious' contains 'ice' as a substring: ", contains_substring)


# In[10]:


#(c)
word1 = "Supercalifragilisticexpialidocious"

word2 = "Honorificabilitudinitatibus"
word3 = "Bababadalgharaghtakamminarronnkonn"


longest_word = max(word1, word2, word3, key=len)
print("The longest word among the given ones is:", longest_word)


# In[13]:


#(d)

composers = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
first_composer = min(composers)
last_composer = max(composers)
print("The first composer in the dictionary is:", first_composer)
print("The last composer in the dictionary is:", last_composer)


# <h3><font color='#004b87'>Question 3</font></h3>
# 
# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3 sides of a triangle
# and returns the area of the triangle. By Heron's formula, the area of a triangle with side lengths a, b,
# and c is s(s - a)(s -b)(s -c) , where s = (a+b+c)/2. >>> triangleArea(2,2,2) 1.7320508075688772

# In[15]:


#
def triangleArea(a, b, c):
    
    #semi-perimeter
    s = (a + b + c) / 2
    
    
    #Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


# Testing
result = triangleArea(2, 2, 2)
print(result)


# <h3><font color='#004b87'>Question 4</font></h3>
# <p></p>
# 
# Write a program in python to separate odd and even integers in separate arrays. Go
# to the editor
# Test Data :
# Input the number of elements to be stored in the array :5
# Input 5 elements in the array :
# element - 0 : 25
# element - 1 : 47
# element - 2 : 42
# element - 3 : 56
# element - 4 : 32
# Expected Output:
# The Even elements are:
# 42 56 32
# The Odd elements are :
# 25 47
# 
# 
# 

# In[21]:


num_elements = int(input("Input the number of elements to be saved in the array: "))

even_numbers = []
odd_numbers = []


for i in range(num_elements):
    element = int(input(f"element - {i} : "))
    if element % 2 == 0:
        even_numbers.append(element)
    else:
        odd_numbers.append(element)


        # result
print("The Even elements are:", *even_numbers)
print("The Odd elements are:", *odd_numbers)


# <h3><font color='#004b87'>Question 5</font></h3>
# <p></p>
# a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False
# depending on whether the point (x,y) lies in the rectangle with lower left
# corner (x1,y1) and upper right corner (x2,y2).
# >>> inside(1,1,0,0,2,3)
# True
# >>> inside(-1,-1,0,0,2,3)
# False
# b. Use function inside() from part a. to write an expression that tests whether
# the point (1,1) lies in both of the following rectangles: one with lower left
# corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower
# left corner (0.5, 0.2) and upper right corner (1.1, 2). 
# <p></p>

# In[31]:


#(a)

#function
def inside(x, y, x1, y1, x2, y2):
    
    
    # Check if point (x, y) is inside the rectangle defined by (x1, y1)for x  and (x2, y2) for y
    if x1 <= x <= x2 and y1 <= y <= y2:
        return True  # If true
    else:
        return False  # or esle false

#Testing

print(inside(1, 1, 0, 0, 2, 3)) # will print true

print(inside(-1, -1, 0, 0, 2, 3)) # will print false



 
    
    


# In[32]:


#(b)
#Testing

if rect1_result and rect2_result:
 print("The point (1,1) lies inside both rectangles.")
else:
 print("The point (1,1) does not lie inside both rectangles.")


# <h3><font color='#004b87'>Question 6</font></h3>
# <p></p>
# You can turn a word into pig-Latin using the following two rules (simplified):
# • If the word starts with a consonant, move that letter to the end and append
# 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# • If the word starts with a vowel, simply append 'way' to the end of the word.
# For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For
# our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# Write a function pig() that takes a word (i.e., a string) as input and returns its pigLatin form. Your function should still work if the input word contains upper case
# characters. Your output should always be lower case however.
# >>> pig('happy')
# 'appyhay'
# >>> pig('Enter')
# 'enterway' 
# <p></p>
# 
# 

# In[50]:


def bldcount(filename):
    
    
    
    # Create a dictionary to save the counts of each type
    blood_count = {'A': 0, 'B': 0, 'AB': 0, 'O': 0, 'OO': 0}

    # iterate through each line after opening file
    with open(filename, 'r') as file:
        for line in file:
            
            # Strip white spaces
            blood_type = line.strip()

            # Increase count of blood typey
            blood_count[blood_type] += 1

            
    # Iterate through the blood_count dictionary and then print out the counts of types
    for blood_type, count in blood_count.items():
        if count == 1:
            print(f"There is one patient of blood type {bloodtype1}.")
        elif count > 1:
            print(f"There are {count} patients of blood type {bloodtype1}.")
        else:
            print(f"There are no patients of blood type {bloodtype1}.")

           
      #testing  
bldcount(r'C:\Users\Dell_User\Desktop\Data Prog 01\bloodtype1.txt')
        


# <h3><font color='#004b87'>Question 8</font></h3>
# <p></p>
# Write a function curconv() that takes as input: 1. a currency represented using a string (e.g., 'JPY' for 
# the Japanese Yen or 'EUR' for the Euro) 2. an amount and then converts and returns the amount in 
# US dollars. >>> curconv('EUR', 100) 122.96544 >>> curconv('JPY', 100) 1.241401 The currency rates 
# you will need are stored in file currencies.txt: AUD 1.0345157 Australian Dollar CHF 1.0237414 
# Swiss Franc CNY 0.1550176 Chinese Yuan BDAT 1004 – Data Programming Page 5 of 6 F2021 BDAT 
# 1004 Computer Studies DKK 0.1651442 Danish Krone EUR 1.2296544 Euro GBP 1.5550989 British 
# Pound HKD 0.1270207 Hong Kong Dollar INR 0.0177643 Indian Rupee JPY 0.01241401 Japanese 
# Yen MXN 0.0751848 Mexican Peso MYR 0.3145411 Malaysian Ringgit NOK 0.1677063 Norwegian 
# Krone NZD 0.8003591 New Zealand Dollar PHP 0.0233234 Philippine Peso SEK 0.148269 Swedish 
# Krona SGD 0.788871 Singapore Dollar THB 0.0313789 Thai Baht
# <p></p>
# 

# In[54]:


def curconv(currency, amount):
    
    # Dictionary to save currency rates
    currency_rates = {}
    
    # Read currency rates from the file and store them in the dictionary
    with open(r'C:\Users\Dell_User\Desktop\Data Prog 01\currencies.txt', 'r') as file:
        for line in file:
            parts = line.split()
            currency_rates[parts[0]] = float(parts[1])
    
    # Check if the given currency is in the dictionary
    if currency in currency_rates:
        # Convert the amount to USD using the rates
        usd_amount = amount * currency_rates[currency]
        return usd_amount
    else:
        # If the currency is not found, return message not found
        return f"Currency '{currency}' not found."

# Testing
print(curconv('EUR', 100))  
print(curconv('CAD', 100))


# <h3><font color='#004b87'>Question 9</font></h3>
# <p></p>
# Each of the following will cause an exception (an error). Identify what type of exception each will
# cause. 
# <p></p>   

# <li>Trying to add incompatible variables which cause a TypeError exception because its trying to perform addition on operands of incompatible types.</li>
# <li>Referring to the 12th item of a list that has only 10 items: This will cause an IndexError exception because its out of the range</li>
# <li>Using a value that is out of range for a function's input which will cause a ValueError exception.</li>
# <li>Using an undeclared variable which will cause a NameError exception because the interpreter cannot find a definition for the variable being referenced.</li>
# <li>Trying to open a file that does not exist which will cause a FileNotFoundError exception because the file does not exist in the specified location or path.</li>

# <h3><font color='#004b87'>Question 10</font></h3>
# <p></p>
# Encryption is the process of hiding the meaning of a text by substituting letters in the message with
# other letters, according to some system. If the process is successful, no one but the intended
# recipient can understand the encrypted message. Cryptanalysis refers to attempts to undo the
# encryption, even if some details of the encryption are unknown (for example, if an encrypted
# message has been intercepted). The first step of cryptanalysis is often to build up a table of letter
# frequencies in the encrypted text. Assume that the string letters is already defined as
# 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a string as its only
# parameter, and returns a list of integers, showing the number of times each character appears in
# the text. Your function may ignore any characters that are not in letters. >>> frequencies('The quick
# red fox got bored and went home.') [1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2, 1, 0, 1, 1, 0, 0]
# >>> frequencies('apple')
# <p></p> 
# 
# 

# In[60]:


def frequencies(text):
    # Define the alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    # Initialize a list to save the frequencies of each letter
    frequency_list = [0] * 26
    
    # here we Convert the text to lowercase to simplify counting
    text = text.lower()
    
    # Iterate through each character in the text
    for char in text:
        
        # Check if the character is a letter
        if char in letters:
            # Increase the frequency count
            index = letters.index(char)
            frequency_list[index] += 1
    
    return frequency_list

# Test
print(frequencies('The quick red fox got bored and went home.'))
print(frequencies('apple'))
print(frequencies('apologies for late submission due to not understanding the submissin protocol'))

