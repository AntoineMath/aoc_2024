
def getABP(m: str) -> tuple:
    lines = m.split("\n")
    ax = int(lines[0].split("X+")[1].split(",")[0])
    ay = int(lines[0].split("Y+")[1])
    a = (ax, ay)
  
    bx = int(lines[1].split("X+")[1].split(",")[0])
    by = int(lines[1].split("Y+")[1])
    b = (bx, by)

    px = int(lines[2].split("X=")[1].split(",")[0])
    py = int(lines[2].split("Y=")[1])
    p = (px, py)

    return a, b, p


def dfs(nba, nbb, a, b, p, mem):
  if p in mem:
    return mem[p]
  px, py = p

  if px < 0 or py < 0:
    return float("inf")
  if px == 0 and py == 0:
    return 3*nba + nbb

  # use A or B
  ax, ay = a 
  bx, by = b
  res = min(dfs(nba+1, nbb, a, b, (px-ax, py-ay), mem), dfs(nba, nbb+1, a, b, (px-bx, py-by), mem))
  mem[p] = res
  return res

def part1(machines: list[str]) -> int:
  ans = 0
  for m in machines:
    mem = {}
    a, b, p = getABP(m)
    count = dfs(0,0, a, b, p, mem)
    if count != float("inf"):
      ans += count
  return ans
    
  

if __name__ == "__main__":
  with open("inputs/day13", "r") as f:
    lines = f.read()
  
  
  machines = lines.split("\n\n")
  
  print(part1(machines))
  #print(part2(stones))