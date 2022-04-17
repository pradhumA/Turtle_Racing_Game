""" main file """
import random
import turtle
import time

WIN_LENGTH = 500
WIN_HEIGHT = 500

turtle.screensize(WIN_LENGTH, WIN_HEIGHT)


class Racer(object):
    """ racer class starting """

    def __init__(self, color, pos):
        """ initialisation """
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        """ move """
        rar_r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + rar_r)
        self.turt.pendown()
        self.turt.forward(rar_r)

    def reset(self):
        """ reset """
        self.turt.penup()
        self.turt.setpos(self.pos)


def setup_file(name, colors):
    """ setup file """
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()


def start_game(turtle_s):
    """ start game"""
    t_list = []
    turtle.clearscreen()
    # turtle.hideturtle()
    colors = ["red", "green", "cyan", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
    start_s = -(WIN_LENGTH / 2) + 20
    for tak_t in range(turtle_s):
        new_posx = start_s + tak_t * WIN_LENGTH // turtle_s
        t_list.append(Racer(colors[tak_t], (new_posx, -230)))
        t_list[tak_t].turt.showturtle()

    run = True
    while run:
        for tor_t in t_list:
            tor_t.move()

        max_color = []
        max_dis = 0
        for tar_t in t_list:
            if tar_t.pos[1] > 230 and tar_t.pos[1] > max_dis:
                max_dis = tar_t.pos[1]
                max_color = [tar_t.color]
            elif tar_t.pos[1] > 230 and tar_t.pos[1] == max_dis:
                max_dis = tar_t.pos[1]
                max_color.append(tar_t.color)

        if len(max_color) > 0:
            run = False
            print('The winner turtle is: ')
            for win in max_color:
                print("***", win, "***")
                if (win == predict):
                    print("correct prediction")
                else:
                    print("Incorrect prediction")
                return 0

    old_score = []
    file = open('col.txt', 'r')
    for line in file:
        lay_l = line.split()
        color = lay_l[0]
        score = lay_l[1]
        old_score.append([color, score])

    file.close()

    file = open('col.txt', 'w')

    for entry in old_score:
        for winner in max_color:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1

        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')

    file.close()
    return 0

print('-----------------------------------')
start = input('Would you like to play ')
if start.upper() == "YES":
    turtles = int(input('Enter the number of racers (2 - 10): '))

    if 2 <= turtles <= 10:
        # turtles
        print("Now predict which TURTLE win ")
        predict=input()
        print("*** Now Turtle are Racing ---->>>")
    else:
        print('Number not in range 2-10. Try Again!')

    start_game(turtles)

    print('-----------------------------------')
    start = input('Would you like to play again ')
    if start.upper() == "YES":
        turtles = int(input('Enter the number of racers (2 - 10): '))

        if 2 <= turtles <= 10:
            # turtles
            print("Now predict which TURTLE win ")
            predict = input()
            print("*** Now Turtle are Racing ---->>>")
        else:
            print('Number not in range 2-10. Try Again!')
        start_game(turtles)
        print('-----------------------------------')
        start = input('Would you like to play again ')
        if start.upper() == "YES":
            turtles = int(input('Enter the number of racers (2 - 10): '))

            if 2 <= turtles <= 10:
                # turtles
                print("Now predict which TURTLE win ")
                predict = input()
                print("*** Now Turtle are Racing ---->>>")
            else:
                print('Number not in range 2-10. Try Again!')
            start_game(turtles)
        else:
            print(" Thank You, Try Again, Next time !!!  ")
    else:
        print(" Thank You, Try Again, Next time !!!  ")
else:
    print(" Thank You, Try Again, Next time !!!  ")
time.sleep(5)
