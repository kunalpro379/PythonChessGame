import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 800
BOX_HEIGHT = 80
BOX_WIDTH = 80

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('LetsPlayChess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 45)
timer = pygame.time.Clock()
fps = 100
selection=1000


############### necessary datas ###########################


white_pieces=['rock','knight','bishop','king','queen','bishop','knight','rock','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations=[(0 ,0 ),(1 ,0 ),(2 ,0 ),(3 , 0),(4 , 0),(5 ,0 ),(6 , 0),(7 ,0 ),
                 ( 0,1 ),(1 ,1 ),(2 ,1 ),(3 , 1),(4 , 1),(5 , 1),(6 , 1),(7 , 1)]
black_pieces=['rock','knight','bishop','king','queen','bishop','knight','rock','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations=[(0 ,7 ),( 1, 7),(2 , 7),(3 ,7 ),(4 , 7),(5 ,7 ),(6 ,7 ),( 7,7 ),
                   ( 0,6 ),(1 ,6 ),(2 ,6 ),(3 , 6),(4 , 6),(5, 6),(6 , 6),(7 , 6)]
captured_white=[]
captured_black=[]
#####################################################################
turn_step=1
selection =100
valid_moves=[]
###################### loadign images #######################################################################
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (72, 72))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king,(72, 72))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook,(72, 72))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop,(72, 72))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight,(72, 72))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (72, 72))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king,(72, 72))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook,(72, 72))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop,(72, 72))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (72, 72))
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
piece_list=['pawn', 'queen', 'king', 'knight', 'rock', 'bishop']


##################### functions ###################################################



def Board_draw():
    for i in range(8):
        for j in range(8):
            row = i
            col = j
            color = "brown" if (i + j) % 2 == 0 else "white"
            pygame.draw.rect(screen, color, (j * 85, i * 85, 85, 85))
            pygame.draw.rect(screen,'gold',[0,680,680 ,120],5)
            pygame.draw.rect(screen,'gold',[680,0,320 ,680],5)
            pygame.draw.rect(screen,'gold',[680,680,320 ,120],5)

            status_text=['White: Select a Piece to move','White: Select a Destination!',
                         'Black: Select a Piece ato Move','Black: Select a Destination']
            
            screen.blit(big_font.render(status_text[turn_step],True,'white'), (20,710))

def pieces():
    # Draw white pieces
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 85, white_locations[i][1] * 85))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 85, white_locations[i][1] * 85))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'green', [white_locations[i][0] * 85 + 2, white_locations[i][1] * 85 + 2, 80, 80], 4)

    # Draw black pieces
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 85, black_locations[i][1] * 85))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 85, black_locations[i][1] * 85))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'green', [black_locations[i][0] * 85 + 2, black_locations[i][1] * 85 + 2, 80, 80], 4)













####################  main ####################################

run = True
while run:
    timer.tick(fps)
    screen.fill((50, 50, 50))  

    Board_draw()
    pieces()


############## Event Handling  ####$$$$$$$$$$$$
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type==pygame.MOUSEBUTTONDOWN & event.button==1:
            Xcord=event.pos[0]
            Ycord=event.pos[1]
        ClikCord=(Xcord, Ycord)
        if turn_step<=1:
            if ClikCord in white_locations:
                    selection=white_locations(ClikCord)
                    if turn_step==0:
                        turn_step=1
            if ClikCord in valid_moves and selection!=1000:
                white_locations[selection]=ClikCord
                if ClikCord in black_locations:
                    black_pieces=black_locations.index(ClikCord)



    pygame.display.flip()

pygame.quit()







