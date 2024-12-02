def part1(lines) -> int:
  ans = 0
  for l in lines:
    nbs = [int(c) for c in l.split(" ")]
    if validNbs(nbs):
      ans += 1
  return ans

def part2(lines) -> int:
  ans = 0
  for l in lines:
    nbs = [int(c) for c in l.split(" ")]
    for i in range(len(nbs)): # brute force, ugly
      cur_nbs = nbs[:i] + nbs[i+1:]
      if validNbs(cur_nbs):
        ans += 1
        break
  return ans

def validNbs(nbs):
  incr = nbs[0] < nbs[1]
  valid = True
  for i in range(1, len(nbs)):
    diff = abs(nbs[i-1] - nbs[i])
    if ((nbs[i] < nbs[i-1] and incr) or
        (nbs[i] > nbs[i-1] and not incr)or
        diff < 1 or diff >3):
        valid = False
        break
  return valid 
    

if __name__ == "__main__":
  with open("inputs/day2", "r") as f:
    lines = f.readlines()
  
  print(part1(lines))
  print(part2(lines))

