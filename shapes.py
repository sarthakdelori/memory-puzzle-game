import pygame, sys
from pygame.locals import *
import random

rectangles=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
shapesarrangement=[]   #ex-[7,4,5,6...] then 7 and 4 have same color rectangle and so on.. 

rectangle1=Rect(0,0,100,100)
rectangle2=Rect(100,0,100,100)
rectangle3=Rect(200,0,100,100)
rectangle4=Rect(300,0,100,100)
rectangle5=Rect(0,100,100,100)
rectangle6=Rect(100,100,100,100)
rectangle7=Rect(200,100,100,100)
rectangle8=Rect(300,100,100,100)
rectangle9=Rect(0,200,100,100)
rectangle10=Rect(100,200,100,100)
rectangle11=Rect(200,200,100,100)
rectangle12=Rect(300,200,100,100)
rectangle13=Rect(0,300,100,100)
rectangle14=Rect(100,300,100,100)
rectangle15=Rect(200,300,100,100)
rectangle16=Rect(300,300,100,100)

rectangleObjects = (rectangle1,rectangle2,rectangle3,rectangle4,rectangle5,rectangle6,rectangle7,rectangle8,rectangle9,rectangle10,rectangle11,rectangle12,rectangle13,rectangle14,rectangle15,rectangle16)

def drawback():
	for i in range(16):
		pygame.draw.rect(window,(255,0,0),rectangleObjects[i],5)

def drawRecShapes(x,color):
	if x==1:
		pygame.draw.rect(window,color,Rect(20,20,60,60))
	elif x==2:
		pygame.draw.rect(window,color,Rect(120,20,60,60))
	elif x==3:
		pygame.draw.rect(window,color,Rect(220,20,60,60))
	elif x==4:
		pygame.draw.rect(window,color,Rect(320,20,60,60))
	elif x==5:
		pygame.draw.rect(window,color,Rect(20,120,60,60))
	elif x==6:
		pygame.draw.rect(window,color,Rect(120,120,60,60))
	elif x==7:
		pygame.draw.rect(window,color,Rect(220,120,60,60))
	elif x==8:
		pygame.draw.rect(window,color,Rect(320,120,60,60))
	elif x==9:
		pygame.draw.rect(window,color,Rect(20,220,60,60))
	elif x==10:
		pygame.draw.rect(window,color,Rect(120,220,60,60))
	elif x==11:
		pygame.draw.rect(window,color,Rect(220,220,60,60))
	elif x==12:
		pygame.draw.rect(window,color,Rect(320,220,60,60))
	elif x==13:
		pygame.draw.rect(window,color,Rect(20,320,60,60))
	elif x==14:
		pygame.draw.rect(window,color,Rect(120,320,60,60))
	elif x==15:
		pygame.draw.rect(window,color,Rect(220,320,60,60))
	elif x==16:
		pygame.draw.rect(window,color,Rect(320,320,60,60))

def drawCirShapes(x,color):
	if x==1:
		pygame.draw.circle(window,color,(50,50),30)
	elif x==2:
		pygame.draw.circle(window,color,(150,50),30)
	elif x==3:
		pygame.draw.circle(window,color,(250,50),30)
	elif x==4:
		pygame.draw.circle(window,color,(350,50),30)
	elif x==5:
		pygame.draw.circle(window,color,(50,150),30)
	elif x==6:
		pygame.draw.circle(window,color,(150,150),30)
	elif x==7:
		pygame.draw.circle(window,color,(250,150),30)
	elif x==8:
		pygame.draw.circle(window,color,(350,150),30)
	elif x==9:
		pygame.draw.circle(window,color,(50,250),30)
	elif x==10:
		pygame.draw.circle(window,color,(150,250),30)
	elif x==11:
		pygame.draw.circle(window,color,(250,250),30)
	elif x==12:
		pygame.draw.circle(window,color,(350,250),30)
	elif x==13:
		pygame.draw.circle(window,color,(50,350),30)
	elif x==14:
		pygame.draw.circle(window,color,(150,350),30)
	elif x==15:
		pygame.draw.circle(window,color,(250,350),30)
	elif x==16:
		pygame.draw.circle(window,color,(350,350),30)


def drawTriShapes(x,color):
	if x==1:
		pygame.draw.polygon(window,color,( (10,20),(90,20),(50,80) ))
	elif x==2:
		pygame.draw.polygon(window,color,( (110,20),(190,20),(150,80) ))
	elif x==3:
		pygame.draw.polygon(window,color,( (210,20),(290,20),(250,80) ))
	elif x==4:
		pygame.draw.polygon(window,color,( (310,20),(390,20),(350,80) ))
	elif x==5:
		pygame.draw.polygon(window,color,( (10,120),(90,120),(50,180) ))
	elif x==6:
		pygame.draw.polygon(window,color,( (110,120),(190,120),(150,180) ))
	elif x==7:
		pygame.draw.polygon(window,color,( (210,120),(290,120),(250,180) ))
	elif x==8:
		pygame.draw.polygon(window,color,( (310,120),(390,120),(350,180) ))
	elif x==9:
		pygame.draw.polygon(window,color,( (10,220),(90,220),(50,280) ))
	elif x==10:
		pygame.draw.polygon(window,color,( (110,220),(190,220),(150,280) ))
	elif x==11:
		pygame.draw.polygon(window,color,( (210,220),(290,220),(250,280) ))
	elif x==12:
		pygame.draw.polygon(window,color,( (310,220),(390,220),(350,280) ))
	elif x==13:
		pygame.draw.polygon(window,color,( (10,320),(90,320),(50,380) ))
	elif x==14:
		pygame.draw.polygon(window,color,( (110,320),(190,320),(150,380) ))
	elif x==15:
		pygame.draw.polygon(window,color,( (210,320),(290,320),(250,380) ))
	elif x==16:
		pygame.draw.polygon(window,color,( (310,320),(390,320),(350,380) ))


def drawDiamShapes(x,color):
	if x==1:
		pygame.draw.polygon(window,color,( (10,50),(50,20),(90,50),(50,80) ))
	elif x==2:
		pygame.draw.polygon(window,color,( (110,50),(150,20),(190,50),(150,80) ))
	elif x==3:
		pygame.draw.polygon(window,color,( (210,50),(250,20),(290,50),(250,80) ))
	elif x==4:
		pygame.draw.polygon(window,color,( (310,50),(350,20),(390,50),(350,80) ))
	elif x==5:
		pygame.draw.polygon(window,color,( (10,150),(50,120),(90,150),(50,180) ))
	elif x==6:
		pygame.draw.polygon(window,color,( (110,150),(150,120),(190,150),(150,180) ))
	elif x==7:
		pygame.draw.polygon(window,color,( (210,150),(250,120),(290,150),(250,180) ))
	elif x==8:
		pygame.draw.polygon(window,color,( (310,150),(350,120),(390,150),(350,180) ))
	elif x==9:
		pygame.draw.polygon(window,color,( (10,250),(50,220),(90,250),(50,280) ))
	elif x==10:
		pygame.draw.polygon(window,color,( (110,250),(150,220),(190,250),(150,280) ))
	elif x==11:
		pygame.draw.polygon(window,color,( (210,250),(250,220),(290,250),(250,280) ))
	elif x==12:
		pygame.draw.polygon(window,color,( (310,250),(350,220),(390,250),(350,280) ))
	elif x==13:
		pygame.draw.polygon(window,color,( (10,350),(50,320),(90,350),(50,380) ))
	elif x==14:
		pygame.draw.polygon(window,color,( (110,350),(150,320),(190,350),(150,380) ))
	elif x==15:
		pygame.draw.polygon(window,color,( (210,350),(250,320),(290,350),(250,380) ))
	elif x==16:
		pygame.draw.polygon(window,color,( (310,350),(350,320),(390,350),(350,380) ))
	
    
def startGame():
	for i in range(4):
		if i==0 or i==1:
			color=(0,0,255)
		else:
			color=(0,255,0)
		x=random.choice(rectangles)  #random numbers chosen each time you play
		shapesarrangement.append(x)  #tells at which random location particular shape is present
		drawRecShapes(x,color) 
		rectangles.remove(x)   # so the same number won't be chosen again 	


	for i in range(4):
		if i==0 or i==1:
			color=(90,0,90)
		else:
			color=(0,128,128)
		x=random.choice(rectangles)  #random numbers chosen each time you play
		shapesarrangement.append(x)
		drawCirShapes(x,color) 
		rectangles.remove(x)   # so the same number won't be chosen again 	


	for i in range(4):
		if i==0 or i==1:
			color=(255,0,255)
		else:
			color=(255,255,0)
		x=random.choice(rectangles)  #random numbers chosen each time you play
		shapesarrangement.append(x)
		drawTriShapes(x,color) 
		rectangles.remove(x)   # so the same number won't be chosen again 	


	for i in range(4):
		if i==0 or i==1:
			color=(0,128,255)
		else:
			color=(128,0,0)
		x=random.choice(rectangles)  #random numbers chosen each time you play
		shapesarrangement.append(x)
		drawDiamShapes(x,color) 
		rectangles.remove(x)   # so the same number won't be chosen again 	

def rightchoice(firstchoice,secondchoice):
	x=shapeIndex(firstchoice)
	y=shapeIndex(secondchoice)

	# below written x and y tells the index from shape arrangement list in pairs
	if(x==0 and y==1 or x==1 and y==0)\
	    or(x==2 and y==3 or x==3 and y==2)\
	    or(x==4 and y==5 or x==5 and y==4)\
	    or(x==6 and y==7 or x==7 and y==6)\
	    or(x==8 and y==9 or x==9 and y==8)\
	    or(x==10 and y==11 or x==11 and y==10)\
	    or(x==12 and y==13 or x==13 and y==12)\
	    or(x==14 and y==15 or x==15 and y==14):
	    return True

#the shape at the index is called 
def shapeIndex(mouse_position):
    for i in range(16):
        if rectangleObjects[i].collidepoint(mouse_position):
            return shapesarrangement.index(i+1)

#rectangle number at which shape is called
def recNumber(mouse_position):
    for i in range(16):
        if rectangleObjects[i].collidepoint(mouse_position):
            return i+1

# for hiding the shapes if they don't match            
def hide(mouse_position):
    rectanglenumber = recNumber(mouse_position)
    for i in range(16):
        if rectanglenumber==i+1:
            pygame.draw.rect(window,(255,255,255),rectangleObjects[i].inflate(-5,-5))
def show(mouse_position):
    rectanglenumber = recNumber(mouse_position)
    shapeindex = shapeIndex(mouse_position)
    if shapeindex==0 or shapeindex==1:
        color = (0,0,255)
        drawRecShapes(rectanglenumber,color)
    elif shapeindex==2 or shapeindex==3:
        color = (0,255,0)
        drawRecShapes(rectanglenumber,color)
    elif shapeindex==4 or shapeindex==5:
        color = (90,0,90)
        drawCirShapes(rectanglenumber,color)
    elif shapeindex==6 or shapeindex==7:
        color = (0,128,128)
        drawCirShapes(rectanglenumber,color)
    elif shapeindex==8 or shapeindex==9:
        color = (255,0,255)
        drawTriShapes(rectanglenumber,color)
    elif shapeindex==10 or shapeindex==11:
        color = (255,255,0)
        drawTriShapes(rectanglenumber,color)
    elif shapeindex==12 or shapeindex==13:
        color = (0,128,255)
        drawDiamShapes(rectanglenumber,color)
    elif shapeindex==14 or shapeindex==15:
        color = (128,0,0)
        drawDiamShapes(rectanglenumber,color)

def main():
	pygame.init()
	global window
	window=pygame.display.set_mode((410,410))
	window.fill((255,255,255))
	pygame.display.set_caption('Memory puzzle')
	drawback()
	startGame()
	# drawDiamShapes(10,(255,0,255))
	pygame.display.update() 
	pygame.time.wait(2000)
	window.fill((255,255,255))
	drawback()
	pygame.display.update()	
	flag=0
	truechoices=[]

	while True:
		for event in pygame.event.get():
			# if event.type==MOUSEBUTTONUP:
			# 	print("Mouse is clicked")

			# if event.type==KEYUP:
			#     print("Keyboard button is pressed")

			if event.type==QUIT:
			    pygame.quit()
			    sys.exit()
			elif (event.type==pygame.MOUSEBUTTONUP):
				mouse_position=pygame.mouse.get_pos()
				show (mouse_position)
				pygame.display.update()
				if flag==0:
					firstchoice = mouse_position
					if recNumber(firstchoice) in truechoices: flag=0 # to check that the rectangle, player is clicking is not the true choice already
					else: flag=1
				else:
					secondchoice = mouse_position
					if recNumber(secondchoice) in truechoices: flag=1 #same as above
					else: flag=0 # so the next choice would be consider as firstchoice
					if not(recNumber(firstchoice) in truechoices) and not (recNumber(secondchoice) in truechoices):
						if rightchoice(firstchoice,secondchoice):  #if the choices selected are right and not in truechoice list, then add
							truechoices.append(recNumber(firstchoice))
							truechoices.append(recNumber(secondchoice))
						else:
							pygame.time.wait(1000)
							hide(firstchoice)
							hide(secondchoice)
							pygame.display.update()

		if len(truechoices)==16:
		    myfont= pygame.font.SysFont('Comic Sans MS',75,True,True)
		    textsurface=myfont.render('Well Done!!',True,(0,0,0))
		    window.blit(textsurface,(20,150))
		    # image= pygame.image.load('won.jpg')
		    # window.blit(image,(0,0))
		    pygame.display.update()			
      
if __name__ == '__main__':
	main()
