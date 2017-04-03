# To run: ~/.local/bin/irc3 config.ini
from irc3.plugins.command import command
import irc3
import markovify

with open("corpus") as f: text = f.read()

text_model = markovify.NewlineText(text)

def getline(): return text_model.make_sentence(tries=100, max_overlap_total=25)

@irc3.plugin
class Plugin(object):
	def __init__(self, bot):
		self.bot = bot

	@command(permission='view')
	def say(self, mask, target, args):
		yield getline()
