class CodeNumber:
  def __init__(self, start):
    self.val = start
    self.zero_count = 0
    self.cross_count = 0

  def rotate(self, rotation, op):
    start_zero = self.val in [0, 100]

    if op == '-':      
      self.val -= rotation
    elif op == '+':
      self.val += rotation
    
    # yoikes
    if self.val != self.val % 100 and not start_zero and self.val not in [0, 100]:
      self.cross_count += 1
      
    self.val = self.val % 100
    
    if self.val == 0:
      self.zero_count += 1

  def read_num(self, input):
    num = int(input[1:])
    self.cross_count += num // 100
    num = num % 100
    code = input[0]

    if code == 'L':
      self.rotate(num, '-')
    elif code == 'R':
      self.rotate(num, "+")

def main():
  test_case = [
    'L68',
    'L30',
    'R48',
    'L5',
    'R60',
    'L55',
    'L1',
    'L99',
    'R14',
    'L82'
  ]

  # safe_test = CodeNumber(50)
  # for instr in test_case:
  #   safe_test.read_num(instr)
  # print(safe_test.zero_count, safe_test.cross_count)

  safe = CodeNumber(50)

  for line in open('python/input01.txt'):
    safe.read_num(line.strip())
  
  print(safe.zero_count)
  print(safe.zero_count + safe.cross_count)

main()