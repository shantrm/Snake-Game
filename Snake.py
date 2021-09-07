#Snake Game Refrence Code Credit:
#https://www.edureka.co/blog/snake-game-with-pygame/'
#Wahija Urooj

#Class to help create pygame buttons, Credit: Tech With Tim
#https://www.youtube.com/watch?v=4_9twnEduFA

import pygame
import pygame_gui
import random
from pygame.locals import *

programIcon = pygame.image.load('Snake Icon.png')

pygame.display.set_icon(programIcon)


SIZE = 608, 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 128, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255,255,255)
YELLOW = (225,255,0)
PURPLE = (255,0,255)


global userlist
global scorelist

userlist = []
scorelist = []


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Snake Game!')

file1 = open("scores.txt", "r")
file2 = open("user.txt", "r")

scorestr =str(file1.readlines())
userstr  = str (file2.readlines())

tempuserstr = userstr.replace("[", "")
tempscorestr= scorestr.replace ("[", "")

tempuserstr = tempuserstr.replace("]", "")
tempscorestr= tempscorestr.replace ("]", "")

tempuserstr = tempuserstr.replace("'", "")
tempscorestr= tempscorestr.replace ("'", "")

tempuserstr = tempuserstr.replace('"', "")
tempscorestr= tempscorestr.replace ('"', "")

tempuserstr = tempuserstr.replace(' ', "")
tempscorestr= tempscorestr.replace (' ', "")

appenduserlist = tempuserstr.split(",")
appendscorelist =  tempscorestr.split(",")

appendscorelist = map(int, appendscorelist)

userlist.extend((appenduserlist))
scorelist.extend((appendscorelist))


#Class to help create pygame buttons, Credit: Tech With Tim
#https://www.youtube.com/watch?v=4_9twnEduFA
        
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,out=None):
        if out:
            pygame.draw.rect(screen, out, (self.x-2,self.y-2,self.width+2,self.height),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('bahnschrift', 45)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        posX = pos[0]
        posY = pos[1]
        
        if posX > self.x and posX < self.x + self.width:
            if posY > self.y and posY < self.y + self.height:
                return True
            
        return False

#Start Screen Fucntion, Displays Start Screen
def startScreen():
    screen.fill(BLACK)
     
    font = pygame.font.SysFont("bahnschrift", 72)
    text = font.render("Snake Game!", True, WHITE)    
    rect = Rect(304 - text.get_width()/2 -5, 50, text.get_width() + 10, 80)
    gameButton = button(GREEN,320,225,250,100, 'Start')
    scoreButton = button(YELLOW,40,225,250,100, 'Highscore')
    quitButton = button (GRAY, 485, 430, 125, 50, 'Quit')
    running = True
    
    while running:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameButton.isOver(pos):
                    gameScreen()
                if scoreButton.isOver(pos):
                    scoreScreen()
                if quitButton.isOver(pos):
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                if gameButton.isOver(pos):
                    gameButton.color = RED
                else:
                    gameButton.color = GREEN
                if scoreButton.isOver(pos):
                    scoreButton.color = BLUE
                else:
                    scoreButton.color = YELLOW
                if quitButton.isOver(pos):
                    quitButton.color = WHITE
                else:
                    quitButton.color = GRAY
            
       
        pygame.draw.rect(screen, RED, rect)
        gameButton.draw(screen, (0,0,0))
        scoreButton.draw(screen, (0,0,0))
        quitButton.draw(screen, (0,0,0))
        screen.blit(text,
            (304 - text.get_width() // 2, 50))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

#Score Screen Function, Displays Highscore Screen
def scoreScreen():

    global userlist
    global scorelist
    
    font = pygame.font.SysFont("bahnschrift", 72)
    scoreFont = pygame.font.SysFont("bahnschrift", 30)
    text = font.render("Highscores:", True, WHITE)    
    rect = Rect(110, 50, text.get_width() + 10, 80)
    backButton = button(GRAY,483,430,125,50, 'Back')
    
    tempuser = userlist
    tempscore = scorelist
    
    keydict = dict(zip(tempuser,tempscore))
    tempuser.sort (key = keydict.get)

    tempscore.sort(reverse = True)
    tempuser.reverse()
    
    if len(tempscore)> 5:
        userlist = tempuser[0:5]
        scorelist = tempscore[0:5]

        
        file1 = open("scores.txt", "w")
        file2 = open("user.txt", "w") 

        file1.write(str(scorelist))
        file2.write(str(userlist))

        file1.close()
        file2.close()

    running = True
    try:
        userText1 = scoreFont.render(str(tempuser[0]), True, WHITE)
        scoreText1 = scoreFont.render(str(tempscore[0]), True, WHITE)
        
        userText2 = scoreFont.render(str(tempuser[1]), True, WHITE)
        scoreText2 = scoreFont.render(str(tempscore[1]), True, WHITE)

        userText3 = scoreFont.render(str(tempuser[2]), True, WHITE)
        scoreText3 = scoreFont.render(str(tempscore[2]), True, WHITE)
        
        userText4 = scoreFont.render(str(tempuser[3]), True, WHITE)
        scoreText4 = scoreFont.render(str(tempscore[3]), True, WHITE)
        
        userText5 = scoreFont.render(str(tempuser[4]), True, WHITE)
        scoreText5 = scoreFont.render(str(tempscore[4]), True, WHITE)
    except:
        pass
    
    while running:
        screen.fill(BLACK)

        
        if len(tempuser) == 0:
            pass
        else:
            try:
                screen.blit(userText1, (114, 160))
                screen.blit(scoreText1, (350, 160))
                
                screen.blit(userText2, (114, 200))
                screen.blit(scoreText2, (350, 200))
                
                screen.blit(userText3, (114, 240))
                screen.blit(scoreText3, (350, 240))
                
                screen.blit(userText4, (114, 280))
                screen.blit(scoreText4, (350, 280))
                
                screen.blit(userText5, (114, 320))
                screen.blit(scoreText5, (350, 320))
                
            except:
                pass
            
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.isOver(pos):
                    startScreen()

            if event.type == pygame.MOUSEMOTION:
                if backButton.isOver(pos):
                    backButton.color = WHITE
                else:
                    backButton.color = GRAY
        
        pygame.draw.rect(screen, BLUE, rect)
        backButton.draw(screen, (0,0,0))
        screen.blit(text,(114, 50))
            
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

#Win Screen Function, Displays the game over screen
def winScreen():

    global glbluser
    glbluser = ''
    
    font = pygame.font.SysFont("bahnschrift", 72)
    scoreFont = pygame.font.SysFont("bahnschrift", 30)
    inputFont = pygame.font.SysFont("bahnschrift", 20)
    text = font.render("You Win!", True, WHITE)
    text2 = font.render("Game Over!", True, WHITE)
    rect = Rect(304 - text2.get_width()/2 -5, 50, text2.get_width() + 10, 80)
    homeButton = button(GRAY,483,430,125,50, 'Home')
    retryButton = button(GRAY,0,430,125,50, 'Retry')
    running = True
    scoreText = scoreFont.render("Score: " + str(glblscore), True, WHITE)
    directText = scoreFont.render("Username:", True, WHITE)
    submitButton = button(GREEN,165,312,160,50, 'Submit')

    once = 0
    charlim = 0
    username = ''
    user_text = ''
    input_rect = pygame.Rect(170, 255, 140, 32)
    color_active = WHITE
    color_passive = GRAY
    color = color_passive
    active = False
    
    while running:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if homeButton.isOver(pos):
                    once = 0
                    startScreen()
                if retryButton.isOver(pos):
                    once = 0
                    gameScreen()
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if submitButton.isOver(pos):  
                    if once == 0:
                        username = user_text
                        glbluser = username
                        if glbluser == "":
                            pass
                        else:
                            submitButton.color = DARKGREEN
                            userlist.append(str(glbluser))
                            scorelist.append(glblscore)
                           
                            file1 = open("scores.txt", "w")
                            file2 = open("user.txt", "w") 

                            file1.write(str(scorelist))
                            file2.write(str(userlist))

                            file1.close()
                            file2.close()

                            once = 1
                    else:
                        pass

            if event.type == pygame.MOUSEMOTION:
                if homeButton.isOver(pos):
                    homeButton.color = WHITE
                else:
                    homeButton.color = GRAY
                if retryButton.isOver(pos):
                    retryButton.color = WHITE
                else:
                    retryButton.color = GRAY

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:      
                    user_text = user_text[:-1]
                    charlim = charlim - 1
                elif charlim <15:
                    user_text += event.unicode
                    charlim = charlim + 1

        if active:
            color = color_active
        else:
            color = color_passive
        
        screen.fill(BLACK)
        pygame.draw.rect(screen, PURPLE, rect)
        homeButton.draw(screen, (0,0,0))
        retryButton.draw(screen, (0,0,0))
        submitButton.draw(screen, (0,0,0))
        screen.blit(text2,(304 - text2.get_width() // 2, 50))
        screen.blit(scoreText,(304 - text.get_width() // 2, 160))
        screen.blit(directText,(304 - text.get_width() // 2, 210))

        pygame.draw.rect(screen, color, input_rect)
        text_surface = inputFont.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

#Game Screen Function, Displays the actual snake game
def gameScreen():
    
    font = pygame.font.SysFont("bahnschrift", 72)
    smallFont = pygame.font.SysFont("bahnschrift", 15, bold = True)
    scoreFont = pygame.font.SysFont("bahnschrift", 30)
    running = True
    score = 0
    text = scoreFont.render("Score: " + str(score), True, WHITE)
    smile = smallFont.render(":)", True, BLACK)

    snakeList = []
    snakeLength = 1

    x1 = 304
    y1 = 240

    x1change = 0
    y1change = 0

    direction = 100

    foodx = round(random.randint(0, 608-20))
    foody = round(random.randint(0, 480-20))

    global glblscore
    glblscore = 0
    
    while running:
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
                        
            if event.type == QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction ==1:
                        pass
                    else:
                        direction = 3
                        x1change = -10
                        y1change = 0
                elif event.key == pygame.K_RIGHT:
                    if direction ==3:
                        pass
                    else:
                        direction = 1
                        x1change = 10
                        y1change = 0
                elif event.key == pygame.K_UP:
                    if direction ==4:
                        pass
                    else:
                        direction = 2
                        y1change = -10
                        x1change = 0

                elif event.key == pygame.K_DOWN:
                    if direction ==2:
                        pass
                    else:
                        direction = 4
                        y1change = 10
                        x1change = 0
                        
        if x1 >= 608 or x1 < 0 or y1 >= 480 or y1 < 0:
            glblscore = score
            winScreen()
        
        x1 += x1change
        y1 += y1change
                
        player = Rect(x1, y1, 20,20)
        food = Rect(foodx,foody, 20, 20)
        
        screen.fill(BLACK)
        screen.blit(text,(10, 10))
        #screen.blit(smile,(foodx + 3, foody + 1))
        pygame.draw.rect(screen, RED, food)
        pygame.draw.rect(screen,YELLOW, player)

        snake = []
        snake.append(x1)
        snake.append(y1)
        snakeList.append(snake)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snake:
                glblscore = score
                winScreen()

        for x in snakeList:
            pygame.draw.rect(screen, YELLOW, [x[0], x[1], 20, 20])
        
        if player.colliderect(food):
            score = score + 1
            text = scoreFont.render("Score: " + str(score), True, WHITE)
            screen.blit(text,(10, 10))
            foodx = round(random.randint(0, 608-20))
            foody = round(random.randint(0, 480-20))
            snakeLength += 2
        
            
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

    
startScreen()








