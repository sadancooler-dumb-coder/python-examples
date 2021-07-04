from googlesearch import search as sus_impostor
query = input('Search: ')
for i in sus_impostor(query, tld="com", num=60, stop=10, pause=2): print(i)