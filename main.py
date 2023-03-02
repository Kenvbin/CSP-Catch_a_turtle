# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

spoco = ['pink','red' ,'green' ,'blue' ,'orange']
sposha = ["turtle","arrow" ,"circle" ,"square" ,"triangle"]
#-----game configuration----
score = 0
spot_size = 2
spot_color = random.choice(spoco)
spot_shape = random.choice(sposha)
spot_size =  random.randint(2,5)

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.speed(0)

#-----countdown variables-----
font_setup = ("Ariel", 10, "bold")
timer = 30
spot_interval = 1000   #1000 represents 1 second
timer_up = False

#-----game functions--------
def circlelelelel_click(x,y):
  global score, spot_size, spot_color, sposhaha, spot_shape, spot
  score = score + 1
  spot_size =  random.randint(2,5)
  spot_color = random.choice(spoco)
  spot_shape = random.choice(sposha)
  spot.shape(spot_shape)
  spot.shapesize(spot_size)
  spot.fillcolor(spot_color)
  wex = random.randint(-400,400)
  why = random.randint(-200,200)
  spot.penup()
  spot.setposition(wex, why)
  spot.pendown()

def countdown():
  global timer, timer_up
  spot.clear()
  if timer <= 0:
    spot.write("Time's Up", font=font_setup)
    timer_up = True
    print("You clicked tracy the shapeshifter a total of",score,"times")
    print("Good job now run the program again!")
    exit()
  else:
    spot.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    spot.getscreen().ontimer(countdown, spot_interval) 

#-----events----------------
spot.onclick(circlelelelel_click)
wn = trtl.Screen()
wn.ontimer(countdown, spot_interval) 
wn.mainloop()