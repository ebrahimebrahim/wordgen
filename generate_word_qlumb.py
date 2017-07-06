#!/usr/bin/env python2.7

from wordgen import *
from qlumb import *

def main():
  word = gen_word(qlumb)
  print display_word(word,"qlumb")
  print display_word(word,"IPA")

if __name__=="__main__":
  main()
