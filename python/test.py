#import sys

#firstname = sys.argv[1]
#lastname = sys.argv[2]
#print (f"Hello {firstname}" , f"Your Father's name is : {lastname}.")

users = ["Nathan" , 2313 , "Geez" , 'pass231' , "Abebe" , '092313133' , "Miki" , 'pl3s34DOntH4ckM3']

print ("The usernames are :" , users[::2])
print ("The passwords are :" , users[1::2])

users1 = {"Nathan" : 2313 , "Geez" : 'pass231' , "Abebe" : '092313133' , "Miki" : 'pl3s34DOntH4ckM3'}

choice = input ("Enter your username :")

print ("Your password is :" , users1[choice])
