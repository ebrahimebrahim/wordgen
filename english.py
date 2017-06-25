#!/usr/bin/env python2.7

from wordgen import *

DJ = 'd\xca\x92'
TH_V = '\xc3\xb0'
NG = '\xc5\x8b'
SH = '\xca\x83'
CH = 't'+SH
TH_U = '\xce\xb8'
SJ = '\xca\x92'

def onset_constraint(onset):
  ipa = [sound.display_IPA for sound in onset]
  if NG in ipa: return False
  if len(onset)>1 and ('h' in ipa or any(sound.is_affricate for sound in onset)): return False
  for i in range(len(onset)-1):
    c1 = onset[i]
    c2 = onset[i+1]
    if c2.display_IPA=='hw' : return False
    if not c1.is_obstruent : return False
    if c1.display_IPA == 's':
      if not (c2.is_nasal or c2.is_liquid or c2.is_glide or (c2.is_obstruent and not c2.is_voiced and not c2.display_IPA==SH)): return False
    else:
      if not (c2.is_liquid or c2.is_glide): return False
  return True
  

def nucleus_constraint(nucleus):
  if not all(sound.is_vowel for sound in nucleus): return False
  return True


CODA_TABLE = [ (['p','f'],[TH_U,'s','t']),
               ([TH_U,'k'],['s','t']),
               (['t'],['s']),
               ([CH,SH],['t']),
               (['s'],['t','k','p']),
               ([NG],['k','d','z','g']),
               (['m'],['p','d','z','b']),
               (['z',SJ,DJ],['d']),
               (['b','g','v',TH_V],['d','z']),
               (['d'],['z']),
               (['l'],[TH_U,'s','t','k','p',CH,DJ,'d','z',SH,'f','v','m','n']),
               (['r'],[TH_U,'s','t','k','p',CH,DJ,'d','z',SH,'f','v','m','n','l']),
               (['n'],[TH_U,'s','t',CH,DJ,'d','z']),
               (['z',SJ,'v',TH_V,'l','r'],['g','b']) ]

def coda_constraint(coda):
  if 'hw' in [sound.display_IPA for sound in coda]: return False
  if 'h' in [sound.display_IPA for sound in coda]: return False
  if any(sound.is_glide for sound in coda): return False
  for i in range(len(coda)-1):
    c1 = coda[i]
    c2 = coda[i+1]
    if not any((c1.display_IPA in first_group and c2.display_IPA in second_group) for first_group,second_group in CODA_TABLE): return False
  return True


english = Language()
english.import_sound_list("english_sounds.csv")
english.onset_length_distr = [0.4,0.8,0.95]
#english.onset_length_distr = [0.3,0.6,0.9]
english.coda_length_distr = [0.5,0.75,0.93,0.9851]
#english.coda_length_distr = [0.8/3,2*0.8/3,0.8,0.95]
english.onset_constraints += [onset_constraint]
english.nucleus_constraints += [nucleus_constraint]
english.coda_constraints += [coda_constraint]
