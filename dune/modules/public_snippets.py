import requests

from ..common.base import DuneModule

PATHS = ("/-/snippets", "/explore/snippets")


class PublicSnippets(DuneModule):
    name = "snippets"
    description = "to find public code snippets"

    def run(self) -> None:
        for path in PATHS:
            with requests.get(self.target + path, verify=False) as response:
                if response.status_code != 200:
                    continue

                self.console.log(f"Public snippets found at {response.url}")
