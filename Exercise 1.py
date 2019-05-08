# Exercise 1
# Answers to questions that ask for non-code answers can simply be added as comments.

# 1) The following line causes a SyntaxError. Please correct the line so that it's output is 'Hallo Welt!' [1P]
print('Hallo Welt!')

# 2) Calculate the difference between a and b and assign the result to a variable called 'v_1'. What are the datatypes of a, b and 'v_1'? [2P]
a = 976.543
b = 345
v_1 = a-b
# a und v_1 sind Floats (Fliesskommazahlen), b ist ein Integer (Ganze Zahl).

# 3) Calculate the remainder of the division 100/17 by only using one operator and save the result in v_2 (maybe the internet can help you) [1P]
v_2 = 100%17

# 4) The speed of light is about 300'000 km/s. What is the wavelength (in nanometers) of a light wave with a frequency of 5.0E+14 per second? Can we see this light? [4P]
#    If you don't know how to convert frequencies to wavelengths, the internet can help you!
#    Save the result in v_3.
#v_3 = 300000 / 5.0E+14 = 600 nm
v_3 =  600
# In diesem Wellenlängenspektrum liegt das (für den Menschen) sichtbare Licht. 


# 5) Print the following string to the console using the format-function and the variables 'n' and 'pi': "Pi rounded to the first 10 decimals is: 3.1415926536" [2P]
n  = 10
pi = 3.14159265358979323846264338
print('{number:.{digits}f}'.format(number=pi, digits=n))


# ------------------------------------
# - Don't change stuff below this line
# ------------------------------------

print(v_1)
print(v_2)
print(v_3)
