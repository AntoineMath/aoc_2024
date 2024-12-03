import re
from collections import deque

def part1(lines) -> int:
  ans = 0
  pattern = r"mul\((\d+),(\d+)\)"
  for l in lines:
    matches = re.findall(pattern, l)
    ans += sum([int(nb1) * int(nb2) for nb1, nb2 in matches])
  return ans


def part2(lines) -> int:
  ans = 0
  pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"
  enabled = True # do not reset the instruction when processing new line... that's sad
  for line in lines:
    matches = re.finditer(pattern, line.strip())
    for match in matches:
        text = match.group()
        if text == "do()":
          enabled = True
        elif text == "don't()":
          enabled = False
        elif text.startswith("mul") and enabled:
            x, y = map(int, match.groups())
            ans += x * y
  return ans


if __name__ == "__main__":
  with open("inputs/day3", "r") as f:
    lines = f.readlines()
  
  print(part1(lines))
  print(part2(lines))

