import browser
# import browser.aio as aio
# from base import *
# from base import getTextInput, make_uno, public, private, join, names, rescroll, rgb, drawRect, drawCircle, drawLabel, gradient2
from base import (
    getTextInput,
    make_uno,
    public,
    private,
    join,
    names,
    rescroll,
    rgb,
    drawRect,
    # drawCircle,
    drawLabel,
    gradient2,
    drawRegularPolygon,
    drawOval,
    restart,
    makeDsdfb, playDsdfb, pauseDsdfb,
)


# print(browser.window.location.origin+'/games/?id=2&uid=1')
# browser.window.history.pushState({},'',browser.window.location.origin+'/games/?id=2&uid=1')
########### setting url without redirect ^

# print(browser.window.location.search)


# print(ID,UID)

# print(type(browser.document.query))
# ID=browser.document.query.get('id')
# UID=browser.document.query.get('uid')
# print(ID,UID)
# from urllib.parse import parse_qs


# from base import drawRegularPolygon

from game import Game

# globalYOffset, globalXOffset = canvas.getBoundingClientRect().top, canvas.getBoundingClientRect().left # used for repositioning the mouse location


# function resizeCanvas() {
# def size:
# canvas.width = window.innerWidth
# canvas.height = window.innerHeight
# window.addEventListener('resize', size, false);


class Menu:
    def __init__(self):
        # self.drawMainMenu()
        
        self.drawSplash()
        self.game = None
        self.paused = False
        self.splash = 2 
        
        self.names = names()
        self.page = 0
        self.i = None

        self.uid = None
        # self.names=await self.names
        
        try:
            ID = int(browser.document.query["id"])

            index = self.names["index"].index(ID)
            self.page = index // 11
            self.i = index % 11
            

            self.uid = int(browser.document.query["uid"])
            if not 0 <= self.uid <= 4:
                self.uid = None

        except Exception as e:
            # print("na", e)
            # self.page = 0
            # self.i = None
            self.uid = None
            pass
            
        self.playing_audio=False
        makeDsdfb()

    def drawSplash(self):
        # drawRect(0, 0, 400, 400, fill='midnightblue')
        # drawLabel("splash", 200, 200, size=130, rotateAngle=45)
        _red = rgb(0xD7, 0x26, 0x00)
        _yellow = rgb(0xEC, 0xD4, 0x07)
        _green = rgb(0x37, 0x97, 0x11)
        _blue = rgb(0x09, 0x56, 0xBF)
        # browser.document.body.style.backgroundColor = _blue

        drawRect(0, 0, 400, 400,fill='black')

        x, y = 200, 200
        font = "comic sans Ms" if "unit4" == "unit3" else "cabin"# or cabin
        scale = 6
        #         drawCircle(x-4,y+3,45/2,fill=rgb(65, 65, 65),border='black',borderWidth=1)
        # drawCircle(
        #     x,
        #     y,
        #     45 / 2 * scale,
        #     fill=rgb(215, 38, 0),
        #     # border="white",
        #     borderWidth=1 * scale,
        # )
        ############## use 2020 version - davidson
        drawOval(x,y,285,190,fill='black',border=_red,borderWidth=6,rotateAngle=-20)
        

        # for i in range(7,-2,-1):
        #     drawLabel(
        #         "ONU",
        #         x - .2 * i * scale,
        #         y + .2 * i * scale,
        #         size=22.5 * 1.1 * scale,
        #         fill="gold",
        #         border='white',
        #         borderWidth=2 * scale,# 3
        #         # bold=True,
        #         rotateAngle=-20,
        #         font='Cabin',
        #     )
        # for i in range(14,-2,-1):
        #     border='black' if i == 10 else 'black' #gradient2('black', 'black', 'dimgrey', 'black', 'black', 'black', 'black', 'black', start='top')
        #     bw=1 if i <-5 else 2
        #     # print(border)
        #     drawLabel(
        #         "ONU",
        #         x - .1 * i * scale,
        #         y + .1 * i * scale,
        #         size=22.5 * 1.1 * scale,
        #         fill='black',
        #         border="black",
        #         borderWidth=bw * scale,
        #         # bold=True,
        #         rotateAngle=-20,
        #         font='Cabin',
        #     )
        # drawLabel(
        #     "ONU",
        #     x,
        #     y,
        #     size=22.5 * 1.1 * scale,
        #     fill='black',
        #     border="white",
        #     borderWidth=4.5 * scale,
        #     # bold=True,
        #     rotateAngle=-20,
        #     font='Cabin',
        # )

        drawLabel(
            "ONU",
            x,
            y,
            size=22.5 * 1.1 * scale,
            fill='black',
            border="black",
            borderWidth=4 * scale,
            # bold=True,
            rotateAngle=-20,
            font='Cabin',
        )

        drawLabel(
            "ONU",
            x,
            y,
            size=22.5 * 1.1 * scale,
            fill=_yellow,
            border="white",
            borderWidth=0.5 * scale,
            # bold=True,
            rotateAngle=-20,
            font='Cabin',
        )
        # drawLabel(
        #     "ONU",
        #     x,
        #     y,
        #     size=20 * 1.1 * scale,
        #     fill="gold",
        #     border="white",
        #     borderWidth=0.5 * scale,
        #     # bold=True,
        #     rotateAngle=-20,
        #     font='Cabin',
        # )

    # def scroll(self, ev):
    #     print(self.ymod)
    #     # while self.ymod< 500 :
    #     if self.ymod< 50:
    #         # print(dir(ev))
    #         # print(ev.layerY)
    #         self.ymod+=1
    #         self.drawMainMenu()
    #         rescroll()

    def drawMainMenu(self):
        browser.document.body.style.backgroundColor = "black"
        browser.window.history.pushState({},'',browser.window.location.origin+"/games/")
        
        # color defs
        _red = rgb(0xD7, 0x26, 0x00)
        _yellow = rgb(0xEC, 0xD4, 0x07)
        _green = rgb(0x37, 0x97, 0x11)
        _blue = rgb(0x09, 0x56, 0xBF)

        drawRect(0, 0, 400, 400, fill="black")  # og dimgray
        # drawRect(0, 0, 4000, 4000, fill="white") # 4 scale testing

        drawRect(
            50,
            5,
            300,
            35,
            fill=gradient2("darkgray", "gray", "dimgray", start="top"),
            border=gradient2("darkgray", "gray", "dimgray", start="bottom"),
        )

        drawLabel(
            "make a new game", 200, 20, size=30, fill="white"
        )  # gradient2(_blue,_green,_yellow,_red, start="left")
        drawLabel("OR", 200, 50, size=10, fill="white")
        drawLabel("browse games...", 200, 70, size=30, fill="white")
        # drawLabel("browse", 200, 150, size=80, fill=_green)
        # drawLabel("re-join", 200, 250, size=80, fill=_blue)
        # drawLabel("spectate", 200, 350, size=80, fill=_yellow)
        # for y in range(0,350+1,100):
        #     drawLine(0,y,400,y,fill='white')
        y = 100
        drawLabel("game name", 100, y, fill=_red, bold=True)
        drawLabel("open spots", 200, y, fill=_green, bold=True)
        drawLabel("password", 300, y, fill=_blue, bold=True)

        page_min, page_max = self.page * 11, self.page * 11 + 11
        # name_list=names()

        for i in range(len(self.names["names"])):
            if page_min <= i < page_max:
                drawLabel(
                    self.names["names"][i], 100, y := y + 25, fill="white", size=20
                )
                drawLabel(
                    4 - self.names["player_count"][i], 200, y, fill="white", size=20
                )
                label = "🔒" if self.names["game_pswd"][i] else "-"  # or ✕
                drawLabel(label, 300, y, fill="white", size=20)
            # y+=20

        if page_min != 0:
            drawRect(0, 100, 25, 300, fill="black", border="white")
            drawRegularPolygon(15, 250, 12.5, 3, fill=_yellow, rotateAngle=180)

        if page_max <= len(self.names["names"]):
            drawRect(375, 100, 25, 300, fill="black", border="white")
            drawRegularPolygon(385, 250, 12.5, 3, fill=_yellow)

    def drawSubMenu(self):
        browser.document.body.style.backgroundColor = "black"
        browser.window.history.pushState({},'',browser.window.location.origin+f"/games/?id={self.names['index'][self.page*11+self.i]}")

        drawRect(0, 0, 400, 400)
        _red = rgb(0xD7, 0x26, 0x00)
        _yellow = rgb(0xEC, 0xD4, 0x07)
        _green = rgb(0x37, 0x97, 0x11)
        _blue = rgb(0x09, 0x56, 0xBF)

        # drawRect(0,0,100,100,fill=_red)
        drawRegularPolygon(50, 50, 30, 3, fill=_red, rotateAngle=180)
        
        drawLabel("game name:", 200, 33.3, size=30, fill=_red)
        drawLabel(
            f"{self.names['names'][self.page*11+self.i]}", 200, 66.6, size=30, fill=_red
        )

        drawLabel("join", 200, 150, size=80, fill=_green)
        drawLabel("re-join", 200, 250, size=80, fill=_blue)
        drawLabel("spectate", 200, 350, size=80, fill=_yellow)
        result=public(self.names['index'][self.page*11+self.i])
        y=0
        drawLabel(  "players:",350,y:=y+20,fill='white'   )
        for i in range(4):
            drawLabel(  result[f'name{i}'] if result[f'name{i}'] !="None" else "",350,y:=y+20,fill='white'   )
    

    def drawPause(self):
        browser.document.body.style.backgroundColor = "rgb(202, 154, 178)"

        drawRect(0, 0, 400, 400, fill=rgb(202, 154, 178))  # origionaly "hotpink"
        y = 0
        drawLabel("Pause Screen\u2122", 200, y := y + 40, size=50)

        drawLabel("Click `new game` to create a new game.", 200, y := y + 50, size=20)

        drawLabel("Click on a game to start to connect,", 200, y := y + 40, size=20)
        drawLabel(
            "then use `join`, `re-connect`, or `spectate`", 200, y := y + 20, size=20
        )

        drawLabel("Clicking cancel on any question", 200, y := y + 40, size=20)
        drawLabel("cancels the curent action", 200, y := y + 20, size=20)

        # drawLabel("Click `re-join` to join game you were", 200, y:=y+40, size=20)
        # drawLabel("previously in.", 200, y:=y+20, size=20)

        # drawLabel("Click `spectate` to watch a game", 200, y:=y+40, size=20)

        drawLabel(
            "Press `r` while on the pause screen (this", 200, y := y + 40, size=20
        )
        drawLabel(
            "screen) to be prompted with the option to", 200, y := y + 20, size=20
        )
        drawLabel("restart the app.", 200, y := y + 20, size=20)

        drawLabel("The game rules can be found at this URL:", 200, y := y + 40, size=20)
        drawLabel(
            "https://trevinspi.freeddns.org/games/rules", 200, y := y + 20, size=20
        )
        drawLabel("(press o to open the rules in a new tab)", 200, y := y + 20, size=20)

    def keyDown(self, key):
        if key == "p":
            self.paused = not self.paused
            rescroll()
            if self.paused:
                self.drawPause()
            else:
                if self.game is None:
                    if self.i == None:
                        self.drawMainMenu()
                    else:
                        self.drawSubMenu()
                else:
                    browser.document.body.style.backgroundColor = "rgb(53,101,77)"
                    self.game.render()

        elif key == 'r' and self.game!=None and self.game.user_num==0 and not self.game.spectate  and (self.game.settings or self.game.winner) and browser.confirm("Do you really want to restart the match?"):
                print("restarting")
                restart(self.game.ID,self.game.user_pswd)
                self.game.settings=False
                self.game.refresh()
        elif key == 'm':
            self.playing_audio = not self.playing_audio
            
            if self.playing_audio: playDsdfb()
            else: pauseDsdfb()
        
        elif key == "r" and self.paused:
            prompt = "Do you really want to restart your game client?"
            if browser.confirm(prompt):
                browser.window.scrollTo(0, 0)
                browser.window.history.pushState(
                    {}, "", browser.window.location.origin + "/games/"
                )
                browser.window.location.reload()
        elif key == "o" and self.paused:
            URL = "https://trevinspi.freeddns.org/games/rules"
            browser.window.open(URL, "_blank")

    def mouseDown(self, x, y):
        print((x, y))
        if self.paused:
            return
        #         globalYOffset=canvas.getBoundingClientRect().top
        #         globalXOffset=canvas.getBoundingClientRect().left

        #         x = math.floor(val.x - globalXOffset)
        #         y = math.floor(val.y - globalYOffset)

        if self.game is not None:
            self.game.mouseDown(x, y)
        else:
            # process button pressing

            # if 20<x<380:# horozontal checking not needed
            # page_min,page_max=,self.page*10+10
            if self.i == None:
                if 00 < y < 100:
                    print("new game")
                    self.new_game()
                elif 100 < y:
                    if x >= 375 and self.page * 11 <= len(self.names["names"]):
                        self.page += 1
                        self.drawMainMenu()
                    elif x <= 25 and self.page * 11 + 11 != 0:
                        self.page -= 1
                        self.drawMainMenu()
                    else:
                        for i in range(11):
                            gameY = i * 25 + 125 + 10
                            if y < gameY:
                                # print(self.names)
                                # print(self.names["names"][self.page * 11 + i])
                                self.i = i
                                self.drawSubMenu()
                                break
            else:
                if y < 100 and x < 75:
                    self.i = None
                    self.drawMainMenu()
                elif 100 < y < 200:
                    print("join game")
                    self.join_empty()
                elif 200 < y < 300:
                    print("re-connect")
                    self.rejoin()
                elif 300 < y < 400:
                    print("spectate")
                    self.spectate()

    def onStep(self):
        # print(4444444444444444444)
        if self.paused:
            return
        if self.game != None:

            self.game.onStep()
        else:
            self.splash -= 1
            if self.splash == 0:
                # self.names = names()
                if self.i == None:
                    self.drawMainMenu()
                else:
                    self.drawSubMenu()
                    if self.uid != None:
                        if self.uid == 4:
                            self.spectate()
                        else:
                            self.rejoin()

    def sqlScan(self, s):
        # Q4 stuff -- sanitize it better
        if "`" in s or "%" in s or "," in s:
            return False
        return True

    def new_game(self):
        # while True:
        # get game id
        # name_list=names()['names']
        # index_list=names()['index']
        name = None
        # q="whats the new game's name?"
        # while type(name)!=str or len(name)>20:
        additive = ""
        #         for i in range(3):
        while True:
            print(additive)
            name = getTextInput(
                f"what's the new game's name? {additive}"
            )  # , can't be an int, unique # game_name
            #             print(type(name_list))
            if (
                type(name) == str
                and len(name) <= 20
                and name not in self.names["names"]
                and not name.isdigit()
                and self.sqlScan(name)
            ):
                break
            elif type(name) != str:
                return
            elif len(name) > 20:
                additive = "(max 20 chars)"
            elif name in self.names["names"]:
                additive = "(that game name is already chosen, did you mean to join?)"
            elif name.isdigit():
                additive = "(name can't be an int)"
            elif not self.sqlScan(name):
                additive = '(disalowed chars: "`", "%", ",")'

        game_pswd = getTextInput("what's the password for the room? (optional)")

        if type(game_pswd) != str:
            return
        while not self.sqlScan(game_pswd):
            game_pswd = getTextInput(
                """what's the password for the room? (optional, disalowed chars: "`", "%", ",")"""
            )
            if type(game_pswd) != str:
                return

        user_name = None
        #         for i in range(3):
        additive = ""
        while True:
            user_name = getTextInput("what's your username? " + additive)
            if (
                type(user_name) == str
                and len(user_name) <= 20
                and len(user_name) != 0
                and self.sqlScan(user_name)
            ):
                break
            elif len(user_name) > 20 or len(user_name) == 0:
                additive = "(max 20, min 1 chars)"
            #             elif user_name==""
            #             elif user_names in user_names:
            elif type(user_name) != str:
                return
            elif not self.sqlScan(user_name):
                additive = '(disalowed chars: "`", "%", ",")'

        user_pswd = getTextInput("what's your password for you account? (optional)")

        if type(user_pswd) != str:
            return
        while not self.sqlScan(user_pswd):
            user_pswd = getTextInput(
                """what's your password for your account? (optional, disalowed chars: "`", "%", ",")"""
            )
            if type(user_pswd) != str:
                return

        ID = make_uno(name, user_name, user_pswd,game_pswd)
        #         print(ID)
        #         drawLabel(ID,200,200)
        self.game = Game(ID, 0, user_pswd)

    def join_empty(self):

        ID = self.names["index"][self.page * 11 + self.i]

        result = public(ID)

        userNames = []
        for i in range(4):
            userNames.append(result["name" + str(i)])

        if "None" not in userNames:
            prompt = "no room in game"
            browser.confirm(prompt)
            return

        userName = None
        #         for i in range(3):
        additive = ""
        while True:
            userName = getTextInput("whats your screen name? " + additive)
            print(ID, type(ID))
            if (
                type(userName) == str
                and len(userName) <= 20
                and len(userName) != 0
                and self.sqlScan(userName)
            ):
                break
            elif len(userName) > 20 or len(userName) == 0:
                additive = "(max 20, min 1 chars)"

            elif userName in userNames:
                additive = f"(username already taken; taken names: {userNames})"

            elif type(userName) != str:
                return

            elif not self.sqlScan(userName):
                additive = '(disalowed chars: "`", "%", ",")'

        userPswd = getTextInput("whats your password for you account? (optional)")

        if type(userPswd) != str:
            return
        while not self.sqlScan(userPswd):
            userPswd = getTextInput(
                """what's your password for your account? (optional, disalowed chars: "`", "%", ",")"""
            )
            if type(userPswd) != str:
                return
                # userPswd=''
        if self.names["game_pswd"][self.page * 11 + self.i]:
            gamePswd = getTextInput("what's the password for the room? (optional)")

            if type(gamePswd) != str:
                return
            while not self.sqlScan(gamePswd):
                gamePswd = getTextInput(
                    """what's the password for the room? (optional, disalowed chars: "`", "%", ",")"""
                )
                if type(gamePswd) != str:
                    return
            userNum = join(ID, userName, userPswd,gamePswd)
        else:
        #         if "None" in userNames:
            userNum = join(ID, userName, userPswd)
        #         print(userNum)
        self.game = Game(ID, userNum, userPswd)

    def rejoin(self):

        #         while self.game==None:
        result = None
        # while True
        #             for i in range(3):
        # result=names()
        # name_list=result['names']
        # index_list=result['index']

        ID = self.names["index"][self.page * 11 + self.i]

        result = public(ID)
        if self.uid == None:
            pass
            user_names = []
            for i in range(4):
                user_names.append(result["name" + str(i)])
            #             user_names=result[0:4]

            user_name = None
            #         for i in range(3):
            while True:
                user_name = getTextInput("what's your username?" + str(user_names))

                if user_name in user_names:
                    user_num = user_names.index(user_name)
                    break
                elif type(user_name) != str:
                    return

        #             print2(user_num)
        else:
            user_num = self.uid

        additive = ""
        #             for i in range(3):
        while True:
            pswd = getTextInput("what's your password?" + additive)

            if type(pswd) != str:
                return

            # input validation
            while not self.sqlScan(pswd):
                pswd = getTextInput(
                    """whats your password for your account? (optional, disalowed chars: "`", "%", ",")"""
                )
                if type(pswd) != str:
                    return
                    # user_pswd=''
            try:
                private(ID, user_num, pswd)
                break
            except:
                prompt = "password wrong"
                browser.confirm(prompt)
            additive = " (try again)"

        self.game = Game(ID, user_num, user_pswd=pswd)

    def spectate(self):

        ID = self.names["index"][self.page * 11 + self.i]

        self.game = Game(ID, spectate=True)
