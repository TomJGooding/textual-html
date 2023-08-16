from textual.app import App, ComposeResult

from textual_html import HTML

EXAMPLE_HTML = """
<h1>This is a heading</h1>
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
"""


class ExampleApp(App):
    def compose(self) -> ComposeResult:
        yield HTML(EXAMPLE_HTML)


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
