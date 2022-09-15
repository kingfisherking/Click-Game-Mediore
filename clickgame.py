import pygame, sys, random, math

pygame.init()


size = width, height = 500, 500
white = 255, 255, 255, 100
black = 0, 0, 0, 100
r = 50
spawnX = 50
spawnY = 50

titleFont =  pygame.font.SysFont('arial', int(height/10))
Title = titleFont.render('Click', True, black)

score = 0
scoreFont = pygame.font.SysFont('arial', 23)
scoreCount = scoreFont.render(str(score), True, black)

particleList = []

modeTrigger = 0

screen = pygame.display.set_mode(size)
screen = screen.convert_alpha()


#class click:
   # width = 50
    #height = 50
    #x = 0
    #y = 0
    #location = pygame.Rect(x, y, width, height)

#def setNew(square):
    #square.update(random.randint(0,450),random.randint(0,450))



#square =  pygame.Surface(50, 50)
#square.fill(black)
#squareRect = square.get_rect()

def newLocation():
    global spawnX
    global spawnY
    spawnX = random.randint(0, width-r)
    spawnY = random.randint(0, height-r)
    
newLocation()

def add():
    global score
    score += 1

def reset():
    global score
    score = 0

def update():
    global score
    global scoreCount
    scoreCount = scoreFont.render(str(score), True, black)

def startGame():
    global modeTrigger
    modeTrigger = 1


counter = 0.0

while modeTrigger == 0:

    counter = counter+0.0011

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            startGame()
    screen.fill(white)
    screen.blit(Title, (int(width/2)-int(width/10), int(height/2)-int(height/10)+(int(5*math.sin(counter)))))
    #print(int(5*math.sin(counter)))
    pygame.display.flip()   

    



while modeTrigger == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pos()[0] > spawnX and pygame.mouse.get_pos()[0] < spawnX+r:
                if pygame.mouse.get_pos()[1] > spawnY and pygame.mouse.get_pos()[1] < spawnY+r:
                    add()
                    print(score)
                    update()
                    newLocation()
            else:
                reset()
                update()
                print(score)


            #print(pygame.mouse.get_pos())
            
            #print(spawnX, spawnY)

    
    screen.fill(white)
    screen.blit(scoreCount, (0,0))
    pygame.draw.rect(screen, black, pygame.Rect(spawnX, spawnY, r, r), 0, 3)
    pygame.display.flip()


