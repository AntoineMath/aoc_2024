import numpy as np
import os


def part1(lines):
  width = 101
  height = 103
  robots = []
  for l in lines:
    x, y = l.split(" ")[0].split("=")[1].split(",")
    vx, vy = l.split(" ")[1].split("=")[1].split(",")
    robots.append((int(x), int(y), int(vx), int(vy)))
  
  for _ in range(100):
      robots = [
          ((x + vx) % width, (y + vy) % height, vx, vy)
          for x, y, vx, vy in robots
      ]

  quadrants = [0, 0, 0, 0]
  for x, y, _, _ in robots:
      if x < width // 2 and y < height // 2:
          quadrants[0] += 1  # Top-left
      elif x > width // 2 and y > height // 2:
          quadrants[3] += 1  # Bottom-right
      elif x > width // 2 and y < height // 2:
          quadrants[1] += 1  # Top-right
      elif x < width // 2 and y > height // 2:
          quadrants[2] += 1  # Bottom-left

  return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

def part2(lines):
   return "Stupid problem"    


if __name__ == "__main__":
  with open("inputs/day14", "r") as f:
    lines = f.readlines()
  
  print(part1(lines))
  print(part2(lines))

