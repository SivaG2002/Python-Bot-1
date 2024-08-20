import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        welcome_message = (
            f"🎉 Welcome to the server, {member.mention}! 🎉\n\n"
            "We're excited to have you here. Please take a moment to read our community guidelines:\n\n"
            "1. **Be respectful and avoid harassment or discrimination.**\n"
            "2. **Engage in civil discussions and respect differing opinions.**\n"
            "3. **No spamming or irrelevant content.**\n"
            "4. **Follow channel-specific rules and topics.**\n"
            "5. **No NSFW content allowed.**\n"
            "6. **Protect personal information and privacy.**\n"
            "7. **Use appropriate and non-offensive language.**\n"
            "8. **No advertising or self-promotion without permission.**\n"
            "9. **Report issues to moderators instead of handling them yourself.**\n"
            "10. **Have fun and contribute positively to the community!**\n\n"
            "If you have any questions, feel free to reach out to the moderators. Enjoy your time here!"
        )
        await channel.send(welcome_message,
                           file=discord.File(r'imges/img.png'))


if __name__ == "__main__":
    keep_alive()
    bot.run(os.environ['TOKEN'])
