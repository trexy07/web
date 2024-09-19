from browser import document, html, window
# import sys
import math
# from random import choice
import json

## minify 21.1 > 6.0 kb

_scaleFactor=2 # change render size of shapes



# from newbase import docio
# docio.enable()


# Initialize the canvas
canvas = document["myCanvas"]

_minSize= min(window.innerWidth,window.innerHeight)
# canvas.width=canvas.height = _minSize

_scaleFactor=_minSize/400

# print(window.innerWidth,document.documentElement.clientWidth,window.innerHeight,document.documentElement.clientHeight)

ctx = canvas.getContext("2d")

# canvas.width=canvas.height = _minSize
# ctx.canvas.width=ctx.canvas.height = _minSize

# TODO: make __all__
#__all__ = (
#    "drawLabel",
#    "drawRect",
#    "drawArc",
#    "drawOval",
#    "drawCircle",
#    "drawPolygon",
#    "drawRegularPolygon",
#    "drawStar",
#)




global_shapes={}
global_id=-1

def getTextInput(text="Enter some text (now with punctuation)."):
#     val=window.prompt(text,"")
#     drawLabel(str(val)+" , "+str(type(val)),100,100)
    return window.prompt(text,"")


def distance(x1,y1,x2,y2):
    a=x1-x2
    b=y1-y2
    return (a**2+b**2)**0.5
    pass

def print2(string):
    document <= html.P(str(string))



def rescroll ():
    window.scrollTo(0,0)
    
    _yOffset = canvas.getBoundingClientRect().top
    
    window.scrollTo(0,_yOffset)


def mouseHandleOffset (fn):
    window.scrollTo(0,0)
    
    globalXOffset = canvas.getBoundingClientRect().left
    globalYOffset = canvas.getBoundingClientRect().top
    # print("offsets",globalXOffset,globalYOffset,canvas.left,canvas.top)

    rect=canvas.getBoundingClientRect()
    # print("dimentions",canvas.width,rect.width,canvas.height,rect.height)
    scale=canvas.width/rect.width
    
    def wrapper (ev):
        # print(  'x', ev.x, globalXOffset,'y',ev.y ,globalYOffset)
        x = math.floor((ev.x - globalXOffset) * scale / _scaleFactor)
        y = math.floor((ev.y - globalYOffset) * scale / _scaleFactor)
        return fn(x, y)
        
    window.scrollTo(0,globalYOffset)
    
    return wrapper

def bind (tp, fn,bound=False):
    if "mouse" in tp:
        fn = mouseHandleOffset(fn)
    if bind:
        canvas.unbind(tp,bound)
        # canvas.removeEventListener(tp,bound)
    canvas.bind(tp, fn)
    return fn


########## web geting
import browser.ajax as ajax


# base_api_url = "https://trevinspi.freeddns.org:8096"
base_api_url = f"https://{window.location.hostname}:8096"

def fetch_data(url,method='GET'):
#     try:
        response = ajax.ajax()
#         print(dir(response))
#         response.set_header("Access-Control-Allow-Origin: https://example.com")
        response.open(method, url, False)# method, url, async - async was False
        # while on local wifi:
        # if false: f"JavascriptError: NetworkError: Failed to execute 'send' on 'XMLHttpRequest': Failed to load {url}" meaning timed out cuz router gets confused about loopback urls
        # if true: "Exception: Error: 0 - " maning ssl error go brr
            
        response.send()
        
        if 200<= response.status <300 :

            return(response.text)
        else:
            # print(f"Error: {response.status} - {response.text}", file=sys.stderr)
            #error_div = html.DIV(f"Error: {response.status} - {response.text}", style={"color": "red"})
            #document <= error_div
            raise Exception(f"Error: {response.status} - {response.text}")
            return "null"
#     except Exception as e:
#         display_error(f"An error occurred: {e}")


def make_uno(game_name,uname,upswd='',gpswd=''):
    print(f'{base_api_url}/new_game/{game_name},{uname}?upswd={upswd}&gpswd={gpswd}')
    
    
    ID=json.loads(fetch_data(f'{base_api_url}/new_game/{game_name},{uname}?upswd={upswd}&gpswd={gpswd}' , 'POST'))['ID']
    print("IDJLKDSFJLSDKJF", ID)

    return ID



def public(ID):
#     data=json.loads("null")
    data=json.loads(fetch_data(f'{base_api_url}/public/{ID}' , 'GET'))
    return data



def private(ID,uid,pswd=''):
    data=json.loads(fetch_data(f'{base_api_url}/private/{ID},{uid}?upswd={pswd}' , 'GET'))
    return data


def join(ID,user_name,upswd='',gpswd=''):
    # try:
        uid=json.loads(fetch_data(f'{base_api_url}/join/{ID},{user_name}?upswd={upswd}&gpswd={gpswd}' , 'PUT'))
        print(uid)
        return uid
    # except:
    #     print('join had an error')
    #     return None
    
    
    
def fountain(ID):
    fetch_data(f'{base_api_url}/fountain/{ID}' , 'PUT')
        
def draw(ID,uid,pswd=''):
    card=json.loads(fetch_data(f'{base_api_url}/draw/{ID},{uid}?pswd={pswd}','PUT'))
    return card
               
def place(ID,uid,card,pswd='',color=''):
    if pswd=='':
        fetch_data(f'{base_api_url}/place_card/{ID},{uid},{card}?color={color}','PUT')
    else:
        fetch_data(f'{base_api_url}/place_card/{ID},{uid},{card}?pswd={pswd}&color={color}','PUT')
        
def names():
#     data=json.loads("null")
##### make new endpoint for names 
    data=json.loads(fetch_data(f'{base_api_url}/names' , 'GET'))
    return data
# import browser.aio as aio
# async def names():
#     return aio.get(f'{base_api_url}/names')

def onu(ID,uid):
#     data=json.loads("null")
    data=json.loads(fetch_data(f'https://trevinspi.freeddns.org:8096/onu/{ID},{uid}' , 'PUT'))
    return data

def restart(ID,pswd=''):
    fetch_data(f'https://trevinspi.freeddns.org:8096/restart/{ID}?upswd={pswd}' , 'PUT')

########## graphics


def drawSvdbf(src="svdbf.png",x=0,y=0,w=None,h=None):
    """
        Static Visual Data Buffer File
    """
    # Create a new image element
    img = html.IMG(src=src)

    if None in (w,h):
        # draw without dimentions
        ctx.drawImage(img, x,y)
        
    else:
        # draw with dimentions
        ctx.drawImage(img, x,y,w,h)
    print("done")


def makeDsdfb(src="media/t_back.mp3"):
    audio = html.AUDIO(src=src, autoplay=True, id="audio", loop=True)
    document <= audio
    
def playDsdfb(tag='audio'):
    """
        play a Dynamic Spectral Data File Buffer
    """
    # audio = html.AUDIO(src=src, autoplay=True, id="myCanvas")
    # document <= audio
    audio = document[tag]
    audio.play()
def pauseDsdfb(tag='audio'):
    audio = document[tag]
    audio.pause()
    
# test
# playDsdfb()




### colors
#rgb
def rgb(r,g,b):
    return(f"rgb({r},{g},{b})")

class gradient2():
    def __init__(self,*args,start="center"):
        self.start=start
        self.args=args
        
    def draw(self,x1,y1,x2,y2):
#         print('grad2')
        if self.start in ('left-top','left','left-bottom',
                         'bottom',
                         'right-bottom','right','right-top',
                         'top'):
            # determine x1,y1,x2,y2 based on start value
            if self.start=='left-top':
                pass
            elif self.start=='left':
                x1,y1,x2,y2=x1,y1,x2,y1
            elif self.start=='left-bottom':
                x1,y1,x2,y2=x1,y2,x2,y1
            elif self.start=='bottom':
                x1,y1,x2,y2=x1,y2,x1,y1
            elif self.start=='right-bottom':
                x1,y1,x2,y2=x2,y2,x1,y1
            elif self.start=='right':
                x1,y1,x2,y2=x2,y1,x1,y1
            elif self.start=='right-top':
                x1,y1,x2,y2=x2,y1,x1,y2
            elif self.start=='top':
                x1,y1,x2,y2=x1,y1,x1,y2   
                
#             print(x1,y1,x2,y2)
#             drawLine(x1,y1,x2,y2)
            # for debugging where the gradient is
            grad=ctx.createLinearGradient(x1,y1,x2,y2)# startX,Y, endX,Y

            skip=1/(len(self.args)-1)
    #         print(skip)

            for i in range(len(self.args)):



                grad.addColorStop(i*skip,self.args[i])
                pass

    #         grad.addColorStop(0,'red')
    #         grad.addColorStop(0.5,'blue')

    #         grad.addColorStop(1,'yellow')

            return(grad)

        elif self.start =="center":
            return f"radial-gradient(circle, {', '.join(self.args)})"


# gradient 
def gradient(*args,start="center"):
    
#     print(start)
#     print(args)
    #radial-gradient(circle, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 16%, rgba(0,212,255,1) 100%);
    #linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 16%, rgba(0,212,255,1) 100%);
    
    
    if start in ('center',
                 'left-top','left','left-bottom',
                 'bottom',
                 'right-bottom','right','right-top',
                 'top'):
        
        grad=ctx.createLinearGradient(242,230,242,260)# startX,Y, endX,Y
        
        skip=1/(len(args)-1)
#         print(skip)
        
        for i in range(len(args)):
            grad.addColorStop(i*skip,args[i])
            pass
        
#         grad.addColorStop(0,'red')
#         grad.addColorStop(0.5,'blue')

#         grad.addColorStop(1,'yellow')
        
        return(grad)
        
    elif start =="center":
        return f"radial-gradient(circle, {', '.join(args)})"
    
    



### shapes



# Function to draw a rectangle (Rect)
def drawRect(x, y, width, height, fill="black", border="transparent", borderWidth=2,rotateAngle=0,opacity=100):
    
    x*=_scaleFactor
    y*=_scaleFactor
    width*=_scaleFactor
    height*=_scaleFactor
    borderWidth*=_scaleFactor
    
    
    
    
    centerX = x + width / 2
    centerY = y + height / 2
    
    # roataion
    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi / 180)
    ctx.translate(-centerX,-centerY)

    # style
    if type(fill)==gradient2:
#         print('grad2')
        fill=fill.draw(centerX-width/2,centerY-height/2,centerX+width/2,centerY+height/2)
        
    ctx.fillStyle = fill
    
    if type(border)==gradient2:
#         print('grad2')
        border=border.draw(centerX-width/2,centerY-height/2,centerX+width/2,centerY+height/2)
        
    ctx.strokeStyle = border
    ctx.lineWidth = borderWidth
    ctx.globalAlpha = opacity / 100

    
    ctx.fillRect(x, y, width, height)
#     ctx.strokeRect(x, y, width, height)

    # adjust the fill and stroke rectangles for the border
#     ctx.fillRect(x + borderWidth, y + borderWidth, width - 2*borderWidth, height - 2*borderWidth)
    ctx.strokeRect(x + borderWidth/2, y + borderWidth/2, width - borderWidth, height - borderWidth)
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    ctx.globalAlpha = 1
        
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawRect({x},{y},{width},{height},{fill},{border},{borderWidth})"})
    #return global_id - 1

# Function to draw an oval (Oval)
def drawOval(x, y, width, height, fill="black", border="transparent", borderWidth=2,rotateAngle=0,opacity=100):


    x*=_scaleFactor
    y*=_scaleFactor
    width*=_scaleFactor
    height*=_scaleFactor
    borderWidth*=_scaleFactor

    
    centerX,centerY=x,y
    
    # re center oval
    x-=width/2
    y-=height/2
    
    
    # style
    ctx.fillStyle = fill
    ctx.strokeStyle = border
    ctx.lineWidth = borderWidth
    ctx.globalAlpha = opacity / 100
    
    # roataion
    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    
    ctx.beginPath()
    ctx.ellipse(x + width / 2, y + height / 2, width / 2, height / 2, 0, 0, math.pi * 2)
    ctx.fill()
    ctx.stroke()
    
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    ctx.globalAlpha = 1
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawOval({x},{y},{width},{height},{fill},{border},{borderWidth})"})
    #return global_id - 1

# Function to draw a circle (Circle)
def drawCircle(x, y, radius, fill="black", border="transparent", borderWidth=2,rotateAngle=0,opacity=100):

    x*=_scaleFactor
    y*=_scaleFactor
    radius*=_scaleFactor
    borderWidth*=_scaleFactor

    
    # style
    ctx.fillStyle = fill
    ctx.strokeStyle = border
    ctx.lineWidth = borderWidth
    ctx.beginPath()
    ctx.globalAlpha = opacity / 100
    
    # roataion
    ctx.translate(x,y)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-x,-y)
    
    
    ctx.arc(x, y, radius, 0, math.pi * 2)
    ctx.fill()
    ctx.stroke()
    
    
    
    # un-rotate
    ctx.translate(x,y)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-x,-y)
    
    ctx.globalAlpha = 1
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawCircle({x},{y},{radius},{fill},{border},{borderWidth})"})
    #return global_id - 1
    

# Function to draw a line (Line)
def drawLine(x1, y1, x2, y2, fill="black",  lineWidth=2,rotateAngle=0,opacity=100):

    # style
    ctx.strokeStyle = fill
    ctx.lineWidth = lineWidth
    ctx.globalAlpha = opacity / 100
    
    
    # roataion
    centerX=x1+(x2-x1)/2
    centerY=y1+(y2-y1)/2
    
    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    # draw it 
    ctx.beginPath()
    ctx.moveTo(x1, y1)
    ctx.lineTo(x2, y2)
    ctx.stroke()
    
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    ctx.globalAlpha = 1

    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawLine({x1},{y1},{x2},{y2},{fill},{lineWidth})"})
    #return global_id - 1

# Function to draw a label (Label)
def drawLabel(text, x, y, fill="black", size=14, bold=False,italic=False, border="transparent", font="arial" ,borderWidth=2,rotateAngle=0,opacity=100):

    x*=_scaleFactor
    y*=_scaleFactor
    size*=_scaleFactor
    borderWidth*=_scaleFactor

    
    # make size fit with cmu
    size*=582/560
    
    # style
    font_weight = "bold" if bold else "normal"
    font_italic = "italic" if italic else "normal"
    ctx.font = f"{font_weight} {font_italic} {size}px {font}"
    
    
        
#     ctx.fillStyle = fill
    ctx.globalAlpha = opacity / 100
    
    # find sizes
    width=ctx.measureText(text).width
    height=size
    
    
    centerX,centerY=x,y

    
    # fix center
    x=x-width/2
    y=y+height/2.9
    
    # rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
#     if type(fill)!=str:
#     if False:
    if type(fill)==gradient2:
#         print('grad2')
        fill=fill.draw(centerX-width/2,centerY-height/2,centerX+width/2,centerY+height/2)
    ctx.fillStyle = fill
        
    #draw it
    ctx.fillText(str(text), x, y)
    
    #draw border
    if type(border)==gradient2:
#         print('grad2')
        border=border.draw(centerX-width/2,centerY-height/2,centerX+width/2,centerY+height/2)
    elif border==None:
        border="transparent"
    ctx.strokeStyle=border
    
    ctx.lineWidth=borderWidth
    ctx.strokeText(text,x,y)
    
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    ctx.globalAlpha = 1
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f""" drawLabel('''{text}''',{x},{y},{fill},{size},{bold})"""})
    #return global_id - 1
    
# Function to draw a regular polygon (RegularPolygon)
def drawRegularPolygon(x, y, size, sides, fill="black", border="transparent", borderWidth=2,rotateAngle=0,opacity=100):
    
    x*=_scaleFactor
    y*=_scaleFactor
    size*=_scaleFactor

    
    # style
    ctx.fillStyle = fill
    ctx.strokeStyle = border
    ctx.lineWidth = borderWidth
    angle = 2 * math.pi / sides
    ctx.globalAlpha = opacity / 100
    
    # rotate
    centerX,centerY=x,y

    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    # draw
    ctx.beginPath()
    for i in range(sides):
        xVertex = x + size * math.cos(i * angle)
        yVertex = y + size * math.sin(i * angle)
        if i == 0:
            ctx.moveTo(xVertex, yVertex)
        else:
            ctx.lineTo(xVertex, yVertex)
    ctx.closePath()
    ctx.fill()
    ctx.stroke()
    
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    ctx.globalAlpha = 1
    
    
    
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawRegularPolygon({x},{y},{sides},{size},{fill},{border},{borderWidth})"})
    #return global_id - 1

# Function to draw a star (Star)
def drawStar(x, y, points, outerRadius, innerRadius, fill="black", border="transparent", borderWidth=2,rotateAngle=0,opacity=100):


    x*=_scaleFactor
    y*=_scaleFactor
    outerRadius*=_scaleFactor
    innerRadius*=_scaleFactor
    
    #style
    ctx.fillStyle = fill
    ctx.strokeStyle = border
    ctx.lineWidth = borderWidth
    angle = math.pi / points
    ctx.globalAlpha = opacity / 100
    
    # rotate
    centerX,centerY=x,y

    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    # draw
    ctx.beginPath()
    for i in range(2 * points):
        radius = outerRadius if i % 2 == 0 else innerRadius
        xVertex = x + radius * math.cos(i * angle)
        yVertex = y + radius * math.sin(i * angle)
        if i == 0:
            ctx.moveTo(xVertex, yVertex)
        else:
            ctx.lineTo(xVertex, yVertex)
    ctx.closePath()
    ctx.fill()
    ctx.stroke()
    
    
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    ctx.globalAlpha = 1
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawStar({x},{y},{points},{ outerRadius}, {innerRadius},{fill},{border},{borderWidth})"})
    #return global_id - 1

# Function to draw a polygon (Polygon)
def drawPolygon(vertices, fill="black", border="transparent", borderWidth=2,rotateAngle=0,opacity=100):
    
    # style
    ctx.fillStyle = fill
    ctx.strokeStyle = border
    ctx.lineWidth = borderWidth
    ctx.globalAlpha = opacity / 100
    
    # rotate
    xs=[vertex[0] for vertex in vertices]
    ys=[vertex[1] for vertex in vertices]
    
    
    width=max(xs)-min(xs)
    height=max(ys)-min(ys)
    
    centerX = min(xs)+width/2
    centerY = min(ys)+height/2
#     centerX,centerY=0,0
    ######################## centerX and y is needed  for rotate, 

    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    # draw
    ctx.beginPath()
    for i, vertex in enumerate(vertices):
        x, y = vertex
        if i == 0:
            ctx.moveTo(x, y)
        else:
            ctx.lineTo(x, y)
    ctx.closePath()
    ctx.fill()
    ctx.stroke()
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    ctx.globalAlpha = 1
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawPolygon({vertices},{fill},{border},{borderWidth})"})
    #return global_id - 1



# Function to draw and fill an oval slice (Arc) with angles in degrees
def drawArc(x, y, width, height, startAngleDegrees, endAngleDegrees, fill="black",  border="transparent", borderWidth=2,rotateAngle=0,opacity=100):
    
    # make like cmu 
    startAngleRadians = math.radians(startAngleDegrees)
    endAngleRadians = math.radians(endAngleDegrees)
    
    # style
    ctx.fillStyle = fill
    ctx.strokeStyle = border
    ctx.lineWidth = borderWidth
    ctx.globalAlpha = opacity / 100
    
    
    # rotate
    centerX,centerY=x,y
    
    # center
    x-=width/2
    y-=height/2
    
    
    
    # rotate
    drawLabel(f"{centerX},{centerY}",centerX,centerY)

    ctx.translate(centerX,centerY)
    ctx.rotate(rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    
    
    # draw
    ctx.beginPath()
    ctx.ellipse(x + width / 2, y + height / 2, width / 2, height / 2, 0, startAngleRadians, endAngleRadians)
    ctx.lineTo(x + width / 2, y + height / 2)  # Connect to the center
    ctx.closePath()
    ctx.fill()
    ctx.stroke()
    
    
    # un-rotate
    ctx.translate(centerX,centerY)
    ctx.rotate(-rotateAngle * math.pi/180)
    ctx.translate(-centerX,-centerY)
    
    ctx.globalAlpha = 1
    
    #global global_id,global_shapes
    #global_id+=1
    #global_shapes.update({global_id:f"drawArc({x},{y},{width},{height}, {startAngleDegrees},{endAngleDegrees},{fill},{border},{borderWidth})"})
    return global_id - 1


# set background
drawRect(0,0,400,400,fill='white')


