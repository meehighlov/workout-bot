import pydantic


class Config(pydantic.BaseSettings):
    WORKOUT_BOT_TOKEN: str


cfg = Config()
