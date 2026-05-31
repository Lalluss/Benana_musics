from pyrogram import Client
import asyncio
from aiohttp import web
from config import Config

app = Client("SESSION",
api_id=Config.APP_ID, 
api_hash=Config.API_HASH, 
bot_token=Config.BOT_TOKEN)

class Lallus(Client):
    def _init_(self):
        super()._init_(
            name=Config.SESSION,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=50,
            plugins={"root": "modules"},
            sleep_threshold=5,
        )
async def handle(request):
    return web.Response(text="Lallus Bot Running")

async def start_web():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)  
    await site.start()
    print("Fake web server started on port 8080")

bot = Lallus()

async def main():
    await start_web() 
    await bot.start()  
    print("Lallus: Started")
    await asyncio.Event().wait()  

if __name__ == "__main__":
    asyncio.run(main())
