#!/usr/bin/env python2.7

from wordgen import *
from english import *

def main():
  word = gen_word(english)
  print display_word(word,"english")
  print display_word(word,"IPA")

if __name__=="__main__":
  main()
