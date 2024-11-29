from tkinter import*
from court import*
from ball import*
from racket import*
red_score=0
green_score=0
winner=' '
width,height=745,374
win=Tk()
win.title("Tennis Game")
win.geometry("745x374+150+150")
win.resizable(False,False)
court=Court(win,745,374,"court.png")
x1,y1=width/2,height/2
x2,y2=x1+30,y1+30
ball=Ball(court,x1,y1,x2,y2)
red_racket=Racket(court,60,180,"red_racket.png")
green_racket=Racket(court,680,180,"green_racket.png")
court.draw_score(red_score,green_score)
def play_game():
    global winner
    red_racket.detect_collision(ball)
    green_racket.detect_collision(ball)
    if ball.x1<=5:
        winner="green"
        ball.stop_ball()
    if ball.x1+ball.width>=court.width-5:
        winner="red"
        ball.stop_ball()
    ball.move_ball()
    win.after(50,play_game)
def score():
    global red_score,green_score,winner
    if winner=="red":
        red_score+=1
        winner=' '
    
    elif winner=="green":
        green_score+=1
        winner=' '
    court.draw_score(red_score,green_score)
def restart(event):
    score()
    red_racket.start_position()
    green_racket.start_position()
    ball.start_ball()


    
play_game()
win.bind("<w>",red_racket.move_up)
win.bind("<s>",red_racket.move_down)
win.bind("<Up>",green_racket.move_up)
win.bind("<Down>",green_racket.move_down)
win.bind("<space>",restart)












win.mainloop()
