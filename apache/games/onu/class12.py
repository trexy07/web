

from base import *
import random

# from newbase import docio
# docio.enable()

class _app():
    def __init__(self):
        pass
    def getTextInput(self,text):
        getTextInput(text)
app=_app()




#jiberish
class TwelfthBit:
    def __init__(self):
        self.board=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.5]
        self.youLost=Label('',200,200,size=75,fill='white',border='black',bold=True)
        self.youLost2=Label('',200,275,size=75,fill='white',border='black',bold=True)
        self.message=Group(Rect(0,170,400,120,fill='white'),Label('use W.A.S.D or arrow keys.'  ,200,185,size=25),Label('Same number squares merge,',200,215,size=25),Label(' and try to get to the highest number.',200,245,size=25),Label('Use e to save and i to load.',200,275,size=25))
        self.squareGroup=Group()
        self.zeros=[]
        app.stepsPerSecond=0.5
        self.keySquareNum=0
        
        self.pickColor={
            0:'gray',
            2:'red',
            4:'orange',
            8:'yellow',
            16:'green',
            32:'blue',
            64:'darkviolet',
            128:'pink',
            256:rgb(255, 195, 30),
            512:rgb(255, 255, 100),
            1024:'lightgreen',
            2048:'cornflowerBlue',
            4096:'mediumSlateBlue',
            8192:'darkred',
            16384:'darkorange',
            32768:'gold',
            65536:'darkgreen',
            131072:'white',
            262144:'purple'}
        
        for i in range(2):
            
            self.keySquareNum=0
            for i in range(16):
                if self.board[self.keySquareNum] ==0:
                    self.zeros.append(self.keySquareNum)
                self.keySquareNum+=1
            self.board[choice(self.zeros)]=2
    
        self.drawboard()
        self.message.toFront()
        
            
        self.c0 = "​"
        self.c1 = "­"
        self.c2 = "﻿"
        self.outD={
            0:self.c0+self.c0+self.c0,
            2:self.c0+self.c0+self.c1,
            4:self.c0+self.c0+self.c2,
            8:self.c0+self.c1+self.c0,
            16:self.c0+self.c1+self.c1,
            32:self.c0+self.c1+self.c2,
            64:self.c0+self.c2+self.c0,
            128:self.c0+self.c2+self.c1,
            256:self.c0+self.c2+self.c2,
            512:self.c1+self.c0+self.c0,
            1024:self.c1+self.c0+self.c1,
            2048:self.c1+self.c0+self.c2,
            4096:self.c1+self.c1+self.c0,
            8192:self.c1+self.c1+self.c1,
            16384:self.c1+self.c1+self.c2,
            32768:self.c1+self.c2+self.c0,
            65536:self.c1+self.c2+self.c1,
            131072:self.c1+self.c2+self.c2,
            262144:self.c2+self.c0+self.c0,
            " ":self.c2+self.c2+self.c2}
        self.inD={
            self.c0+self.c0+self.c0:0,
            self.c0+self.c0+self.c1:2,
            self.c0+self.c0+self.c2:4,
            self.c0+self.c1+self.c0:8,
            self.c0+self.c1+self.c1:16,
            self.c0+self.c1+self.c2:32,
            self.c0+self.c2+self.c0:64,
            self.c0+self.c2+self.c1:128,
            self.c0+self.c2+self.c2:256,
            self.c1+self.c0+self.c0:512,
            self.c1+self.c0+self.c1:1024,
            self.c1+self.c0+self.c2:2048,
            self.c1+self.c1+self.c0:4096,
            self.c1+self.c1+self.c1:8192,
            self.c1+self.c1+self.c2:16384,
            self.c1+self.c2+self.c0:32768,
            self.c1+self.c2+self.c1:65536,
            self.c1+self.c2+self.c2:131072,
            self.c2+self.c0+self.c0:262144,
            self.c2+self.c2+self.c2:" "}
        self.pauseMenu=Group(Rect(0,0,400,400,fill="white"),Label("paused!",200,100,size=75),visible=False)
        self.restartButton=Group(Rect(200,315,372.5,50,align="center",fill="green"),Label("press this or hit r to restart",200,315,size=32)  )
        self.pauseMenu.add(self.restartButton)
        self.message.toFront()
    
    
    def check(self):
        action=False
        self.keySquareNum=0
        for i in range(15):
            if self.board[self.keySquareNum+1]==0 and not self.board[self.keySquareNum]==0:
                if not (self.keySquareNum+1==4 or self.keySquareNum+1==8 or self.keySquareNum+1==12 or self.keySquareNum+1==16):
                    action=True
            self.keySquareNum+=1
        self.keySquareNum=15
        for i in range(16):
            if not self.board[self.keySquareNum]==0:
                if self.board[self.keySquareNum+1]==self.board[self.keySquareNum] and not (self.keySquareNum==3 or self.keySquareNum==7 or self.keySquareNum==11 or self.keySquareNum==15):
                   action=True
            self.keySquareNum-=1
        self.keySquareNum=15
        for i in range(16):
            if self.board[self.keySquareNum-1]==0 and not self.board[self.keySquareNum]==0:
                if not self.keySquareNum-1==-1:
                    if not (self.keySquareNum-1==3 or self.keySquareNum-1==7 or self.keySquareNum-1==11):
                        action=True
            self.keySquareNum-=1
        self.keySquareNum=0
        for i in range(16):
            if not self.keySquareNum==0 and not self.board[self.keySquareNum]==0 :
                if self.board[self.keySquareNum-1]==self.board[self.keySquareNum] and not (self.keySquareNum==0 or self.keySquareNum==4 or self.keySquareNum==8 or self.keySquareNum==12):
                   action=True
            self.keySquareNum+=1
        self.keySquareNum=0
        for i in range(12):
            if not self.board[self.keySquareNum]==0:
                if self.board[self.keySquareNum+4]==0 and not self.keySquareNum==12:
                    action=True
            self.keySquareNum+=1
        self.keySquareNum=11
        for i in range(12):
            if not self.board[self.keySquareNum]==0:
                if self.board[self.keySquareNum]==self.board[self.keySquareNum+4]:
                    action=True
            self.keySquareNum-=1
        self.keySquareNum=15
        for i in range(12):
            if not self.board[self.keySquareNum]==0:
                if self.board[self.keySquareNum-4]==0:
                    action=True
            self.keySquareNum-=1
        self.keySquareNum=11
        for i in range(12):
            if not self.board[self.keySquareNum]==0:
                if self.board[self.keySquareNum]==self.board[self.keySquareNum+4]:
                    action=True
            self.keySquareNum-=1
        return(action)
    
    
    def score(self):
        self.keySquareNum=0
        e=0
        for i in range(16):
            e+=self.board[self.keySquareNum]
            self.keySquareNum+=1
        return(e)
    
    
    def drawboard(self):
        self.squareGroup.clear()
        squareNum=0
        topY=0
        sideX=0
        for i in range(16):
            b='black'
            t='black'
            if self.board[squareNum]==2.1:
                self.board[squareNum]=2
                b='white'
            elif self.board[squareNum]==4.1:
                self.board[squareNum]=4
                b='white'
            elif self.board[squareNum]==131072:
                t='black'
            self.squareGroup.add(Rect(sideX,topY,100,100,fill=self.pickColor[self.board[squareNum]],border=b))
            if not self.board[squareNum]==0:
                self.squareGroup.add(Label(self.board[squareNum],sideX+50,topY+50,size=150/len(str(self.board[squareNum]))-1,bold = True,fill=t))
            sideX+=100
            if sideX==400:
                sideX=0
                topY+=100
            squareNum+=1
        if self.score()>=262140:
            self.youLost.value='You Win!'
            self.youLost.toFront()
        elif not self.check():
            self.youLost.value='You Lost!'
            self.youLost2.value=self.score()
            self.youLost.toFront()
            self.youLost2.toFront()
    
    
    def onKeyPress(self,key):
        if self.pauseMenu.visible:
            if key=="escape":
                self.pauseMenu.visible=False
                self.message.visible=False
            elif key =="r":
                if app.getTextInput('type "RESTART" to confirm')=="RESTART":
                    self.board=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.5]
                    self.zeros=[]
                    for i in range(2):
                        self.keySquareNum=0
                        for i in range(16):
                            if self.board[self.keySquareNum] ==0:
                                self.zeros.append(self.keySquareNum)
                            self.keySquareNum+=1
                        self.board[choice(self.zeros)]=2
                    
                    self.drawboard()
                    self.youLost.visible=False
                    self.youLost2.visible=False
                    self.pauseMenu.visible=False
                    self.message.visible=False
        else:
            self.message.visible=False
            action=False
            if key=='d':
                self.onKeyPress('right')
            elif key=='a':
                self.onKeyPress('left')
            elif key=='s':
                self.onKeyPress('down')
            elif key=='w':
                self.onKeyPress('up')
            elif 'right' in key:
                for i in range(4):
                    self.keySquareNum=0
                    for i in range(15):
                        if self.board[self.keySquareNum+1]==0 and not self.board[self.keySquareNum]==0:
                            if not (self.keySquareNum+1==4 or self.keySquareNum+1==8 or self.keySquareNum+1==12 or self.keySquareNum+1==16):
                                self.board[self.keySquareNum+1]=self.board[self.keySquareNum]
                                self.board[self.keySquareNum]=0
                                action=True
                        self.keySquareNum+=1
                self.keySquareNum=15
                for i in range(16):
                    if not self.board[self.keySquareNum]==0:
                        if self.board[self.keySquareNum+1]==self.board[self.keySquareNum] and not (self.keySquareNum==3 or self.keySquareNum==7 or self.keySquareNum==11 or self.keySquareNum==15):
                           self.board[self.keySquareNum+1]=self.board[self.keySquareNum]*2
                           self.board[self.keySquareNum]=0
                           action=True
                    self.keySquareNum-=1
                for i in range(4):
                    self.keySquareNum=0
                    for i in range(15):
                        if self.board[self.keySquareNum+1]==0 and not self.board[self.keySquareNum]==0:
                            if not (self.keySquareNum+1==4 or self.keySquareNum+1==8 or self.keySquareNum+1==12 or self.keySquareNum+1==16):
                                self.board[self.keySquareNum+1]=self.board[self.keySquareNum]
                                self.board[self.keySquareNum]=0
                                action=True
                        self.keySquareNum+=1
            elif 'left' in key:
                for i in range(4):
                    self.keySquareNum=15
                    for i in range(16):
                        if self.board[self.keySquareNum-1]==0 and not self.board[self.keySquareNum]==0:
                            if not self.keySquareNum-1==-1:
                                if not (self.keySquareNum-1==3 or self.keySquareNum-1==7 or self.keySquareNum-1==11):
                                    self.board[self.keySquareNum-1]=self.board[self.keySquareNum]
                                    self.board[self.keySquareNum]=0
                                    action=True
                        self.keySquareNum-=1
                self.keySquareNum=0
                for i in range(16):
                    if not self.keySquareNum==0 and not self.board[self.keySquareNum]==0 :
                        if self.board[self.keySquareNum-1]==self.board[self.keySquareNum] and not (self.keySquareNum==0 or self.keySquareNum==4 or self.keySquareNum==8 or self.keySquareNum==12):
                           self.board[self.keySquareNum-1]=self.board[self.keySquareNum]*2
                           self.board[self.keySquareNum]=0
                           action=True
                    self.keySquareNum+=1
                for i in range(4):
                    self.keySquareNum=15
                    for i in range(16):
                        if self.board[self.keySquareNum-1]==0 and not self.board[self.keySquareNum]==0:
                            if not self.keySquareNum-1==-1:
                                if not(self.keySquareNum-1==3 or self.keySquareNum-1==7 or self.keySquareNum-1==11):
                                    self.board[self.keySquareNum-1]=self.board[self.keySquareNum]
                                    self.board[self.keySquareNum]=0
                                    action=True
                        self.keySquareNum-=1
            elif 'down' in key:
                for i in range(4):
                    self.keySquareNum=0
                    for i in range(12):
                        if not self.board[self.keySquareNum]==0:
                            if self.board[self.keySquareNum+4]==0 and not self.keySquareNum==12:
                                self.board[self.keySquareNum+4]=self.board[self.keySquareNum]
                                self.board[self.keySquareNum]=0
                                action=True
                        self.keySquareNum+=1
                self.keySquareNum=11
                for i in range(12):
                    if not self.board[self.keySquareNum]==0:
                        if self.board[self.keySquareNum]==self.board[self.keySquareNum+4]:
                            self.board[self.keySquareNum+4]=self.board[self.keySquareNum]*2
                            self.board[self.keySquareNum]=0
                            action=True
                    self.keySquareNum-=1
                for i in range(4):
                    self.keySquareNum=0
                    for i in range(12):
                        if not self.board[self.keySquareNum]==0:
                            if self.board[self.keySquareNum+4]==0 and not self.keySquareNum==12:
                                self.board[self.keySquareNum+4]=self.board[self.keySquareNum]
                                self.board[self.keySquareNum]=0
                                action=True
                        self.keySquareNum+=1
            elif 'up' in key:
                for i in range(4):
                    self.keySquareNum=15
                    for i in range(12):
                        if not self.board[self.keySquareNum]==0:
                            if self.board[self.keySquareNum-4]==0:
                                self.board[self.keySquareNum-4]=self.board[self.keySquareNum]
                                self.board[self.keySquareNum]=0
                                action=True
                        self.keySquareNum-=1
                self.keySquareNum=11
                for i in range(12):
                    if not self.board[self.keySquareNum]==0:
                        if self.board[self.keySquareNum]==self.board[self.keySquareNum+4]:
                            self.board[self.keySquareNum+4]=self.board[self.keySquareNum]*2
                            self.board[self.keySquareNum]=0
                            action=True
                    self.keySquareNum-=1
                for i in range(4):
                    self.keySquareNum=15
                    for i in range(12):
                        if not self.board[self.keySquareNum]==0:
                            if self.board[self.keySquareNum-4]==0:
                                self.board[self.keySquareNum-4]=self.board[self.keySquareNum]
                                self.board[self.keySquareNum]=0
                                action=True
                        self.keySquareNum-=1
            #if 'up' or 'down' or 'left' or 'right' in key:
            self.zeros.clear()
            self.keySquareNum=0
            for i in range(16):
                if self.board[self.keySquareNum] ==0:
                    self.zeros.append(self.keySquareNum)
                self.keySquareNum+=1
            if not len(self.zeros)==0 and action:
                self.board[choice(self.zeros)]=choice([2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,4.1])
                self.drawboard()
            if key=='e':
                self.keySquareNum=0
                save=''
                for i in range(randrange(4,8)):
                    save+=choice("""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/? """)
                for i in range(16):
                    save+=self.outD[self.board[self.keySquareNum]]+self.outD[' ']
                    self.keySquareNum+=1
                for i in range(randrange(4,8)):
                    save+=choice("""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890`~!@#$%^&*()-_=+[{]}\|;:'",<.>/? """)
                app.getTextInput('copy the text betwen the quotes "'+save+'  "then press ok.')
            elif key=='i':
                text=app.getTextInput('pase in the save and pess ok.')
                text2=''
                for item in text:
                    if item in self.c0+self.c1+self.c2:
                        text2+=item
                    
                text=''
                for i in range(len(text2)//3):
                    text+=str(self.inD[text2[i*3:i*3+3]]) 
                
                self.inport(text)
            elif key=="escape":
                self.pauseMenu.visible=True
                self.message.visible=True
                self.message.toFront()
    
    
    def inport(self,text):
        self.keySquareNum=0
        charNum=0
        piece=''
        for i in range(len(text)+1):
            if not str(text)[charNum:charNum+1]==' ':
                piece+=text[charNum:charNum+1]
            else:
                self.board[self.keySquareNum]=int(piece)
                ###
                piece=''
                self.keySquareNum+=1
            charNum+=1
        self.drawboard() 
    
    def onMousePress(self,x,y):
        if self.restartButton.contains(x,y):
            self.onKeyPress("r")

game=TwelfthBit()


def onKeyPress(ev):
    drawLabel(ev.key,200,200)
    key=ev.key
    game.onKeyPress(key)
document.bind("keydown", onKeyPress)
def onMousePress(ev):
    x,y=ev.x,ev.y
    game.onMousePress(x,y)
document["myCanvas"].bind("mousedown", onMousePress)


































