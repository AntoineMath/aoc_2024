from collections import defaultdict
def part1(rules, pages) -> int:
  ans = 0
  rules_dict = defaultdict(set)

  for r in rules.split("\n"):
      start, end = r.strip().split("|")
      rules_dict[start].add(end)

  for line in pages.split("\n"):
      update = line.split(",")
      valid = True
      seen = set()
      for nb in update:
          nb = nb.strip()
          if nb in rules_dict:
              end_pages = rules_dict[nb]
              if end_pages & seen:  # Only check for overlap; no need for 'seen' to be True
                  valid = False
                  break
          seen.add(nb)
      if valid:
          ans += int(update[len(update)//2]) 
  return ans



def part1(rules, pages) -> int:
  ans = 0
  rules_dict = defaultdict(set)

  for r in rules.split("\n"):
      start, end = r.strip().split("|")
      rules_dict[start].add(end)

  for line in pages.split("\n"):
      update = line.split(",")
      valid = True
      seen = set()
      pos = 0
      for nb in update:
          nb = nb.strip()
          if nb in rules_dict:
              end_pages = rules_dict[nb]
              if end_pages & seen:  # Only check for overlap; no need for 'seen' to be True
                  valid = False
                  break
          seen.add(nb)
          pos += 1
      if not valid:
        # rearange
        invalid_nb = update[pos]
        nums_set = set(update)

        ans += int(update[len(update)//2]) 
  return ans


if __name__ == "__main__":
  with open("inputs/day5", "r") as f:
    txt = f.read()
  
  rules, pages = txt.split("\n\n")

  rules_dict = {k: v for k, v in (r.strip().split("|") for r in rules.split("\n"))}
  rules_list = [[int(start), int(end)] for start, end in (r.strip().split("|") for r in rules.split("\n"))]
  print(part1(rules, pages))
  

