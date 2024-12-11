def decompress(line):
  decompressed = []
  file_id = 0

  for i, char in enumerate(line):
      count = int(char)
      if i % 2 == 0:  # even index: file length
          decompressed.extend([str(file_id)] * count)
          file_id += 1
      else:  # odd index: free space
          decompressed.extend(['.'] * count)
  return decompressed

def part1(line: str) -> int:
  decompressed = decompress(line)

  p = len(decompressed) - 1
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
  mem = decompress(line)

  # compute free space and files intervals
  files = [] 
  free_spaces = []
  current = mem[0]
  start = 0
  for i in range(1, len(mem)+1):
    if i == len(mem) or mem[i] != current:
      interval = (start, i-1)
      if current == ".":
         free_spaces.append(interval)
      else:
         files.append(interval)
      if i < len(mem):
        current = mem[i]
        start = i
  
  # reorganize the memory
  for i, (fileStart, fileEnd) in enumerate(files[::-1]): # revert files order
     for j, (start, end) in enumerate(free_spaces):
        if fileStart < end:
           break # free space is located on the right of the file -> ignore
        fileSize = fileEnd - fileStart + 1
        free_space_size = end - start + 1
        if fileSize <= free_space_size:
          mem[start:start+fileSize] = [str(len(files)-1-i)]*fileSize # i correspond to the file id (reversed !)
          mem[fileStart:fileEnd+1] = ["."]*fileSize # erase previous mem for this file
          free_spaces[j] = (start+fileSize, end)
          break # found a spot, do not treat this file again
  return sum(int(f) * i for i, f in enumerate(mem) if f != ".")


if __name__ == "__main__":
  with open("inputs/day9", "r") as f:
    lines = f.readlines()
  
  print(part1(lines[0]))
  print(part2(lines[0]))