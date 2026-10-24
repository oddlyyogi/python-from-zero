lines = ["4.5", "", "-20", "900", "-3.25"]

def read_amounts(lines):
    for line in lines:
        print("reading", repr(line))
        line = line.strip()
        if not line:
            continue
        yield float(line)

spend = (a for a in read_amounts(lines) if a < 0)
print(sum(spend))
print(list(spend))
