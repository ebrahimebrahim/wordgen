#!/usr/bin/env python2.7

from wordgen import *
from english import *

def main():
  r = random.random()
  num_syllables = len([x for x in [0.5,0.9,0.97,0.995] if r > x]) + 1
  word = gen_word(num_syllables,english)
  print display_word(word,"English")
  print display_word(word,"IPA")


if __name__=="__main__":
  main()
