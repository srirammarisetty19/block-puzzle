import pygame
import time
moves=0
flag=0
speed=500
count=0

pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow=(200,200,0)
purple = (111,25,120)
silver=(169,169,169)
gold=(238,180,34)
grey=(153,153,153)
green=(0,128,0)
darkgreen=(0,60,0)
light_green=(0,255,0)
white2=(200,200,200)
orange=(255,128,0)
gameexit=False

def message(msg,colour,i,j,size,gameDisplay,Font,state):
    screen_text=Font.render(msg,True,colour)
    if flag==0 or state==2 or state==1:
        gameDisplay.blit(screen_text,[i,j])

    elif size>6:
        gameDisplay.blit(screen_text,[i*50+20,j*50+20])
    else:
        gameDisplay.blit(screen_text,[i*100+50,j*100+50])

def pause():
    paused =True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused=False





def display(size,puzzle,state):
    font=pygame.font.SysFont(None,35)
    font2=pygame.font.SysFont("comicsansms",40*size/3)
    font3=pygame.font.SysFont(None,35*size/3)
    font4=pygame.font.SysFont(None,22*size/3)
    fontl4=pygame.font.SysFont(None,10*size/3)
    fontl2=pygame.font.SysFont("comicsansms",20*size/3)
    fontl3=pygame.font.SysFont(None,17*size/3)
    global moves
    global flag
    global speed
    global count
    if size>=7:
        gameDisplay= pygame.display.set_mode((size*50+1,size*50+51))
    else:
        gameDisplay= pygame.display.set_mode((size*100+1,size*100+51))
    pygame.display.set_caption("Sliding Puzzle")
    gameexit=False



    if flag==0 :
        intro=True
        while intro:

            gameDisplay.fill(black)
            for event in pygame.event.get():
                pass
            cur=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            if size<=6:
                if (size-1)*101/2<cur[0]<(100*size/3 + (size-1)*101/2) and (size)*101-15<cur[1]<(size)*101-15+51-size:
                    gameDisplay.fill(light_green,rect=[(size-1)*101/2,(size)*101-15,100*size/3,51-size])
                    if click[0]==1:
                        intro=False
                else:
                    gameDisplay.fill(darkgreen,rect=[(size-1)*101/2-2,(size)*101-13,100*size/3+4,51-size+4])
                    gameDisplay.fill(green,rect=[(size-1)*101/2,(size)*101-15,100*size/3,51-size])

                message("START",black,(size-1)*101/2+100*size/6-40*size/3,(size)*101-15+(51-size)/2-10*size/3,size,gameDisplay,font3,state)
                message("PUZZLE",white,40*size/3,(size-3)*100/2,size,gameDisplay,font2,state)
                message("SOLVER",white,40*size/3+50*size/3,(size-1)*100/2,size,gameDisplay,font2,state)
                message("CONTROLS:",red,40*size/3,(size+1)*100/2,size,gameDisplay,font3,state)
                message("F: Fast",gold,40*size/3+30*size/3,(size+2)*100/2-20*(3/size),size,gameDisplay,font4,state)
                message("N: Normal",gold,40*size/3+30*size/3,(size+2)*100/2+20*size/3-20*(3/size),size,gameDisplay,font4,state)
                message("S: Slow",gold,40*size/3+30*size/3,(size+2)*100/2+40*size/3-20*(3/size),size,gameDisplay,font4,state)


            else:
                if (size-1)*51/2-35*size/7<cur[0]<(50*size/3 + (size-1)*51/2-35*size/7) and (size)*51-15<cur[1]<(size)*51-5+51-size:
                    gameDisplay.fill(light_green,rect=[(size-1)*51/2-35*size/7,(size)*51-5,50*size/3,51-size])
                    if click[0]==1:
                        intro=False
                else:
                    gameDisplay.fill(darkgreen,rect=[(size-1)*51/2-2-35*size/7,(size)*51-7,50*size/3+4,51-size+4])
                    gameDisplay.fill(green,rect=[(size-1)*51/2-35*size/7,(size)*51-5,50*size/3,51-size])

                message("START",black,(size-1)*51/2+20*size/6-20*size/3,(size)*51-5+(51-size)/2-5*size/3,size,gameDisplay,fontl3,state)
                message("PUZZLE",white,20*size/3,(size-3)*50/2,size,gameDisplay,fontl2,state)
                message("SOLVER",white,20*size/3+20*size/3,(size-1)*50/2,size,gameDisplay,fontl2,state)
                message("CONTROLS:",red,20*size/3,(size+1)*50/2+30*size/7,size,gameDisplay,fontl3,state)
                message("F: Fast",gold,20*size/3+10*size/3,(size+2)*50/2-10*(3/size)+40*size/7,size,gameDisplay,fontl4,state)
                message("N: Normal",gold,20*size/3+10*size/3,(size+2)*50/2+10*size/3-10*(3/size)+40*size/7,size,gameDisplay,fontl4,state)
                message("S: Slow",gold,20*size/3+10*size/3,(size+2)*50/2+20*size/3-10*(3/size)+40*size/7,size,gameDisplay,fontl4,state)



            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        flag=1
        return flag
    if state ==0:
        moves+=1

    if size<=6:
        gameDisplay.fill(black)
        gameDisplay.fill(grey,rect=[1,(size)*101,size*101-size-1,51-size])
        pygame.draw.rect(gameDisplay,black,[50-2,size*101+8,75*size/3+4,30+4])
        pygame.draw.rect(gameDisplay,red,[50,size*101+10,75*size/3,30])
        pygame.draw.rect(gameDisplay,black,[200*size/3-2,size*101+8,25*size+4,34])
        pygame.draw.rect(gameDisplay,white,[200*size/3,size*101+10,25*size,30])
        flag=0
        message(str(moves),black,200*size/3+25*size/2-8*size/3,size*101+10+15-8*size/3,size,gameDisplay,font4,state)
        message("P: Pause",black,50+25*size/2-30*size/3,size*101+10+15-6*size/3,size,gameDisplay,font4,state)


    else:
        gameDisplay.fill(black)
        gameDisplay.fill(grey,rect=[1,(size)*51,size*51-size-1,51-size])
        pygame.draw.rect(gameDisplay,black,[50-2,size*51+8,40*size/3+4,30+4])
        pygame.draw.rect(gameDisplay,red,[50,size*51+10,40*size/3,30])
        pygame.draw.rect(gameDisplay,black,[100*size/3-2,size*51+8,15*size+4,34])
        pygame.draw.rect(gameDisplay,white,[100*size/3,size*51+10,15*size,30])
        flag=0
        message(str(moves),black,100*size/3+15*size/2-4*size/3,size*51+10+15-4*size/3,size,gameDisplay,fontl4,state)
        message("P: Pause",black,50+40*size/6-15*size/3,size*51+10+15-3*size/3,size,gameDisplay,fontl4,state)
    flag=1
    i=1
    while i<(size*100+1 if size<7 else size*50+1):
        j=1
        while j<(size*100+1 if size<7 else size*50+1) :
            if size<=6:
                gameDisplay.fill(purple,rect=[i,j,99,99])
                j+=100
            else:
                gameDisplay.fill(purple,rect=[i,j,49,49])
                j+=50
        if size>6:
            i+=50
        else:
            i+=100


    for i in range(size):
        for j in range(size):
            k=puzzle[j][i]
            if k=='0':
                if size<=6:
                    gameDisplay.fill(black,rect=[i*100+1,j*100+1,99,99])
                else:
                    gameDisplay.fill(black,rect=[i*50+1,j*50+1,49,49])

            else:
                message(str(k),black,i,j,size,gameDisplay,font,0)
    if state ==2:
        if size<=6:
            message("PUZZLE",white,40*size/3,(size-1)*100/2,size,gameDisplay,font2,state)
            message("SOLVED!!!",white,40*size/3+50*size/3,(size+1)*100/2,size,gameDisplay,font2,state)
        else:
            message("PUZZLE",white,20*size/3,(size-1)*50/2,size,gameDisplay,fontl2,state)
            message("SOLVED!!!",white,20*size/3+20*size/3,(size+1)*50/2,size,gameDisplay,fontl2,state)


    elif state ==1:
        if size<=6:
            message("PUZZLE NOT",white,30*size/3,(size-1)*100/2,size,gameDisplay,font2,state)
            message("SOLVABLE!!!",white,40*size/3+10*size/3,(size+1)*100/2,size,gameDisplay,font2,state)
        else:
            message("PUZZLE NOT",white,10*size/3,(size-1)*50/2,size,gameDisplay,fontl2,state)
            message("SOLVABLE!!!",white,15*size/3+5*size/3,(size+1)*50/2,size,gameDisplay,fontl2,state)

    pygame.display.update()
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                    pygame.display.update()

                if event.key == pygame.K_f and (count==0 or count==-1 or count ==-2):
                    speed = 200*3/size
                    count=1
                    pygame.display.update()

                if event.key == pygame.K_f and count==1:
                    speed = 50.000*3/size
                    count=2
                    pygame.display.update()

                if event.key == pygame.K_n:
                    speed = 500*3/size
                    count=0
                    pygame.display.update()

                if event.key == pygame.K_s and (count==0 or count==1 or count==2):
                    speed = 1000*3/size
                    count=-1
                    pygame.display.update()

                if event.key == pygame.K_s and count==-1:
                    speed = 1500*3/size
                    count=-2
                    pygame.display.update()
    time.sleep(0.001*speed)

def exit(size,outcome,puzzle):
    time.sleep(size)
    while True:
        display(size,puzzle,1+outcome)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
