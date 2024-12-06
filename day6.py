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
  print(grid)
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


  




def part2(lines) -> int:
  pass


if __name__ == "__main__":
  with open("inputs/day6", "r") as f:
    lines = f.readlines()

  grid = [l.strip() for l in lines]
  
  print(part1(grid))
  print(part2(lines))