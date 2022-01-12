from tkinter import *
from random import choice
from time import sleep

class Game:
    def __init__(self):
        self.master = Tk()
        self.master.title('Pong game')
        self.master.resizable(0, 0)
        self.canvas = Canvas(self.master, width=1000, height=600, bg='black', highlightthickness=0)
        self.canvas.pack()
        self.started = False
        self.ball_xv, self.ball_yv = 0, 0
        self.ball_speed = 4
        self.player1_score, self.player2_score = 0, 0
        self.player1_direction, self.player2_direction = '', ''
        self.canvas.bind_all('<Button-1>', self.start_game)
        self.canvas.bind_all('<KeyPress-w>', self.player1_up)
        self.canvas.bind_all('<KeyRelease-w>', self.player1_stop)
        self.canvas.bind_all('<KeyPress-s>', self.player1_down)
        self.canvas.bind_all('<KeyRelease-s>', self.player1_stop)
        self.canvas.bind_all('<KeyPress-Up>', self.player2_up)
        self.canvas.bind_all('<KeyRelease-Up>', self.player2_stop)
        self.canvas.bind_all('<KeyPress-Down>', self.player2_down)
        self.canvas.bind_all('<KeyRelease-Down>', self.player2_stop)
        self.draw_graphics()
        self.mainloop()

    def player1_up(self, a): self.player1_direction = 'up'
    def player1_down(self, a): self.player1_direction = 'down'
    def player1_stop(self, a): self.player1_direction = ''
    def player2_up(self, a): self.player2_direction = 'up'
    def player2_down(self, a): self.player2_direction = 'down'
    def player2_stop(self, a): self.player2_direction = ''

    def draw_graphics(self):
        self.paddle1 = self.canvas.create_rectangle(20, 200, 50, 400, outline='', fill='white')
        self.paddle2 = self.canvas.create_rectangle(980, 200, 950, 400, outline='', fill='white')
        self.ball = self.canvas.create_oval(485, 285, 515, 315, outline='', fill='white')
        self.player1_scoretext = self.canvas.create_text(10, 30, font=("", 25), anchor='w', fill='white', text='0')
        self.player2_scoretext = self.canvas.create_text(990, 30, font=("", 25), anchor='e', fill='white', text='0')
        self.start_text = self.canvas.create_text(500, 50, font=("", 50, 'bold'), fill='white', text='Click to start')

    def update_graphics(self):
        ball_coords = self.canvas.coords(self.ball)
        paddle1_coords = self.canvas.coords(self.paddle1)
        paddle2_coords = self.canvas.coords(self.paddle2)
        if self.player1_direction == 'up':
            if paddle1_coords[1] > 0:
                self.canvas.move(self.paddle1, 0, -4 + self.ball_speed * -0.5)
            else:
                self.canvas.move(self.paddle1, 0, 4 + self.ball_speed * 0.5)
        elif self.player1_direction == 'down':
            if paddle1_coords[3] < 600:
                self.canvas.move(self.paddle1, 0, 4 + self.ball_speed * 0.5)
            else:
                self.canvas.move(self.paddle1, 0, -4 + self.ball_speed * -0.5)
        if self.player2_direction == 'up':
            if paddle2_coords[1] > 0:
                self.canvas.move(self.paddle2, 0, -4 + self.ball_speed * -0.5)
            else:
                self.canvas.move(self.paddle2, 0, 4 + self.ball_speed * 0.5)
        elif self.player2_direction == 'down':
            if paddle2_coords[3] < 600:
                self.canvas.move(self.paddle2, 0, 4 + self.ball_speed * 0.5)
            else:
                self.canvas.move(self.paddle2, 0, -4 + self.ball_speed * -0.5)
        self.canvas.move(self.ball, self.ball_xv, self.ball_yv)
        if ball_coords[1] <= 0:
            self.ball_yv = self.ball_speed
        if ball_coords[3] >= 600:
            self.ball_yv = self.ball_speed * -1
        if ball_coords[0] <= paddle1_coords[2] and ball_coords[0] >= paddle1_coords[0] \
           and ball_coords[3] > paddle1_coords[1] and ball_coords[1] < paddle1_coords[3]:
            self.ball_xv = self.ball_speed
        if ball_coords[2] >= paddle2_coords[0] and ball_coords[2] <= paddle2_coords[2] \
           and ball_coords[3] > paddle2_coords[1] and ball_coords[1] < paddle2_coords[3]:
            self.ball_xv = self.ball_speed * -1
        if ball_coords[0] < 0:
            self.canvas.delete(self.ball)
            self.ball = self.canvas.create_oval(485, 285, 515, 315, outline='', fill='white')
            self.ball_xv = choice([-1 * self.ball_speed, self.ball_speed])
            self.ball_yv = choice([-1 * self.ball_speed, self.ball_speed])
            self.player2_score += 1
        if ball_coords[2] > 1000:
            self.canvas.delete(self.ball)
            self.ball = self.canvas.create_oval(485, 285, 515, 315, outline='', fill='white')
            self.ball_xv = choice([-1 * self.ball_speed, self.ball_speed])
            self.ball_yv = choice([-1 * self.ball_speed, self.ball_speed])
            self.player1_score += 1
        self.canvas.itemconfig(self.player1_scoretext, text=str(self.player1_score))
        self.canvas.itemconfig(self.player2_scoretext, text=str(self.player2_score))
        self.ball_speed += 0.001

    def start_game(self, x=None):
        self.started = True
        self.ball_xv = choice([-4, 4])
        self.ball_yv = choice([-4, 4])
        self.canvas.delete(self.start_text)

    def mainloop(self):
        while 1:
            try:
                if self.started:
                    self.update_graphics()
                self.canvas.update()
                sleep(0.01)
            except:
                exit

if __name__ == '__main__':
    app = Game()
