from typing import Annotated

from pydantic import BaseModel, Field


class Environment(BaseModel):
    repo_host: Annotated[str, Field(validation_alias='APP_REPO_HOST')]
    repo_port: Annotated[int, Field(validation_alias='APP_REPO_PORT')]
    repo_db: Annotated[str, Field(validation_alias='APP_REPO_DB')]
    repo_schema: Annotated[str, Field(validation_alias='APP_REPO_SCHEMA')]
    openai_api_key: Annotated[str, Field(validation_alias='APP_OPENAI_API_KEY')]
