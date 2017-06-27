#!/usr/bin/env python2.7

import csv,random

# A syllable is a tuple consisting of an onset, a nucleus, and a coda,
# each of which is a list of Sounds.
# A word is a list of syllables.


class Sound(object):
  """ A phone/phoneme (don't care about difference for now).
 
      Initialized using a csv table.

      Args:
        header: header row of table, a list of strings
        row: row of table representing this sound, a list of strings
  """
  def __init__(self, header, row):
    for key,val in zip(header,row):
      if key[0:3] == "is_" :
        val = True if val == 'y' else False
      self.__dict__[key]=val
    self.is_consonant = not self.is_vowel
    self.is_continuant = not self.is_stop and not self.is_affricate
    self.is_obstruent = self.is_fricative or (self.is_stop and not self.is_nasal)

  def display(self,style):
    """ Returns string to display sound, in given style.
        style is one of the following:
          'IPA': print in IPA
          'English': print in English
    """
    return self.__dict__["display_"+style]

  def __eq__(self,other):
    return self.display_IPA == other.display_IPA

def no_doubles(subsyllable):
  for i in range(len(subsyllable)-1):
    if subsyllable[i] == subsyllable[i+1]:
      return False
  return True

class Language(object):
  """ Should consist of a list of Sounds, which can be imported from a csv file,
      and some lists of phonotactic constraints.
      Each constraint list should be a list of functions that return True/False based on whether something passes a constraint.
      For example, onset_constraints would be a list of functions each of which takes an onset and returns whether that onset passes a constraint.
  """
  def __init__(self):
    self.sounds = []
    self.constraints = { 'onset':[no_doubles],
                         'nucleus':[],
                         'coda':[no_doubles],
                         'syllable':[],
                         'word':[] }

    # these will determine the probability of each onset/coda length showing up in generation
    # for example onset_length_distr==[0.25,0.5] means a 25% chance of 0 or 1 consonant onset, and 50% chance of 2 consonant onset
    self.length_distr = { 'onset':[],
                          'nucleus':[],
                          'coda':[],
                          'word':[] }

    self.pool = { 'onset':[],
                  'nucleus':[],
                  'coda':[] }
    
  def import_sound_list(self,csv_filename):
    f=open(csv_filename)
    rows = [row for row in csv.reader(f)]
    f.close()
    self.sounds = [Sound(rows[0],row) for row in rows[1:]]
    self.pool['onset']   = [sound for sound in self.sounds if sound.is_consonant]
    self.pool['nucleus'] = [sound for sound in self.sounds if sound.is_vowel or sound.is_liquid or sound.is_nasal]
    self.pool['coda']    = [sound for sound in self.sounds if sound.is_consonant]

def gen_subsyllable(language,subsyllable_type):
  subsyllable = None
  r = random.random()
  subsyllable_len = len([x for x in language.length_distr[subsyllable_type] if r > x])
  while subsyllable is None or not all(constraint_holds(subsyllable) for constraint_holds in language.constraints[subsyllable_type]):
    subsyllable = [random.choice(language.pool[subsyllable_type]) for i in range(subsyllable_len)]
  return subsyllable

def gen_syllable(language):
  syllable = None
  while syllable is None or not all(constraint_holds(syllable) for constraint_holds in language.constraints['syllable']):
    syllable = tuple(gen_subsyllable(language,subsyllable_type) for subsyllable_type in ('onset','nucleus','coda'))
  return syllable

def gen_word(language):
  word = None
  r = random.random()
  num_syllables = len([x for x in language.length_distr['word'] if r > x]) + 1
  while word is None or not all(constraint_holds(word) for constraint_holds in language.constraints['word']):
    word = [gen_syllable(language) for i in range(num_syllables)]
  return word



display_subsyllable = lambda subsyllable,style : ''.join([sound.display(style) for sound in subsyllable])
display_syllable = lambda syllable,style : ''.join([display_subsyllable(subsyllable,style) for subsyllable in syllable])
display_word = lambda word,style : '-'.join(display_syllable(syllable,style) for syllable in word)
