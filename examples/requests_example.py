import requests
from textual.app import App, ComposeResult

from textual_html import HTML

# URL = "https://blog.mozilla.org/en/products/firefox/reader-view/"
URL = "http://example.com/"


class ExampleApp(App):
    def compose(self) -> ComposeResult:
        yield HTML()

    def on_mount(self) -> None:
        req = requests.get(URL)
        self.query_one(HTML).update(req.text)


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
