import sys
import time
from graphics import *

def main(): 
   global exitButtonX, exitButtonY
   global mouseX, mouseY, mousePoint
   global win
   exitButtonX = Point(0,0)
   exitButtonY = Point(50,50)
   win = GraphWin("D&D Dungeon Master Map", 500, 500, True)
   displayExit(win, exitButtonX,exitButtonY)
   setMouse()
   while(not exitPressed()):
      setMouse()

def  displayExit(window,exitButtonX,exitButtonY):
   exitButton = Rectangle(exitButtonX,exitButtonY)
   window.draw(exitButton)

def exitPressed():
   if(((mouseX >= 0) and (mouseY >= 0)) and ((mouseX<=  50) and (mouseY<= 50))) == True:
      return True
   else:
      return False

def setMouse():
   mousePoint = win.getMouse()
   mouseX = mousePoint.getX()
   mouseY = mousePoint.getY



if __name__ == "__main__":
   main()