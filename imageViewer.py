import tkinter as tk
from PIL import ImageTk,Image
import os, traceback

root = tk.Tk()

def listDir():

    imageFolder = '/Users/benjaminrobbins/Documents/python/gui/imageFolder'
    os.chdir(imageFolder)
    #print(os.listdir())
    listDir = []
    for image in os.listdir():
        if not image.startswith('.'):
            listDir.append(image)
    #print(listDir)
    listDirTk = []
    for image in listDir:
    
        image = Image.open(image)
        image = image.resize((300,300))
        image = ImageTk.PhotoImage(image)
        listDirTk.append(image)
        #print(type(image))
    

    return listDirTk
ld = listDir()
#print(f'Image list: {ld}')

def back(imageNumber):
    global picLabel
    global forwardButton
    global buttonBack
    print(ld)
    print(f'current image number: {imageNumber}')
    
    try:
        
        if imageNumber < 0: #technically don't need this anymore
            print('back1') 
            print(f'current image number: {imageNumber}')
            picLabel.grid_forget()
            picLabel = tk.Label(text='Out of pictures',width=300,height=300)
            picLabel.grid(row=1,column=1)
            backButton = tk.Button(root,text='Back',state=tk.DISABLED)
        
        elif imageNumber == 0: #initial state       
            print('back2')
            print(f'current image number: {imageNumber}')
            
            picLabel.grid_forget()
            picLabel = tk.Label(image=ld[imageNumber]) 
            picLabel.grid(row=1,column=1)
            
            backButton = tk.Button(root,text='Back', command=lambda :back(0), state=tk.DISABLED)
            quitButton = tk.Button(root,text='Quit app',command=root.quit)
            forwardButton = tk.Button(root,text='Forward',command=lambda: forward(0))
            
            backButton.grid(row=2,column=0)
            quitButton.grid(row=2,column=1)
            forwardButton.grid(row=2,column=2)
        
        elif imageNumber > len(ld) - 1: #in this case at imageNunber: 2, hitting back would change the nezxt picture to picture index 1 (second picture) with imageNumber decrement 
            print('back3')
            print(f'current image number: {imageNumber}') # == 2
\
            picLabel.grid_forget()
            picLabel = tk.Label(image=ld[imageNumber]) 
            forwardButton = tk.Button(root,text='Forward',command=lambda: forward(imageNumber-1)) #button is now 1 
            backButton = tk.Button(root,text='Back',command=lambda: back(imageNumber-1)) #button is now 1
            picLabel.grid(row=1,column=1)
            forwardButton.grid(row=2,column=2)
            backButton.grid(row=2,column=0)
        else:
            print('back4')
            print('else statement back')
            print(f'current image number: {imageNumber}')
            #print(f'Current picture: {ld[imageNumber]}')
            picLabel.grid_forget()
            picLabel = tk.Label(image=ld[imageNumber]) 
            forwardButton = tk.Button(root,text='Forward',command=lambda: forward(imageNumber - 1))
            backButton = tk.Button(root,text='Back',command=lambda: back(imageNumber - 1))
            picLabel.grid(row=1,column=1)
            forwardButton.grid(row=2,column=2)
            backButton.grid(row=2,column=0)
            print(f'current image number: {imageNumber}')

    
    except:
        print(traceback.format_exc())

def forward(imageNumber):
    print(ld)
    global picLabel
    global forwardButton
    global buttonBack
    
    try:        
        if (imageNumber + 1) > (len(ld)-1):
            print('Out of pictures statement')
            print(f'current image number: {imageNumber}')
            picLabel.grid_forget()
            picLabel = tk.Label(text='Out of pictures',width=15,height=10)
            picLabel.grid(row=1,column=1)
            forwardButton = tk.Button(root,text='Forward',state=tk.DISABLED)
            forwardButton.grid(row=2,column=2)

        else:   
            print(f'current image number: {imageNumber}')
            #print(len(ld))
            picLabel.grid_forget()
            picLabel = tk.Label(image=ld[imageNumber+1]) #move picture forward in list 
            forwardButton = tk.Button(root,text='Forward',command=lambda: forward(imageNumber + 1))
            backButton = tk.Button(root,text='Back',command=lambda: back(imageNumber + 1))
            picLabel.grid(row=1,column=1)
            forwardButton.grid(row=2,column=2)
            backButton.grid(row=2,column=0)
    except:
        print(traceback.format_exc())
            
    
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='/Users/benjaminrobbins/Documents/python/gui/play.png'))
root.title('Image Viewer')

curdir = os.path.abspath(os.curdir)
topLabel = tk.Label(text=curdir)
topLabel.grid(row=0, column=0, columnspan=3)

picLabel = tk.Label(image = ld[0])
picLabel.grid(row=1,column=1)

#print(f'First picture int list: {ld[0]}')

backButton = tk.Button(root,text='Back',command=lambda :back(0),state=tk.DISABLED)
quitButton = tk.Button(root,text='Quit app',command=root.quit)
forwardButton = tk.Button(root,text='Forward',command=lambda: forward(0))

backButton.grid(row=2,column=0)
quitButton.grid(row=2,column=1)
forwardButton.grid(row=2,column=2)

root.mainloop()