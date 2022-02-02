def text_to_bin(text):
	return ' '.join(format(ord(x), 'b') for x in text)
def bin_to_text(bin):
	return "".join([chr(int(binary, 2)) for binary in bin.split(" ")])
mode = input('e/d: ')
if mode.lower() == 'e':
	text = input('Text to encrypt: ')
	bin = text_to_bin(text)
	vid = bin.replace('1', 'Ø').replace('0', 'ø').replace(' ', 'þ')
	input(vid)
elif mode.lower() == 'd':
	vid = input('Text to decrypt: ')
	bin = vid.replace('Ø', '1').replace('ø', '0').replace('þ', ' ')
	text = bin_to_text(bin)
	input(text)
