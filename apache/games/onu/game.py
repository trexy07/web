# from random import choice
from browser import document, window
# from base import public, private, draw, place, onu, fountain, distance, rgb, gradient2, drawRect, drawLabel, drawCircle
from base import public, private, draw, place, onu, fountain, distance, rgb, gradient2, drawRect, drawLabel, drawCircle, drawStar
from card import Card

# import time

class Game:
    def __init__(self, ID, user_num=0, user_pswd="",spectate=False):

        print(ID, user_num, user_pswd,spectate)

        self.ID = ID
        self.user_num = user_num
        self.user_pswd = user_pswd
        self.spectate=spectate

        if spectate:
            user_num=4
        window.history.pushState({},'',window.location.origin + f'/games/?id={ID}&uid={user_num}')


        self.hand = []
        self.user_names = []
        self.user_card_count = []
        self.card = None

        self.top_card = "u "
        self.direction = 1

        self.rate = 0
        self.time = 0
        self.winner = 0
        self.onu = 0

        self.settings=False
        # self.audio=84
        
        
        document.body.style.backgroundColor = "rgb(53,101,77)"
        # set page background background to "gambling table green"
        
        self.refresh()

        print("game inited")

        # 19 Red cards – 0 to 9. (1 zero)
        # 19 Blue cards – 0 to 9.
        # 19 Green cards – 0 to 9.
        # 19 Yellow cards – 0 to 9.
        # 8 Skip cards – two cards of each color.
        # 8 Reverse cards – two cards of each color.
        # 8 Draw cards – two cards of each color.
        # 8 Black cards – 4 wild cards and 4 Wild Draw 4 cards.

    #         self.posible_cards=[]
    # #         values=[str(i) for range(9+1)]+[str(i) for i in range(1,9+1)]+['s','r','+2']*2
    #         for color in 'rgby':
    #             for i in [i for i in range(9+1)]+[i for i in range(1,9+1)]:
    #                 self.posible_cards.append(color+str(i))
    #             for special in ['s','r','+2','s','r','+2']:
    #                 self.posible_cards.append(color+special)
    #         for i in range(4):
    #             self.posible_cards.append("B ")
    #             self.posible_cards.append("B+4")
    # #         drawLabel(self.posible_cards,200,250)
    #         new_str=''
    #         for item in self.posible_cards:
    #             new_str+=item+','

    #         print(new_str)
    #         print(self.posible_cards)

    def mouseDown(self, mx, my):
        if self.card == None:
            self.refresh()
            
        self.time = 0
        self.settings=False 
        
        if self.spectate:
            if distance(375, 25, mx, my) <= 50:
                print('set')
                self.settings=True
                self.render() # double renders cuz line 6 up also calls render indirectley
            return
        
        
        #         rdm_card=choice(self.posible_cards)
        #         # when drawing card replace s with u+21bb↻ or u+21ba↺
        #         value=rdm_card[1:]
        #         for card in self.hand:
        #         self.render()
        if self.winner != 0 or self.player_count == 1:
            return
        position = (50, 375, 1, 0, 0)# regular
        position = (350, 375, -1, 0, 0)

        x, y = position[0], position[1]  # starting pos
        mod = 300 / (len(self.hand))  # how much the card position changes

        x += position[2] * mod / 2  # move the card in half a step to center
        y += position[3] * mod / 2

        if self.card is not None:
            # if a color was selected then place the wild card with the new color added
            x = 200
            y = 200
            c = ""

            if x - 16 < mx < x + 16 and y - 44.5 - 44.5 < my < y - 44.5:
                c = "b"
            elif x - 16 < mx < x + 16 and y + 44.5 + 44.5 > my > y + 44.5:
                c = "y"
            elif x + 32 < mx < x + 64 and y - 22.25 < my < y + 22.25:
                c = "g"
            elif x - 32 > mx > x - 64 and y - 22.25 < my < y + 22.25:
                c = "r"
            else:
                print("no color", mx, my)
            #             print(c)
            if c != "":
                place(self.ID, self.user_num, self.card, self.user_pswd, color=c)
            self.refresh()
            self.card = None
        elif 268 < mx < 268 + 32 and 177.75 < my < 177.75 + 44.5:
            #             if self.turn!=self.user_num:
            #             for card in self.hand:
            #                 if (card[0]=='B' # if the card is wild
            #                  or card[0]==self.top_card[0] # if the color matches
            #                  or card[1:]==self.top_card[1:] # if the value matches
            #                  or (self.top_card[0]=='B' and card[0]==self.top_card[-1]) # if the top card is wild && the color matches
            #                 ):
            #                     print('bro you still have cards to play' )
            #                     return
            #                     raise HTTPException(status_code=428, detail="bruh, you have cards you can play")
            print("drawing")
            print(draw(self.ID, self.user_num, self.user_pswd))
            self.refresh()
            #             print('end drawing')
            pass
        elif distance(375, 25, mx, my) <= 50:
            print('set')
            self.settings=True
            self.render()
        elif distance(300, 300, mx, my) <= 30:  # onu button
            press = False

            onu_bin = bin(self.onu + 16)[2:]
            #         print(onu_bin)
            for user in range(4):

                # onu=sonu//(user+1)==1
                count = self.user_card_count[user]
                #             print(user+1,count,onu_bin[user])
                #             print(onu_bin[user] , count)
                if onu_bin[-user - 1] == "0" and count == 1:
                    press = True

            if press or (
                (
                    self.turn == self.user_num
                    and len(self.hand) == 2  # 2 cards your turn
                    or len(self.hand) == 1
                )  # 1 card, any turn
                and onu_bin[-self.user_num] == "0"
            ):  # press is needed

                print("ONU button")
                onu(self.ID, self.user_num)
                self.refresh()
        else:
            print(" attempt place")
            for j in range(len(self.hand)):
                j= -j -1

                #             Card(card[0],value,angle=position[i][4]).draw(x-16,y-22.25)#-32/2,-44.5 /2
                #                 drawCircle(x,y,5) # helpfull for debuging positions
                #             cx,cy=x-16,y-22.25
                #             print(x,y)
                if x - 16 < mx < x + 16 and y - 22.25 < my < y + 22.25:
                    #                 print(self.hand[j])
                    print("placing")
                    card = self.hand[j]
                    if (
                        self.user_num == self.turn  # if it's your turn
                        and not (  # nand, only + cards can be played while an active stack
                            self.draw  # draw stack >0
                            and ("+" not in card
                                 or not card[2]>=self.top_card[2])   # playing a draw card
                            )
                        and (  # and the card can be played
                            card[0] == "B"  # if the card is wild
                            # if the color matches
                            or card[0] == self.top_card[0]
                            # if the value matches
                            or card[1:] == self.top_card[1:]
                            # if the top card is wild && the color matches
                            or (
                                self.top_card[0] == "B" and card[0] == self.top_card[-1]
                            )
                        )
                    ):
                        if card[0] == "B":

                            # selecting a color if its a wild
                            self.card = card
                            unoRed = rgb(215, 38, 0)
                            unoYellow = rgb(236, 212, 7)
                            unoGreen = rgb(55, 151, 17)
                            unoBlue = rgb(9, 86, 191)
                            print("wild color select")

                            # x=y=200
                            x = 200 - 16
                            y = 200 - 22.5
                            drawRect(
                                x,
                                y - 66.75,
                                32,
                                44.5,
                                fill=unoBlue,
                                border="black",
                                borderWidth=1,
                            )
                            drawRect(
                                x,
                                y + 66.75,
                                32,
                                44.5,
                                fill=unoYellow,
                                border="black",
                                borderWidth=1,
                            )
                            drawRect(
                                x - 48,
                                y,
                                32,
                                44.5,
                                fill=unoRed,
                                border="black",
                                borderWidth=1,
                            )
                            drawRect(
                                x + 48,
                                y,
                                32,
                                44.5,
                                fill=unoGreen,
                                border="black",
                                borderWidth=1,
                            )
                            # x=200-19.5-5-16
                            # y=200-29.5-5-22.5
                            # 
                            # drawRect(x+12, y+47, 32, 44.5, fill=unoGreen,
                            #          border='black', borderWidth=1 )
                            # drawRect(x+37, y+22, 32, 44.5, fill=unoYellow,
                            #          border='black', borderWidth=1 )
                            # drawRect(x+19.5, y+29.5, 32,44.5, fill=unoBlue,
                            #          border='black', borderWidth=1 )
                            # drawRect(x+29.5, y+39.5, 32,44.5, fill=unoRed,
                            #          border='black', borderWidth=1 )
                        else:
                            print("before place")
                            place(self.ID, self.user_num, card, self.user_pswd)
                            print("place")
                            self.refresh()
                            print("place refreshed")
                    else:
                        print(
                            "id10t error - bruh, you cant play that card",
                            self.top_card,
                            card,
                        )
                    #                         self.refresh()
                    # self.refresh()
                    return None

                x += position[2] * mod
                y += position[3] * mod
            self.render()

    def drawSettings(self):
        drawRect(50,50,300,300,fill=rgb(202, 154, 178))
        y=40
        drawLabel(f"GID: {self.ID}",200,y:=y+20)
        drawLabel(f"name: {self.game_name}",200,y:=y+20)
        if self.user_num==0:
            drawLabel("Press r to restart the match",200,y:=y+20)
        else:
            drawLabel("The game creator can reset the match",200,y:=y+20)

        drawLabel("Press 'm' to play or pause the music",200,y:=y+20)
    
    def render(self):

        
        
        # this part should be replaced with shape clear, then add rect
        drawRect(0, 0, 400, 400, fill=rgb(53,101,77)) # origianly dimgray

        drawStar(375,25,8,28,12,fill='grey')
        drawCircle(375,25,24 ,fill="transparent",border=rgb(53,101,77),borderWidth=10)
        
        drawLabel(f"game id: {self.ID}", 100, 300)
        drawLabel(f"game name: {self.game_name}", 100, 320)

        #         drawLine(200,0,200,400) # used to center hands
        #         drawLine(0,200,400,200)

        # render hands
        hands = []
        for user_num in range(4):
            #             if user_num!=self.user_num-1:
            #                 hands.append(["ba " for i in range(self.user_card_count[user_num%4])] )
            #             hands.append(self.user_card_count[user_num])
            hands.append(["u " for i in range(self.user_card_count[user_num])])
        hands[self.user_num ] = self.hand

        # rotate cards
        for i in range(self.user_num + 2):
            hands.append(hands.pop(0))

        # render cards

        position = (
            (50, 25, 1, 0, 180),
            (375, 50, 0, 1, 270),
            (50, 375, 1, 0, 0),
            (25, 50, 0, 1, 90),
        )

        for i in range(4):
            if len(hands[i]) == 0:
                continue

            x, y = position[i][0], position[i][1]  # starting pos
            mod = 300 / (len(hands[i]))  # how much the card position changes

            # move the card in half a step to center
            x += position[i][2] * mod / 2
            y += position[i][3] * mod / 2

            for j in range(len(hands[i])):
                card = hands[i][j]
                if card == "":
                    continue
                value = card[1:]
                if value == "r":
                    if self.direction == 0:
                        value = "↻"
                    else:
                        value = "↺"
                elif value == "s":
                   value = "🛇" if window.screen.availWidth>window.screen.availHeight else "🚫" 

                valid = (
                    15
                    if not self.spectate and ( # dont highlight is spectating 
                        self.user_num == self.turn  # if it's your turn
                        and not (  # nand, only + cards can be played while an active stack
                            self.draw  # draw stack >0
                            and ("+" not in card # plus card is played
                                or not card[2]>=self.top_card[2]) # plus card >= than top card
                        )
                        and (  # and the card can be played
                            card[0] == "B"  # if the card is wild
                            # if the color matches
                            or card[0] == self.top_card[0]
                            # if the value matches
                            or card[1:] == self.top_card[1:]
                            # if the top card is wild && the color matches
                            or (
                                self.top_card[0] == "B" and card[0] == self.top_card[-1]
                            )
                        )
                    )
                    else 0
                )
                
                Card(card[0], value, angle=position[i][4]).draw(
                    x - 16, y - 22.25 - valid
                )  # -32/2,-44.5 /2 # opacity= opac
                
                if valid == 0 and i==2 and not self.spectate:
                    drawRect(x - 16, y - 22.25, 32, 58, fill='grey', opacity=50) 
                    # for graying out unplayable cards
                    # fix height
                    
                # drawCircle(x,y,10) # helpfull for debuging positions
                x += position[i][2] * mod
                y += position[i][3] * mod

            # drawLine(x,y,position[i][0],position[i][1]) # helped align card lines

        # direction label
        if self.direction == 1:
            value = "↻"
        else:
            value = "↺"
        drawLabel(value, 200, 200, size=100)  # =100

        # render top card and "draw pile"
        #         print(self.top_card)
        value = self.top_card[1:]
        if value == "r":
            if self.direction == 1:
                value = "↻"
            else:
                value = "↺"
        elif value == "s":
            value = "🛇" if window.screen.availWidth>window.screen.availHeight else "🚫" 


        if self.draw:
            drawLabel(f"+{self.draw}", 200, 250)
        
        
        Card(self.top_card[0], value).draw(200 - 16, 200 - 44.5 / 2)  # -32/2,-44.5 /2
        Card("back", "ONU").draw(200 - 16 + 64 + 20, 200 - 44.5 / 2)  # -32/2,-44.5 /2

        # render user_names
        # position = ((200, 60, 0), (340, 200, 270), (200, 340, 0), (60, 200, 90))
        position = ((200, 60, 0), (340, 200, 270), (200, 340 - 15, 0), (60, 200, 90)) 
        # moved self's username up to compensate for cards moving

        #         print(self.user_names)
        # rotate to account for player at bottom
        #         print(self.user_names)
        target = self.turn 
        winner = self.winner
        user_names = [self.user_names[i] for i in range(4)]
        #         print('here',user_names)

        for i in range(self.user_num +2):
            user_names.append(user_names.pop(0))
            target -= 1
            winner -= 1

        #         print(self.user_names)
        name = None
        for i in range(4):
            if self.winner != 0 and i == (winner - 0) % 4:
                fill = rgb(9, 86, 191)
                name = user_names[i]  # set the thingy
            else:
                fill = "black"
            bold = i == (target - 0) % 4 
            size = 22 if bold else 16
            fill = (rgb(215, 38, 0), rgb(236, 212, 7), rgb(55, 151, 17), rgb(9, 86, 191))[(self.time + self.time // 3 ) % 4] if bold else 'black'
            drawLabel(
                user_names[i],
                *position[i][0:2],
                rotateAngle=position[i][2],
                bold=bold,
                size=size,
                fill=fill,
            )
        if name is not None:
            drawRect(0, 160, 400, 80, fill="white")
            drawLabel(f"{name} won!", 200, 200, size=20)
            drawLabel("press r as player 1 to restart the match", 200, 220, size=10)

        # ONU button
        # when onu can't be called, then decrese the opacity/ cover with trasparent gray circle

        x, y = 300, 300
        font = "comic sans Ms" if "unit4" == "unit3" else "arial"

        #         drawCircle(x-4,y+3,45/2,fill=rgb(65, 65, 65),border='black',borderWidth=1)
        drawCircle(x, y, 45 / 2, fill=rgb(215, 38, 0), border="black", borderWidth=1)

        drawLabel(
            "ONU",
            x - 2,
            y + 1.5,
            size=22.5 * 1.1,
            fill=gradient2(
                "midnightBlue", "lightCyan", "midnightBlue", "midnightBlue", start="top"
            ),
            border=None,
            borderWidth=0.5,
            bold=True,
            rotateAngle=-20,
            font=font,
        )

        drawLabel(
            "ONU",
            x,
            y,
            size=22.5 * 1.1,
            fill=gradient2(
                "gold", "gold", "lightgoldenrodyellow", "white", start="top"
            ),
            border="midnightBlue",
            borderWidth=0.5,
            bold=True,
            rotateAngle=-20,
            font=font,
        )

        press = False

        onu_bin = bin(self.onu + 16)[2:]
        #         print(onu_bin)
        for user in range(4):

            # onu=sonu//(user+1)==1
            count = self.user_card_count[user]
            #             print(user+1,count,onu_bin[user])
            #             print(onu_bin[user] , count)
            if onu_bin[-user - 1] == "0" and count == 1:
                press = True
        #         print(press,self.turn==self.user_num , len(self.hand)==2 , onu_bin[-self.user_num]) # debug
        if press or (
            (
                self.turn == self.user_num
                and len(self.hand) == 2  # 2 cards your turn
                or len(self.hand) == 1
            )  # 1 card, any turn
            and onu_bin[-self.user_num] == "0"
        ):  # press is needed
            pass
        else:
            drawCircle(x, y, 30, fill = rgb(53,101,77), opacity=50) # origianly dimgray

        if self.player_count == 1:
            drawRect(0, 160, 400, 80, fill="white")
            drawLabel("> 1 player needed for game", 200, 200, size=20)
            drawLabel("(get some friends)", 200, 235, size=10)

            drawRect(180, 45, 40, 25, fill = rgb(53,101,77)) # origianly dimgray

        if self.settings:
            self.drawSettings()
    
    def refresh(self):
        # start=time.time()
        # await aio.sleep(3)
        # for i in range(9999):
        #     for i in range(999):
        #         pass
        result = public(self.ID)

        #         drawLabel(str(result),200,300)

        if result["age"] > 0 and result["winner"] == 0:
            fountain(self.ID)

        #         self.hand=result["cards"+str(self.user_num)].split(",")

        self.direction = 2 * result["direction"] - 1

        #         self.user_names=result[0:4]
        self.user_names = []
        for i in range(4):
            self.user_names.append(result["name" + str(i)])

        #         self.user_names=[]
        self.user_card_count = []
        for i in range(4):
            self.user_card_count.append(result["len" + str(i)])

        self.top_card = result["top_card"]
        self.turn = result["turn"]
        self.game_name = result["game_name"]
        self.winner = result["winner"]
        self.onu = result["onu"]
        self.player_count = result["player_count"]
        self.draw = result["draw"]

        if not self.spectate:
            self.hand = private(self.ID, self.user_num, self.user_pswd)["cards"]
            #         print(self.hand)
            self.hand = sorted(self.hand.split(","))
            # self.hand.remove("") #list fix
        else:
            self.hand=["u " for i in range(self.user_card_count[0])]

        #         for i in range(4):
        # #             self.user_names.append(result["name"+str((self.user_num+i)%4)])
        #             self.user_card_count.append(len( result["cards"+str((self.user_num+i)%4)]  ))
        # print(time.time()-start)
        self.render()

    def onStep(self):
        
        if self.winner != 0:
            return
        self.time += 1

        # if self.playing_audio:
        #     self.audio-=1 
        #     if self.audio ==0:
        #         playDsdfb()
        #         self.audio=84 # 83+1 for buffer
              

        # log method
        #         if self.time>1.3**self.rate:
        #             self.rate+=1
        # #             print(self.time)

        #             self.time=0
        #             if self.card==None:
        #                 self.refresh()

        # boring linear method

        # manual exponential method
        if (
            (self.time < 10 and self.time % 2 == 1)
            or (10 < self.time < 61 and self.time % 5 == 1)
            or (self.time > 61 and self.time % 10 == 1)
        ):
            if self.card == None:
                self.refresh()

        #         self.render()

        pass
