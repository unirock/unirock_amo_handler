import asyncio
import json

import pytest
import qsparser
from fastapi.testclient import TestClient
from httpx import AsyncClient

from lead_orchestrator.main import app

client = TestClient(app)
pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_webhook():
    with open('/home/michael/projects/lead_orchestrator/tests/testhook.json', "r", encoding='utf-8') as f:
        hook = json.load(f)

    async with AsyncClient(app=app) as ac:

        r = await ac.post('http://127.0.0.1:5000/tasks/webhook', content=qsparser.stringify(hook))

    print(r.json())
