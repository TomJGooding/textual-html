from pathlib import Path

from textual.app import App, ComposeResult

from textual_html import HTML

EXAMPLE_PATH = Path(__file__).parent / "./example.html"


class ExampleApp(App):
    def compose(self) -> ComposeResult:
        yield HTML()

    def on_mount(self) -> None:
        self.query_one(HTML).load(EXAMPLE_PATH)


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
