def part1(lines) -> int:
  grid = [l.strip() for l in lines]
  ROWS = len(grid)
  COLS = len(grid[0])

  res = 0
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == "X":
        for dr, dc in [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, -1), (0, 1), (0, -1), (-1, 1)]:
          nr, nc = r + dr, c + dc
          found = True
          for letter in "MAS":
            if not(0 <= nr < ROWS and 0 <= nc < COLS) or grid[nr][nc] != letter:
              found = False
              break
            nr, nc = nr + dr, nc + dc
          if found:
            res += 1
  return res


def part2(lines) -> int:
  res = 0
  a_set = set()

  grid = [l.strip() for l in lines]
  ROWS = len(grid)
  COLS = len(grid[0])

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == "M":
        for dr, dc in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
          nr, nc = r + dr, c + dc
          found = True
          a_pos = (-1, -1)
          for letter in "AS":
            if letter == "A":
              a_pos = (nr, nc)
            if not(0 <= nr < ROWS and 0 <= nc < COLS) or grid[nr][nc] != letter:
              found = False
              break
            nr, nc = nr + dr, nc + dc

          if found:
            if a_pos in a_set:
              res += 1
            a_set.add(a_pos)
  return res


if __name__ == "__main__":
  with open("inputs/day4", "r") as f:
    lines = f.readlines()
  
  print(part1(lines))
  print(part2(lines))

