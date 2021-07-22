import pygame, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
random_food_x = int((random.randrange(0, frame_size_x));
random_food_y = int((random.randrange(0, frame_size_y));                    
food_pos = [random_food_x,random_food_y]
food_spawn = False

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()




def check_for_events():
          
                    
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """

     for i in pygame.event.get():
        if event.type == pygame.Quit:
            sys.exit()
        else
            continue
                    
def update_snake():
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    
    global direction,x,y,score
    if event.type == K_RIGHT:
        x = 5
    elif event.type == K_LEFT
        x = -5
    elif event.type == K_UP:
        y = 5
    elif event.type == K_DOWN
        y = -5
                    




    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    





    # End the game if the snake collides with the wall or with itself. 
    






def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
                    
    pygame.draw.circle(game_window,color=red,center=random_food_x,radius=5)
    pygame.display.update()                




def show_score(pos, color, font, size):
                    
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
      ac_score = "SCORE : " + score             
      display_message(str(ac_score),size=16)






def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    update_snake(5)
    game_window.fill((2,1,3),(0,1,2))
    show_score([20,20], , 16)





def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    display_message([100,100],"Try Again",,)
    show_score([200,100],,)
    pygame.display.update()
                   





# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    display_message([200,200],"Press Enter to play again or Press ESC to quit the game", , )
    pygame.display.update()
    show_score()
    pygame.display.update()
    for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESC:
                    pygame.quit()
                elif event.key==pygame.K_Enter:
                    continue
    

    # To set the speed of the screen
    fps_controller.tick(25)