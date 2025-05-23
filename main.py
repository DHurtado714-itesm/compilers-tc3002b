from Lexer import *
from Parser import *
from Translator import *
import sys

if __name__ == "__main__":
  print("----GOOD TEST CASES----")
  for i in range(1):
    parser = Parser(f"test_cases/good/prog{i + 1}.txt")
    tree = parser.analize()

    if tree != None:
      tree.eval()

    print(f"Test #{i + 1}: END")

  print("----BAD TEST CASES----")
  for i in range(1):
    try:
      parser = Parser(f"test_cases/bad/prog{i + 1}.txt")
      tree = parser.analize()

      if tree != None:
        tree.eval()

      print(f"Test #{i + 1} Passed <-- Shouln't pass")
    except Exception as e:
      print(f"Test #{i + 1} failed: {e}")
