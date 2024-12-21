def part(patterns: list[str], designs: list[str], part: int) -> int:
    ans = 0
    for d in designs:
        mem = {}
        if part == 1:
            if dfs(d, patterns, mem) > 0:
                ans += 1
        if part == 2: ans += dfs(d, patterns, mem)
    return ans


def dfs(word, patterns, mem):
    if word in mem:
        return mem[word]
    if word == "":
        return 1
    ans = 0
    for p in patterns:
        if word.startswith(p):
            ans += dfs(word[len(p):], patterns, mem)
    mem[word] = ans
    return mem[word]



if __name__ == "__main__":
    with open("inputs/day19", "r") as f:
        text = f.read()

    patterns, designs = text.split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")
    print(part(patterns, designs, 1))
    print(part(patterns, designs, 2))


