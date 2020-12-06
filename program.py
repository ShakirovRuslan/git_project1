import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = [[0] * width for i in range(height)]
        self.left = 10
        self.top = 10
        self.player = 1
        self.cell_size = 70

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                color = [0, 0, 0]
                color[self.board[y][x]] = 255 * int(self.board[y][x] != 1)
                color = tuple(color)
                x_pos, y_pos = self.left + x * self.cell_size, self.top + y * self.cell_size

                pygame.draw.rect(screen, "white",
                                 (x_pos, y_pos,
                                  self.cell_size, self.cell_size),
                                 width=1)
                if self.board[y][x] == 1:
                    pygame.draw.line(screen, "blue",
                                     (x_pos + 2, y_pos + 2),
                                     (x_pos + self.cell_size - 3, y_pos + self.cell_size - 3), width=2)
                    pygame.draw.line(screen, "blue",
                                     (x_pos + 2, y_pos + self.cell_size - 3),
                                     (x_pos + self.cell_size - 3, y_pos + 2), width=2)
                elif self.board[y][x] == 2:
                    r = self.cell_size // 2
                    pygame.draw.circle(screen, "red",
                                       (x_pos + r + 2, y_pos + r + 2),
                                       r - 4, width=2)

    def get_cell(self, pos):
        x = (pos[0] - self.left) // self.cell_size
        y = (pos[1] - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return None

    def on_click(self, cell):
        if cell is not None:
            x, y = cell[0], cell[1]
            if not self.board[y][x]:
                self.board[y][x] += self.player
                self.board[y][x] %= 3
                self.player += 1 - 2 * (self.player == 2)

    def get_click(self, pos):
        cell = self.get_cell(pos)
        self.on_click(cell)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Крестики-нолики")

    board = Board(5, 5)
    running = True
    screen = pygame.display.set_mode((600, 400))
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        board.render()
        pygame.display.flip()

pygame.quit()
