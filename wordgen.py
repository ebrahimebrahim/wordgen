#!/usr/bin/env python2.7

# A syllable is a tuple consisting of an onset, a nucleus, and a coda,
# each of which is a list of Sounds.
# A word is a list of syllables.

# A language is a pair consisting of a list of Sounds and a list of phonotactic constraints,
# where a phonotactic constraint is a function that, given a syllable, returns whether or not the syllable passes.

class Sound(object):
  """ A phone/phoneme (don't care about difference for now).
 
      Initialized using a csv table.

      Args:
        header: header row of table, a list of strings
        row: row of table representing this sound, a list of strings
  """
  def __init__(self, header, row):
    raise Exception("not implemented")

  def display(self,style):
    """ Returns string to display sound, in given style.
        style is one of the following:
          'IPA': print in IPA
          'English': print in English
    """
    raise Exception("not implemented")


# TODO: define "english"


def gen_onset(sounds):
  raise Exception("not implemented")

def gen_nucleus(sounds):
  raise Exception("not implemented")

def gen_coda(sounds):
  raise Exception("not implemented")

def phonotactic(syllable,constraints):
  """ Returns True if syllable meets phonotactic constraints.
      Otherwise returns False, and returns False if syllable is None.
  """
  if syllable is None: return False
  return all(constraint_holds(syllable) for constraint_holds in constraints)

def gen_syllable(language):
  sounds,constraints = language
  syllable = None
  while not phonotactic(syllable,constraints):
    syllable = (gen_onset(sounds), gen_nucleus(sounds), gen_coda(sounds))
  return syllable


def gen_word(num_syllables,language):
  return [gen_syllable(language) for i in range(num_syllables)]



display_subsyllable = lambda subsyllable,style : ''.join([sound.display(style) for sound in subsyllable])
display_syllable = lambda syllable,style : ''.join([display_subsyllable(subsyllable,style) for subsyllable in syllable])
display_word = lambda word,style : ''.join(display_syllable(syllable,style) for syllable in word)


def main():
  print display_word(gen_word(2,english),"English")


if __name__=="__main__":
  main()
