#!/usr/bin/env python2.7

from wordgen import *
from arabic import *

def main():
  word = gen_word(arabic)
  print display_word(word,"english")
  print display_word(word,"arabic")
  print display_word(word,"IPA")


if __name__=="__main__":
  main()
