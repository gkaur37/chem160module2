from random import choices
nrolls=10000
total=0
ndice=25
for i in range(nrolls):
    dice=choices(range(1,7), k=ndice)
    dice.sort(reverse=True)
    total=total+dice[0]+dice[1]
print("Average roll=",total/nrolls)

#by increasing the ndice from 2 to 3, the average sum increased from 6.9898 to 8.4435.
#No it would not be a fair game to allow a friend to add one to sum for just 2 dice.