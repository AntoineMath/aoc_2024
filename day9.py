def decompress(line):
  decompressed = []
  file_id = 0

  for i, char in enumerate(line):
      count = int(char)
      if i % 2 == 0:  # Even index: file length
          decompressed.extend([str(file_id)] * count)
          file_id += 1
      else:  # Odd index: free space
          decompressed.extend(['.'] * count)
  return decompressed

def part1(line: str) -> int:
  # decompress
  decompressed = decompress(line)

  p = len(decompressed) - 1  # Start from the end
  for i in range(len(decompressed)):
      if decompressed[i] == '.':
          while p > i and decompressed[p] == '.':
              p -= 1
          if p > i:
              decompressed[i] = decompressed[p]
              decompressed[p] = '.'
          else:
              break

  pts_nb = decompressed.count('.')

  return sum(int(n) * i for i, n in enumerate(decompressed[:-pts_nb] if pts_nb > 0 else decompressed))


def part2(line: str) -> int:
  decompressed = decompress(line)
  free_spaces = []
  print(decompressed)
  # compute blocks of free space
  p = 0
  while p < len(decompressed):
    if decompressed[p] == ".":
      idx = p
      size = 0
      while decompressed[p] == ".":
        p+=1
        size += 1
      free_spaces.append((idx, size))
    p+=1
  
  # replace

  




if __name__ == "__main__":
  with open("inputs/day9", "r") as f:
    lines = f.readlines()
  
  print(part1(lines[0])) # one line
  print(part2(lines[0]))
  

