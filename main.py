#############################
#          GK Lab2
#############################
#   Jakub Pawleniak 248897
#############################

import sys
import random

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

#losowanie koloru prostokąta ( od 0.1 do 1.0 )
red = random.random()
green = random.random()
blue = random.random()
################### Samopodobienstwo (dywan Sierpińskiego)
samopodo = 5
###################
def startup():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    update_viewport(None, 400, 400)



def shutdown():
    pass

def dywano(x,y,a,b,moc):
    if moc > 0:
        moc = moc - 1
        a = a/3
        b = b/3

        dywano(x + a, y , a, b, moc)
        dywano(x+a, y-b ,a, b, moc)
        dywano(x,y-b,a,b,moc)
        dywano(x-a,y-b,a,b,moc)
        dywano(x-a,y,a,b,moc)
        dywano(x-a,y+b,a,b,moc)
        dywano(x,y+b,a,b,moc)
        dywano(x+a,y+b,a,b,moc)
    else:
        drawRectange2(x,y,a,b)

def drawColorfulTriangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-100,-100)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-90, -95)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-93,-80)
    glEnd()

def drawRectange(x, y, a, b, d = 0.0):
    # x,y to współrzędne środka

    glColor3f(red,green,blue)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - (a/2), y + (b/2) + d*b)          #lewa góra + deformacja
    glVertex2f(x + (a/2), y + (b/2))                #prawa góra
    glVertex2f(x - (a/2), y - (b/2))                #lewy dół
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(x + (a/2), y + (b/2))                #prawa góra
    glVertex2f(x - (a/2), y - (b/2))                #lewy dół
    glVertex2f(x + (a/2), y - (b/2) - d*b)          #prawy dół + deformacja
    glEnd()

def drawRectange2(x, y, a, b, d = 0.0):
    # x,y to współrzędne środka

    glColor3f(0,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - (a/2), y + (b/2) + d*b)          #lewa góra + deformacja
    glVertex2f(x + (a/2), y + (b/2))                #prawa góra
    glVertex2f(x - (a/2), y - (b/2))                #lewy dół
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(x + (a/2), y + (b/2))                #prawa góra
    glVertex2f(x - (a/2), y - (b/2))                #lewy dół
    glVertex2f(x + (a/2), y - (b/2) - d*b)          #prawy dół + deformacja
    glEnd()

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

   #  drawColorfulTriangle()          # CZĘŚĆ NA 3.0
   #  drawRectange(0,0,100,50,0.2)    # 3.5 + 4.0 (x,y to środek)
    dywano(0,0,200,100,samopodo)    # 4.5

    glFlush()

def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio, 1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0, 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def main():

    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()