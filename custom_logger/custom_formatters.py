import logging


class LogLevelFormatter:
    # ANSI escape codes for coloring text in console
    COLORS = {
        "grey": "\x1b[38;20m",
        "blue": "\x1b[34;20m",
        "cyan": "\x1b[36;20m",
        "green": "\x1b[32;20m",
        "yellow": "\x1b[33;20m",
        "red": "\x1b[31;20m",
        "bold_red": "\x1b[31;1m",
        "reset": "\x1b[0m",
    }

    LEVEL_COLOR_MAPPING = {
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
        'DEBUG': 'cyan',
        'SUCCESS': 'green'
    }

    # Log level icons with emoji + name
    LEVEL_ICONS = {
        "SUCCESS": "✅  SUCCESS",
        "DEBUG": "🐛 DEBUG",
        "INFO": "ℹ️ INFO",
        "WARNING": "⚠️ WARNING",
        "ERROR": "❌  ERROR",
        "CRITICAL": "🔥 CRITICAL",
    }

    @classmethod
    def get_colored_text(cls, text: str, color: str) -> str:
        """
        Wrap the given text with ANSI color codes.
        If the color is not defined, default to grey.
        Example: get_colored_text("INFO", "blue") → "\x1b[34;20mINFO\x1b[0m"
        """
        return f"{cls.COLORS.get(color, cls.COLORS['grey'])}{text}{cls.COLORS['reset']}"

    @classmethod
    def get_colored_levels(cls):
        """
        Returns a dictionary mapping each log level to its colored version.
        Example: {'INFO': '\x1b[34;20mINFO\x1b[0m', ...}
        """
        return {level: cls.get_colored_text(level, color) for level, color in cls.LEVEL_COLOR_MAPPING.items()}

    @classmethod
    def get_levels_with_icon(cls):
        """
         Returns log levels combined with their emoji icon and properly padded for alignment.
         Example: {'INFO': 'ℹ️ INFO:   ', 'ERROR': '❌ ERROR:  ', ...}
        """
        icon_levels = {}
        max_len = max(len(level) for level in cls.LEVEL_ICONS.values())
        for level, level_with_icon in cls.LEVEL_ICONS.items():
            level_text = f"{level}:"  # Adding colon with the level

            # Doing the alignment by padding
            icon_levels[level] = f"{level_with_icon.split()[0]} {level_text:<{max_len}}"
        return icon_levels

    @classmethod
    def get_colored_levels_with_icon(cls):
        """
        Returns a dictionary mapping each log level to a colored + emoji + padded string.
        Example: {'INFO': 'ℹ️ \x1b[34;20mINFO\x1b[0m:   ', ...}
        """
        colored_levels = cls.get_colored_levels()
        icon_colored_levels = {}
        for level, level_icon in cls.LEVEL_ICONS.items():
            colored_level = colored_levels.get(level)
            icon_colored_level = level_icon.replace(level, colored_level)
            icon_colored_levels[level] = icon_colored_level
        max_len = max(len(level) for level in icon_colored_levels.values()) + 1
        for level, text in icon_colored_levels.items():
            padded_level_name = f"{text:<{max_len}}"
            icon_colored_levels[level] = padded_level_name

        return icon_colored_levels


class ConsoleFormatter(logging.Formatter):
    __icon_colored_levels = None

    @property
    def icon_colored_levels(self):
        if ConsoleFormatter.__icon_colored_levels is None:
            ConsoleFormatter.__icon_colored_levels = LogLevelFormatter.get_colored_levels_with_icon()
        return ConsoleFormatter.__icon_colored_levels

    def format(self, record: logging.LogRecord) -> str:
        icon_colored_level = self.icon_colored_levels.get(record.levelname)
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        return f"{icon_colored_level} {record.asctime} | message: {record.getMessage()}"


class FileFormatter(logging.Formatter):
    __icon_levels = None

    @property
    def levels_with_icon(self):
        if FileFormatter.__icon_levels is None:
            FileFormatter.__icon_levels = LogLevelFormatter.get_levels_with_icon()
        return FileFormatter.__icon_levels

    def format(self, record: logging.LogRecord) -> str:
        level_name = self.levels_with_icon.get(record.levelname)
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        return f"{level_name} {record.asctime} | message: {record.getMessage()}"
