import tkinter as tk

class Point():
    def __init__(self, x, y, list) -> None:
        self.__x = int(x)
        self.__y = int(y)
        self.__verticies = list

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def verticies(self):
        return self.__verticies
    
    @verticies.setter
    def verticies(self, value):
        self.__verticies = value
    
    

class AwsomeGraphics:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Noe Stuff")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()
        
        self.pointsreadout()
        self.linemaker()
        
        
        self.root.mainloop()

        
    def pointsreadout(self):
        with open('graph.txt', 'r+') as f:
            line_amount = int(f.readline().strip())
            self.pointlist = [[]]*line_amount
            for n in range(0,line_amount):
                linestring = f.readline()
                pointnumber = int(linestring[0:1])       
                valuelist = (linestring[2:].rstrip('\n')).split(" ",2) #[x,y, p1 p2 p3\n]
                values = valuelist[2].split()
                self.pointlist[pointnumber] = (Point(valuelist[0], valuelist[1], values))
        self.pointmaker()


    def pointmaker(self):
        for point in self.pointlist:
            self.canvas.create_oval(point.x-2, point.y-2, point.x+2, point.y+2, fill='black')
    
    def linemaker(self):
        existing_lines = []
        for point in self.pointlist:
            spokes = point.verticies
            for spoke in spokes:
                spoke = int(spoke)
                if (point.x+self.pointlist[spoke].x)*10+point.y+self.pointlist[spoke].y not in existing_lines:#sjekk om en string med lik index finnes
                    existing_lines.append((point.x+self.pointlist[spoke].x)*10+point.y+self.pointlist[spoke].y) #lag en index basert på sum av koordinata.
                    self.canvas.create_line(point.x, point.y, self.pointlist[spoke].x,  self.pointlist[spoke].y)
        

AwsomeGraphics()
            
#def read_file():
#    with open("graph.txt", "r") as file:
#        data = []
#        n = file.readline().strip()
#        for i in range(int(n)):
#            data.append(file.readline().strip())
#
#        pointslist = []
#        for line in data:
#            line = line.split()
#            line = [int(x) for x in line]
#            pointslist.append(line)
#
#        return pointslist