#!/usr/bin/env python2.7

from wordgen import *

def nucleus_constraint(nucleus):
  if len([sound for sound in nucleus if sound.is_vowel]) != 1: return False
  if not all(sound.is_vowel or sound.is_glide for sound in nucleus): return False
  if len(nucleus) == 3 and not nucleus[1].is_vowel: return False
  return True

def eibage(word):
  for i in range(len(word)-1):
    s1 = word[i]
    s2 = word[i+1]
    if len(s1[2])==2 and s2[0]: return False
    if not s1[2] and not s2[0]: return False
  return True

def no_glides(subsyllable):
  if any(sound.is_glide for sound in subsyllable): return False
  return True

arabic = Language()
arabic.import_sound_list("arabic_sounds.csv")
arabic.onset_length_distr = [0.5]
arabic.nucleus_length_distr = [0,0.80,0.975]
arabic.coda_length_distr = [0.45,0.90]
arabic.nucleus_constraints += [nucleus_constraint]
arabic.word_constraints += [eibage]
arabic.onset_constraints += [no_glides]
arabic.coda_constraints += [no_glides]
