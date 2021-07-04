# Examples
These are python examples you can use! Or tidy up, so far. 
# Testing
I haven't tested these yet, please point out the errors in the "Issues" tab as I will try my best to resolve your issues (and tidy up the code a little)
# Files
links.py

```py
from googlesearch import search # use to determine all the links and its state

query = input('Search: ') # use to determine what links they want to get

for i in search(query, tld="com", num=60, stop=10, pause=2): # what links in return
 print(i) # print that following link
```

hello_world.py

```py
print("Hello World!")
```

color_text.py

```py

from colorama import Back, Fore, init # you need to install this from pip
colorama.init() # initiliaze the module.
print(Fore.RED + 'Red Text') # print red text

print(Back.YELLOW + 'Highlighted Text') # print yellow-highlighted text
```

introduction.py

```py

print("What is your name?") # print the user a message
name = input('Name: ') # ask the user for their name
print("What is your age?") # print the user a message
age = input('Age: ') # ask the user for their age
print("Your name is " + name + "\nYour age is " + age) # get the state of the user's age && name
```
