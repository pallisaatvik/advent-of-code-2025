def is_repeat_n(inp, n):
  # checks for n length sequences
  if len(inp) % n != 0:
    return False
  slices = [inp[i: i+n] for i in range(0, len(inp), n)]
  return all([i == slices[0] for i in slices])

# # no longer needed
# def is_repeat_twice(inp):
#   if len(inp) % 2 == 1:
#     # Odd length can't repeat twice
#     return False
#   return inp[0:len(inp)//2] == inp[len(inp)//2:]

# Return the sum of invalid IDs
def solve_range(start, end, any_length=True):
  # print(f"{start}-{end}")
  finds = 0
  for i in range(start, end+1):
    # substring lengths to check
    num_check = str(i)
    check_indexes = [len(num_check)//2]
    
    if any_length:
      check_indexes = [i for i in range(1, len(num_check)//2 + 1)]
    
    for index in check_indexes:
      if is_repeat_n(num_check, index):
        finds += i
        # alr know its invalid
        # print(i)
        break
  return finds


def test():
  print(is_repeat_n("111", 1))
  ranges = [
    "11-22","95-115","998-1012","1188511880-1188511890","222220-222224",
    "1698522-1698528","446443-446449","38593856-38593862","565653-565659",
    "824824821-824824827","2121212118-2121212124"
  ]

  sum = 0

  for range in ranges:
    start, end = range.split("-")
    start = int(start)
    end = int(end)
    sum += solve_range(start, end)
  print(sum)


def main():
  ranges = []
  for line in open("input/input02.txt"):
    ranges.extend(line.split(','))

  sum = 0

  for range in ranges:
    start, end = range.split("-")
    start = int(start)
    end = int(end)
    sum += solve_range(start, end)
  print(sum)


test()