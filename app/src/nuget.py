import requests
from requests import Response

class Nuget:
    def __init__(self):
        self.base_url: str = "https://api.nuget.org/v3-flatcontainer"

    def _build_url(self, package: str):
        return f"{self.base_url}/{package.lower()}/index.json"

    def get_latest_version(self, package: str):
        url: str = self._build_url(package)
        print(url)
        response: Response = requests.get(url, timeout=10)


        data: dict = response.json()
        versions: list = []

        if data is not None:
            versions = data.get("versions")
            if versions is not None:
                return versions[-1]

