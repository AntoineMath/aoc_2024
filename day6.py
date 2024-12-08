
dirs = {
  "^": (-1, 0),
  ">": (0, 1),
  "v": (1, 0),
  "<": (0, -1)
}
rotations = {
  "^": ">",
  ">": "v",
  "v": "<",
  "<": "^"
}

def part1(grid) -> int:
  ROWS, COLS = len(grid), len(grid[0])
  visited = set()
  guard_dir = ""
  start_pos = (-1, -1)
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] in "<^>v":
        start_pos = (r, c)
        guard_dir = grid[r][c]
        visited.add(start_pos)


  x, y = start_pos
  while 0 <= x < ROWS and 0 <= y < COLS:
    if grid[x][y] == "#":
      dx, dy = dirs[guard_dir]
      x, y = x - dx, y - dy # one step back
      guard_dir = rotations[guard_dir]
    else:
      visited.add((x, y))
    dx, dy = dirs[guard_dir]
    x, y = x + dx, y + dy


  return len(visited)


def is_cycle(start_x, start_y, grid):
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    x, y = start_x, start_y
    guard_dir = grid[start_x][start_y]

    while 0 <= x < ROWS and 0 <= y < COLS:
        if (x, y, guard_dir) in visited:
            return True # infinite loop
        visited.add((x, y, guard_dir))

        if grid[x][y] == "#":  
            dx, dy = dirs[guard_dir]
            x, y = x - dx, y - dy  
            guard_dir = rotations[guard_dir] 

        dx, dy = dirs[guard_dir]
        x, y = x + dx, y + dy
    return False

def part2(grid) -> int:
  start_x, start_y = (-1, -1)
  for r in range(len(grid)):
      for c in range(len(grid[0])):
          if grid[r][c] in "<^>v":
              start_x, start_y = r, c
              break

  obstacle_positions = set()

  guard_start = (start_x, start_y)

  # brute force ugly
  for x in range(len(grid)):
      for y in range(len(grid[0])):
          if grid[x][y] == "#" or (x, y) == guard_start:
              continue

          curr_grid = grid[:]
          modified_line = curr_grid[x][:y] + "#" + curr_grid[x][y + 1:]
          curr_grid = curr_grid[:x] + [modified_line] + curr_grid[x + 1:]

          if is_cycle(start_x, start_y, curr_grid):  # detect cycle
              obstacle_positions.add((x, y))

  return len(obstacle_positions)




if __name__ == "__main__":
  with open("inputs/day6", "r") as f:
    lines = f.readlines()

  grid = [l.strip() for l in lines]
  
  print(part1(grid))
  print(part2(grid))