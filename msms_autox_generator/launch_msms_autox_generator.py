from contextlib import redirect_stdout
from io import StringIO
import webview
from gui import app


if __name__ == '__main__':
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window(f'fleX MS/MS AutoXecute Generator 0.4.0b0', app.server)
        webview.start()
