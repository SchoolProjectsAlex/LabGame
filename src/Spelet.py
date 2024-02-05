import pygame # importera det behölvliga delarna
import sys
import random
from button import Button


pygame.init() #kallar in pygame så jag kan avända den
SCREEN = pygame.display.set_mode((900, 500)) #ställer in skärmstorlek
pygame.display.set_caption("Menu") #vanlig text 

BG = pygame.image.load("pic/backgound.jpg")

def get_font(size):  # En defintion som ger en font från en fil!
    return pygame.font.Font("font.ttf", size)

def play():
    
    screen = pygame.display.set_mode((900, 500))  # (width, height)
    clock = pygame.time.Clock()  # Med at sätta in tiden så kontrollerar jag frameraten och pausen mellan game over och gå vidare 
    spelfonten = pygame.font.Font(None, 50)
    game_over_font = pygame.font.Font(None, 100)
    running = True
    size = (400, 300) #storlek till fontdefintionen
    
#Här kommer alla bilder som används..
    background_img = pygame.image.load('pic/forestbackground.png')
    text_surface = spelfonten.render('Bunny', False, 'Green')
    bunny_img = pygame.image.load('pic/bunni.png')
    arrow_upimg = pygame.image.load('pic/arrow_up1.png')
    arrow_downimg = pygame.image.load('pic/arrow_down1.png')
    arrow_rightimg = pygame.image.load('pic/arrow_right1.png')
    arrow_leftimg = pygame.image.load('pic/arrow_left1.png')
    carrot = pygame.image.load('pic/carrot.png')
    game_over_text = game_over_font.render('GAME OVER', False, 'Red') #många steg här, undrar om jag kan ändra det?
    carrot_y_pos = -100
    gameOver = False


    font = pygame.font.SysFont('Arial', 30)

    arrow_directions = ["up", "down", "left", "right"] #sätter in dem i ett bibliotek så att man enklare kan randomisera de

    arrow_images = {
        'up': arrow_upimg,
        'down': arrow_downimg,
        'left': arrow_leftimg,
        'right': arrow_rightimg
    }
    current_arrows = random.sample(arrow_directions, random.randint(4, 4))

    score = 0
    life = 3
    end_score_font = pygame.font.Font(None, 50)
    end_score_text = end_score_font.render(f'End Score: {score}', False, 'White')
    end_score_rect = end_score_text.get_rect(center=(size[0] // 3, size[1] // 3 + 100))
    backButton = Button(image=None, pos=(750, 420),
                       text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Green")

    while running:
        # Här ritar vi in alla saker plus spellogiken
        while not gameOver:
            MousePosition = pygame.mouse.get_pos() #berättar vad musen är på skärmen

            screen.fill("teal")
            screen.blit(background_img, (0, 0))
            screen.blit(text_surface, (400, 50))
            screen.blit(bunny_img, (450, 300))
            screen.blit(carrot, (400, carrot_y_pos))

            keys_pressed = pygame.key.get_pressed()
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            if len(current_arrows) == 0: #sätter in pialrna på random
                current_arrows = random.sample(arrow_directions, random.randint(4, 4))

            for i, arrow_direction in enumerate(current_arrows):
                arrow_image = arrow_images[arrow_direction]
                arrow_rect = arrow_image.get_rect()
                arrow_rect.center = ((i + 3) * 100, size[1] // 2)
                carrot_y_pos += 3

                if carrot_y_pos >= 350: #moroten stannar med detta
                    carrot_y_pos = 350

                screen.blit(arrow_image, arrow_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and 'up' and current_arrows[0] == 'up' in current_arrows:
                        current_arrows.remove('up')
                    elif event.key == pygame.K_DOWN and 'down' and current_arrows[0] == 'down' in current_arrows:
                        current_arrows.remove('down')
                    elif event.key == pygame.K_LEFT and 'left' and current_arrows[0] == 'left' in current_arrows:
                        current_arrows.remove('left')
                    elif event.key == pygame.K_RIGHT and 'right' and current_arrows[0] == 'right' in current_arrows:
                        current_arrows.remove('right')
                    else:
                        life -= 1

                    if len(current_arrows) == 0:
                        score += 1
                        carrot_y_pos = -50

            if life == 0:
                
                screen.blit(game_over_text, (200, 150))
                      
                score_text = end_score_font.render(f'End Score: {score}', False, 'White')
                score_rect = score_text.get_rect(center=(size[0] // 1, size[1] // 2 + 70))
                screen.blit(score_text, score_rect)

                gameOver = True
                pygame.display.update()
                pygame.time.delay(2000)#här ska en timer in som ska via skärmen en stund innan menyn kommer tillbaka
                main_menu()
            # om jag sätter moroten till att falla så kan man skapa hichsvore på hur länge man klarar sig 
            score_text = font.render(f'Score: {score}', True, (0, 0, 0))
            score_rect = score_text.get_rect(topright=(size[0] - 10, 10))
            screen.blit(score_text, score_rect)

            life_text = font.render(f'Life: {life}', True, (0, 0, 0))
            life_rect = life_text.get_rect(topright=(size[0] + 200, 10))
            screen.blit(life_text, life_rect)

            backButton.changeColor(MousePosition)
            backButton.update(screen)

            pygame.display.flip()
            clock.tick(80) #gick upp från 60 fps då pilarna strulade 

            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
              if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.checkForInput(MousePosition):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        mousePositionOption = pygame.mouse.get_pos()

        SCREEN.fill("white")

        optionText = get_font(15).render("OPTIONS", True, "Black")
        optionsRect = optionText.get_rect(center=(450, 200))
        SCREEN.blit(optionText, optionsRect)

        backbuttonOptions = Button(image=None, pos=(750, 420),
                              text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")

        backbuttonOptions.changeColor(mousePositionOption)
        backbuttonOptions.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbuttonOptions.checkForInput(mousePositionOption):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        menuMousePos = pygame.mouse.get_pos()

        menyText = get_font(30).render("MAIN MENU", True, "#b68f40")
        menyRect = menyText.get_rect(center=(450, 100))

        playButton = Button(image=pygame.image.load("pic/Rect.png"), pos=(450, 180),
                             text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        optionButton = Button(image=pygame.image.load("pic/Rect.png"), pos=(450, 290),
                                text_input="OPTIONS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        quitButton = Button(image=pygame.image.load("pic/Rect.png"), pos=(450, 400),
                             text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(menyText, menyRect)
        playButton.changeColor(menuMousePos)
        playButton.update(SCREEN)

        optionButton.changeColor(menuMousePos)
        optionButton.update(SCREEN)

        quitButton.changeColor(menuMousePos)
        quitButton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    play()
                if optionButton.checkForInput(menuMousePos):
                    options()
                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main_menu()
