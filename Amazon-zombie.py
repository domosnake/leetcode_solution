from typing import List

# Given a 2D grid, each cell is either a zombie 1 or a human 0.
# Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
# Find out how many hours does it take to infect all humans?


class Solution:
    def zombie(self, grid: List[List[int]]) -> int:
        hours = 0
        # zombie coordinates queue
        zombie = []
        zombie_temp = []
        human = 0
        row = len(grid)
        col = len(grid[0])
        # count human and zombie
        for r in range(row):
            for c in range(col):
                # if the cell is a zombie
                if grid[r][c] == 1:
                    # save rc
                    zombie.append((r, c))
                else:
                    human += 1
        # start infecting
        while human > 0:
            # start a new hour
            hours += 1
            # pop first
            while zombie:
                cur_zombie = zombie.pop(0)
                x = cur_zombie[0]
                y = cur_zombie[1]
                # 4 directions
                for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 0:
                        # infect a human
                        grid[r][c] = 1
                        # human counter --
                        human -= 1
                        # check if no human left, return hours
                        if human == 0:
                            print(f'After {hours} hours, infection is:')
                            print(grid)
                            print(f'It takes {hours} hours to infect all human')
                            return hours
                        grid[r][c] = 1
                        # add new zombie
                        zombie_temp.append((r, c))
            print(f'After {hours} hours, infection is:')
            print(grid)
            # swap queues
            zombie = zombie_temp
            zombie_temp = []
        return hours


s = Solution()
b = [[0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]]
print(b)
a = s.zombie(b)
print(a)
