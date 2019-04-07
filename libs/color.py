#!/usr/bin/python
"""Color codes for terminal output.

    re = (?:(?:(?:\\033\[)([0-3]|(?:5)))\;((?:[3][0-7]))\;((?:[4][0-7]m))((?:.*))((?:\\033\[0;37;40m)))

    group 0 = Full Match
    group 1 = Style
    group 2 = Color
    group 3 = Background
    group 4 = String
    group 5 = End Style
"""

import re
import textwrap


class text_style:
    """Class for converting style string and returning ANSI code."""

    def none(self):
        return '0'

    def bold(self):
        return '1'

    def underline(self):
        return '2'

    def negative1(self):
        return '3'

    def negative2(self):
        return '5'


class text_color:
    """Class for converting color string and returning ANSI code."""

    def white(self):
        return "37"

    def black(self):
        return "30"

    def red(self):
        return "31"

    def green(self):
        return "32"

    def blue(self):
        return "34"

    def yellow(self):
        return "33"

    def purple(self):
        return "35"

    def cyan(self):
        return "36"


class text_background:
    """Class for converting background string and returning ANSI code."""

    def white(self):
        return "47m"

    def black(self):
        return "40m"

    def red(self):
        return "41m"

    def green(self):
        return "42m"

    def blue(self):
        return "44m"

    def yellow(self):
        return "43m"

    def purple(self):
        return "45m"

    def cyan(self):
        return "46m"


def reg_checker(text, debugger=False):
    """RegEX debugger for checking converted code result.

    :param text: String to test with appropriate ANSI format.
    :param debugger: Boolean (defaults 'False') for enabling debugger messages.

    :returns True: Boolean (defaults 'True') if text change was made.
    """

    if not text:
        return False
    matchObj = re.match(r'(?:(?:(?:\\033\[)([0-3]|(?:5)))\;((?:[3][0-7]))\;((?:[4][0-7]m))((?:.*))((?:\\033\[0;37;40m)))', text)
    if matchObj.group():
        grouped = matchObj.group()
    if matchObj.group(1):
        style = matchObj.group(1)
    if matchObj.group(2):
        color = matchObj.group(2)
    if matchObj.group(3):
        background = matchObj.group(3)
    if matchObj.group(4):
        text = matchObj.group(4)
    if matchObj.group(5):
        end_style = matchObj.group(5)

    if debugger:
        wrapped_text = textwrap.TextWrapper(width=57, replace_whitespace=False).wrap(text=grouped)
        print(wrapped_text)
        print(" {:-^60}\n".format(" Style Guide "))
        print(" {: <30}".format(" Grouped: "))
        for line in wrapped_text:
            if line:
                print(" {: >59}".format(line))
        print(" {: <30}{: >29}".format(" Style: ", style))
        print(" {: <30}{: >29}".format(" Color: ", color))
        print(" {: <30}{: >29}".format(" Background: ", background))
        print(" {: <30}{: >29}\n".format(" Closing Style: ", end_style))

        print(" {:-^60}\n".format(" Text "))
        for line in textwrap.TextWrapper(width=58).wrap(text=text):
            print(" {: >59}".format(line))
    return True


def terminal_text_effect(text, **kwargs):
    """Converts string to include ANSI code for color format in terminal.

    :param text: String to be converted into ANSI format.
    :param **kwargs: See below...
    :kwargs:
        -'style' ('str') -  none, bold, underline, negative1, negative2
        -'color' ('str') -  white, black, red, green, blue, yellow, purple,
                            cyan.
        -'background' ('str') - white, black, red, green, blue, yellow, purple,
                                cyan.
        -'end_style' ('str') - Defaults to "\\033[0;37;40m" ANSI format.
        -'debugger' ('bool') - Defaults to False. Used to print messages.

    :returns result: String containing the ANSI coded style.
    """

    debugger = False
    style = text_style()
    color = text_color()
    background = text_background()
    begin_style = "\\033["
    end_style = "\\033[0;37;40m"

    if not kwargs.items():
        print("No changes were made.")
    for key, value in kwargs.items():
        if key == "style":
            style = getattr(style, value)()
        elif key == "color":
            color = getattr(color, value)()
        elif key == "background":
            background = getattr(background, value)()
        elif key == "end_style":
            end_style = getattr(end_style, value)()
        elif key == "debugger":
            debugger = value
        else:
            print("INVALID KWARG: {}={}".format(key, value))
            return

    result = (begin_style + style + ";" + color + ";" + background + text + end_style)
    if not reg_checker(result, debugger):
        print("No changes were made.")

    return result