
import random

def get_random_word(fobj):
  """Return random line in given file"""
  with open(fobj) as f:
    contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0,len(lines))
    return lines[line_number]

def generate_word_dict(word):
  word_dict = {}  # dictionary of word
  i = 0           # position of char in word
  for key in word:
    if key in word_dict:
      word_dict[key].append(i)
    else:
      word_dict[key] = [i]
    i = i + 1
  return word_dict


