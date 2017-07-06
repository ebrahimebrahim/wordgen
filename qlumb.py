#!/usr/bin/env python2.7

from wordgen import *

def onset_constraint(onset):
  return len(onset) <= 1 or onset[1].display_IPA=='l'

def coda_constraint(coda):
  return len(coda) <= 1 or coda[0].display_IPA=='r'

qlumb = Language()
qlumb.import_sound_list("qlumb_sounds.csv")
qlumb.length_distr['onset'] = [0,0.67]
qlumb.length_distr['nucleus'] = [0]
qlumb.length_distr['coda'] = [0,0.67]
qlumb.length_distr['word'] = [0.75,0.95,0.99]
qlumb.constraints['onset'] += [onset_constraint]
qlumb.pool['nucleus'] = [sound for sound in qlumb.sounds if sound.is_vowel]
qlumb.constraints['coda'] += [coda_constraint]
qlumb.constraints['word'] += []
