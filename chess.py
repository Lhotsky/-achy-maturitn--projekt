import pygame
import sqlite3
# python -c "import sqlite3; print(sqlite3.sqlite_version)"
pygame.init()
screen = pygame.display.set_mode([1000,800])
pygame.display.set_caption('checkers game')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
mid_font = pygame.font.Font('freesansbold.ttf', 40)
mainvoidtime = pygame.time.Clock()
fps = 60
conn = sqlite3.connect("game_results.db")
cursor = conn.cursor()
def resetgame():
    global half_of_draw_rule, draw_rule, counter, game_drawn, winner
    global time_w_secs, time_b_secs, time_w, time_b
    global castle_king_w, castle_king_b, castle_queenside_w, castle_kingside_b
    global castle_kingside_w, castle_queenside_b, en_passant_b, en_passant_w
    global enpassantfileb, enpassantfilew, white_pieces, white_locals
    global black_pieces, black_locals, taken_pieces_white, taken_pieces_black
    global whom_turn, selected_piece, legal_moves, legal_options
    global white_moves, black_moves,rightclicklist
    global game_over,white_moves, black_moves,rightclicklist
    global time_w_secs, time_b_secs, time_w, time_b

    half_of_draw_rule = 0  # 50-move draw rule
    draw_rule = 0
    counter = 0  # Check animation
    game_drawn = False  # 1 if the game is declared a draw
    winner = ''
    game_over = False
    time_w_secs = 600  # White's time in seconds
    time_b_secs = 600  # Black's time in seconds
    time_w = 0  # White's time in milliseconds
    time_b = 0  # Black's time in milliseconds

    castle_king_w = True # logika pro rošádu
    castle_king_b = True
    castle_queenside_w = True
    castle_kingside_b = True
    castle_kingside_w = True
    castle_queenside_b = True  

    en_passant_b = False # en passant logika
    en_passant_w = False
    enpassantfileb = 9
    enpassantfilew = 9

    white_pieces = ['rook', 'rook', 'honse', 'bishop', 'queen', 'king', 'bishop', 'honse', # základní pozice
                    'pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp']
    white_locals = [(0, 7), (7, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

    black_pieces = ['rook', 'rook', 'bishop', 'queen', 'king', 'bishop', 'honse', 'honse',
                    'pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp']
    black_locals = [(0, 0), (7, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (1, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

    taken_pieces_white = []
    taken_pieces_black = []

    whom_turn = 0  # 0 = White's turn, 1 = Black's turn
    selected_piece = 16  # No piece selected initially
    legal_moves = []
    legal_options = []
    rightclicklist = []
    white_moves = []
    black_moves = []
resetgame()
black_pp = pygame.transform.scale(pygame.image.load('assets/black_pp.png'), (100, 100))
black_honse = pygame.transform.scale(pygame.image.load('assets/black_horse.png'), (100, 100))
black_bishop = pygame.transform.scale(pygame.image.load('assets/black_bishop.png'), (100, 100))
black_rook = pygame.transform.scale(pygame.image.load('assets/black_rook.png'), (100, 100))
black_queen = pygame.transform.scale(pygame.image.load('assets/black_queen.png'), (100, 100))
black_king = pygame.transform.scale(pygame.image.load('assets/black_king.png'), (100, 100))

white_pp = pygame.transform.scale(pygame.image.load('assets/white_pp.png'), (100, 100))
white_honse = pygame.transform.scale(pygame.image.load('assets/white_horse.png'), (100, 100))
white_bishop = pygame.transform.scale(pygame.image.load('assets/white_bishop.png'), (100, 100))
white_rook = pygame.transform.scale(pygame.image.load('assets/white_rook.png'), (100, 100))
white_queen = pygame.transform.scale(pygame.image.load('assets/white_queen.png'), (100, 100))
white_king = pygame.transform.scale(pygame.image.load('assets/white_king.png'), (100, 100))

backboard = pygame.transform.scale(pygame.image.load('assets/backboard.png'), (800, 800))
bookshelf1 = pygame.transform.scale(pygame.image.load('assets/kebab.png'), (200, 800))
bookshelf3 = pygame.transform.scale(pygame.image.load('assets/EEE.png'), (400, 200))
bob = pygame.transform.scale(pygame.image.load('assets/bob.png'), (400, 200))
white_ring = pygame.transform.scale(pygame.image.load('assets/ring_W.png'), (100, 100))
black_ring = pygame.transform.scale(pygame.image.load('assets/ring_B.png'), (100, 100))
black_selected_piece_icon = pygame.transform.scale(pygame.image.load('assets/whitesellection.png'), (100, 100))
white_selected_piece_icon = pygame.transform.scale(pygame.image.load('assets/blacksellection.png'), (100, 100))

captured_black_pp = pygame.transform.scale(black_pp, (40, 40))
captured_black_honse = pygame.transform.scale(black_honse, (40, 40))
captured_black_bishop = pygame.transform.scale(black_bishop, (40, 40))
captured_black_rook = pygame.transform.scale(black_rook, (40, 40))
captured_black_queen = pygame.transform.scale(black_queen, (40, 40))
captured_black_king = pygame.transform.scale(black_king, (40, 40))

captured_white_pp = pygame.transform.scale(white_pp, (40, 40))
captured_white_honse = pygame.transform.scale(white_honse, (40, 40))
captured_white_bishop = pygame.transform.scale(white_bishop, (40, 40))
captured_white_rook = pygame.transform.scale(white_rook, (40, 40))
captured_white_queen = pygame.transform.scale(white_queen, (40, 40))
captured_white_king = pygame.transform.scale(white_king, (40, 40))

white_images = [white_pp, white_honse, white_bishop, white_rook, white_queen, white_king]  
black_images = [black_pp, black_honse, black_bishop, black_rook, black_queen, black_king]  
taken_w = [captured_white_pp, captured_white_honse, captured_white_bishop, captured_white_rook, captured_white_queen, captured_white_king]  
taken_b = [captured_black_pp, captured_black_honse, captured_black_bishop, captured_black_rook, captured_black_queen, captured_black_king]  
piece_types = ['pp', 'honse', 'bishop', 'rook', 'queen', 'king']  

def draw_board():
    screen.blit(backboard, (0, 0)) # board
    screen.blit(bookshelf1, (800, 0))
    
    screen.blit(font.render(f'čas bílý:{time_w_secs} ', True, 'white'), (830, 280)) # clock
    screen.blit(font.render(f'čas černý:{time_b_secs} ' , True, 'white'), (830, 250))
    pygame.draw.rect(screen,(74, 42, 9),[800,0,200,100],10) 
    pygame.draw.rect(screen,(74, 42, 9),[800,100,200,100],10)

    half_of_draw_rule = draw_rule // 2 # ending games if:
    screen.blit(mid_font.render('vzdát se', True, 'white'), (820, 35)) 
    screen.blit(mid_font.render('remíza', True, 'white'), (830, 135))
    screen.blit(font.render(f'50 pro remízu: {half_of_draw_rule}', True, 'white'), (820, 220))


    screen.blit(font.render(f'sebrané figury:', True, 'white'), (830, 320)) #  dekorace
    screen.blit(font.render('kdo hraje:', True, 'white'), (850, 760))
    if whom_turn ==2: # indicator whom's move it is
        pygame.draw.rect(screen,(0,0,0),[800,780,200,20])
    else:
        pygame.draw.rect(screen,(255,255,255),[800,780,200,20]) 

def draw_game_over():
    screen.blit(bookshelf3, (200, 200))  
    screen.blit(bob, (200, 400)) 
    screen.blit(font.render(f'press enter to restart the game', True, 'white'), (250, 327)) 
    
    if draw == False:
        screen.blit(big_font.render(f'{wictor} has won', True, 'white'), (225, 250))
    else:
        screen.blit(big_font.render('game is a draw', True, 'white'), (217, 250))

    black_score, white_score, draw_score = get_results()

    # Render text
    screen.blit(font.render("Black", True, 'white'), (485, 470)) 
    screen.blit(font.render("White", True, 'white'), (260, 470))
    screen.blit(font.render("Draw", True, 'white'), (375, 470))
    screen.blit(font.render(str(black_score), True, 'white'), (500, 510)) 
    screen.blit(font.render(str(white_score), True, 'white'), (285, 510)) 
    screen.blit(font.render(str(draw_score), True, 'white'), (385, 510))

def draw_pieces():
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'air': # placeholder for castle thing
            continue 
        
        index = piece_types.index(white_pieces[i])  # draws pieces 
        screen.blit(white_images[index], (white_locals[i][0] * 100 , white_locals[i][1] * 100 )) # zijstí pozici figurek z listu pozic, vynásobí je 100, pro x a y
        
        if whom_turn == 0 and selected_piece == i: # nakreslí kolem vybrané figury čtverec 
            pygame.draw.rect(screen, (0, 106, 149), [white_locals[i][0] * 100, white_locals[i][1] * 100,
                                             100, 100], 5)

    for i in range(len(black_pieces)):
        if black_pieces[i] == 'air':
            continue
        
        index = piece_types.index(black_pieces[i])     
        screen.blit(black_images[index], (black_locals[i][0] * 100 , black_locals[i][1] * 100 ))
        
        if whom_turn ==2 and selected_piece == i:
            pygame.draw.rect(screen, ((194, 0, 116)), [black_locals[i][0] * 100, black_locals[i][1] * 100,
                                              100, 100], 5)
            

    for i in range(len(taken_pieces_white)): # projde sebranými figury a 
        captured_piece = taken_pieces_white[i]
        index = piece_types.index(captured_piece)
        screen.blit(taken_b[index], (830, 355 + 25 * i))
    for i in range(len(taken_pieces_black)):
        captured_piece = taken_pieces_black[i]
        index = piece_types.index(captured_piece)
        screen.blit(taken_w[index], (930, 355 + 25 * i))
def draw_right_click():
    for i in range(len(rightclicklist)):  
        if whom_turn == 0 :    
            screen.blit(white_ring, (rightclicklist[i][0] * 100 , rightclicklist[i][1] * 100 ))
        else:    
            screen.blit(black_ring, (rightclicklist[i][0] * 100 , rightclicklist[i][1] * 100 ))
def draw_check():
        if game_over == False: # do not delete (it scashes)
            if 'king' in white_pieces and 'king' in black_pieces:
                king_index = white_pieces.index('king')
                king_location = white_locals[king_index]
                for i in range(len(black_moves)):
                    if king_location in black_moves[i]:
                        if counter < 15:
                            pygame.draw.rect(screen,(0, 106, 149), [white_locals[king_index][0] * 100 , white_locals[king_index][1] * 100 , 100, 100], 5)

            if 'king' in white_pieces and 'king' in black_pieces:
                king_index = black_pieces.index('king')
                king_location = black_locals[king_index]
                for i in range(len(white_moves)):
                    if king_location in white_moves[i]:
                        if counter < 15:
                            pygame.draw.rect(screen, (194, 0, 116), [black_locals[king_index][0] * 100 ,black_locals[king_index][1] * 100 , 100, 100], 5)
def check_options(pieces, locations, turn):
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        
        if piece == 'pp':
            moves_list = check_pp(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'honse':
            moves_list = check_honse(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        elif piece == 'air':
            moves_list = [] 
        
        all_moves_list.append(moves_list)
    
    return all_moves_list# king can move to max 8sq
def check_king(position, turn):
    moves_list = []
    king_in_check = False

    if turn == 'white':
        enemies_list = black_locals
        friends_list = white_locals
        castle_king = castle_king_w
        castle_kingside = castle_kingside_w
        castle_queenside = castle_queenside_w
        enemy_moves = black_moves  
 
    else:
        friends_list = black_locals
        enemies_list = white_locals
        castle_king = castle_king_b
        castle_kingside = castle_kingside_b
        castle_queenside = castle_queenside_b
        enemy_moves = white_moves 
    for i, moves in enumerate(enemy_moves):
        if position in moves:
            king_in_check = True
 

    bobs = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for bob_offset in bobs:
        bob = (position[0] + bob_offset[0], position[1] + bob_offset[1])
        if bob not in friends_list and 0 <= bob[0] <= 7 and 0 <= bob[1] <= 7:
                    moves_list.append(bob)
    if castle_king:
        if castle_kingside:
            kingside_squares = [(5, position[1]), (6, position[1])]
            if all(sq not in friends_list and sq not in enemies_list for sq in kingside_squares):
                if not any(sq in enemy_moves for sq in kingside_squares):
                    if king_in_check == False:
                            moves_list.append((6, position[1]))
        if castle_queenside:
            queenside_squares = [(3, position[1]), (2, position[1])]
            if all(sq not in friends_list and sq not in enemies_list for sq in [(1, position[1])] + queenside_squares):
                if not any(sq in enemy_moves for sq in queenside_squares):
                    if king_in_check == False:
                            moves_list.append((2, position[1]))

    return moves_list
def check_queen(position, turn): # queen just checks for rooks and bishops moves
    bishops_list = check_bishop(position, turn)
    rooks_list = check_rook(position, turn)
    for i in range(len(rooks_list)):
        bishops_list.append(rooks_list[i])
    return bishops_list
def check_bishop(position, turn): 
    moves_list = []
    if turn == 'white':
        enemies_list = black_locals
        friends_list = white_locals
    else:
        friends_list = black_locals
        enemies_list = white_locals
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list
def check_rook(position, turn):
    moves_list = []
    if turn == 'white':
        enemies_list = black_locals
        friends_list = white_locals
    else:
        friends_list = black_locals
        enemies_list = white_locals
    for i in range(4):  # y- y+, x+, y-
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list
def draw_valid(moves):# displays valid moved for the sellected piece
    if whom_turn ==0:
        bob = white_selected_piece_icon
    else:
        bob = black_selected_piece_icon
    for i in range(len(moves)):
        screen.blit(bob, (moves[i][0] * 100 , moves[i][1] * 100 ))
def check_legal_moves():
    if whom_turn < 2:
        options_list = white_moves
    else:
        options_list = black_moves
    legal_options = options_list[selected_piece]
    return legal_options
def check_pp(position, turn):
    moves_list = []
    
    if turn == 'white':
        # Normal one-step move
        if (position[0], position[1] - 1) not in white_locals and (position[0], position[1] - 1) not in black_locals and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        
        # Starting two-step move
        if (position[0], position[1] - 2) not in white_locals and (position[0], position[1] - 2) not in black_locals \
                and (position[0], position[1] - 1) not in white_locals and (position[0], position[1] - 1) not in black_locals \
                and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        
        # Capturing diagonally
        if (position[0] + 1, position[1] - 1) in black_locals:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in black_locals:
            moves_list.append((position[0] - 1, position[1] - 1))
        
        # En passant
        if en_passant_b:
            if position[0] - 1 == enpassantfileb or position[0] + 1 == enpassantfileb:
                if position[1] == 3:
                    moves_list.append((enpassantfileb, 2))
    
    else:  # Black pawn moves
        # Normal one-step move
        if (position[0], position[1] + 1) not in white_locals and (position[0], position[1] + 1) not in black_locals and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        
        # Starting two-step move
        if (position[0], position[1] + 2) not in white_locals and (position[0], position[1] + 2) not in black_locals \
                and (position[0], position[1] + 1) not in white_locals and (position[0], position[1] + 1) not in black_locals \
                and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        
        # Capturing diagonally
        if (position[0] + 1, position[1] + 1) in white_locals:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in white_locals:
            moves_list.append((position[0] - 1, position[1] + 1))
        
        # En passant
        if en_passant_w:
            if position[0] - 1 == enpassantfilew or position[0] + 1 == enpassantfilew:
                if position[1] == 4:
                    moves_list.append((enpassantfilew, 5))
    
    return moves_list
def check_honse(position, turn):
    moves_list = []
    if turn == 'white':
        friends_list = white_locals
    else:
        friends_list = black_locals
    # 8 squares to check for honses, they can go two squares in one direction and one in another
    bobs = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        bob = (position[0] + bobs[i][0], position[1] + bobs[i][1])
        if bob not in friends_list and 0 <= bob[0] <= 7 and 0 <= bob[1] <= 7:
            moves_list.append(bob)
    return moves_list# check for valid moves for just selected piece
def check_for_promotion_w():
    for i in range(len(white_pieces)): 
        if white_pieces[i] == "pp" and white_locals[i][1] == 0:  
            white_pieces[i] = "queen"  
def check_for_promotion_b():
    for i in range(len(black_pieces)): 
        if black_pieces[i] == "pp" and black_locals[i][1] == 7:  
            black_pieces[i] = "queen" 
# sql wheeee

cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        black INTEGER DEFAULT 0,
        white INTEGER DEFAULT 0,
        draw INTEGER DEFAULT 0
    )
""")
cursor.execute("SELECT COUNT(*) FROM results")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO results (black, white, draw) VALUES (0, 0, 0)")
    conn.commit()
def update_winner(winner):
    """Update the correct column in the database"""
    if winner == "black":
        cursor.execute("UPDATE results SET black = black + 1")
    elif winner == "white":
        cursor.execute("UPDATE results SET white = white + 1")
    elif winner == "draw":
        cursor.execute("UPDATE results SET draw = draw + 1")
    
    conn.commit()
def get_results():
    cursor.execute("SELECT black, white, draw FROM results")
    result = cursor.fetchone()
    if result:
        return result  # (black, white, draw)
    return (0, 0, 0)  # Default if no results found

black_moves = check_options(black_pieces, black_locals, 'black')
white_moves = check_options(white_pieces, white_locals, 'white')
# main game loop
run = True

while run:
    mainvoidtime.tick(fps)
    screen.fill((0, 255, 0))  # background colo
    if not game_over:  # clock logic
        if whom_turn == 2:
            if time_b == fps:
                time_b = 0
                time_b_secs -= 1
                if time_b_secs == 0:
                    winner = 'white'
            else:
                time_b += 1
        else:
            if time_w == fps:
                time_w = 0
                time_w_secs -= 1
                if time_w_secs == 0:
                    winner = 'black'
            else:
                time_w += 1
    if counter < 30:  # check animation
        counter += 1
    else:
        counter = 0
    draw_board()
    draw_pieces()
    draw_check()
    draw_right_click()
    if selected_piece != 16:
        legal_moves = check_legal_moves()
        draw_valid(legal_moves)
    if draw_rule == 100:  # 50-move draw rule
        game_drawn = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handle the window close button
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and not game_over:  # Right-click logic
                x_axis = event.pos[0] // 100
                y_axis = event.pos[1] // 100
                if x_axis <= 7:
                    rightclick = (x_axis, y_axis)
                    rightclicklist.append(rightclick)
            elif event.button == 1 and not game_over:  # Left-click logic
                rightclicklist = []  # Reset right-click list
                x_axis = event.pos[0] // 100
                y_axis = event.pos[1] // 100
                where_leftclick = (x_axis, y_axis)

                # Draw and Resign functions
                if where_leftclick in [(9, 0), (8, 0)]:
                    winner = 'white' if whom_turn == 2 else 'black'
                if where_leftclick in [(8, 1), (9, 1)]:
                    game_drawn = True
                if whom_turn == 0:  # White's turn
                    if where_leftclick in white_locals:
                        selected_piece = white_locals.index(where_leftclick)
                    elif where_leftclick not in white_locals and where_leftclick not in legal_moves:
                        selected_piece = 16
                    if where_leftclick in legal_moves and selected_piece != 16:
                        piece_moved = white_pieces[selected_piece]
                        white_locals[selected_piece] = where_leftclick
                        # Pawn move and en passant
                        if piece_moved == 'pp':
                            draw_rule = 0
                            if en_passant_b and where_leftclick == (enpassantfileb, 2):
                                black_piece = black_locals.index((enpassantfileb, 3))
                                taken_pieces_white.append(black_pieces[black_piece])
                                black_pieces.pop(black_piece)
                                black_locals.pop(black_piece)
                            if white_locals[selected_piece][1] == 6 and where_leftclick[1] == 4:
                                en_passant_w = True
                                enpassantfilew = where_leftclick[0]
                        # King move and castling
                        if piece_moved == 'king':
                            castle_king_w = False
                            if where_leftclick == (6, 7):
                                white_locals[1] = (5, 7)
                                castle_king_w = False
                            if where_leftclick == (2, 7):
                                white_locals[0] = (3, 7)
                                castle_king_w = False
                        # Capture piece logic
                        if where_leftclick in black_locals:
                            draw_rule = 0
                            black_piece = black_locals.index(where_leftclick)
                            taken_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            if black_pieces[black_piece] == 'rook':
                                if where_leftclick == (0, 0):
                                    castle_queenside_b = False
                                if where_leftclick == (0, 7):
                                    castle_king_b = False
                            black_pieces[black_piece] = 'air'
                            black_locals[black_piece] = (9, 9)
                        if selected_piece == 1:  # Rook moves invalidate castling
                            castle_kingside_w = False
                        if selected_piece == 0:
                            castle_queenside_w = False
                        check_for_promotion_w()
                        white_moves = check_options(white_pieces, white_locals, 'white')
                        black_moves = check_options(black_pieces, black_locals, 'black')
                        whom_turn = 2
                        selected_piece = 16
                        legal_moves = []
                        enpassantfileb = 9
                        en_passant_b = False
                elif whom_turn ==2:  # Black's turn
                    if where_leftclick in black_locals:
                        selected_piece = black_locals.index(where_leftclick)
                    elif where_leftclick not in black_locals and where_leftclick not in legal_moves:
                        selected_piece = 16
                    if where_leftclick in legal_moves and selected_piece != 16:
                        piece_moved = black_pieces[selected_piece]
                        black_locals[selected_piece] = where_leftclick
                        # Pawn move and en passant
                        if piece_moved == 'pp':
                            draw_rule = 0
                            if en_passant_w and where_leftclick == (enpassantfilew, 5):
                                white_piece = white_locals.index((enpassantfilew, 4))
                                taken_pieces_black.append(white_pieces[white_piece])
                                white_pieces.pop(white_piece)
                                white_locals.pop(white_piece)
                            if black_locals[selected_piece][1] == 1 and where_leftclick[1] == 3:
                                en_passant_b = True
                                enpassantfileb = where_leftclick[0]
                        # King move and castling
                        if piece_moved == 'king' and castle_king_b:
                            if where_leftclick == (6, 0):
                                black_locals[1] = (5, 0)
                            if where_leftclick == (2, 0):
                                black_locals[0] = (3, 0)

                            castle_queenside_b = False
                            castle_kingside_b = False
                            castle_king_b = False
                        # Capture piece logic
                        if where_leftclick in white_locals:
                            draw_rule = 0
                            white_piece = white_locals.index(where_leftclick)
                            taken_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            if white_pieces[white_piece] == 'rook':
                                if where_leftclick == (7, 0):
                                    castle_queenside_w = False
                                if where_leftclick == (7, 7):
                                    castle_kingside_w = False
                            white_pieces[white_piece] = 'air'
                            white_locals[white_piece] = (9, 9)
                        if selected_piece == 1:  # Rook moves invalidate castling
                            castle_kingside_w = False
                        if selected_piece == 0:
                            castle_queenside_w = False
                        draw_check()
                        black_moves = check_options(black_pieces, black_locals, 'black')
                        white_moves = check_options(white_pieces, white_locals, 'white')
                        whom_turn = 0
                        selected_piece = 16
                        legal_moves = []
                        check_for_promotion_b()
                        en_passant_w = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                resetgame()
                black_moves = check_options(black_pieces, black_locals, 'black')
                white_moves = check_options(white_pieces, white_locals, 'white')

    if winner or game_drawn:
        game_over = True
        update_winner(winner if not game_drawn else "draw")
        cursor.execute("SELECT * FROM results")
        print(cursor.fetchall())
        wictor = winner
        draw = game_drawn
        winner = ''
        game_drawn = False

    if game_over == True:
        draw_game_over()
    pygame.display.update()
