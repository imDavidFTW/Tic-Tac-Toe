import pygame
Width, Height = 860, 733
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic-Tac-Toe")
image = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\TTT.jpg')
image2 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 000015.jpg.png')
image3 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 001026.png')
player1 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 004824.png')
player2 = pygame.image.load(r'C:\Users\xdryn\GitHub Projects\Tic-Tac-Toe\images\Screenshot 2022-08-06 004740.png')

def main():
    matrix = [[0, 0, 0]]*3
    print(matrix)
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
                            print('clicked on image')
                            pygame.display.update()
                            count+= 1
                            if 0 < x < 326 and 0 < y < 263:
                                matrix[0][0] = 1
                            elif 326 <= x < 531 and 0 < y < 263:
                                matrix[0][1] = 1
                            elif 531 < x < 860 and 0 < y < 263:
                                matrix[0][2] = 1
                            elif 0 < x < 326 and 263 <= y < 465:
                                matrix[1][0] = 1
                            elif 326 <= x < 531 and 263 <= y < 465:
                                matrix[1][1] = 1
                            elif 531 < x < 860 and 263 <= y < 465:
                                matrix[1][2] = 1
                            elif 0 < x < 326 and 463 <= y < 733:
                                matrix[2][0] = 1
                            elif 326 <= x < 531 and 463 <= y < 733:
                                matrix[2][1] = 1
                            else:
                                matrix[2][2] = 1
                        else:
                            Window.blit(image3, (x - 60, y - 53))
                            print('clicked on image')
                            pygame.display.update()
                            count+= 1
                            if 0 < x < 326 and 0 < y < 263:
                                matrix[0][0] = 2
                            elif 326 <= x < 531 and 0 < y < 263:
                                matrix[0][1] = 2
                            elif 531 < x < 860 and 0 < y < 263:
                                matrix[0][2] = 2
                            elif 0 < x < 326 and 263 <= y < 465:
                                matrix[1][0] = 2
                            elif 326 <= x < 531 and 263 <= y < 465:
                                matrix[1][1] = 2
                            elif 531 < x < 860 and 263 <= y < 465:
                                matrix[1][2] = 2
                            elif 0 < x < 326 and 463 <= y < 733:
                                matrix[2][0] = 2
                            elif 326 <= x < 531 and 463 <= y < 733:
                                matrix[2][1] = 2
                            else:
                                matrix[2][2] = 2                                         
    pygame.quit()
    print(matrix)
if __name__ == "__main__":
    main()