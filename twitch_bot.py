from twitchio.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.getenv("TWITCH_TOKEN"), client_id=os.getenv("TWITCH_CLIENT_ID"), nick="guguBOT", prefix="!", initial_channels=[os.getenv("TWITCH_CHANNEL")])

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")
        print(f"Joined {len(self.joined_channels)} channels")

    async def event_message(self, message):
        if message.echo:
            return
        await self.handle_commands(message)

    @commands.command(name="hello")
    async def hello_command(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")

bot = Bot()
bot.run()