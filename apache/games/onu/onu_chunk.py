from browser import document, window, html
# from base import bind
from base import bind#, playDsdfb

#from newbase import docio
#docio.enable()

# from browser import 
# configuration variable, NOT a permanent part of the code
Q__ = 4


# import menu
# import game
# import card
# print(
#     window.screen.availHeight,
#     window.screen.availWidth,
#     window.screen.availWidth<window.screen.availHeight  
# )
from menu2 import Menu






# def play_audio(src="media/700k.mp3"):
#     audio = html.AUDIO(src=src, autoplay=True)
#     document <= audio
#     audio.play()

# document["playButton"].bind("click", play_audio)


def playDsdfb(src="media/t_back.mp3"):
    """
        Dynamic Spectral Data File Buffer
    """
    audio = html.AUDIO(src=src, autoplay=True)
    document <= audio
    audio.play()

playDsdfb()







# init the menu
menu=Menu()

# new menu test
# document.addEventListener("scroll",menu.scroll)




# mouseDown
# canvas.bind("mousedown", menu.mouseDown)
_stored=False
def rebind(trash=None):
    global _stored
    _stored=bind("mousedown", menu.mouseDown,_stored)
    # _stored=bind("mousedown", play_audio)

window.onresize = rebind
rebind()

# key press event
def keyDown (event):
    menu.keyDown(event.key)

document.bind("keydown", keyDown)



####### onstep
# import browser.aio as aio

def onStep():
    menu.onStep()
    
    # t=aio.sleep(5)
    # await t
    # print("end")
    #required option a or b, dynamic step interval
    # window.setTimeout(onStep, 1000)

# option b, set step iterval



# async def runos():
#     print(333333333)
window.setInterval(menu.onStep, 1000)   
# # print(runos())
# aio.run(onStep())

# playDsdfb()# start music


print("chunk ended")
# menu.drawMainMenu()













