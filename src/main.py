import pygame,socket,sys,time,threading,math,pickle

from pygame.locals import *


#Create a timer class
class Timer: #Debugging timer
    def __init__(self):
        self.time_start = time.time()
        print(self.time_start)
    def start(self):
        self.time_start = time.time()
    def stop(self):
        time_end = time.time()
        return time_end - self.time_start

#Define a function to convert ortographic coordinates to screen coordinates
def ortographic_to_screen(x,y, offset_x = 0, offset_y = 0):
    return x*16 - y*16 + offset_x, y*8 + x * 8 + offset_y

#Define a function to convert screen coordinates to ortographic coordinates
def screen_to_ortographic(x,y, offset_x = 0, offset_y = 0):
    return (x + offset_x)//16, (y + offset_y)//8


#Create a basic pygame template
pygame.init()

#Set the debug mode to false
debug = False

#Create a screen
pygame.display.set_caption("AOTN")
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Create a clock
clock = pygame.time.Clock()
FPS = 60
#Create a fps timer
fps_timer = Timer()

#Create a font
font = pygame.font.SysFont("Arial", 20)

cubes_id = []

#Apeend 0 to the 0th index of the cubes list
cubes_id.append(0)

#Load the cube template onto the cubes id list
cubes_id.append(pygame.image.load("AOTN/src/Sprites/cube_template.png"))

#Create a 3D list of all the cubes
cubes = [
    [
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]],
        [cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1], cubes_id[1]]
    ]
]

while True:
    #Check for events
    for event in pygame.event.get():
        #If the user quits, quit the game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #If the user presses a key
        if event.type == KEYDOWN:
            #Check if the key pressed is the F3 key
            if event.key == K_F3:
                #Set the debug mode to its opposite
                debug = not debug
    

    #Fill the screen with black
    screen.fill((0,0,0))
    
    #For each height in the cubes list
    for y in reversed(range(0,len(cubes))):
        #For each row in the cubes list
        for row in range(0,len(cubes[0])):
            #For each column in the cubes list
            for column in range(0,len(cubes[0][0])):
                #If the cube is not empty
                if cubes[-y-1][row][column] != 0:
                    #Draw the cube template to the screen
                    screen.blit(cubes[-y-1][row][column], ortographic_to_screen(column+y,row+y,400-10*2,150+10*4))


    if debug:
        #Start the fps timer
        fps_timer.start()
    #Delay to get the correct FPS
    clock.tick(15)
    if debug:
        #Stop the fps timer
        fpst_end = fps_timer.stop()

    if debug:
        #If the fpst_end is too low, round it up to 1
        if fpst_end < 0.0000001:
            #print("fps_timer is too high")
            screen.blit(font.render("FPS too high", True, (255,255,255)), (0,0))
            fpst_end = 0.0000001
        else:
            #else, print the fps rounded to 1 decimal place
            screen.blit(font.render("FPS: " + str(round(1/fpst_end,1)), True, (255,255,255)), (0,0))

        #Blit the fps to the screen
        screen.blit(font.render("FPS: " + str(round(1 / fpst_end, 1)), True, (255, 255, 255)), (0, 0))

        #Blit the Milliseconds to the screen
        screen.blit(font.render("Milliseconds: " + str(round(fpst_end * 1000, 2)), True, (255, 255, 255)), (0, 20))

    #Update the screen
    pygame.display.update()