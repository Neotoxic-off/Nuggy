import json
from pathlib import Path

class Cache:
    def __init__(self):
        self.path: Path = Path("cache.json")
        self.content: dict = self._load()
    
    def _load(self):
        content: dict = {}

        if self.path.exists():
            with open(self.path, "r") as f:
                content = json.loads(f.read())

        return content

    def save(self):
        with open(self.path, "w+") as f:
            f.write(json.dumps(self.content))

