import discord
import sys

BOT_TOKEN = ("MTIyMTQ1ODY0ODg2MjI5NDEyOQ.GGHH-s."
             "-NjN8PscjzgEj9UYX9SCk44gQW3MtVPMBURclk")
CHANNEL_ID = 1196940212165689385

# Create an Instance of the Discord Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Logged in as", client.user.name)
    print("------")

    # Define channel to send file
    channel = client.get_channel(CHANNEL_ID)

    if channel:
        try:
            # Open file to send
            with open("screenshot.png", "rb") as f:
                # Send the file
                await channel.send(file=discord.File(f, "screenshot.png"))
        except Exception as e:
            print(f"Failed to send file: {e}")
        finally:
            # Close Discord client and exit script
            await client.close()
            sys.exit()
    else:
        print("Channel not found")
        sys.exit()


# Run client
client.run(BOT_TOKEN)
