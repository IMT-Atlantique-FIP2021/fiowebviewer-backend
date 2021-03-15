from pydantic import (
    BaseSettings,
    Field,
)


class MongoSettings(BaseSettings):
    host: str = "localhost"
    port: int = 27017
    db: str = "fiowebviewer"
    username: str = ""
    password: str = ""

    class Config:
        env_prefix = "MONGODB_"

    def getConnectConfig(self):
        conf = self.dict()
        conf.pop("db")
        return conf


mongo_settings = MongoSettings()
