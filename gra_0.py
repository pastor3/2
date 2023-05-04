import pygame
import random
import pygame.mixer
import os

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()

color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red
color6 = pygame.Color(0, 255, 0)       # green
color7 = pygame.Color(0, 0, 255)       #blue
color8 = pygame.Color(255, 255, 0)     #yellow
color9 = pygame.Color(128, 0, 128)     #purple

widht = 800
hight = 600

widht_pl = 70
hight_pl = 50
boobl_x = 360
boobl_y = 450
enemy1_x = 810
enemy1_y = (random.randint(0, 600))
screen = pygame.display.set_mode((widht,hight))
pygame.display.set_caption("Страшна гра")
icon = pygame.image.load("Images\\player_icon_r2.png").convert_alpha()
pygame.display.set_icon(icon)



player_icon_r2 = pygame.image.load("Images\\player_icon_r2.png").convert_alpha()
player_r = pygame.transform.scale(player_icon_r2,(widht_pl,hight_pl))
player_icon_l2 = pygame.image.load("Images\\player_icon_l2.png").convert_alpha()
player_l = pygame.transform.scale(player_icon_l2,(widht_pl,hight_pl))

life_icon_heart = 2
life_icon = pygame.transform.scale(player_icon_l2,(35,25))

weart1 = life_icon
weart2 = life_icon
weart3 = life_icon


enemy1 = pygame.image.load("Images\\1075.png").convert_alpha()
enemy_1 = pygame.transform.scale(enemy1,(70,50))
enemy2 = pygame.image.load("Images\\1054.png").convert_alpha()
enemy_2 = pygame.transform.scale(enemy2,(70,50))

enemy1_list = []

bg = pygame.image.load("Images\\vore.png").convert_alpha()
bg = pygame.transform.scale(bg,(widht,hight))
screen.blit(bg,(0,0))
hearts = [weart1,weart2,weart3]
hearts_count = 0

panel = pygame.Surface((800,50))
panel.fill(color6)
panel.blit(hearts[0],(662,15))
panel.blit(hearts[1],(708,15))
panel.blit(hearts[2],(754,15))
kill = 0
# виведення кількості очок на екран під час гри
score_font = pygame.font.Font(None, 36)  # задаємо шрифт для тексту
score_text = score_font.render(f"Score: {kill}", True, (255, 255, 255))  # формуємо текст з кількістю очок
panel.blit(score_text, (20, 10))  # відображаємо текст в лівому верхньому кутку


def open_GameOver():
    GameOver = pygame.display.set_mode((800,600))
    GameOver.fill(color1)

    # ініціалізація шрифту
    pygame.font.init()
    font = pygame.font.SysFont(None, 40)

    # текст надпису "GAME OVER"
    game_over = font.render("GAME OVER", False, color4)
    GameOver.blit(game_over, (300, 200))

    # кнопка рестарту
    restart_button_width = 200
    restart_button_height = 50
    restart_rect = pygame.Rect((800 - restart_button_width) // 2, 400, restart_button_width, restart_button_height)
    restart_button = font.render("Restart", True, (0, 0, 0))
    pygame.draw.rect(GameOver, color2, restart_rect)
    GameOver.blit(restart_button, (restart_rect.x + (restart_button_width - restart_button.get_width()) // 2, restart_rect.y + (restart_button_height - restart_button.get_height()) // 2))

    pygame.display.flip()




count = 3            

life = 0
anime_count = 0
bg_x = 0

#shwim_r = [
    
player_speed = 10
player_x = 50
player_y = 350
pygame.display.flip()

#bg_sound1 = pygame.mixer.Sound("Sounds\\8-bit_dendy_-_alien_3_rock_cover_(zf.fm).mp3")
bg_sound2 = pygame.mixer.Sound("Sounds\\ShidSoncja.mp3")
sound1 = pygame.mixer.Sound("Sounds\\sfx-17.mp3")
bg_sound4 = pygame.mixer.Sound("Sounds\\1prince1.mp3")
bg_sound5 = pygame.mixer.Sound("Sounds\\5-swimming-around.mp3")
sound2 = pygame.mixer.Sound("Sounds\\sfx-16.mp3")



#
#bg_sound2.play()
bg_sound4.play()
#bg_sound5.play()






boobl_timer = pygame.USEREVENT + 1
pygame.time.set_timer(boobl_timer, 2000)

running = True
game_over = False
while running:
    if not game_over:
    
        keys = pygame.key.get_pressed()
        pygame.display.flip()
        screen.blit(bg,(bg_x,0))
        screen.blit(bg,(bg_x+800,0))
        screen.blit(enemy_1,(810,enemy1_y))
        screen.blit(panel,(0,0))
        pygame.display.flip()
        
        if keys[pygame.K_a]:
            screen.blit(player_l,(player_x,player_y))
            
        else:        
            screen.blit(player_r,(player_x,player_y))
   
      
    
    
        if keys[pygame.K_d] and player_x < (widht - widht_pl):
            player_x += player_speed
        elif  keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        elif  keys[pygame.K_w] and player_y > 0:
            player_y -= player_speed
        elif  keys[pygame.K_s] and player_y < (hight - hight_pl):
            player_y += player_speed
        pygame.display.flip()      
                
                
        if anime_count == 2:
            anime_count = 0
        else:   
            anime_count += 1
               
            
            
                    
        bg_x -= 2
        if bg_x == -800:
            bg_x = 0
        boobl_y -= 10 
        if enemy1_list:
            for (i, el) in enumerate(enemy1_list):
                pygame.display.flip()
                screen.blit(enemy_1,el)
    
                el.x -= 15
                player_rect = player_r.get_rect(topleft = (player_x, player_y))
                enemy1_rect1 = enemy_1.get_rect(topleft = (el.x,el.y))
                if player_rect.colliderect(enemy1_rect1):
                    sound1.play()  
                    enemy1_list.pop(i)
    
    
    
                if el.x < -70:
                    if life < count:
                        
                                            
                        life += 1
                        sound2.play()
                        hearts.pop(life_icon_heart)
                        enemy1_list.pop(i)
                        life_icon_heart -= 1
                       
                    if life == 3:
                        game_over = True
                
                        if game_over:
                            pygame.mixer.init()
                            bg_sound4.stop()
                            open_GameOver()
                
                
    clock.tick(20)                   
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == boobl_timer:
            enemy1_list.append(enemy1.get_rect(topleft = (810,(random.randint(0, 550)))))
                
        
                        
            
            
            
                
                
                
 