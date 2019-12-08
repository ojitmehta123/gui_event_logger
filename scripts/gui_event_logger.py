#! /usr/bin/env python
__author__='Ojit Mehta'
import rospy , Tkinter as tk

rospy.init_node("event_logger", anonymous=True)
class Gui(object):
    def __init__(self):
        self.count=1
        self.root = tk.Tk()
        self.img = tk.PhotoImage\
            (file = "../image.gif")
        tk.Label(self.root , image = self.img , ).pack()
        tk.Button(self.root , fg="red" , text = "QUIT" , width = 70 , command = self.root.destroy)\
            .pack(side = tk.LEFT)
        tk.Button(self.root , text = "LOG" , width = 70 , command = self.log_info)\
            .pack(side = tk.RIGHT)
    
    def log_info(self):
        rospy.loginfo("Logging event %r at time %r"%(self.count , rospy.get_time()))
        self.count+=1

    def start(self):
        self.root.mainloop()

if __name__=="__main__":
    o=Gui()
    o.start()