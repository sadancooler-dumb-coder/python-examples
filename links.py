from googlesearch import search # use to determine all the links and its state

query = input('Search: ') # use to determine what links they want to get

for i in search(query, tld="com", num=60, stop=10, pause=2): # what links in return
 print(i) # print that following link
