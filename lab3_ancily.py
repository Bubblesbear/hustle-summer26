# Ancily Liu | Lab3 | Green

username = "Bubblesbear"
print(len(username)) #11
#PREDICT: print 11
# len() counted all 11 characters
print(username [0])
print(username [3])
#PREDICT should only print the first letter B and the b in bears
#
welcome = "Welcome to Loop," + " " + "@" + username + "!"
print(welcome)
print(f"Welcome to Loop, @{username}!")
#Predict they will print the same
# f string felt easier because you only needed to use one quotation mark for the whole thing, while concatenation needed a Quotation for even a space
print(username.upper())
#Predict it will say syntax error line 16
#Immutable for a string means object does not support item assignment
feed = ["ASMR", "Mukbang", "Gaming"]
print(len(feed)) #3
print(feed[0]) #ASMR
# I used index 0 because in python it starts with 0
feed.append("TV-Shows")
print(feed) #index is 3
#it has a 3 instead 4 bc python always start with zero.
feed.pop(0)  #Predict both removed ASMR
# .pop removed by in")dex and .remove remoced by name
profile = {"username": "Bubblesbear", "followers": 150, "verified": False,"Bio": "Nature"}
print(profile["followers"]) #predict 100
# profile[0] #predict syntax error 31
# dictionaries look up by key because index would be confusing as username would be 0 and then the real username would then be 1, and even if it was both 0 it wouldn't know which one to print, needs to be specific
print(profile.get("age")) #predict print syntax error line 33 and 29
#.get() is better bc it grabs a value without crashing if the key is not there
print(f"@{profile['username']} has {profile['followers']} followers and 3 post. Top post: {feed[0]}")
#@Bubblesbear has 150 followers and 3 posts. Top post: ASMR.
#used f string, grabbed value by key
