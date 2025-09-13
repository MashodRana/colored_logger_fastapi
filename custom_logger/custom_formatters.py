import logging


class Color:
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

    @classmethod
    def get_colored_text(cls, text, color=None):
        color = cls.COLORS.get(color, 37)
        return f"{cls.PREFIX}{color}m{text}{cls.SUFFIX}"
        # return (self.PREFIX + '%dm%s' + self.SUFFIX) % (color, text)


class ConsoleFormatter(logging.Formatter):
    MAPPED_LEVEL = {
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bgred',
        'DEBUG': 'cyan',
        'SUCCESS': 'green'
    }

    LEVEL_ICONS = {
        'SUCCESS': '✅',
        'DEBUG': '🐛',
        'INFO': 'ℹ️',
        'WARNING': '⚠️',
        'ERROR': '❌',
        'CRITICAL': '🔥',
    }

    MAX_LEVEL_LEN = max(len(level) for level in MAPPED_LEVEL.keys()) + 1

    def format(self, record: logging.LogRecord) -> str:
        icon = self.LEVEL_ICONS[record.levelname]
        color: str = self.MAPPED_LEVEL.get(record.levelname, 'white')
        # Align levelname to max length
        level_name = f"{record.levelname}:"
        padded_level_name = f"{level_name:<{self.MAX_LEVEL_LEN}}"
        colored_text = Color().get_colored_text(text=padded_level_name, color=color)

        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        return f"{colored_text} | {record.asctime} | message: {record.getMessage()}"
