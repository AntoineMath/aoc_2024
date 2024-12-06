def part1(grid) -> int:
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


def walk(grid):
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
  ROWS, COLS = len(grid), len(grid[0])
  visited = set()
  path = []
  guard_dir = ""
  start_pos = (-1, -1)
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] in "<^>v":
        start_pos = r, c
        guard_dir = grid[r][c]


  # 1- compute path (visited)
  x, y = start_pos
  while 0 <= x < ROWS and 0 <= y < COLS:

    if (x, y, rotations[guard_dir]) in visited:
      obstacles += 1
      dx, dy = dirs[guard_dir]
      print(x+dx, y+dy)
    if grid[x][y] == "#":
      dx, dy = dirs[guard_dir]
      x, y = x - dx, y - dy # one step back
      guard_dir = rotations[guard_dir]
    else:
      visited.add((x, y, guard_dir))
      path.append((x, y, guard_dir))
    dx, dy = dirs[guard_dir]
    x, y = x + dx, y + dy
  

def part2(grid) -> int:
  """
   intuition: for each position along the way, if rotating 90deg (aka adding an obstacle)
   would put you in a previous position with the same previous direction 
   Then it means you'll be in a loop
   """
  obstacles = 0
  


  # 2 - replay path, but replace 1 position by an obstacle
  # and check if one position is reached again
  for i in range(path):
    cur_grid = grid[::]



    

  return obstacles

if __name__ == "__main__":
  with open("inputs/day6", "r") as f:
    lines = f.readlines()

  grid = [l.strip() for l in lines]
  
  #print(part1(grid))
  print(part2(grid))