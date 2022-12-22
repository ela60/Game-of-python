print("Welcome to my computer quiz !")

playing = input("Do you want to play >")

if playing != "yes":
    quit()

print ("okay! Let's play :)")  

score =0

answer = input("What does cpu stands for >")
if answer.lower() == "central processing unit":
    print('correct !')
    score +=1
else:
    print('incorrect !')    

answer = input("What does RAM stands for >")
if answer.lower() == "random access memory":
    print('correct !')
    score +=1
else:
    print('incorrect !')  

answer = input("What does psu stands for >")
if answer.lower() == "power supply":
    print('correct !')
    score +=1
else:
    print('incorrect !')  

answer = input("What does GPU stands for >")
if answer.lower() == "graphics processing unit":
    print('correct !')
    score +=1
else:
    print('incorrect !') 

print("You got"+ str(score) +("question correct !"))
print("You got"+ str(score / 4)* 100 +("% ."))