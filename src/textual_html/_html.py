from markdownify import markdownify
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Markdown


class HTML(Widget):
    def __init__(
        self,
        html: str,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._html = html

    def compose(self) -> ComposeResult:
        markdown = self._convert_html_to_markdown(self._html)
        yield Markdown(markdown)

    def _convert_html_to_markdown(self, html: str) -> str:
        markdown = markdownify(html)
        assert isinstance(markdown, str)
        return markdown
