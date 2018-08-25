import turtle
import math
import random
import system


wn=turtle.Screen()
wn.bgcolor("black")
wn.bgpic("source2.gif")



player=turtle.Turtle()
player.color("red")
player.shape("turtle")
player.penup()
speed=0.6



#drawboard
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()




score=0








#create goal
goal=turtle.Turtle()
goal.color("yellow")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100,-80)

#create goals
maxGoal=6
goals=[]


    






#function
def turnleft():
    player.left(30)
def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed+=1
def decreasespeed():
    global speed
    speed-=1



def isCollision(player,goal):
    d=math.sqrt(math.pow(player.xcor()-goal.xcor(),2)+ math.pow(player.ycor()-goal.ycor(),2))
    if d  < 20:
        return True
    else:
        return False
        




#set keybord
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")



while True:
    player.forward(speed)
    #boundryHit x cordinate
    if player.xcor()>300 or player.xcor()<-300:
        player.right(180)
       
        #boundryHit for y cordinate
    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)
        

    
        
    #move the goal
    goal.forward(1)
    #boundry hit for goal
    if goal.xcor()>300 or goal.xcor()<-300:
        goal.right(180)
        #boundryHit for y cordinate
    if goal.ycor()>300 or goal.ycor()<-300:
        goal.right(180)
    #collision check

    if isCollision(player,goal):
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        goal.right(random.randint(0,360))
        score+=10
        print(score)
        if(score==100):
            print("YOU WON!")
            wn.bgpic("sk.gif")
            speed=0
            
            
        #to have score on screen
                










delay=raw_input("press enter to finish")
