import pygame
import random
pygame.init()

#Colors
white= (255,255,255)
red= (255,0,0)
black=(0,0,0)


screen_width=900
screen_height=600

gameWindow=pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_captions("Snakes with Sujal")
pygame.display.update()

exit_game=False
game_over= False
snake_x=45
snake_y=55
snake_size=30
velocity_x=4
velocity_y=4
score=0
init_velocity=5
food_x=random.randint(20,screen_width/2)
food_y=random.randint(20,screen_height/2)
fps=60


clock= pygame.time.Clock()


#CREATING A GAME LOOP
while not exit_game:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            velocity_x=init_velocity
            velocity_y=0
          


        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_RIGHT:
                velocity_x=-init_velocity
                velocity_y=0


        
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                velocity_y=-init_velocity
                velocity_x=0

        
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                velocity_y=init_velocity
                velocity_x=0


        snake_x=snake_x+velocity_x
        snake_y=snake_y+velocity_y                         

                
    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=1
        print("Score:", score * 10)
        food_x=random.randint(20,screen_width/2)
        food_y=random.randint(20,screen_height/2)

    gameWindow.fill(white)    
    pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()    


