#python Quiz

character=[0]*5 #initializing array named character of length 5 with all '0'

#index and it's corresponding characters
#ironman=0
#groot=1
#thanos=2
#blackwidow=3
#blackpanther=4

q1=input("Is Your character Female?")
#import emoji module
import emoji
print(emoji.emojize(":woman: :woman: :woman:"))

print("===============================\n")

q2=input("Is your character born rich?")
print(emoji.emojize(":heavy_dollar_sign: :heavy_dollar_sign: :heavy_dollar_sign:"))

print("===============================\n")

q3=input("Is Your character a villian?")

print("===============================\n")

q4=input("Is Your Character a king?")

print("===============================\n")


q5=input("Is your character a normal character(No Super powers)?")

print("===============================\n")

if(q1.lower()=="yes"):
	character[3]+=1 #increment counter for black widow

if(q2.lower()=="yes"):
	character[0]+=1 #increment counter for ironman
	character[4]+=1 #increment counter for blackpanther

if(q3.lower()=="yes"):
	character[2]+=1 #increment counter for thanos

if(q4.lower()=="yes"):
	character[1]+=1 #increment counter for groot yes

maxval=max(character) #finding most points from list of the characters
maxind=character.index(maxval) #finding index in which corresponds to max points

#printing name corresponding to index
print("\n\nYour Character is:")

if(maxind==0):print("====Ironman====")
elif(maxind==1):print("====Groot====")
elif(maxind==2):print("====Thanos====")
elif(maxind==3):print("===Blackwidow===")
elif(maxind==4):print("===Blackpanther===")
print("===============================\n")

print("Thankyou For Playing! Yay :-))))")

print("===============================\n")