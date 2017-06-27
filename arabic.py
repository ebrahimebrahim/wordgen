#!/usr/bin/env python2.7

from wordgen import *

def nucleus_constraint(nucleus):
  if len([sound for sound in nucleus if sound.is_vowel]) != 1: return False
  if len(nucleus) == 3 and not nucleus[1].is_vowel: return False
  return True

def eibage(word):
  for i in range(len(word)-1):
    s1 = word[i]
    s2 = word[i+1]
    if len(s1[2])==2 and s2[0]: return False
    if not s1[2] and not s2[0]: return False
  return True

arabic = Language()
arabic.import_sound_list("arabic_sounds.csv")
arabic.length_distr['onset'] = [0.5]
arabic.length_distr['nucleus'] = [0,0.80,0.975]
arabic.length_distr['coda'] = [0.45,0.90]
arabic.length_distr['word'] = [0.5,0.9,0.97,0.995]
arabic.pool['onset'] = [sound for sound in arabic.sounds if sound.is_consonant and not sound.is_glide]
arabic.pool['nucleus'] = [sound for sound in arabic.sounds if sound.is_vowel or sound.is_glide]
arabic.pool['coda'] = [sound for sound in arabic.sounds if sound.is_consonant and not sound.is_glide]
arabic.constraints['nucleus'] += [nucleus_constraint]
arabic.constraints['word'] += [eibage]
