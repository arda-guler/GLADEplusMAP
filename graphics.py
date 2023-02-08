import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

def drawOrigin():
    glBegin(GL_LINES)
    glColor(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(0,1,0)
    glColor(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    glColor(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)
    glEnd()

def drawGalaxies(galaxies, min_mass, max_mass, inverse_mass_range, cam):
    
    glBegin(GL_POINTS)
    for galaxy in galaxies:
        blue = (galaxy.M - min_mass) * inverse_mass_range
        red = 1 - blue
        glColor(red, 0, blue)
        x = galaxy.pos.x
        y = galaxy.pos.y
        z = galaxy.pos.z
        glVertex3f(x, y, z)
    glEnd()
