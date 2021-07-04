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
colorama.init()
print(Fore.RED + 'Red Text')
print(Back.YELLOW + 'Highlighted Text')
```
