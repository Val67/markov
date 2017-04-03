import markovify

with open("corpus") as f: text = f.read()

text_model = markovify.NewlineText(text)

print(text_model.make_sentence(tries=100, max_overlap_total=25))
