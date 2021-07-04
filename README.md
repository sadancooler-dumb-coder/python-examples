# Examples
These are python examples you can use! Or tidy up, so far. 
# Testing
I haven't tested these yet, please point out the errors in the "Issues" tab as I will try my best to resolve your issues (and tidy up the code a little)

By the way! Lazy to check all the files? I can't entirely help but here's content of a file!

```py
from googlesearch import search # use to determine all the links and its state

query = input('Search: ') # use to determine what links they want to get

for i in search(query, tld="com", num=60, stop=10, pause=2): # what links in return
 print(i) # print that following link
```
