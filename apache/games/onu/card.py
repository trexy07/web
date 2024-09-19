# from base import rgb, drawRect, drawOval, drawLabel, gradient2
from base_mini import rgb, drawRect, drawOval, drawLabel, gradient2

class Card():
    # example Cards
    # Card("b",'+2').draw(0,200)
    # card('black'," ").draw(80,200)
    # card('black',"+4").draw(160,200)
    # card('back'," ").draw(240,200)
    # card("green","5").draw(320,200)

    _black  = rgb(0x00, 0x00, 0x00)
    _red    = rgb(0xd7, 0x26, 0x00)
    _yellow = rgb(0xec, 0xd4, 0x07)
    _green  = rgb(0x37, 0x97, 0x11)
    _blue   = rgb(0x09, 0x56, 0xbf)
    _white  = rgb(0xff, 0xff, 0xff)
    _colors = {
        "u":      _black,
        "back":   _black,
        "B":      _black,
        "black":  _black,
        "r":      _red,
        "red":    _red,
        "y":      _yellow,
        "yellow": _yellow,
        "g":      _green,
        "green":  _green,
        "b":      _blue,
        "blue":   _blue,
    }
    _ovalFills = {
        "u":     _red,
        "back":  _red,
        "B":     _white,
        "black": _white,
    }
    _ovalBorders = {
        "u":     _red,
        "back":  _red,
    }
    _values = {
        
    }


    def __init__(self, color, symbol='-', scale=.5, angle=0):
        #print(color,value)
        self.color = self._colors[color]

        if color == "back" or symbol==' ':
            self.value = "ONU"
        elif symbol == "-":
            self.value = " "
        else:
            self.value = symbol

        self.ovalFill = self._ovalFills.get(color, self.color)
        self.ovalBorder = self._ovalBorders.get(color, self._white)
        
        self.size=1
        self.scale=scale
        
        if self.value[0] in '+🛇':
            self.size=.8
        if color=='black':
            self.size=1
        
        self.size*=scale
        
        # simpler cards for unit 3
        self.unit3=False
        
        
    def draw(self,x,y):
        if self.unit3:
            
            drawRect(x,y,64*self.scale,89*self.scale,fill= self.color,border="white",borderWidth=6*self.scale)
            
            if self.value!='ONU':
                self.size*=2
            
            drawLabel(self.value,x+32*self.scale,y+44.5*self.scale,size=22.5* self.size,
                fill=gradient2("gold","gold",'lightgoldenrodyellow',"white",start="top"),
                border="black",borderWidth=.5*self.scale,
                bold=True,rotateAngle=-20, font='comic sans Ms')
            
            
            
            return
        ## with base groups, throw all these shape in a group, then apply rotate

        drawRect(x,y,64*self.scale,89*self.scale,fill= self.color,border="white",borderWidth=6*self.scale)

        drawOval(x+32*self.scale,y+44.5*self.scale,45*self.scale,75*self.scale,rotateAngle=30, fill=self.ovalFill, border=self.ovalBorder, borderWidth=4 * self.scale)
        if self.value=='ONU':
            # Label(number,232-4,344.5+1.5,size=20*size,fill='black',bold=True,rotateAngle=-45)

            drawLabel(self.value,x+30*self.scale,y+46*self.scale,size=22.5* self.size,
                fill=gradient2('midnightBlue', 'lightCyan', 'midnightBlue', 'midnightBlue', start="top"),
                border=None,borderWidth=.5*self.scale,
                bold=True,rotateAngle=-20)

            drawLabel(self.value,x+32*self.scale,y+44.5*self.scale,size=22.5* self.size,
                fill=gradient2("gold","gold",'lightgoldenrodyellow',"white",start="top"),
                border="black",borderWidth=.5*self.scale,
                bold=True,rotateAngle=-20)

            #©, 
            #u+00AE above onu on back, black, 3*size
            # drawLabel("© BirdFace",x+47.5*self.scale,y+80*self.scale,size=3* self.size,fill='white',bold=True) # og size 3*



        # if self.color=='black' and self.value !="ONU":
        if self.value==' ':

            # wild card cards
            drawRect(x+12*self.scale,   y+47*self.scale,    15*self.scale,20*self.scale, fill=self._green, border='black',    borderWidth=1*self.scale)
            drawRect(x+37*self.scale,   y+22*self.scale,    15*self.scale,20*self.scale, fill=self._yellow, border='black',   borderWidth=1*self.scale)
            drawRect(x+19.5*self.scale, y+29.5*self.scale,  15*self.scale,20*self.scale, fill=self._blue, border='black',     borderWidth=1*self.scale)
            drawRect(x+29.5*self.scale, y+39.5*self.scale,  15*self.scale,20*self.scale, fill=self._red, border='black',      borderWidth=1*self.scale)


        if not (self.color=='black' or self.value=='ONU'):

            drawLabel(self.value,x+28*self.scale,y+46*self.scale,size=50* self.size,fill='black',bold=True)
            drawLabel(self.value,x+32*self.scale,y+44.5*self.scale,size=50* self.size, fill='white', border='black', borderWidth=2*self.scale, bold=True)
            
        # elif value[0]=='+':

        if not (self.value=='wild' or self.value=='ONU'):
            drawLabel(self.value, x+15.5*self.scale, y+15.375*self.scale,size=15* self.size,fill='black',bold=True,)
            drawLabel(self.value, x+17*self.scale, y+15*self.scale,size=15* self.size, fill='white', border='black', borderWidth=.5*self.scale, bold=True)

            drawLabel(self.value, x+49.5*self.scale, y+72.125*self.scale, size=15* self.size, fill='black', bold=True, rotateAngle=180)
            drawLabel(self.value, x+47.5*self.scale, y+72.5*self.scale, size=15* self.size, fill='white', border='black', borderWidth=.5*self.scale, bold=True, rotateAngle=180)


        drawRect(x,y,64*self.scale,89*self.scale,fill="transparent",border="white",borderWidth=6*self.scale)
