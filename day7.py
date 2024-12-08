def dfs1(i, nbs, curr, tot):
  if curr == tot and i == len(nbs):
    return True
  if i >= len(nbs):
    return False
  return dfs1(i+1, nbs, curr+nbs[i], tot) or dfs1(i+1, nbs, curr*nbs[i], tot)

def dfs2(i, nbs, curr, tot):
  if curr == tot and i == len(nbs):
    return True
  if i >= len(nbs):
    return False
  return dfs2(i+1, nbs, curr+nbs[i], tot) or dfs2(i+1, nbs, curr*nbs[i], tot) or dfs2(i+1, nbs, int(str(curr) + str(nbs[i])), tot)

def part(lines, dfs) -> int:
  ans = 0
  for l in lines:
    total = int(l.split(":")[0])
    nbs = [int(nb) for nb in l.split(":")[1].strip().split(" ")]
    if dfs(1, nbs, nbs[0], total):
      ans += total
  return ans

if __name__ == "__main__":
  with open("inputs/day7", "r") as f:
    lines = f.readlines()
  print(part(lines, dfs1))
  print(part(lines, dfs2))
  

