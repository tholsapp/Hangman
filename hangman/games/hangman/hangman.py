
from utility import get_random_word, generate_word_dict


class Hangman:

  """A hangman game

  Attributes:
         key_word: word to be guessed
             size: length of word to be guessed
        word_dict: dictionary of key_word characters and positions
    chars_guessed: dictionary of all guessed chars through game
  """

  def __init__(self):
    """Return a new HangmanGame object"""
    self.key_word   = get_random_word("data/words.txt")
    self.size       = len(self.key_word)
    self.word_dict  = generate_word_dict(self.key_word)
    self.chars_guessed = {}

  def submit_guess(self, guess):
    if guess in self.chars_guessed: # check if guess has been guessed previosly
      return [-1]
    if guess in self.word_dict: # correct guess has been made
      char_coordinates = self.word_dict[guess]      # coordinate of guess
      self.chars_guessed[guess] = char_coordinates  # track guess
      return char_coordinates   # return coordinates of guess
    else: # wrong guess
      self.chars_guessed[guess] = [-1]
    return [-1]

