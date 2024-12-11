from collections import deque
def part1(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  ans = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == "0":
        q = deque()
        q.append((r,c))
        visited = set()
        while q:
          x, y = q.popleft()
          level = grid[x][y]
          for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in visited:
              new_level = grid[nx][ny]
              if new_level != "." and int(new_level) == 1 + int(level):
                q.append((nx, ny))
                visited.add((nx, ny))
                if new_level == "9":
                  ans += 1
  return ans

def dfs(i, x, y, grid):
  if i == 9:
    return 1
  ans = 0
  for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    nx, ny = x+dx, y+dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]): 
      new_level = grid[nx][ny]
      if new_level != "." and int(new_level) == 1 + int(grid[x][y]):
        ans += dfs(i+1, nx, ny, grid)
  return ans


# NOTE: you can copy paste part1 and get rid of visited to get part 2
def part2(grid):
  ROWS = len(grid)
  COLS = len(grid[0])

  ans = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == "0":
        ans += dfs(0, r, c, grid)
  return ans


if __name__ == "__main__":
  with open("inputs/day10", "r") as f:
    lines = f.readlines()
  
  grid = [l.strip() for l in lines]

  print(part1(grid))
  print(part2(grid))