from turtle import*
class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor("red")

turtle = MyTurtle()
turtle.shape("turtle")
turtle.onclick(turtle.glow)  #거북이를 클릭하면 색상이 빨간색으로 변한다.
