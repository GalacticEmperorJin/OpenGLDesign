# start drawing single point
import math as math
import sys
# import P
import OpenGL.GL as gl

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

except:
    print("Error: PyOpengl was not installed correctly")
    sys.exit()

class assignment1(object):
    
    def __init__(self) -> None:
    
        self.width = 800
        self.height = 600

    def initScene(self):
       
        glClearColor(0.9, 0.9, 0.9,0.00) #bg  color
        glClearDepth(1.0) 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
        glLoadIdentity() 

    def text(self):
        glPushMatrix()
        glColor4f(1,1,1,1)
        glTranslatef(-2.55,0.48,0)
        glScalef(0.005, 0.005, 0.005)
        glLineWidth(5.0)
        glutStrokeString(GLUT_STROKE_ROMAN, b"SABAH") 
        glPopMatrix()
        
        glPushMatrix()
        glColor4f(1,1,1,1)
        glTranslatef(-2.0,-0.05,0)
        glScalef(0.005, 0.005, 0.005)
        glLineWidth(5.0)
        glutStrokeString(GLUT_STROKE_ROMAN, b"MAJU") 
        glPopMatrix()
        
        glPushMatrix()
        glColor4f(1,1,1,1)
        glTranslatef(-1.6,-0.6,0)
        glScalef(0.005, 0.005, 0.005)
        glLineWidth(5.0)
        glutStrokeString(GLUT_STROKE_ROMAN, b"JAYA") 
        glPopMatrix()
        
    def background(self): 
        
        #frame
        glBegin(GL_QUADS)
        glColor3f((31/255),(111/255),(164/255))
        glVertex2f(-3.0,-4.0)
        glVertex2f(3.0,-4.0)
        glColor3f((133/255),(203/255),(204/255))
        glVertex2f(3.0,4.0)
        glVertex2f(-3.0,4.0)
        glEnd()

        #trees background
        glPushMatrix()
        glTranslatef(0,0.2,0)
        glColor3f((14/255),(119/255),(14/255))
        self.tree()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(0,-0.3,0)
        glColor3f((34/255),(139/255),(34/255))
        self.tree()
        glPopMatrix()
        
        #hill
        glBegin(GL_POLYGON)
        glColor3f((35/255),(104/255),(35/255))
        glVertex2f(3.0,-2.1)
        glVertex2f(1.95,-1.45)
        glColor3f((224/255),(215/255),(43/255))
        glVertex2f(-3.0,-1.45)
        glVertex2f(-3.0,-2.1)
        glEnd()

    def tree(self):
        glBegin(GL_QUADS),glVertex2f(-3,0.5),glVertex2f(3,0.5),glVertex2f(3,-2.0),glVertex2f(-3,-2.0),glEnd()
        self.circle(posx = 2.7,posy = 0.6,radius = 0.75)
        self.circle(posx = 1.5,posy = 0.3,radius = 0.55)
        self.circle(posx = 0.5,posy = 0.22,radius = 0.55)
        self.circle(posx = -1.3,posy = 0.3,radius = 0.55)
        self.circle(posx = -0.25,posy = 0.4,radius = 0.55)
        self.circle(posx = -2.5,posy = 0.6,radius = 0.75)
    
    def window(self):
        #semicircle
        glColor3f((43/255),(27/255),(23/255)),self.semiCircle(posx = 0.85,posy = 1.26,radius = 0.12)
        
        #frame
        glColor3f((43/255),(27/255),(23/255))
        glBegin(GL_QUADS)
        glVertex2f(0.73,1.26)
        glVertex2f(0.73,1.05)
        glVertex2f(0.97,1.05)
        glVertex2f(0.97,1.26)
        glEnd()
             
    def door(self):
        #semicircle
        glColor3f((43/255),(27/255),(23/255)),self.semiCircle(posx = 0.85,posy = -1.48,radius = 0.15)        
        
        #frame
        glColor3f((43/255),(27/255),(23/255))
        glBegin(GL_QUADS)
        glVertex2f(0.7,-1.75)
        glVertex2f(0.7,-1.48)
        glVertex2f(1.0,-1.48)
        glVertex2f(1.0,-1.75)
        glEnd()   
             
    def base(self):
        
        #main base
        glColor3f((232/255),(230/255),(222/255))
        glBegin(GL_QUADS)
        glVertex2f(1.13,1.5)
        glVertex2f(1.13,-1.75)
        glColor3f((248/255),(246/255),(240/255))
        glVertex2f(0.56,-1.75)
        glVertex2f(0.56,1.5)
        glEnd()
        
        glColor3f(0.0,0.0,0.0)
        glLineWidth(2.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(1.13,1.5)
        glVertex2f(1.13,-1.75)
        glVertex2f(0.56,-1.75)
        glVertex2f(0.56,1.5)
        glEnd()   

    def clock(self):
        #frame
        glColor3f((43/255),(27/255),(23/255)),self.circle(posx = 0.85,posy = 0.6,radius = 0.19)
        #clock
        glColor3f(0.95,0.95,0.95),self.circle(posx = 0.85,posy = 0.6,radius = 0.15)
        #minute clock hand
        glColor3f((43/255),(27/255),(23/255))
        glBegin(GL_LINES)
        glVertex2f(0.85,0.6)
        glVertex2f(0.85,0.72)
        glEnd()
        
        #second clock hand
        glColor3f((43/255),(27/255),(23/255))
        glBegin(GL_LINES)
        glVertex2f(0.85,0.6)
        glVertex2f(0.92,0.6)
        glEnd()
    
    def deco(self):
        #base
        glColor3f((248/255),(246/255),(240/255))
        glBegin(GL_QUADS)
        glVertex2f(0.7,0.41)
        glVertex2f(1.0,0.41)
        glVertex2f(1.0,-1.20)
        glVertex2f(0.7,-1.20)
        glEnd()
        
        #frame
        glColor3f((43/255),(27/255),(23/255))
        glLineWidth(2.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(0.7,0.41)
        glVertex2f(0.7,-1.20)
        glVertex2f(1.0,-1.20)
        glVertex2f(1.0,0.41)
        glEnd()
               
    def roof(self):
        
        glColor3f((220/255),(56/255),(31/255))
        glBegin(GL_QUADS)
        glVertex2f(0.56,1.65)
        glVertex2f(0.56,1.45)
        glVertex2f(1.365,1.45)
        glVertex2f(0.95,1.65)
        glEnd()
        
        glColor3f((220/255),(56/255),(31/255))
        glBegin(GL_TRIANGLES)
        glVertex2f(0.56,1.65)
        glVertex2f(0.95,1.65)
        glVertex2f(0.56,2.0)
        glEnd()
        
        #line
        glColor3f((43/255),(27/255),(23/255))
        glBegin(GL_LINE_LOOP)
        glVertex2f(0.56,2.0)
        glVertex2f(0.56,1.45)
        glVertex2f(1.365,1.45)
        glVertex2f(0.95,1.65)
        glEnd()
        
    def awning(self):
        
        #making the back
        glColor3f((43/255),(27/255),(23/255)),self.semiCircle(posx = 0.85,posy = 0.77,radius = 0.22)

        #making crescent
        posx = 0.85
        posy = 0.73
        radius = 0.21
        radius2 = 0.15
        sides = 99
        glColor3f((232/255),(230/255),(222/255))
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine = radius*math.cos(i*math.pi/sides) + posx
            sine = radius2*math.sin(i*math.pi/sides) + posy
            glVertex2f(cosine,sine)
        glEnd()
        
    def tower(self):
        self.base()       
        self.awning()
        self.window()
        self.clock()
        self.deco()
        self.door()
        
    def fences(self):
        #bottom base
        glColor3f((243/255),(232/255),(234/255))
        glLineWidth(3.5)
        glBegin(GL_LINES)
        glVertex3f(-0.76,-1.75,0)
        glVertex3f(1.14,-1.75,0)
        glEnd()
        
        #line
        glColor3f((243/255),(232/255),(234/255))
        glLineWidth(2.5)
        glBegin(GL_LINES)
        glVertex2f(1.14,-1.31)
        glVertex2f(1.14,-1.76)
        
        glVertex2f(1.04,-1.31)
        glVertex2f(1.04,-1.76)
        
        glVertex2f(0.94,-1.31)
        glVertex2f(0.94,-1.76)
        
        glVertex2f(0.84,-1.31)
        glVertex2f(0.84,-1.76)
        
        glVertex2f(0.74,-1.31)
        glVertex2f(0.74,-1.76)
        
        glVertex2f(0.64,-1.31)
        glVertex2f(0.64,-1.76)
        
        glVertex2f(0.54,-1.31)
        glVertex2f(0.54,-1.76)
        
        glVertex2f(0.44,-1.31)
        glVertex2f(0.44,-1.76)
        
        glVertex2f(0.34,-1.31)
        glVertex2f(0.34,-1.76)
        
        glVertex2f(0.24,-1.31)
        glVertex2f(0.24,-1.76)
        
        glVertex2f(0.14,-1.31)
        glVertex2f(0.14,-1.76)
        
        glVertex2f(0.04,-1.31)
        glVertex2f(0.04,-1.76)
        
        glVertex2f(-0.06,-1.31)
        glVertex2f(-0.06,-1.76)
        
        glVertex2f(-0.16,-1.31)
        glVertex2f(-0.16,-1.76)
        
        glVertex2f(-0.26,-1.31)
        glVertex2f(-0.26,-1.76)
        
        glVertex2f(-0.36,-1.31)
        glVertex2f(-0.36,-1.76)
        
        glVertex2f(-0.46,-1.31)
        glVertex2f(-0.46,-1.76)
        
        glVertex2f(-0.56,-1.31)
        glVertex2f(-0.56,-1.76)
        
        glVertex2f(-0.66,-1.31)
        glVertex2f(-0.66,-1.76)
        
        glVertex2f(-0.76,-1.31)
        glVertex2f(-0.76,-1.76)
        glEnd()
        
        #top base
        glColor3f((243/255),(232/255),(234/255))
        glLineWidth(3.5)
        glBegin(GL_LINES)
        glVertex3f(-0.76,-1.45,0)
        glVertex3f(1.14,-1.45,0)
        glEnd()
    
    def circle(self,posx=0,posy=0,radius=1):
        #Draw a circle
        sides = 99
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine=radius*math.cos(i*2*math.pi/sides)+posx
            sine=radius*math.sin(i*2*math.pi/sides)+posy
            glVertex2f(cosine,sine)
        glEnd()
    
    def semiCircle(self,posx=0,posy=0,radius=1):
       #Draw a circle
        sides = 99
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine=radius*math.cos(i*math.pi/sides)+posx
            sine=radius*math.sin(i*math.pi/sides)+posy
            glVertex2f(cosine,sine)
        glEnd() 
              
    def drawScene(self):
        
        self.background()
        
        #fence1(back.right)
        glPushMatrix()
        glTranslatef(1.2,0.0,-0.9)
        self.fences()
        glPopMatrix()
        
        #fence(back.left)
        glPushMatrix()
        glTranslatef(-1.2,0.0,-0.9)
        self.fences()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(-2,0,-0.9)
        self.fences()
        glPopMatrix()
        
        #tower
        glPushMatrix()
        glRotatef(25,0,2,0)
        self.tower()
        self.roof()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(-0.53,0,-0.70)
        glRotatef(25,0,-2.0,0)
        self.tower()
        glPopMatrix()
    
        #left side roof
        glPushMatrix()
        glScalef(1.0,0.91,0.9)
        glRotatef(155,0.0,0.01,0.0)
        glTranslatef(-1.15,-0.056,-0.22)
        self.roof()
        glPopMatrix()
        
        #fence(right)
        glPushMatrix()
        glTranslatef(1.9,0,0.0)
        glRotatef(40,0,1,0)
        glTranslatef(-0.95,0.22,0.0)
        self.fences()
        glPopMatrix()
        
        #fence(front)
        glPushMatrix()
        glTranslatef(-0.45,-0.01,0.5)
        self.fences()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(-2.36,-0.01,0.5)
        self.fences()
        glPopMatrix()
        
        #fence(left)
        glPushMatrix()
        glTranslatef(-2,0,-0.9,)
        glRotatef(40,0,1,0)
        glTranslatef(-1.85,0.10,0.0)
        self.fences()
        glPopMatrix()
        
        self.text()
        
    def keyPressed(self,*args):
        
        if args[0] == b"q":
            os.exit(0)
            
        if args[0] == b"Q":
            os.exit(0)   
                    
        glutPostRedisplay()
        
    def display(self):

        self.initScene()
        glLoadIdentity()
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) #set camera properties
        self.drawScene()
        glutSwapBuffers()
        
    def reshape (self,width,height) :
        
        width=self.width
        height=self.height
        
        if height == 0: 
            height = 1

        glViewport (0, 0, (int)(width), (int)(height)) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective (45, (float)(width) / (float)(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
 
    def sceneLoop(self):
        glutInit(sys.argv) 
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) 
        glutInitWindowSize(self.width, self.height) 
        glutInitWindowPosition(100, 100) 
        glutCreateWindow(b"Sabah Maju Jaya")  
        glutDisplayFunc(self.display)  
        glutReshapeFunc (self.reshape)
        glutIdleFunc(self.display) 
        glutKeyboardFunc(self.keyPressed) 
        glutMainLoop() 

def main():
    myCg = assignment1()
    myCg.sceneLoop()

if __name__== "__main__":
    main()