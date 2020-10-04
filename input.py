import pygame 
import cv2

class input:
    def __init__(self):
        pygame.init()

        self.WHITE = (255,255,255)
        self.BLUE = (0,50,100)
        self.BLACK = (0,0,0)

        self.image = "create_grid/grid.png"
        img = cv2.imread(self.image)
        height, width = img.shape[:2]

        WINDOW_SIZE = [int(width), int(height)]
        self.display = pygame.display.set_mode(WINDOW_SIZE) 
        bg = pygame.image.load("create_grid/grid.png")
        self.display.blit(bg, (0, 0))

        pygame.display.set_caption("Coordinate Input")

        self.clock = pygame.time.Clock()

        self.zero = [90, 420]

        self.inputArr = []

    def getCoordinates(self):
        done=False
        while not done:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    done = True  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    if (x-self.zero[0]) > 0: x_coord = int((x-self.zero[0])/24) + 1 
                    else: x_coord = 0
                    if (self.zero[1]-y) > 0: y_coord = int((self.zero[1]-y)/18) + 1
                    else: y_coord = 0    
                    inp = [x, y]
                    pygame.draw.circle(self.display, self.BLUE, inp, 5)
                    self.inputArr.append([x_coord, y_coord])

            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()
        return self.inputArr

    def quitInterface(self):
        pygame.quit()
        quit()

