print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play: ")
score=0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    score -= 1

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    score -= 1


answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    score -= 1


answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    score -= 1


print("You got " + str(score) + " marks")
print("You got " + str((score / 4) * 100)+ "%")