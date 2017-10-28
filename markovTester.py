from pymarkovchain import MarkovChain


# Create an instance of the markov chain. By default, it uses MarkovChain.py's location to
# store and load its database files to. You probably want to give it another location, like so:
mc = MarkovChain("./markov")

# To generate the markov chain's language model, in case it's not present
mc.generateDatabase("This is a string of Text. It won't generate an interesting database though.")
# To let the markov chain generate some text, execute
mc.generateString()