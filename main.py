import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 800
BOX_HEIGHT = 80
BOX_WIDTH = 80

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('LetsPlayChess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 100


############### necessary datas ###########################


white_pieces=['rock','knight','bishop','king','queen','bishop','knight','rock','pawn','pawn','pawn','pwan','pawn','pawn','pawn','pwan']
white_locations=[(0 ,0 ),(1 ,0 ),(2 ,0 ),(3 , 0),(4 , 0),(5 ,0 ),(6 , 0),(7 ,0 ),
                 ( 0,1 ),(1 ,1 ),(2 ,1 ),(3 , 1),(4 , 1),(5 , 1),(6 , 1),(7 , 1)]
black_pieces=['rock','knight','bishop','king','queen','bishop','knight','rock','pawn','pawn','pawn','pwan','pawn','pawn','pawn','pwan']
black_locations=[(0 ,7 ),( 1, 7),(2 , 7),(3 ,7 ),(4 , 7),(5 ,7 ),(6 ,7 ),( 7,7 ),
                   ( 0,6 ),(1 ,6 ),(2 ,6 ),(3 , 6),(4 , 6),(5, 6),(6 , 6),(7 , 6)]
captured_white=[]
captured_black=[]
#####################################################################
turn_step=0
selection =100
valid_moves=[]
#loadign images#######################################################################
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images=[white_pawn, white_queen, white_king, white_knight, white_rook,white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list=['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']


##################### functions ###################################################



def Board_draw():
    for i in range(8):
        for j in range(8):
            row = i
            col = j
            color = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * 85, i * 85, 85, 85))
            pygame.draw.rect(screen,'gold',[0,680,680 ,120],5)
            pygame.draw.rect(screen,'gold',[680,0,320 ,680],5)
            pygame.draw.rect(screen,'gold',[680,680,320 ,120],5)
####################  main ####################################

run = True
while run:
    timer.tick(fps)
    screen.fill((50, 50, 50))  

    Board_draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()







