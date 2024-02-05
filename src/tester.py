import pygame  # importera pygame
import random
# pygame setup
pygame.init()

# skapa skärmen
screen = pygame.display.set_mode((900, 500))  # (widh,height)
clock = pygame.time.Clock()  # hjälper till med tid och kontrollera framerate
test_font = pygame.font.Font(None, 50)
game_over_font = pygame.font.Font(None,100)
running = True
size = (400, 300)


background_img = pygame.image.load('pic/forestbackground.png')
text_surface = test_font.render('Bunny', False, 'Green')
bunny_img = pygame.image.load('pic/bunni.png')
arrow_upimg = pygame.image.load('pic/arrow_up1.png')
arrow_downimg = pygame.image.load('pic/arrow_down1.png')
arrow_rightimg = pygame.image.load('pic/arrow_right1.png')
arrow_leftimg = pygame.image.load('pic/arrow_left1.png')
carrot= pygame.image.load('pic/carrot.png')
game_over = game_over_font.render('GAME OVER', False, 'Red') # ska se om jag får in en bild 
carrot_y_pos=-50

# Define arrow directions
arrow_directions = ["up", "down", "left", "right"]
# Set up the font
font = pygame.font.SysFont('Arial', 30)

arrow_cue = random.shuffle(arrow_directions)
arrow_images = {
    'up': arrow_upimg,
    'down': arrow_downimg,
    'left': arrow_leftimg,
    'right': arrow_rightimg
}
current_arrows = random.sample(arrow_directions, random.randint(4, 4))
#    Display the current arrow combination
score = 0
life = 3
# Behöver få pilarna att visas på random
while running:
    # ritar alla elemlent
    # upptaderar allting

    screen.fill("teal")  # färg på skärmen
    screen.blit(background_img, (0, 0))  # lägga till bilder
    screen.blit(text_surface, (400, 50))  # texten på skärmen
    screen.blit(bunny_img, (450, 300))  # lägga till bilder
    screen.blit(carrot,(400,carrot_y_pos))
    
    keys_pressed = pygame.key.get_pressed()

    # Check if the player has finished the current set of arrows
    if len(current_arrows) == 0:
        # Genererar ett set pilar
        current_arrows = random.sample(arrow_directions, random.randint(4, 4))
    for i, arrow_direction in enumerate(current_arrows):
        arrow_image = arrow_images[arrow_direction]
        arrow_rect = arrow_image.get_rect()
        arrow_rect.center = ((i+3)*100, size[1]//2)
        carrot_y_pos+=2

        if carrot_y_pos >= 350: carrot_y_pos = 350
            
        screen.blit(arrow_image, arrow_rect)

       
    for event in pygame.event.get():  # denna del ger mig alla event
        if event.type == pygame.QUIT:  # pygame.QUIT käner när användaren trycker x på skärmen man skapat
            running = False

        elif event.type == pygame.KEYDOWN:
            # Kollar om pilen jag trycker på matchar den första pilen
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

            # kollar om pilarna är bora alla 4 å uppdatera poängen
            if len(current_arrows) == 0:
                score += 1
                carrot_y_pos = -50

    if life == 0:
                screen.blit(game_over, (200, 150))

               # texten på skärmen  # vill sätta in en game over här och tillbaka till meny
          
    # Visar poängen
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    score_rect = score_text.get_rect(topright=(size[0]-10, 10))
    screen.blit(score_text, score_rect)
    # visar liven
    life_text = font.render(f'life: {life}', True, (0, 0, 0))
    life_rect = life_text.get_rect(topright=(size[0]+200, 10))
    screen.blit(life_text, life_rect)

    pygame.display.flip()
    clock.tick(60)  # kallar på funktionen och sätter den till 60 FPS

pygame.quit()
