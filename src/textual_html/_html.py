from pathlib import Path

import httpx
from markdownify import markdownify  # type: ignore[import]
from readabilipy import simple_json_from_html_string  # type: ignore[import]
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
        use_readability: bool = False,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._html = html
        self._use_readability = use_readability

    def compose(self) -> ComposeResult:
        yield Markdown()

    def on_mount(self) -> None:
        if self._html is not None:
            self.update(self._html)

    def update(self, html: str) -> None:
        markdown = self._convert_html_to_markdown(html)
        self.query_one(Markdown).update(markdown)

    def load(self, location: Path | httpx.URL) -> None:
        if isinstance(location, Path):
            self._load_file(location)
        elif isinstance(location, httpx.URL):
            self._load_url(location)
        else:
            raise ValueError("Unknown location type")

    @work(exclusive=True)
    async def _load_file(self, location: Path) -> None:
        # TODO: Handle exceptions
        with open(location, "r") as f:
            contents = f.read()
        self.update(contents)

    @work(exclusive=True)
    async def _load_url(self, location: httpx.URL) -> None:
        # TODO: Handle exceptions
        async with httpx.AsyncClient() as client:
            resp = await client.get(location)
            self.update(resp.text)

    def _convert_html_to_markdown(self, html: str) -> str:
        if self._use_readability is True:
            html_data = simple_json_from_html_string(html, use_readability=True)
            html_title = html_data["title"]
            html_content = html_data["content"]
        else:
            html_title = None
            html_content = html
        markdown = markdownify(html_content)
        if html_title is not None:
            markdown = f"# {html_title}" + markdown
        assert isinstance(markdown, str)
        return markdown
