from json import encoder
import pprint
import random
from pygments import style
from pygments import formatter
from pygments.formatters import Terminal256Formatter as Formatter
from pyfiglet import Figlet                                        # convert strings to ASCII art
from datetime import datetime                                      # timestamps
from pygments import highlight                                     # tools for colorizing the json output
from pygments.style import Style
from pygments.token import Token
from pygments.lexers import Python3Lexer as Lexer
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic
import sys                                                         # user input

font = sys.argv[1]
text_color = sys.argv[2]
bg_color = sys.argv[3]
payload = sys.argv[4]

class MyStyle(Style):
        styles = {
            Token.String:  f'{text_color} bg:{bg_color}',
            Token.Name:    f'{text_color} bg:{bg_color}',
            Token.Comment: f'{text_color} bg:{bg_color}',
            Token.String:  f'{text_color} bg:{bg_color}',
            Token.Error:   f'{text_color} bg:{bg_color}',
            Token.Number:  f'{text_color} bg:{bg_color}',
            Token.Operator:f'{text_color} bg:{bg_color}',
            Token.Generic: f'{text_color} bg:{bg_color}'
        }

def main():
    debug = True

    settings = {
        'font': font,
        'text_color': text_color,
        'bg_color': bg_color,
        'payload': payload
    }

    graphic = get_graphic(settings, debug)

    print(graphic)

def random_color():
    color_names = [
        "ansiblack",
        "ansired",
        "ansigreen",
        "ansiyellow",
        "ansiblue",
        "ansimagenta",
        "ansicyan",
        "ansigray",
        "ansibrightblack",
        "ansibrightred",
        "ansibrightgreen",
        "ansibrightyellow",
        "ansibrightblue",
        "ansibrightmagenta",
        "ansibrightcyan",
        "ansiwhite"
    ]

    color = random.choice(color_names)
    return color

def word_art(settings, debug=False):     # returns figlet art of string input
    # more fonts http://www.figlet.org/examples.html
    f = Figlet(font=settings['font'])
    art = f.renderText(settings['payload'])
    return art

def colorize(data, debug=False):                               # prints colorful json and red text
    # Colorize it
    colorful = highlight(
        data,
        Lexer(),
        Formatter(style=MyStyle)
    )

    return colorful

def get_graphic(settings: dict, debug=False):
    try:
        art = word_art(settings, debug)
        colorized  = colorize(art, debug)
        encoded_string = colorized.encode()
    except:
        print(f"Well shit, i cant parse this {payload}")
        if debug:
            name = input("Any key to continue")

    return colorized

def get_terminal_graphic(settings: dict, debug=False):
    try:
        art = word_art(settings, debug)
        colorized  = colorize(art, debug)
        encoded_string = colorized.encode()
    except:
        print(f"Well shit, i cant parse this {payload}")
        if debug:
            name = input("Any key to continue")

    return encoded_string


main()

