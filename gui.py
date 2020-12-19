from tkinter import *

from tkinter import messagebox 

from mininetbackend import MyNet

  

top = Tk()

width = top.winfo_screenwidth()

height = top.winfo_screenheight()

c = Canvas(top,bg = "gray", height = height-200,width = width-200)

filename = PhotoImage(file = "comp.png")

switchImage = PhotoImage(file = "switch.png")

net = MyNet()





class Host:

    def __init__(self, x, y, hasLinkWith, isSwitch):     

        self.x = x

        self.y = y

        self.hasLinkWith=hasLinkWith

        self.isSwitch= isSwitch

        self.node = None

        

hostList=[]



#55x82 =imageSize Host

#100x44 =Switch



widthImage= 55

heightImage =82

widthImageSwitch=100

heightImageSwitch=44



addhostActive=False

addlinkActive=False

addSwitchActive=False

h1Select=-1

h1x=-1

h1y=-1

h2Select=-1

h2x=-1

h2y=-1







def addSwitch():

    global addSwitchActive

    addSwitchActive = True

    

    c.bind('<Button-1>', MouseClick)

    



    

def addHost():

    global addhostActive

    addhostActive = True

    c.bind('<Button-1>', MouseClick)

    

    



def addLink():

    global addlinkActive

    addlinkActive = True

    c.bind('<Button-1>', MouseClickLink1)



B = Button(top, text ="Add host", command = addHost)

C = Button(top, text ="Add link", command = addLink)

D = Button(top, text ="Add Switch", command = addSwitch)





def MouseClickLink2(event):

    

    global addlinkActive

    global h1Select

    global h2Select



        

        

    global h1x, h2x, h1y, h2y

    if h1Select != -1:

        placeholder1=False

        placeholder2=False

        for index, obj in enumerate(hostList):

            if index==h1Select:

                placeholder1=obj.isSwitch

        for index, obj in enumerate(hostList):

                if event.x < (obj.x + widthImage) and (event.x + widthImage)> obj.x and (event.y < obj.y) + heightImage and(event.y + heightImage) > obj.y:

                    if placeholder1==False and obj.isSwitch==False:

                        messagebox.showinfo(title='Error',

                                message='Link can not be created between two hosts.')

                        C["state"] = NORMAL

                        return

                    

                        

                        

                    h2Select = index

                    

                        

                    h2x=obj.x

                    h2y=obj.y

                    c.create_line(h1x,h1y,h2x,h2y,fill='black', width =5)

                    

                    

        if h1Select==h2Select:

            messagebox.showinfo(title='Error',

                                message='Link can not be created between a single host, Its already present.')

            h2Select=-1

                    

        for index, obj in enumerate(hostList):

            print(obj.hasLinkWith ,index )

            if index == h1Select:

                obj.hasLinkWith = h2Select

                

            if index == h2Select:

                obj.hasLinkWith = h1Select

                C["state"] = NORMAL



                h1Select= -1

                h2Select= -1

        

                

def MouseClickLink1(event):

    global addlinkActive

    global h1Select

    global h1x, h2x, h1y, h2y

    if addlinkActive:

        

        if len(hostList) < 2:

            messagebox.showinfo(title='Error',

                                message='There are less than two device or hosts')

            

        else:

            for index, obj in enumerate(hostList):

                if event.x < (obj.x + widthImage) and (event.x + widthImage)> obj.x and (event.y < obj.y) + heightImage and(event.y + heightImage) > obj.y:

                    h1Select = index

                    h1x=obj.x

                    h1y=obj.y

                    addlinkActive=False

                    C["state"] = DISABLED

                    c.bind('<Button-1>', MouseClickLink2)

    print(h1Select)



                

        



                



        

    

    

def MouseClick(event):

    global addhostActive

    global addSwitchActive

    

    if addhostActive:

        for obj in hostList: 

            if event.x < (obj.x + widthImage) and (event.x + widthImage)> obj.x and (event.y < obj.y) + heightImage and (event.y + heightImage) > obj.y:

                   return

        addhostActive=False

        hostList.append(Host(event.x,event.y,hasLinkWith=-1, isSwitch=False))

        c.create_image(event.x,event.y, anchor = CENTER, image=filename)

    if addSwitchActive:

        for obj in hostList: 

            if event.x < (obj.x + widthImage) and (event.x + widthImage)> obj.x and (event.y < obj.y) + heightImage and (event.y + heightImage) > obj.y:

                   return

        addSwitchActive=False

        switch = net.addSwitch()

        h =Host(event.x,event.y,hasLinkWith=-1, isSwitch=True)

        h.node = switch

        # h.node.name

        # h.node.IP()

        hostList.append(h)

        c.create_image(event.x,event.y, anchor = CENTER, image=switchImage)

    





c.bind('<Button-1>', MouseClickLink1)







c.pack()

B.pack()

C.pack()

D.pack()

top.mainloop()

