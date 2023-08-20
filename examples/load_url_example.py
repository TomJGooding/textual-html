from textual.app import App, ComposeResult

from textual_html import HTML

# EXAMPLE_URL = "http://example.com/"
EXAMPLE_URL = "https://blog.mozilla.org/en/products/firefox/reader-view/"


class ExampleApp(App):
    def compose(self) -> ComposeResult:
        yield HTML(use_readability=True)

    def on_mount(self) -> None:
        self.query_one(HTML).load_url(EXAMPLE_URL)


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
