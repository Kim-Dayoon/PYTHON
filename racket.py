from tkinter import*
from ball import*
from court import*
class Racket:
    def __init__(self,court,x,y,img,w=53,h=121):
        self.canvas=court.canvas
        self.img=PhotoImage(file=img)
        self.racket=self.canvas.create_image(x,y,image=self.img)
        self.x=x
        self.y=y
        self.x_start=x
        self.y_start=y
        self.width=w
        self.height=h
        self.speed=25
    def start_position(self):
        self.x=self.x_start
        self.y=self.y_start
        self.canvas.coords(self.racket,self.x,self.y)
    def move_up(self,event):
        self.y-=self.speed
        self.canvas.coords(self.racket,self.x,self.y)
    def move_down(self,event):
        self.y+=self.speed
        self.canvas.coords(self.racket,self.x,self.y)
    def detect_collision(self,ball):
        left,top=self.x,self.y
        right,botton=left+self.width,top+self.height
        if ball.y2>top and ball.y1<botton and ball.x2> left and ball.x1<right:
            if left<ball.x2 and (ball.y2>top or ball.y1<botton):
                ball.x1-=randint(0,10)
                ball.x_dist*=-1
            if  right>ball.x1 and (botton>ball.y1 or top<ball.y2):
                ball.x1+=randint(0,10)
            
