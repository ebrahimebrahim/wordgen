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
    self.is_nucleus = self.is_vowel or self.is_liquid or self.is_nasal

  def display(self,style):
    """ Returns string to display sound, in given style.
        style is one of the following:
          'IPA': print in IPA
          'English': print in English
    """
    return self.__dict__["display_"+style]


class Language(object):
  """ Should consist of a list of Sounds, which can be imported from a csv file,
      and some lists of phonotactic constraints.
      Each constraint list should be a list of functions that return True/False based on whether something passes a constraint.
      For example, onset_constraints would be a list of functions each of which takes an onset and returns whether that onset passes a constraint.
  """
  def __init__(self):
    self.sounds = []
    self.onset_constraints = []
    self.coda_constraints = []
    self.syllable_constraints = []
    self.word_constraints = []

    # these will determine the probability of each onset/coda length showing up in generation
    # for example onset_length_distr==[0.25,0.5] means a 25% chance of 0 or 1 consonant onset, and 50% chance of 2 consonant onset
    self.onset_length_distr = []
    self.coda_length_distr = []
    
  def import_sound_list(self,csv_filename):
    f=open(csv_filename)
    rows = [row for row in csv.reader(f)]
    f.close()
    self.sounds = [Sound(rows[0],row) for row in rows[1:]]

english = Language()
english.import_sound_list("english_sounds.csv")
english.onset_length_distr = [0.3,0.6,0.9]
english.coda_length_distr = [0.8/3,2*0.8/3,0.8,0.95]
# TODO: add constraints


def gen_onset(language):
  onset = None
  r = random.random()
  onset_len = len([x for x in language.onset_length_distr if r > x])
  while onset is None or not all(constraint_holds(onset) for constraint_holds in language.onset_constraints):
    onset = [random.choice([sound for sound in language.sounds if sound.is_consonant]) for i in range(onset_len)]
  return onset

def gen_nucleus(language):
  return [random.choice([sound for sound in language.sounds if sound.is_nucleus])]

def gen_coda(language):
  coda = None
  r = random.random()
  coda_len = len([x for x in language.coda_length_distr if r > x])
  while coda is None or not all(constraint_holds(coda) for constraint_holds in language.coda_constraints):
    coda = [random.choice([sound for sound in language.sounds if sound.is_consonant]) for i in range(coda_len)]
  return coda

def gen_syllable(language):
  syllable = None
  while syllable is None or not all(constraint_holds(syllable) for constraint_holds in language.syllable_constraints):
    syllable = (gen_onset(language), gen_nucleus(language), gen_coda(language))
  return syllable

def gen_word(num_syllables,language):
  word = None
  while word is None or not all(constraint_holds(word) for constraint_holds in language.word_constraints):
    word = [gen_syllable(language) for i in range(num_syllables)]
  return word



display_subsyllable = lambda subsyllable,style : ''.join([sound.display(style) for sound in subsyllable])
display_syllable = lambda syllable,style : ''.join([display_subsyllable(subsyllable,style) for subsyllable in syllable])
display_word = lambda word,style : ''.join(display_syllable(syllable,style) for syllable in word)


def main():
  print display_word(gen_word(2,english),"English")


if __name__=="__main__":
  main()
