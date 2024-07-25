import sys, pygame, time

if __name__ == "__main__":
    WIDTH = 600
    HEIGHT = 600
    BACKGROUND_COLOR = (51,174,255)
    LINE_COLOR = (255,255,255)
    PLAYER_COLOR = (204,0,0)

    
    #The basic Pygame code
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe Clone')
    
    #Define the units
    board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    play = 1
    end = 0

    #Position for the plays
    pos_x = 0
    pos_y = 0

    #The text

    font = pygame.font.SysFont('lucidasansroman', 60)
    finishText = font.render(f'  Wins', True, LINE_COLOR)
    finishTextRect = finishText.get_rect()
    finishTextRect.left = WIDTH/2-finishTextRect.width/2
    finishTextRect.top = HEIGHT/2-finishTextRect.height/2
    
    while True:
        pos_y = 0
        pos_x = 0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                boardPosX = mousePos[0]//200
                boardPosY = mousePos[1]//200
                if board[boardPosX+3*boardPosY] == -1:
                    board[boardPosX+3*boardPosY] = play%2
                    play+=1
                if board[0]==board[1] and board[1]==board[2] and board[0] != -1:
                    end = 1
                elif board[3]==board[4] and board[4]==board[5] and board[3] != -1:
                    end = 1
                elif board[6]==board[7] and board[7]==board[8] and board[6] != -1:
                    end = 1
                elif board[0]==board[4] and board[4]==board[8] and board[0] != -1:
                    end = 1
                elif board[2]==board[4] and board[4]==board[6] and board[2] != -1:
                    end = 1
                
                
        
        screen.fill(BACKGROUND_COLOR)

        #Draw X and O
        for position in board:
            
            if position == 1:
                pygame.draw.line(screen, PLAYER_COLOR, (pos_x+20, pos_y+20), (pos_x+180, pos_y+180), 20)
                pygame.draw.line(screen, PLAYER_COLOR, (pos_x+180, pos_y+20), (pos_x+20, pos_y+180), 20)
            elif position == 0:
                pygame.draw.circle(screen, PLAYER_COLOR,(pos_x+100, pos_y+100), 80, 10)
            
            pos_x += WIDTH/3
            if pos_x==600:
                pos_x = 0
                pos_y+=HEIGHT/3
            
        #The end
        if end:
            screen.fill(BACKGROUND_COLOR)
            if (play-1)%2 == 0:
                finishText = font.render(f'O Wins', True, LINE_COLOR)
            else:
                finishText = font.render(f'X Wins', True, LINE_COLOR)
            screen.blit(finishText, finishTextRect)
            pygame.display.update() 
            time.sleep(1)
            end = 0
            play = 1
            board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        elif play == 10:
            screen.fill(BACKGROUND_COLOR)
            finishText = font.render(f'Draw', True, LINE_COLOR)
            screen.blit(finishText, finishTextRect)
            pygame.display.update()
            time.sleep(1)
            end = 0
            play = 1
            board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        else:
            pygame.draw.rect(screen, LINE_COLOR, (WIDTH/3-5, 0, 10, HEIGHT)) # Vertical Left Line
            pygame.draw.rect(screen, LINE_COLOR, (WIDTH/3*2-5, 0, 10, HEIGHT)) # Vertical Right Line
            pygame.draw.rect(screen, LINE_COLOR, (0, HEIGHT/3, WIDTH, 10)) # Orizontal Top Line
            pygame.draw.rect(screen, LINE_COLOR, (0, HEIGHT*2/3, WIDTH, 10)) # Orizontal Bottom Line
            pygame.display.update() 

        #Update the screen
        clock.tick(120)