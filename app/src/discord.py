import requests
from requests import Response
from datetime import datetime

class Discord:
    def __init__(self, webhook_url: str):
        self.webhook_url: str = webhook_url

    def send_new_version(self, package_name: str, version: str) -> None:
        embed: dict = {
            "title": f"{package_name} has been updated",
            "description": f"**{package_name}** has been updated",
            "color": 3066993,
            "fields": [
                {"name": "📦 Package", "value": package_name, "inline": False},
                {"name": "🔺 Version", "value": version, "inline": False},
                {
                    "name": "🔗 NuGet",
                    "value": f"[View Package](https://www.nuget.org/packages/{package_name}/{version})",
                    "inline": False
                }
            ],
            "timestamp": datetime.now().isoformat(),
            "footer": {"text": "NuGet Tracker"}
        }
        response: Response = requests.post(self.webhook_url, json={"embeds": [embed]})
