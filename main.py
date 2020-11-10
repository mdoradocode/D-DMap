import sys
from graphics import GraphWin

def main(): 
   win = GraphWin("This is a window", 800, 800, True)
   print(win.getMouse())
   #win.close() 

main()
