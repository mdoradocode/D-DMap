import sys
import time
from graphics import *

def main(): 
   
   win = GraphWin("This is a window", 500, 500, True)
   R = Rectangle(Point(50,50),Point(100,100))
   R.draw(win)
   global closeX, closeY, mousePoint
   mousePoint = win.getMouse()
   closeY = mousePoint.getY()
   closeX = mousePoint.getX()
   while (((closeX >= 50) and (closeY >= 50)) and ((closeX<=  100) and (closeY <= 100))) != True:
      start = time.time()
      mousePoint = win.getMouse()
      print(mousePoint)
      closeY = mousePoint.getY()
      closeX = mousePoint.getX()
      print(time.time() - start)
   win.close()

main()