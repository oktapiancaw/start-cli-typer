from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class ApplicationConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    output_dir: str = "./public/output"
