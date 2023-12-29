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
# selection=60


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

valid_moves=[]
###################### loadign images #######################################################################
black_queen = pygame.image.load('assets/images/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (72, 72))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black_king.png')
black_king = pygame.transform.scale(black_king,(72, 72))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black_rook.png')
black_rook = pygame.transform.scale(black_rook,(72, 72))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop,(72, 72))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black_knight.png')
black_knight = pygame.transform.scale(black_knight,(72, 72))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (72, 72))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white_king.png')
white_king = pygame.transform.scale(white_king,(72, 72))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white_rook.png')
white_rook = pygame.transform.scale(white_rook,(72, 72))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop,(72, 72))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (72, 72))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white_pawn.png')
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
selection=1000

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
        x, y = white_locations[i][0] * 85, white_locations[i][1] * 85

        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (x, y))
        else:
            screen.blit(white_images[index], (x, y))

        # Draw border around selected piece
        if turn_step < 2 and selection == i:
            pygame.draw.rect(screen, (0, 255, 0), [x - 5, y - 5, 95, 95], 4)

    # Draw black pieces
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        x, y = black_locations[i][0] * 85, black_locations[i][1] * 85

        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (x, y))
        else:
            screen.blit(black_images[index], (x, y))

        if turn_step >= 2 and selection == i:
            pygame.draw.rect(screen, (0, 255, 0), [x - 5, y - 5, 95, 95], 4)

            def cheak_options():
                pass


"""
def Board_draw():
    for i in range(8):
        for j in range(8):
            color = "brown" if (i + j) % 2 == 0 else "white"
            pygame.draw.rect(screen, color, (j * 85, i * 85, 85, 85))
            pygame.draw.rect(screen, 'gold', [0, 680, 680, 120], 5)
            pygame.draw.rect(screen, 'gold', [680, 0, 320, 680], 5)
            pygame.draw.rect(screen, 'gold', [680, 680, 320, 120], 5)

            status_text = ['White: Select a Piece to move', 'White: Select a Destination!',
                           'Black: Select a Piece to Move', 'Black: Select a Destination']

            screen.blit(big_font.render(status_text[turn_step], True, 'white'), (20, 710))


def draw_piece(image, x, y, condition):
    screen.blit(image, (x, y))
    if condition:
        pygame.draw.rect(screen, (0, 255, 0), [x - 5, y - 5, 95, 95], 4)


def pieces():
    for pieces, locations, images, step_condition in [
        (white_pieces, white_locations, white_images, turn_step < 2),
        (black_pieces, black_locations, black_images, turn_step >= 2)
    ]:
        for i, (piece, location) in enumerate(zip(pieces, locations)):
            index = piece_list.index(piece)
            x, y = location[0] * 85, location[1] * 85
            draw_piece(images[index] if piece != 'pawn' else (white_pawn if step_condition else black_pawn), x, y,
                       selection == i and step_condition)

"""
def cheak_options(pieces,locations,turn):
        moves_list=[]
        all_moves_list=[]
        for i in range (pieces):
                    location=locations[i]
                    piece=pieces[i]
                    if piece =='pawn':
                        moves_list=cheak_pawn(location,turn)
                    elif piece=='knight':
                        moves_list=cheak_knight(location,turn)
                    elif piece=='bishop':
                        moves_list=cheak_bishop(location,turn)
                    elif piece=='rock':
                        moves_list=cheak_rock(location,turn)
                    elif piece=='queen':
                        moves_list=cheak_queen(location,turn)
                    elif piece=='king':
                        moves_list=cheak_king(location,turn)
                    all_moves_list.append(moves_list)
                    return all_moves_list
        
        def cheak_bishop(position,color):
            pass
        
        def cheak_king():
            pass

        def cheak_knight():
            pass

        def cheak_pawn(position,color):
            moves_list=[]
            if color =='white':
                # position[o]=x  position[1]=y
                if(position[0], position[0]+1) not in white_locations and (position[0],position[1]+1)not in black_locations and position[1]<7:
                            moves_list.append(position[0],position[1]+1)
                if(position[0], position[1]+2) not in white_locations and ()not in black_locations and position[1]<7:
                            moves_list.append(position[0],position[1]+1)
                if(position[0], position[0]+1) not in white_locations and ()not in black_locations and position[1]<7:

                if(position[0], position[0]+1) not in white_locations and ()not in black_locations and position[1]<7:

        def cheak_queen():
            pass

        def cheak_rock():
            pass

        
black_options = cheak_options(black_pieces, black_locations, 'black')
white_options = cheak_options(white_pieces, white_locations, 'white')


           
############## Event Handling  ####$$$$$$$$$$$$
run=True
while run:
    timer.tick(fps)
    screen.fill((50, 50, 50))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left click
            Xcord = event.pos[0] // 85   # x and y cord of mouse
            Ycord = event.pos[1] // 85
            ClikCord = (Xcord, Ycord)

            if turn_step <= 1:
                if ClikCord in white_locations:
                    selection = white_locations.index(ClikCord)
                    if turn_step == 0:
                        turn_step = 1
                if ClikCord in valid_moves and selection != 1000:
                    white_locations[selection] = ClikCord
                    if ClikCord in black_locations:
                        black_piece = black_locations.index(ClikCord)
                        captured_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = cheak_options(black_pieces, black_locations, 'black')
                    white_options = cheak_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 1000
                    valid_moves = []

            if turn_step > 1:
                if ClikCord in black_locations:
                    selection = black_locations.index(ClikCord)
                    if turn_step == 2:
                        turn_step = 3
                if ClikCord in valid_moves and selection != 1000:
                    black_locations[selection] = ClikCord
                    if ClikCord in white_locations:
                        white_piece = white_locations.index(ClikCord)
                        captured_white.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = cheak_options(black_pieces, black_locations, 'black')
                    white_options = cheak_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 1000
                    valid_moves = []

    # Draw the chessboard and pieces
    Board_draw()
    pieces()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()