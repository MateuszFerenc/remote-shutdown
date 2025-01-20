import http.client

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 1234
    conn = http.client.HTTPSConnection(host=host, port=port)
    conn.request("GET", "/", headers={"Host": host})
    response = conn.getresponse()
    print(response.status, response.reason)

# probably it will be better to use an asyncio when using GUI
# for GUI I'll use PyQt5

# import aiohttp
# import asyncio

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://swapi.dev/api/starships/9/') as response:
#             print(await response.json())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())