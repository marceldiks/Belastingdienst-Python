import string

s = r"""\
Hebt u in juli 2023 een brief gekregen waarin wij lieten weten dat wij uw betalingsregeling voor het bijzonder uitstel vanwege de coronacrisis gingen intrekken? En hebt u - ondanks een eventuele actie - nog steeds een betalingsachterstand? Dan kunt u vanaf eind september 2023 aanmaningen verwachten voor alle belastingaanslagen waarvoor u bijzonder uitstel van betaling hebt gekregen.
Bent u ondernemer en lukt het u niet uw belastingschuld en andere schulden te betalen? Dan kunt u misschien een saneringsakkoord sluiten. Dat wil zeggen dat u met al uw schuldeisers afspreekt dat u maar een deel van uw schulden betaalt. Vanwege de coronacrisis gingen wij soepeler om met 1 van onze voorwaarden om mee te werken aan een saneringsakkoord. Dat blijven wij doen tot 1 april 2024.
Hebt u in april 2023 een brief gekregen waarin stond dat u niet voldeed aan de voorwaarden voor de betalingsregeling voor het bijzonder uitstel vanwege de coronacrisis? En hebt u daarna niets gedaan? Dan sturen wij u in juli 2023 een brief waarin wij u laten weten dat wij uw betalingsregeling intrekken."""

# clean up
s = s.lower().translate(str.maketrans('áäâàéëêèíïìîóöôòúüûù', 
                                      'aaaaeeeeiiiioooouuuu', 
                                      string.punctuation))

words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    d[word] = words.count(word)

for word, n in sorted(d.items()):
    print(f'{word:25}: {n:3} {"*" * n}')
    












# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')








# or with a dict comprehension
d = {word: words.count(word) for word in set(words)}

# for word, n in sorted(d.items()):
#     print(f'{word:20}: {n:3} {"*" * n}')

# from operator import itemgetter
# for word, n in sorted(d.items(), key = itemgetter(1, 0), reverse = True):
#    print(f'{word:20}: {n:3}')

# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')

# def get_values(item):
#     return item[1]
#
# for word, n in sorted(d.items(), key=get_values, reverse=True):
#     # print(word, n)
#     # print('%-25s: %3d' % (word, n))
#     print(f'{word:<25}: {n:3}')
#     # or
#     print('%-15s: %3d %s' % (word, n, '*' * n))



# # or with collection.Counter
# from collections import Counter
# d = Counter(s.lower().translate(str.maketrans('', '', string.punctuation)).split())
# print(d)
