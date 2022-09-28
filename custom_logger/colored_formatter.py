import logging


class Color(object):
    """
     utility to return ansi colored text.
    """

    COLORS = {
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'white': 37,
        'bgred': 41,
        'bggrey': 100
    }

    PREFIX = '\033['
    SUFFIX = '\033[0m'

    def get_colored_text(self, text, color=None):
        color = self.COLORS.get(color, 37)
        return f"{self.PREFIX}{color}m{text}{self.SUFFIX}"
        # return (self.PREFIX + '%dm%s' + self.SUFFIX) % (color, text)


class ColorFormatter(logging.Formatter):
    MAPPED_LEVEL = {
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bgred',
        'DEBUG': 'cyan',
        'SUCCESS': 'green'
    }

    def format(self, record: logging.LogRecord) -> str:
        color: str = self.MAPPED_LEVEL.get(record.levelname, 'white')
        color_obj = Color()
        colored_text = color_obj.get_colored_text(text=record.levelname, color=color)

        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        return f"{colored_text}:\t  Time: {record.asctime} | message: {record.getMessage()}"



