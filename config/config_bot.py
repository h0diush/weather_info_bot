from dataclasses import dataclass
from typing import Union

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class ConfigBot:
    bot: TgBot


def load_config_bot(path: Union[str] = None) -> ConfigBot:
    env = Env()
    env.read_env(path)
    return ConfigBot(bot=TgBot(token=env('BOT_TOKEN')))
