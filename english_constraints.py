#!/usr/bin/env python2.7

DJ = 'd\xca\x92'
TH_V = '\xc3\xb0'
NG = '\xc5\x8b'
SH = '\xca\x83'
CH = 't'+SH
TH_UV = '\xce\xb8'
SJ = '\xca\x92'

def onset_constraint(onset):
  ipa = [sound.display_IPA for sound in onset]
  if NG in ipa: return False
  if len(onset)>1 and ('h' in ipa or any(sound.is_affricate for sound in onset)): return False
  for i in range(len(onset)-1):
    c1 = onset[i]
    if not c1.is_obstruent: return False
    c2 = onset[i+1]
    if c1.display_IPA == 's':
      if not (c2.is_nasal or c2.is_liquid or c2.is_glide or (c2.is_obstruent and not c2.is_voiced and not c2.display_IPA==SH)): return False
    else:
      if not (c2.is_liquid or c2.is_glide): return False
  return True
  

def nucleus_constraint(nucleus):
  return True


def coda_constraint(coda):
  return True

