from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from openai import OpenAI
from psycopg.conninfo import make_conninfo
from psycopg_pool import ConnectionPool

from src.environment import Environment


__all__ = [
    'lifespan'
]


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:

    env = Environment(**os.environ)

    conn_info = make_conninfo(host=env.repo_host, port=env.repo_port, dbname=env.repo_db)
    params = {'options': f'-c search_path={env.repo_schema}'}

    with ConnectionPool(conninfo=conn_info, kwargs=params) as conn_pool:
        with OpenAI(api_key=env.openai_api_key) as openai_client:
            yield {'conn_pool': conn_pool, 'openai_client': openai_client}
