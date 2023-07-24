import pygame
import time
import math
import datetime
pygame.init()

start1= datetime.datetime.now()
# Set the dimensions of the screen and the background color
screen_width, screen_height = 1500, 1000
background_color = (0, 0, 0)

# Set the dimensions of the circles and the space between them
circle_radius = 20
circle_space = 30

# Set the number of circles and the time between filling them
num_circles = int(input("Enter the number of circles: "))
fill_time = float(input("Enter the time to fill each circle (in seconds): "))

# Calculate the number of rows and columns to organize the circles
num_columns = min(num_circles, 13)
num_rows = (num_circles - 1) // num_columns + 1

# Set up the screen and the font
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Learning Race")
font = pygame.font.SysFont("Arial", 30)

# Create a list of circles that starts filled with blue
circles = []
for i in range(num_circles):
    row = i // num_columns
    column = i % num_columns
    circle_x = circle_radius + column * (circle_radius * 2 + circle_space)
    circle_y = circle_radius + row * (circle_radius * 2 + circle_space)
    circles.append((circle_x, circle_y, False, False))

# Set the start time for filling the circles
start_time = time.time()

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a circle has been clicked
            pos = pygame.mouse.get_pos()
            for circle in circles:
                circle_x, circle_y, filled, clicked = circle
                distance = ((pos[0] - circle_x) ** 2 + (pos[1] - circle_y) ** 2) ** 0.5
                if distance <= circle_radius and not clicked:
                    circles[circles.index(circle)] = (circle_x, circle_y, True, True)
    
    # Fill the screen with the background color
    screen.fill(background_color)
    
    # Update the circles
    green_circles = 0
    red_circles = 0
    #elapsed_red=0
    for i, circle in enumerate(circles):
        circle_x, circle_y, filled, clicked = circle
        if not filled:
            elapsed_time = time.time() - start_time
            if elapsed_time >= i * fill_time:
                circles[i] = (circle_x, circle_y, True, clicked)
                #elapsed_red+= 1
        if clicked:
            green_circles += 1
        elif filled:
            red_circles += 1
        color = (0, 255, 0) if clicked else (255, 0, 0) if filled else (255, 255, 255)
        pygame.draw.circle(screen, color, (circle_x, circle_y), circle_radius)
    
    # Update the screen with the percentage of green and red circles
    green_percentage = green_circles*100 / num_circles
    red_percentage = round((elapsed_time*100 / (num_circles*fill_time)),1)
    green_text = font.render(f"Green Circles: {green_percentage:.2f}%", True, (0, 255, 0))
    red_text = font.render(f"Red Circles: {red_percentage:.2f}%", True, (255, 0, 0))
    temp=(green_circles*fill_time-math.floor(elapsed_time))/60
    minutes = math.floor(temp)
    seconds = round((temp-minutes)*60,2)
    if temp>0:
        time_text = font.render(f"You have: {minutes} min {seconds} sec", True, (0, 255,0))
    else:
        time_text = font.render(f"You have: {minutes} min {seconds} sec", True, (255,0,0))

    if green_circles>0:
        Estim_finish_time=(elapsed_time/green_circles)*(num_circles-green_circles)
    else:
        Estim_finish_time=(fill_time)*(num_circles-green_circles)
    # get the current time
    now = datetime.datetime.now()

    # add x seconds to the current time
    p = Estim_finish_time # for example, add 60 seconds
    new_time = now + datetime.timedelta(seconds=p)
    plan_time=Estim_finish_time=start1 + datetime.timedelta(seconds=fill_time*num_circles)

    # format the new time as a string
    time_str = new_time.strftime("%H:%M:%S")
    temtime_text = font.render(f"Estimated finishing time: {time_str}", True, (255, 255, 255))

    plan_time_str = plan_time.strftime("%H:%M:%S")
    plan_temtime_text = font.render(f"Planned finishing time: {plan_time_str}", True, (255, 255, 255))
    sum_text = font.render(f"You have finished: {green_circles} out of {num_circles}", True, (255, 255, 255))
    
   
    screen.blit(green_text, (900, 10))
    screen.blit(red_text, (900, 50))
    screen.blit(time_text, (900, 90))
    screen.blit(temtime_text, (900, 130))
    screen.blit(plan_temtime_text, (900, 170))
    screen.blit(sum_text, (900, 210))
    pygame.display.update()

# Quit pygame and exit
pygame.quit()