from word_renderer import WordRenderer

def main(word, positive='O', negative=' '):
	renderer = WordRenderer()
	print renderer.create_rendered_word(word, positive, negative)

if __name__ == '__main__':
	import sys
	main(*sys.argv[1:])