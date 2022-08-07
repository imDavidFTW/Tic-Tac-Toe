import pygame
Width, Height = 860, 733
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic-Tac-Toe")
image = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\TTT.jpg')
image2 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 000015.jpg.png')
image3 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 001026.png')
player1 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 004824.png')
player2 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 004740.png')


def hasSameHorizontal(lst):
    for i in range(len(lst) - 1):
        print(lst)
        if lst[i] != lst[i + 1] or lst[i] == 0 or lst[i + 1] == 0:
            return False
    return True

def hasSameColumn(matrix):
    for k in range(3):
        count = 1
        for j in range(2):
            if matrix[j][k] == matrix[j+1][k] and matrix[j][k] != 0:
                count += 1
            print(count)
            if count == 3:
                if k == 0:
                    return 0
                if k == 1:
                    return 1
                if k == 2:
                    return 2
    return -1

def hasSameLeftToRightDiagonal(matrix):
    for i in range(2):
        if matrix[i][i] != matrix[i + 1][i + 1] or matrix[i][i] == 0 or matrix[i+1][i + 1] == 0:
            return False
    return True

def hasSameRightToLeftDiagonal(matrix):
    i = 2
    j = 0
    while i > 0:
        if matrix[j][i] != matrix[j+1][i - 1] or matrix[j][i] == 0 or matrix[j+1][i - 1] == 0:
            return False
        i-=1
        j+=1
    return True


def winner(matrix):
    for i in range(3):
        if hasSameHorizontal(matrix[i]):
            if matrix[i][0] == 1:
                Window.blit(player1, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 1")
            elif matrix[i][0] != 0:
                Window.blit(player2, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 2")
    if hasSameColumn(matrix) >= 0:
        if hasSameColumn(matrix) == 0:
            if matrix[0][0] == 1:
                Window.blit(player1, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 1")
            else:
                Window.blit(player2, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 2")
        if hasSameColumn(matrix) == 1:
            if matrix[0][1] == 1:
                Window.blit(player1, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 1")
            else:
                Window.blit(player2, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 2")
        if hasSameColumn(matrix) == 2:
            if matrix[0][2] == 1:
                Window.blit(player1, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 1")
            else:
                Window.blit(player2, (0, 0))
                pygame.display.update()
                return True, print("Winner, Player 2")
    if hasSameLeftToRightDiagonal(matrix):
        if matrix[0][0] == 1:
            Window.blit(player1, (0, 0))
            pygame.display.update()
            return True, print("Winner, Player 1")
        elif matrix[0][0] != 0:
            Window.blit(player2, (0, 0))
            pygame.display.update()
            return True, print("Winner, Player 2")
    print(hasSameRightToLeftDiagonal(matrix))
    if hasSameRightToLeftDiagonal(matrix):
        if matrix[0][2] == 1:
            Window.blit(player1, (0, 0))
            pygame.display.update()
            return True, print("Winner, Player 1")
        elif matrix[0][2] != 0:
            Window.blit(player2, (0, 0))
            pygame.display.update()
            return True, print("Winner, Player 2")
    return False, print("No Winner")




def main():
    matrix = [[0, 0, 0] for i in range(3)]
    x, y = 0, 0
    run = True
    Window.blit(image, (0, 0))
    count = 0
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if count <= 8:
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                    x, y = event.pos
                    if image.get_rect().collidepoint(x, y):
                        if count % 2 == 0:
                            Window.blit(image2, (x - 60, y - 53))
                            pygame.display.update()
                            count+= 1
                            if 0 < x < 326 and 0 < y < 263:
                                matrix[0][0] = 1
                            elif 326 <= x < 531 and 0 < y < 263:
                                matrix[0][1] = 1
                            elif 531 <= x < 860 and 0 < y < 263:
                                matrix[0][2] = 1
                            elif 0 < x < 326 and 263 <= y < 465:
                                matrix[1][0] = 1
                            elif 326 <= x < 531 and 263 <= y < 465:
                                matrix[1][1] = 1
                            elif 531 <= x < 860 and 263 <= y < 465:
                                matrix[1][2] = 1
                            elif 0 < x < 326 and 463 <= y < 733:
                                matrix[2][0] = 1
                            elif 326 <= x < 531 and 463 <= y < 733:
                                matrix[2][1] = 1
                            else:
                                matrix[2][2] = 1 
                        else:
                            Window.blit(image3, (x - 60, y - 53))
                            pygame.display.update()
                            count+= 1
                            if 0 < x < 326 and 0 < y < 263:
                                matrix[0][0] = 2
                            elif 326 <= x < 531 and 0 < y < 263:
                                matrix[0][1] = 2
                            elif 531 <= x < 860 and 0 < y < 263:
                                matrix[0][2] = 2
                            elif 0 < x < 326 and 263 <= y < 465:
                                matrix[1][0] = 2
                            elif 326 <= x < 531 and 263 <= y < 465:
                                matrix[1][1] = 2
                            elif 531 <= x < 860 and 263 <= y < 465:
                                matrix[1][2] = 2
                            elif 0 < x < 326 and 463 <= y < 733:
                                matrix[2][0] = 2
                            elif 326 <= x < 531 and 463 <= y < 733:
                                matrix[2][1] = 2
                            else:
                                matrix[2][2] = 2
                        if winner(matrix) == True:
                            if count <= 9:
                                count = 10
                                winner(matrix)
            




if __name__ == "__main__":
    main()                                     
    pygame.quit()
