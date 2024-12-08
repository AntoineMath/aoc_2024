from collections import defaultdict
def part1(grid) -> int:
  ROWS, COLS = len(grid), len(grid[0])
  ant_pos = defaultdict(list)
  antinodes = set()

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] not in "#.":
        ant_pos[grid[r][c]].append((r, c))
  
  antenna_types = ant_pos.keys()
  for type in antenna_types:
    antennas = ant_pos[type]
    for i in range(len(antennas)-1):
      for j in range(i+1, len(antennas)):
        x0, y0 = antennas[i]
        x1, y1 = antennas[j]
        dx, dy = x1-x0, y1-y0
        x2, y2 = x0-dx, y0-dy
        x3, y3 = x1+dx, y1+dy
        if 0 <= x2 < ROWS and 0 <= y2 < COLS: 
          antinodes.add((x2, y2))
        if 0 <= x3 < ROWS and 0 <= y3 < COLS:
          antinodes.add((x3, y3))
  return len(antinodes)

def find_all_points(grid, x0, y0, dx, dy):
    ROWS, COLS = len(grid), len(grid[0])
    points = []

    # Forward direction
    x, y = x0 + dx, y0 + dy
    while 0 <= x < ROWS and 0 <= y < COLS:
        points.append((x, y))
        x += dx
        y += dy

    # Backward direction
    x, y = x0 - dx, y0 - dy
    while 0 <= x < ROWS and 0 <= y < COLS:
        points.append((x, y))
        x -= dx
        y -= dy

    return points
        

def part2(grid) -> int:
  ROWS, COLS = len(grid), len(grid[0])
  ant_pos = defaultdict(list)
  antinodes = set()

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] not in "#.":
        ant_pos[grid[r][c]].append((r, c))
  
  antenna_types = ant_pos.keys()
  for type in antenna_types:
    antennas = ant_pos[type]
    for i in range(len(antennas)-1):
      for j in range(i+1, len(antennas)):
        x0, y0 = antennas[i]
        x1, y1 = antennas[j]
        dx, dy = x1-x0, y1-y0
        antinodes.update(find_all_points(grid, x0, y0, dx, dy))
        antinodes.update(find_all_points(grid, x1, y1, dx, dy))
  return len(antinodes)

if __name__ == "__main__":
  with open("inputs/day8", "r") as f:
    lines = f.readlines()
  
  grid = [l.strip() for l in lines]
  print(part1(grid))
  print(part2(grid))
  

