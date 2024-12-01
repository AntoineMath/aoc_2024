from collections import defaultdict

def day1(left, right) -> int:
  return sum([abs(int(r)-int(l)) for l, r in zip(left, right)])

def day2(left, right) -> int:
  right_freq = defaultdict(int)
  for n in right:
    right_freq[n] += 1
  return sum([int(n)*right_freq[n] for n in left])


if __name__ == "__main__":
  with open("inputs/day1", "r") as f:
    lines = f.readlines()

  left = sorted([l.split(" ")[0].strip() for l in lines])
  right = sorted([l.split("   ")[1].strip() for l in lines])
  
  print(day1(left, right))
  print(day2(left, right))

  # time complexity: O(n log n) (timsort in python)
  # space complexity: O(n)