import json
from difflib import get_close_matches

data = json.load(open('dictionary.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
      print('Did you mean %s instead' %get_close_matches(word, data.keys())[0])
      decide = input('press y for yes n for no')
      if decide == 'y':
        return data[get_close_matches(word, data.keys())[0]]
      elif decide == 'n':
        return ('We do not have that word')
      else:
        return('Please enter just y or n')

    else:
        print('We do not have that word')


word = input('Enter a word to search')
output = translate(word)

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)