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

n = 0
while(n<20):
    print(*markov.generate(16, start=['sentence', 'start']))
    n = n + 1

markov.save()

markov = Markov.load('markov.db')