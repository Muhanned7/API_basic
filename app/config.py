from pydantic import BaseSettings


class Setting(BaseSettings):
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_time: int

    class Config:
        env_file = ".env"


setting = Setting()
