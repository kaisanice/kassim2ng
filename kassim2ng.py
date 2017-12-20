import tkinter
from tkinter import messagebox

okToPressReturn = True

k6ht = 100
skoor = 0
raha = 0
toit = 2


def startGame(event):
    
    global okToPressReturn
    
    if okToPressReturn == True:
    
        startLabel.config(text="")
        updatek6ht()
        updateskoor()
        updateraha()
        
        updateDisplay()
        
        okToPressReturn = False

 
def updateDisplay():
    
    global k6ht, skoor
    
    if k6ht <= 0:
        catPic.config(image = gameoverpic)
    elif k6ht <= 25:
        catPic.config(image = n2ljaseim)
    elif k6ht <= 50:
        catPic.config(image = n2ljasem)
    elif k6ht <= 75:
        catPic.config(image = n2ljane)
    else:
        catPic.config(image = tavaline)

    k6htLabel.config(text="kõht: " + str(k6ht))
    skoorLabel.config(text="skoor: " + str(skoor))
    rahaLabel.config(text="raha: " + str(raha))
    toitLabel.config(text="toit: " + str(toit))
    
    catPic.after(100, updateDisplay)


def updatek6ht():
    
    global k6ht, skoor
    k6ht -= 1
    
    if isAlive():
        k6htLabel.after(250 if skoor > 10 else 500, updatek6ht)

def updateskoor():
    
    global skoor
    skoor += 1
    if isAlive():
        skoorLabel.after(5000, updateskoor)
                
def updateraha():
    
    global raha, k6ht 
    rahaLabel.after(1000, updateraha)
    if k6ht < 75:
        return
    raha = raha + 1
    
def feed():
    
    global k6ht, toit    
    if isAlive() and toit >= 2:
        toit = toit -2
        if k6ht <= 95:
            k6ht += 20
        else:
            k6ht -=20
    

def isAlive():
    
    global k6ht
    if k6ht <= 0:
        startLabel.config(text="jooksis minema sest nälg")     
        return False
    else:
        return True
        
def open_store():
    
    store = tkinter.Toplevel(root)
    store.title("kauplus")
    store.geometry("600x300")
    
    btnheatoit = tkinter.Button(store, command = tehing1)
    btnheatoit.pack(side = "right")
    btnheatoit.config(image = heatoit, width="300",height="300")
    
    btnhalbtoit = tkinter.Button(store, command = tehing2) 
    btnhalbtoit.pack(side = "left")
    btnhalbtoit.config(image = halbtoit, width="300",height="300")
    

def tehing1():
    
    global raha, toit
    if raha < 10:
        messagebox.showerror("viga!", "kes ei tööta, see ei söö :(")
    else:
        if raha >= 10:
            raha = raha -10
            toit = toit +4
 
def tehing2():
    
    global raha, toit
    if raha < 5:
        messagebox.showerror("viga!", "kes ei tööta, see ei söö :(")
    else:
        if raha >= 5:
            raha = raha -5
            toit = toit +2
            
root = tkinter.Tk()

root.title("kassimäng")
root.config(bg = "black")

root.geometry("960x690")

labels = tkinter.Frame(height = "50", bg = "black")
labels.pack(fill = tkinter.X)

startLabel = tkinter.Label(labels, text="VAJUTA TÜHIK ALUSTAMISEKS", font=('Helvetica', 18), bg="black", fg="white")
startLabel.pack(side="left")

k6htLabel = tkinter.Label(labels, text="kõht: " + str(k6ht), font=('Helvetica', 12), bg="black", fg="white")
k6htLabel.pack(side="right", ipadx = "20")

skoorLabel = tkinter.Label(labels, text="skoor: " + str(skoor), font=('Helvetica', 12), bg="black", fg="white")
skoorLabel.pack(side="right", ipadx = "20")

toitLabel = tkinter.Label(labels, text="toit: " + str(skoor), font=('Helvetica', 12), bg="black", fg="white")
toitLabel.pack(side="right", ipadx = "20")

rahaLabel = tkinter.Label(labels, text="raha: " + str(skoor), font=('Helvetica', 12), bg="black", fg="white")
rahaLabel.pack(side="right", ipadx = "20")

n2ljane = tkinter.PhotoImage(file="must kass poolnäljane.gif")
n2ljasem = tkinter.PhotoImage(file="must kass näljane.gif")
n2ljaseim = tkinter.PhotoImage(file="must kass näljane ja must.gif")
tavaline = tkinter.PhotoImage(file="must kass catcoin.gif")
heatoit = tkinter.PhotoImage(file="hea.gif")
halbtoit = tkinter.PhotoImage(file="halb.gif")
gameoverpic = tkinter.PhotoImage(file="uus kass piilub.gif")

catPic = tkinter.Label(root, image=tavaline, height = "600")
catPic.pack()

btnFeed = tkinter.Button(root, text="anna talle", command=feed)
btnFeed.pack(side = "left", ipadx = "100", ipady = "100")
btnFeed.config(bg = "green")
btnFeed.pack()

btnStore = tkinter.Button(root, text="osta süüa nh", command=open_store)
btnStore.pack(side = "right", ipadx = "100", ipady = "100")
btnStore.config(bg = "red")
btnStore.pack()
               

root.bind('<space>', startGame)

root.mainloop()