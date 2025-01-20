import socket

host = "localhost"
port = 1234

if __name__ == "__main__": 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sfd:
        sfd.connect((host, port))
        sfd.sendall(b"Hello, world")
        data = sfd.recv(1024)

    print(f"Received {data!r}")


# ASYNCIO!!!!!!!!!!!!!!
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