from typing import Set

from pydantic import BaseSettings


class Environment(BaseSettings):
    endpoints: Set[str] = {
        "https://app-dev-micebot.herokuapp.com",
        "https://micebot-prod.herokuapp.com"
    }
    interval: int = 600  # 10 minutes (time in seconds).


env: Environment = Environment()
