import os
import json
import time
import logging
from pathlib import Path
from logging import Logger
from src.discord import Discord
from src.nuget import Nuget

class Core:
    def __init__(self):
        self.index: dict = {}
        self.packages: list = []
        self.interval: dict = 1 * 60 * 60
        self.processed: bool = False
        self.logger: Logger = logging.getLogger("nuggy")
        self.discord: Discord = Discord(os.environ.get("DISCORD_WEBHOOK"))
        self.nuget: Nuget = Nuget()

        logging.basicConfig(level=logging.INFO)

        self._load_packages()

    def _load_packages(self):
        path: Path = Path("config/packages.json")

        if path.exists() == True:
            with open(f"{path}", 'r') as f:
                self.packages = json.loads(f.read())
        self.logger.info(f"{len(self.packages)} packages are now tracked")

    def _set_latest_version(self, package: str, version: str):
        self.index[package] = version

    def _get_latest_version(self, package: str):
        return self.index.get(package)

    def _check_for_updates(self, package: str):
        self.logger.info(f"tracking {package} version")

        latest_version: str = self.nuget.get_latest_version(package)
        version: str = self._get_latest_version(package)

        if latest_version is not None:
            self.logger.info(f"latest {package} version: {latest_version}")        
            if latest_version is None or version != latest_version:
                self._set_latest_version(package, latest_version)
                self.logger.info(f"new version: {latest_version} > {version}")
                self.discord.send_new_version(package, latest_version)
        else:
            self.logger.error("failed to fetch version")

    def _check_all_packages(self):
        for package in self.packages:
            self._check_for_updates(package)

    def run(self):
        self._check_all_packages()
