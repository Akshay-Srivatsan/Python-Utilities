import sys

modifiers = {
	'bold' : '1m',
	'faint' : '2m',
	'italics' : '3m',
	'underline' : '4m',
	'blink': '5m',
	'fast_blink': '6m',
	'invert': '7m',
	'conceal': '8m',
	'cross-out': '9m'
}

cancel_modifiers = {
	'bold' : '21m',
	'faint' : '22m',
	'italics' : '23m',
	'underline' : '24m',
	'blink': '25m',
	'fast_blink': '26m',
	'invert': '27m',
	'conceal': '28m',
	'cross-out': '29m'
}

foreground = {
	'black' : '30m',
	'red' : '31m',
	'green' : '32m',
	'yellow' : '33m',
	'blue' : '34m',
	'magenta' : '35m',
	'cyan' : '36m',
	'grey' : '37m',
	'default' : '39m'
}

background = {
	'black' : '40m',
	'red' : '41m',
	'green' : '42m',
	'yellow' : '43m',
	'blue' : '44m',
	'magenta' : '45m',
	'cyan' : '46m',
	'grey' : '47m',
	'default' : '49m'
}

bright_foreground = {
	'black' : '90m',
	'red' : '91m',
	'green' : '92m',
	'yellow' : '93m',
	'blue' : '94m',
	'magenta' : '95m',
	'cyan' : '96m',
	'grey' : '97m',
	'default' : '39m'
}

bright_background = {
	'black' : '100m',
	'red' : '101m',
	'green' : '102m',
	'yellow' : '103m',
	'blue' : '104m',
	'magenta' : '105m',
	'cyan' : '106m',
	'grey' : '107m',
	'default' : '49m'
}

reset_color = '0m'
escape = '\033['

def reset():
	sys.stdout.write(escape + reset_color)

def set_foreground(color, bright=False):
	if color not in foreground: return
	sys.stdout.write(escape + (bright_foreground if bright else foreground)[color])

def set_background(color, bright=False):
	if color not in background: return
	sys.stdout.write(escape + (bright_background if bright else background)[color])

def set_modifier(modifier, on=True):
	if modifier not in modifiers: return
	sys.stdout.write(escape + (modifiers if on else cancel_modifiers)[modifier])

def cursor_up(lines=1):
	sys.stdout.write(escape + str(lines) + 'A')

def cursor_down(lines=1):
	sys.stdout.write(escape + str(lines) + 'B')

def cursor_forward(lines=1):
	sys.stdout.write(escape + str(lines) + 'C')

def cursor_back(lines=1):
	sys.stdout.write(escape + str(lines) + 'D')

def set_cursor_position(column, row):
	sys.stdout.write(escape + str(row+1) + ';' + str(column+1) + 'H')

def clear(command=2):
	sys.stdout.write(escape + str(command) + 'J')

def scroll_up(lines=1):
	sys.stdout.write(escape + str(lines) + 'S')

def scroll_down(lines=1):
	sys.stdout.write(escape + str(lines) + 'T')

def save_cursor_position():
	sys.stdout.write(escape + 's')

def restore_cursor_position():
	sys.stdout.write(escape + 'u')

def hide_cursor():
	sys.stdout.write(escape + '?25l')

def show_cursor():
	sys.stdout.write(escape + '?25h')

if __name__ == '__main__':
	for f in foreground:
		for b in background:
			set_foreground(f, True)
			set_background(b)
			sys.stdout.write(' Colors ')
		reset()
		print
	reset()
