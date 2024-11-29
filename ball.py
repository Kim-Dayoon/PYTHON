from tkinter import *
from random import*


class Ball :
    def __init__ (self, court, x1, y1, x2, y2) :
        # 공의 좌표 초기화하기
        self.x1 = x1                            
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x1_start=x1
        self.y1_start=y1
        self.x2_start=x2
        self.y2_start=y2

        # 공의 이동 거리 초기화하기
        self.x_dist = -10
        self.y_dist = -10
	
	# 공의 가로, 세로 길이 초기화하기
        self.width = x2 -x1
        self.height = y2 - y1

	# Court 클래스 객체 저장하기
        self.court = court

	# Court 클래스의 캔버스 저장하기
        self.canvas = court.canvas

	# 캔버스에 공 생성
        self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = "red")

    def stop_ball(self):
        self.x_dist=0
        self.y_dist=0
    def start_ball(self):
        if randint(0,1):
             self.x_dist=10
        else:
             self.x_dist=10
        if randint(0,1):
             self.y_dist=10
        else:
             self.y_dist=10
        self.x1=self.x1_start
        self.y1=self.x1_start
        self.x2=self.x1_start
        self.y2=self.x1_start
        self.canvas.coords(self.ball,self.x1,self.y1,self.x2,self.y2)
    # 공을 움직이는 메소드 정의하기
    def move_ball(self) :
        self.x1 += self.x_dist
        self.y1 += self.y_dist     
        # 위쪽 벽 충돌하면 방향 바꾸기
        if self.y1 <= 5 :
            self.y1=5
            self.y_dist *= -1
        # 아래쪽 벽 충돌하면 방향 바꾸기
        if self.y1 >= (self.court.height - (self.height - 5)) :
            self.y1 = self.court.height - (self.height - 5)
            self.y_dist *= -1

        # 왼쪽 벽 충돌하면 방향 바꾸기
	# 왼쪽, 오른쪽 벽 충돌 시 방향 바꾸는 것을 주석을 풀고 확인해 보세요. 
        if self.x1 <= 5 :
            self.x1 = 5
            self.x_dist *= -1
            self.stop_ball()        # 공 멈추기 메소드 호출
               

        # 오른쪽 벽 충돌하면 방향 바꾸기
        if self.x1 + self.width >= self.court.width - 5 :
            self.x_dist *= -1
            self.stop_ball()       # 공 멈추기 메소드 호출
                
        # 공 이동 좌표 저장
        self.x1 = self.x1
        self.x2 = self.x1 + self.width
        self.y1 = self.y1
        self.y2 = self.y1 + self.height
        # 공 위치 변경
        self.canvas.coords(self.ball,self.x1,self.y1,self.x2,self.y2)  
        
        


        

