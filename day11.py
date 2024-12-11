def part1(stones: list[int]) -> int:
  for i in range(25):
    new_stones = []
    for s in stones:
      if s == 0:
        new_stones.append(1)
      elif len(str(s)) % 2 == 0:
        new_stones.append(int("".join(str(s)[:len(str(s))//2])))
        new_stones.append(int("".join(str(s)[len(str(s))//2:])))
      else:
        new_stones.append(s*2024)
      stones = new_stones
  return len(stones)
      

def part2(stones: list[int]) -> int:
  counter = {}
  for stone in stones:
      counter[stone] = counter.get(stone, 0) + 1

  for _ in range(75):
    new_counter = {}
    for num, count in counter.items():
      if num == 0:
        new_counter[1] = new_counter.get(1, 0) + count
      else:
        num_str = str(num)
        if len(num_str) % 2 == 0:
            half_len = len(num_str) // 2
            left = int(num_str[:half_len])
            right = int(num_str[half_len:])
            new_counter[left] = new_counter.get(left, 0) + count
            new_counter[right] = new_counter.get(right, 0) + count
        else:
            new_val = num * 2024
            new_counter[new_val] = new_counter.get(new_val, 0) + count
        
    counter = new_counter
  return sum(counter.values())
      


if __name__ == "__main__":
  with open("inputs/day11", "r") as f:
    lines = f.readlines()
  
  stones = [int(c) for c in lines[0].split(" ")]
  
  print(part1(stones))
  print(part2(stones))