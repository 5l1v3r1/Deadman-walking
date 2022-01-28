import logging, discord, discord_slash, secrets
from discord.ext import commands


def log():
    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
    handler.setFormatter(
        logging.Formatter("%(asctime)s: %(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)


log()

bot = commands.Bot(command_prefix="/")
slash = discord_slash.SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print("Bot is online")


@slash.slash(
    name="test",
    description="Those burgers look tasty",  # Adding a new slash command with our slash variable
    options=[
        discord_slash.manage_commands.create_option(
            name="first_option",
            description="Please enter what you want on your burger",
            option_type=3,
            required=False,
        )
    ],
)
async def test(ctx: discord_slash.SlashContext, first_option):
    await ctx.send(f"I am now gonna get you a burger with {first_option}")


@slash.slash(
    name="link",
    description="Verknüpft deinen Clash Royale Account mit deinem Discord Account",
    options=[
        discord_slash.manage_commands.create_option(
            name="token",
            description="Bitte gebe deinen Clash Royale API token ein. Du findest ihn in den Einstellungen.",
            option_type=3,
            required=False,
        )
    ],
)
async def link(ctx: discord_slash.SlashContext, token):
    await ctx.send(f"Du hast dich erfolgleich als {token} verifiziert.")


# @slash.slash (
#     name = "checkPermission",
#     description = "bla",
#     options = []
# )

# def getUsernameFromToken(token):
#     username = token
#     return username

# def checkPermission(author):
#     if 555512755331923969 in [y.id for y in author.roles]:
#         return True
#     else:
#         False


@slash.slash(
    name="checkperms",
    description="perms",
)
async def checkperms(ctx: discord_slash.SlashContext):
    await ctx.send(f"{0}".format(discord.ClientUser.name))


bot.run(secrets.token)
