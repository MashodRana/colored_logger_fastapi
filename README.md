# Coloured Custom Logger FastAPI

A FastAPI project featuring a custom logger with colored, emoji-enhanced log levels for both console and file outputs. Supports log rotation, custom log formatting, and a custom `SUCCESS` log level.

## Features

- **Colored Console Logs:** Log levels are color-coded and include emoji icons for quick identification.
- **File Logging:** Logs are written to files with rotation and backup support.
- **Custom Log Level:** Adds a `SUCCESS` log level between `INFO` and `WARNING`.
- **Configurable:** Easily configure log file location, size, backup count, and log level via environment variables or [`core.config.Settings`](core/config.py).
- **Thread-Safe Singleton Logger:** Ensures logging configuration is applied only once.

## Usage

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
### More Reading

[Logging in Python](https://realpython.com/python-logging/#basic-configurations)<br>
[Logging](https://github.com/madkote/fastapi-plugins/blob/master/docs/logger.md)<br>
[Three ways to configure logging for FastAPI](https://www.codeschat.com/article/145.html)<br>
[gist](https://gist.github.com/hit9/5635505)<br>
[How To Color Python Logging Output?](https://betterstack.com/community/questions/how-to-color-python-logging-output/)<br>
[Make your own custom color formatter with Python logging](https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/)
