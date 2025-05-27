

# THE BACKSLASH (\) -> is called the escape character.

# The backslash doesn't mean anything in itself, but is only a kind of announcement, that the next character after the backslash has a different meaning too.

#In this example, after we put the backslash (\), the second part of the sentence sentence will appears on the next line:

#print("Black keys white keys, \nbettet friends understand.")
      # Output: 
          #   Black keys white keys, 
          #   bettet friends understand.
#___________________________________________________________________________________________________

# KEYWORD ARGUMENTS -> Are another mechanism for the passing of arguments.

# /// end= ---> The end keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments. 

# print('Hello, mate', end=', ')
# print('How are you?')
      #Output: Hello, mate, How are you?

# /// sep= ---> The sep keyword function separates its outputted arguments with a characther given. 

# print('eva','00','Rei',sep='_')
      #Output: eva_00_Rei

#___________________________________________________________________________________________________
# THE INPUT FUNCTION: The input() function is able to read data entered by the user and to return the same data to the running program.

# We can pass an argument to the input function to show a message for the user, by doing this, is more clear wath kind of data needs to be input.


# user_name = input('Insert your user name:')
# print('User name:',user_name)

# user_email = input('Insert yout email')
# print('Email: ', user_email)


#  /////  -------------------------------------------------------------------
#int() and float() functions could work with the input() function but only accept integeres and float data values, like their name specified.

# Ej. 1:
# user_integer = int(input('Type your number: '))
# user_float = float(input('Typer your float: '))
# print('Your integer: ', user_integer, '\n', 'Your float: ', user_float)

# Ej. 2:
# user_number = float(input('Type your number: '))
# result = user_number ** 2
# print(user_number, 'to the power of 2 is: ', result)

#  /////  -------------------------------------------------------------------
# Python always chooses the more economical form of the number's presentation, and you should take this into consideration when creating literals. 
# Ej.:
# print(0.0000000000000000000001) #output --> 1e-22

#  /////  -------------------------------------------------------------------
# An operator is a symbol of the programming language, which is able to operate on the values.

# Operators which are associated with the most widely recognizable arithmetic operations:
# +
# -
# *
# /
# //
# %
# **

#  /////  -------------------------------------------------------------------
# COMPARISON OPERATORS

# //// Equality (==)

# Ej.1:
# num_a = 3
# num_b = 3
# print(num_a == num_b) #output -> True

# Ej.2:
# text_1 = "Ja"
# text_2 = "Nein"
# comparison_text = text_1 == text_2
# print(comparison_text) # Output -> False


# //// Inequality - not equal operator (!=)

# Ej.1:
# num_a = 3
# num_b = 3
# print(num_a != num_b) #output -> False

# Ej.2:
# text_1 = "Ja"
# text_2 = "Nein"
# comparison_text = text_1 != text_2
# print(comparison_text) # Output -> True


# //// Greater than / greater than or equal (>  / >=)

# Ej.1:
# print(23 > 23) # Output -> False
# print(42 > 23) # Output -> True

# Ej.2:
# print(24 >= 24) # Output -> True
# print(24 >= 23) # Output -> True
# print(24 >= 28) # Output -> False

# //// Less than / less than or equal (<  / <=)

# Ej.1:
# print(23 < 23) # Output -> False
# print(42 < 23) # Output -> True

# Ej.2:
# print(24 >= 24) # Output -> True
# print(24 >= 23) # Output -> True
# print(24 >= 28) # Output -> False


# ///// Conditions and conditional execution

n = float(input('Type a number:'))

if n >= 100:
      print('You pass')
elif n < 100 and n > 70:
      print('You have another chance')
else: 
      print('Sorry, try tomorrow')