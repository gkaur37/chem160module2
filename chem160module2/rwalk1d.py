from random import choice
trials=10000
steps=10000
gothome=0
for i in range(trials):
    point=0
    for step in range(steps):
        point+=choice((-1,1))
        if point==0:
            gothome+=1
            break
print("Fraction that got home=",gothome/trials)

#the result was 0.97 and yes the random walker made it home.
#Changing the trials from 100 to 1000 resulted in fraction 0.991. yes increasing trails increased the fractions.