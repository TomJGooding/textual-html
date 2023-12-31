from textual.app import App, ComposeResult

from textual_html import HTML

EXAMPLE_HTML = """
<h1>This is a heading</h1>
<p>This is a paragraph.</p>
<p><b>This text is bold.</b></p>
<p><a href="https://www.w3schools.com">This is a link</a></p>
"""


class ExampleApp(App):
    def compose(self) -> ComposeResult:
        yield HTML(EXAMPLE_HTML)


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
