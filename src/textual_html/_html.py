from pathlib import Path

from httpx import URL, AsyncClient
from markdownify import markdownify
from readabilipy import simple_json_from_html_string
from textual import work
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Markdown


class HTML(Widget):
    DEFAULT_CSS = """
    HTML {
        height: auto;
        layout: vertical;
    }
    """

    def __init__(
        self,
        html: str | None = None,
        readability: bool = True,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._html = html
        self._readability = readability

    def compose(self) -> ComposeResult:
        yield Markdown()

    def on_mount(self) -> None:
        if self._html is not None:
            self.update(self._html)

    def update(self, html: str) -> None:
        markdown = self._convert_html_to_markdown(html)
        self.query_one(Markdown).update(markdown)

    def load(self, location: Path | URL) -> None:
        if isinstance(location, Path):
            self._local_load(location)
        elif isinstance(location, URL):
            self._remote_load(location)
        else:
            raise ValueError("Unknown location type")

    @work(exclusive=True)
    async def _local_load(self, location: Path) -> None:
        # TODO: Handle exceptions
        with open(location, "r") as f:
            contents = f.read()
        self.update(contents)

    @work(exclusive=True)
    async def _remote_load(self, location: URL) -> None:
        # TODO: Handle exceptions
        async with AsyncClient() as client:
            resp = await client.get(location)
            self.update(resp.text)

    def _convert_html_to_markdown(self, html: str) -> str:
        if self._readability is True:
            html_content = simple_json_from_html_string(html)["plain_content"]
        else:
            html_content = html
        markdown = markdownify(html_content)
        assert isinstance(markdown, str)
        return markdown
