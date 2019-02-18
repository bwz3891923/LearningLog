
alien_color_1='green'   #5.3
point_1=0
if alien_color_1=='green':
    print(" You get 5 point")
    point_1+=5

if alien_color_1=='yellow':
    print(" You get 5 point")
    point_1+=5

if alien_color_1=='red':
    print(" You get 5 point")
    point_1+=5


alien_color_2='yellow'  #5.4
point_2=0
if alien_color_2=='green':
    print(" You get 5 point")
    point_2+=5

else:
    print(" You get 10 point")
    point_2+=10


alien_color_3='yellow'  #5.5
point_3=0
if alien_color_3=='green':
    print("You get 5 point")
    point_3+=5

elif alien_color_3=='yellow':
    print("You get 10 point")
    point_3+=10

else:
    print("You get 15 point")
    point+=15


favorite_fruits=['orange','apple','watermelon']    #5.7
guess=['orange','melon','banana','straberry','apple','lemon']

for i in range(2):
    for guna in guess:
        if str(guna)==str(favorite_fruits[i]):
            print(guna)


          

