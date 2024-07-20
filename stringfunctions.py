# STRING FUNCTIONS - 1

w = "Welcome to wscubetech"
a = w.lower()   # used to small all the letters
print(a)

b = w.upper()   # used to capital all the letters
print(b)

c = w.title()  # used to capital only the starting letter of every word
print(c)

d = w.capitalize()  # used to capital only starting letter of word/sentence
print(d)


# STRING FUNCTIONS  - 2

w = "Welcome"
print(w.find('e'))  # find the indexing no. of given character , if not same then give -1
print(w.find('e',2))
print(w.find('z'))

w = "Welcome" # find the indexing no. of given character , but it will give error if not same
print(w.index('e'))
print(w.index('z')) # use (#) if get all output

w = "Welcome"
print(w.isalpha()) # true if alphabet only
w = "Welcome123"
print(w.isalpha())

w = "Welcome"
print(w.isdigit()) # true if numeric only
w = "123"
print(w.isdigit())

w = "Welcome123"
print(w.isalnum()) # true if both (alphabet and music) but not any special character
w = "Welcome@123"
print(w.isalnum())