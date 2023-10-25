words = 'de kat lafhg dieren dan die da abacadabra oesterzwamen anderenhalfmeter'.split()

def aantal_a(word):
    return word.count('a')

def aantal_klinkers(word):
    return sum(word.count(vowel) for vowel in 'aeiou')
  
print(sorted(words, key = lambda word: sum(word.count(vowel) for vowel in 'aeiou')))
