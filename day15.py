

def part1(grid, instructions):
    dirs = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1)
    }

    ROWS = len(grid)
    COLS = len(grid[0])
    x, y = -1, -1  
    boxes = set()
    walls = set()

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "O":
                boxes.add((r, c))
            elif grid[r][c] == "@":
                x, y = r, c
            elif grid[r][c] == "#":
                walls.add((r, c))

    grid = [list(row) for row in grid]

    for move in instructions:
        dx, dy = dirs[move]
        nx, ny = x + dx, y + dy

        moving_boxes = []
        cx, cy = nx, ny
        while (cx, cy) in boxes: 
            moving_boxes.append((cx, cy))
            cx, cy = cx + dx, cy + dy

        if (cx, cy) in walls or (cx, cy) in boxes:
            continue  # If blocked, ignore the move

        # Move all the boxes
        for bx, by in reversed(moving_boxes):  # Move boxes from last to first
            grid[bx][by] = "."
            new_bx, new_by = bx + dx, by + dy
            boxes.remove((bx, by))
            boxes.add((new_bx, new_by))
            grid[new_bx][new_by] = "O"

        # Move the robot
        if moving_boxes or (nx, ny) not in walls:  # Valid move
            grid[x][y] = "." 
            grid[nx][ny] = "@"
            x, y = nx, ny 

    score = 0
    for r in range(ROWS):
      for c in range(COLS):
          if grid[r][c] == "O":
            score += r*100 + c 
    return score



if __name__ == "__main__":
    with open("inputs/day15", "r") as f:
        text = f.read()

    grid_txt, instructions = text.split("\n\n")
    instructions = "".join(line.strip() for line in instructions.split("\n"))
    grid = grid_txt.split("\n")

    print(part1(grid, instructions))

