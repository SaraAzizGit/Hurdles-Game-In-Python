import pygame

pygame.init()

# Game Screen Display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Night RiderZ")
icon = pygame.image.load("Icon.jpeg")
pygame.display.set_icon(icon)

# Music
pygame.mixer.music.load("Background.wav")
pygame.mixer.music.play(-1)

# Images - Background, Ground, Rider and Hurdles
background = pygame.image.load("Background.jpeg")
background = pygame.transform.scale(background, (800, 450))
ground = pygame.image.load("Ground.jpeg")
rider = pygame.image.load("Rider.png")
car1 = pygame.image.load("Car1.png")
car1 = pygame.transform.scale(car1, (200, 80))
car2 = pygame.image.load("Car2.png")
car2 = pygame.transform.scale(car2, (200, 80))
car3 = pygame.image.load("Car3.png")
car3 = pygame.transform.scale(car3, (200, 80))
car4 = pygame.image.load("Car4.png")
car4 = pygame.transform.scale(car4, (200, 80))
car5 = pygame.image.load("Car5.png")
car5 = pygame.transform.scale(car5, (200, 80))
car6 = pygame.image.load("Car6.png")
car6 = pygame.transform.scale(car6, (200, 80))

# Game Constants
font = pygame.font.Font('freesansbold.ttf', 20)
crash_font = pygame.font.Font('freesansbold.ttf', 50)
fps = 60
timer = pygame.time.Clock()
white = (255, 255, 255)
blue = (0, 0, 42)

# Game Variables
instruction = True
active = False
replay = False
score = 0
highest_score = 0

# For Collisions
rider_rect = rider.get_rect()
car1_rect = car1.get_rect()
car2_rect = car2.get_rect()
car3_rect = car3.get_rect()
car4_rect = car4.get_rect()
car5_rect = car5.get_rect()
car6_rect = car6.get_rect()

# Movement of hurdles
car1X = 1000
carY = 340
carX_change = 10
car1_rect.x = car1X
car1_rect.y = carY
car2X = car1X + 750
car2_rect.x = car2X
car2_rect.y = carY
car3X = car1X + 1500
car3_rect.x = car3X
car3_rect.y = carY
car4X = car1X + 2250
car4_rect.x = car4X
car4_rect.y = carY
car5X = car1X + 3000
car5_rect.x = car5X
car5_rect.y = carY
car6X = car1X + 3750
car6_rect.x = car6X
car6_rect.y = carY

# Placement and Jumping of Rider
riderX = 30
riderY = 300
riderY_change = 0
gravity = 1
rider_rect.x = riderX
rider_rect.y = riderY


def scoring():
    global score, game_speed, carX_change
    score += 0.1
    score_text = font.render("Score: " + str(int(score)), True, white)
    screen.blit(score_text, (680, 40))
    if score % 100 == 0:
        game_speed += 1
        carX_change += 1


def high_score():
    global score, highest_score
    highest_score_text = font.render("Highest Score: " + str(int(highest_score)), True, white)
    screen.blit(highest_score_text, (490, 40))


# Movement of Ground
game_speed = 10

ground = pygame.transform.scale(ground, (1280, 220))
groundX = 0
ground_rect = ground.get_rect(center=(640, 400))

# Infinite While Loop
running = True
while running:
    timer.tick(fps)
    screen.blit(background, (0, 0))
    screen.blit(ground, (groundX, 395))
    screen.blit(ground, (groundX + 1280, 395))
    screen.blit(rider, rider_rect)
    high_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and instruction is True and active is False and replay is False:
                instruction = False
                active = True

            if event.key == pygame.K_SPACE and riderY_change == 0 and active is True and instruction is False and\
                    replay is False:
                riderY_change = 25

            if event.key == pygame.K_SPACE and replay is True and instruction is False and active is False:
                instruction = True
                replay = False

    if instruction is True and active is False and replay is False:
        instruction_text1 = font.render("Instructions:", True, white)
        screen.blit(instruction_text1, (350, 60))
        instruction_text2 = font.render("Press Space to Jump", True, white)
        screen.blit(instruction_text2, (315, 90))
        instruction_text3 = font.render("Avoid Crashing With Any Vehicle", True, white)
        screen.blit(instruction_text3, (260, 120))
        instruction_text4 = font.render("Press Space to Continue", True, white)
        screen.blit(instruction_text4, (295, 200))

    if active is True and instruction is False and replay is False:
        if riderY_change > 0 or rider_rect.y < 300:
            rider_rect.y -= riderY_change
            riderY_change -= gravity
        if rider_rect.y > 300:
            rider_rect.y = 300
        if rider_rect.y == 300 and riderY_change < 0:
            riderY_change = 0

        groundX -= game_speed
        if groundX <= -1280:
            groundX = 0

        car1_rect.x -= carX_change
        car2_rect.x -= carX_change
        car3_rect.x -= carX_change
        car4_rect.x -= carX_change
        car5_rect.x -= carX_change
        car6_rect.x -= carX_change
        screen.blit(car1, (car1_rect.x, car1_rect.y))
        screen.blit(car2, (car2_rect.x, car2_rect.y))
        screen.blit(car3, (car3_rect.x, car3_rect.y))
        screen.blit(car4, (car4_rect.x, car4_rect.y))
        screen.blit(car5, (car5_rect.x, car5_rect.y))
        screen.blit(car6, (car6_rect.x, car6_rect.y))

        if rider_rect.colliderect(car1_rect):
            crash = pygame.mixer.Sound("Crash.wav")
            crash.play()
            active = False
            replay = True

        if rider_rect.colliderect(car2_rect):
            crash = pygame.mixer.Sound("Crash.wav")
            crash.play()
            active = False
            replay = True

        if rider_rect.colliderect(car3_rect):
            crash = pygame.mixer.Sound("Crash.wav")
            crash.play()
            active = False
            replay = True

        if rider_rect.colliderect(car4_rect):
            crash = pygame.mixer.Sound("Crash.wav")
            crash.play()
            active = False
            replay = True

        if rider_rect.colliderect(car5_rect):
            crash = pygame.mixer.Sound("Crash.wav")
            crash.play()
            active = False
            replay = True

        if rider_rect.colliderect(car6_rect):
            crash = pygame.mixer.Sound("Crash.wav")
            crash.play()
            active = False
            replay = True

        if car1_rect.x <= -4000:
            car1_rect.x = 800
        if car2_rect.x <= -4000:
            car2_rect.x = 800
        if car3_rect.x <= -4000:
            car3_rect.x = 800
        if car4_rect.x <= -4000:
            car4_rect.x = 800
        if car5_rect.x <= -4000:
            car5_rect.x = 800
        if car6_rect.x <= -4000:
            car6_rect.x = 800

        scoring()

    if replay is True and instruction is False and active is False:
        replay_text = crash_font.render("You Crashed!", True, white)
        screen.blit(replay_text, (245, 200))
        continue_text = font.render("Press Space to Continue", True, white)
        screen.blit(continue_text, (290, 280))
        if score > highest_score:
            highest_score = score
        score = 0
        car1X = 1000
        carY = 340
        carX_change = 10
        car1_rect.x = car1X
        car1_rect.y = carY
        car2X = car1X + 750
        car2_rect.x = car2X
        car2_rect.y = carY
        car3X = car1X + 1500
        car3_rect.x = car3X
        car3_rect.y = carY
        car4X = car1X + 2250
        car4_rect.x = car4X
        car4_rect.y = carY
        car5X = car1X + 3000
        car5_rect.x = car5X
        car5_rect.y = carY
        car6X = car1X + 3750
        car6_rect.x = car6X
        car6_rect.y = carY
        riderX = 30
        riderY = 300
        riderY_change = 0
        rider_rect.x = riderX
        rider_rect.y = riderY

    pygame.display.update()
