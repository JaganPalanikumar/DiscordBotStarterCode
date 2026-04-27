import responses
import discord
import os
from discord import app_commands


# Load key=value pairs from a local .env file into environment variables.
def load_env_file(file_path=".env"):
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            # Support optional quoted .env values, e.g. TOKEN="abc123".
            if (value.startswith('"') and value.endswith('"')) or (
                value.startswith("'") and value.endswith("'")
            ):
                value = value[1:-1]
            os.environ.setdefault(key, value)


# Initialize Discord client settings, register events, and start the bot session.
def run_discord_bot(): 
    load_env_file()
    secretToken = os.getenv("DISCORD_BOT_TOKEN")
    guild_id = os.getenv("DISCORD_GUILD_ID")

    if not secretToken:
        raise ValueError("DISCORD_BOT_TOKEN is missing. Add it to your .env file.")

    #TODO - 1 (Setting up Bot)

    @tree.command(name="thelp", description="Show translation bot help.")
    async def thelp_command(interaction: discord.Interaction):
        await interaction.response.send_message(responses.translate("/thelp"))

    @tree.command(name="tlangs", description="List available translation languages.")
    async def tlangs_command(interaction: discord.Interaction):
        await interaction.response.send_message(responses.translate("/tlangs"))

    @tree.command(name="translate", description="Translate text to a target language.")
    @app_commands.describe(text="Text to translate", language="Target language (optional)")
    #TODO - 2 (Translate Slash Command)

    @client.event
    # Announce in console when the bot account has connected and is ready.
    async def on_ready():
        try:
            if guild_id:
                await tree.sync(guild=discord.Object(id=int(guild_id)))
                print(f"Slash commands synced to guild {guild_id}.")
            else:
                await tree.sync()
                print("Slash commands synced globally.")
        except Exception as e:
            print(f"Slash command sync failed: {e}")

        print(f'{client.user} is now running!')

    # TODO - 3 (Handle every new message, ignoring the bot's own messages to prevent loops.)
    #TODO - 4 (runs bot using secret token)
