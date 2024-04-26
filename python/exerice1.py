users = {"Messi" : 'barca10' , "Hazard" : 'blue10' , "Ronald" : 'manu7' , "Neymar" : 'brazil10' }
count = 1

while True :
        if count <= 5 :
            username = input("Enter your username : ")
            password = input("Enter your password : ")

            if username not in users or password != users[username] :
                print (f">>trial {count} : Login failed! Please try again.")
                count += 1
            elif username in users and password == users[username] :
                print ("Welcome to GTST Company. ")
                break
        else : 
             print ("Sorry you are limited! ")
             break 
                
    








    
