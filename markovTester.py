from markovchain import MarkovBase, MarkovSqliteMixin

class Markov(MarkovSqliteMixin, MarkovBase):
    pass

markov = Markov(db='markov.db')

with open('realDonaldTrump_tweets.csv') as fp:
    markov.data(fp.read())

with open('realDonaldTrump_tweets.csv') as fp:
    for line in fp:
        markov.data(line, True)
markov.data('', False)

print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))
print(*markov.generate(16, start=['sentence', 'start']))


markov.save()

markov = Markov.load('markov.db')