import asyncio
import httpx
import pytest


async def test_get_home():
    async with httpx.AsyncClient() as cli:
        r = await cli.get("http://0.0.0.0:80/")
        assert r.status_code == 200
        print("OK")


async def test_true_form():
    response = httpx.post("http://0.0.0.0:80/get_form?f_name1=79663678900&f_name2=boba@iu.ru")
    assert response.status_code == 200


async def test_fake_form():
    response = httpx.post("http://0.0.0.0:80/get_form?f_name1=79656788823&f_name2=shlepa@zo4.gb")
    assert response.status_code == 200


