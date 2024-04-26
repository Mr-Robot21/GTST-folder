#import sys

#firstname = sys.argv[1]
#lastname = sys.argv[2]
#print (f"Hello {firstname}" , f"Your Father's name is : {lastname}.")

#users = ["Nathan" , 2313 , "Geez" , 'pass231' , "Abebe" , '092313133' , "Miki" , 'pl3s34DOntH4ckM3']

#print ("The usernames are :" , users[::2])
#print ("The passwords are :" , users[1::2])

#users1 = {"Nathan" : 2313 , "Geez" : 'pass231' , "Abebe" : '092313133' , "Miki" : 'pl3s34DOntH4ckM3'}

#choice = input ("Enter your username :")

#print ("Your password is :" , users1[choice])

code = [2313, 2314, 4325, 6546]
errors = 1 

while True : 
    if errors <= 5 :
        user = int(input(f"Enter the code correctly {code[0]} : "))
        if user != int(code[0]) :
            print (int(code[0]))
            print (f"trial {errors} : incorrect , try again.")
            errors += 1
        elif user == int(code[0]) :
            print ("welcome")
            break
    else :
        print ("try again after 5 minutes.")
        break


