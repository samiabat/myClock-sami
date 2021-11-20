# Analog clock by Samuel Abatneh section 1
# we should import turtle,
# and if we want to use time package we should import first
import time
from turtle import*

# lets adjust the window
screen = Screen()
screen.title("AnalogClock by SamuelAbatneh_UGR_7229_12")
screen.bgcolor("white")
screen.setup(600, 600)


# draw circle as the frame to the circle
frame = Turtle()
frame.speed(0)
frame.hideturtle()
frame.color("black")
frame.pensize(10)
frame.penup()
frame.goto(0, -200)
frame.hideturtle()
frame.pendown()
frame.begin_fill()
frame.color("silver")
frame.circle(200)
frame.end_fill()

# here we can insert center circle
frame.penup()
frame.hideturtle()
frame.goto(0, 0)
frame.pendown()
frame.circle(150)

# write number (1-12) i use for loop to write the number
writeNumber = Turtle()
writeNumber.hideturtle()
writeNumber.penup()
writeNumber.goto(0, 150)
writeNumber.pendown()
writeNumber.speed(0)
for i in range(12):
    writeNumber.color("black")
    writeNumber.right(15)
    writeNumber.penup()
    writeNumber.forward(90)
    writeNumber.right(15)
    writeNumber.pendown()
    writeNumber.write(i + 1, align="center", font=("areal", 25, "bold"))

# now i can inter corner hatch to know time precisely
cornerHatch = Turtle()
cornerHatch.hideturtle()
cornerHatch.home()
cornerHatch.pensize(5)
cornerHatch.speed(0)
for i in range(61):
    cornerHatch.hideturtle()
    cornerHatch.penup()
    cornerHatch.forward(190)
    cornerHatch.pendown()
    cornerHatch.forward(10)
    cornerHatch.penup()
    cornerHatch.backward(200)
    cornerHatch.setheading(6 * i)

# I insert the shape from turtle, using shape method
# I insert second hand
sHand = Turtle()
sHand.shape("arrow")
sHand.color("white")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=15)

# Insert minute hand similar to second hand
mHand = Turtle()
mHand.shape("arrow")
mHand.color("white")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.5, stretch_len=12)

# I insert hour hand arrow shape
hHand = Turtle()
hHand.shape("arrow")
hHand.color("white")
hHand.speed(5)
hHand.shapesize(stretch_wid=0.6, stretch_len=8)

# I insert small center circle to the origin
Center = Turtle()
Center.speed(10)
Center.shape("circle")
Center.color("white")
Center.shapesize(stretch_wid=1, stretch_len=1)

# the last thing i did is rotate those arrows accordingly
# I import time module and use time.localtime() to know the exact time
# here i use 90 to move the arrow from the x axis to the vertical and to start from 12 O'clock
# later I multiply the update second by 6 because the second hand should move 6 degree to for each second
# I use the minus sign to move the arrow clockwise or negative direction
# I multiply the update minute by 6 because the minute hand should move 6 degree  for each minute
# I multiply the update hour by 30 because the hour hand should move 30 degree to for each hour
# the while loop will continue fore ever and the arrows will set their heads towards the updated time units
while True:
    degree = 90 - time.localtime().tm_sec * 6
    sHand.setheading(degree)
    degreeM = 90 - time.localtime().tm_min * 6
    mHand.setheading(degreeM)
    degree = 90 - time.localtime().tm_hour * 30
    hHand.setheading(degree)

# here I can add the terminator but the the execution do not reach here because it can't move from the loop
