# httpx - library which act like browser or postman

# get a list of event
import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        token = "xxxxxx"
        response = await client.get(f"http://localhost:8001/event/all/{token}")
        print("status code", response.status_code)
        print("Response body", response.text)

asyncio.run(main())