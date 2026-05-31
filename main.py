import os
import asyncio
from aiohttp import web
from pyrogram import Client
from config import Config

bot = Client("SESSION",
api_id=Config.APP_ID, 
api_hash=Config.API_HASH, 
bot_token=Config.BOT_TOKEN)

class Lallus(Client):
    def init(self):
        super().init(
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
    port = int(os.environ.get('PORT', 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Fake web server started on port {port}")

async def main():
    await start_web()
    await bot.start()
    print("Lallus: Started")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
