import requests
from textual.app import App, ComposeResult

from textual_html import HTML

# URL = "https://blog.mozilla.org/en/products/firefox/reader-view/"
URL = "http://example.com/"


class ExampleApp(App):
    def __init__(self, html: str):
        super().__init__()
        self.html = html

    def compose(self) -> ComposeResult:
        yield HTML(self.html)


if __name__ == "__main__":
    req = requests.get(URL)
    html = req.text
    app = ExampleApp(html)
    app.run()
