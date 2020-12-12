from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# Конфигурации окна
WIDTH = 800
HEIGHT = 600
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
    """ снаряд """

    def __init__(self, x=40, y=450):
        """
        Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = 3
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30  # шарик показывается пока live > 0

    def set_coords(self):
        canv.coords(
                    self.id,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r
                    )

    def move_bullet(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 1.2 + (abs(self.vy) / self.vy) * 0.7
        self.vx -= (abs(self.vx) / self.vx) * 0.15

        if self.x > WIDTH - 3 * self.r or self.x < 2 * self.r:
            self.vx = - self.vx
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()

        if self.y + 3 * self.r > HEIGHT or self.y < 3 * self.r:
            self.vy = - self.vy
            self.vy -= 3
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()
        if abs(self.vx) and abs(self.vy) < 1.5:
            self.live -= 1

        else:
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()

    def delete(self):
        canv.delete(self.id)

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
        obj: Обьект, с которым проверяется столкновение.
        Returns:
        Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2):
            return True
        else:
            return False


class Gun():
    """ пушка """

    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]  # Создаётся список шариков
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """
        Прицеливание. Зависит от положения мыши.
        """
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(
                    self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1  # Цель отображается на экране пока live > 0
        self.vx = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 50, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """первая цель"""
        x = self.x = rnd(200, 700)
        y = self.y = rnd(200, 550)
        r = self.r = rnd(10, 50)
        vx = self.vx = rnd(5, 15)
        vy = self.vy = rnd(5, 15)

        color = self.color = 'blue'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        """движение цели"""
        if self.x + self.r > WIDTH or self.x - self.r < 0:
            self.vx = - self.vx
            self.x += self.vx
            self.set_coords()

        if self.y + self.r > HEIGHT or self.y - self.r < 0:
            self.vy = - self.vy
            self.y -= self.vy
            self.x += self.vx
            self.set_coords()
        else:
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r)

    def hit(self, points=1):
        """Попадание шарика в цель"""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def delete(self):
        canv.coords(self.id, -10, -10, -10, -10)


class Target2():
    """вторая цель"""

    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(100, 50, text=self.points, font='35')  # Счётчик для второй цели
        self.new_target()

    def new_target(self):
        """инициализация второй цели"""
        x = self.x = rnd(200, 700)
        y = self.y = rnd(200, 550)
        r = self.r = rnd(10, 50)
        vx = self.vx = rnd(5, 15)
        vy = self.vy = rnd(5, 15)
        color = self.color = 'pink'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        """ движение цели"""
        if self.x + self.r > WIDTH or self.x - self.r < 0:
            self.vx = - self.vx
            self.x += self.vx
            self.set_coords()

        if self.y + 2 * self.r > HEIGHT or self.y - self.r < 0:
            self.vy = - self.vy
            self.y -= self.vy
            self.x += self.vx
            self.set_coords()
        else:
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r)

    def hit(self, points=1):
        """Попадание шарика в цель"""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = Target()
t2 = Target2()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1

    while t1.live or t2.live or balls:
        for b in balls:
            b.move_bullet()

            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if t1.live == 0 and t2.live == 0:
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')

        for i in range(len(balls)):
            if balls[i].live <= 0:
                balls[i].delete()
                balls[i] = None

        if t1.live > 0:
            t1.move()
        if t2.live > 0:
            t2.move()

        balls = [ball for ball in balls if ball is not None]

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()

    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
    root.after(750, new_game)


new_game()

root.mainloop()