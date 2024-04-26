
#print("Welcome GTST to Python")   # This is question 1
#print ("Programming is Fun!")   # This is question 2
#print ("Hackers can code.")      # This is question 2
#print ('Welcome GTST' , 'to python' , sep = ',')

#print ('New year' , 2023 , 'See you soon!' , sep = '.')
#print ('Good Morning!' , end = ' .')

#name = ["Ethiopia" , "banana" , "china" , "apple"]
#print (name [::-1])
#print (name [::-2])
#print ("countries are:" , name [-2::-2])

#a = 5
#b = 2
#a **= b 
#print (a)

number = input ("Enter your number : ")

if number.strip() == "" :
    print ("Nothing inserted!")
else :
    if number.isdigit() :
        number = int(number)
        if (number % 2 == 0) :
            print ("The number is even.")
        else : 
            print ("The number is odd.")
    else : 
        print ("Please enter a number only!")

    
 
    