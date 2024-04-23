import discord
from discord import Embed
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

allowed_channel_id = 1211401871990726706  # ID del canale consentito

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def review(ctx, emoji, *, text):
    if ctx.channel.id != allowed_channel_id:  # Verifica se il comando è stato inviato nel canale consentito
        await ctx.send("Questo comando può essere utilizzato solo in un canale specifico.")
        return

    vouched = ctx.author.display_name  # Ottieni il nome visualizzato dell'autore del messaggio come vouched
    vouched_by = f"<@{ctx.author.id}>"  # Ottieni il riferimento all'utente con "@"
    user_id = ctx.author.id  # Ottieni l'ID dell'utente

    publish_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formatta la data e l'ora correnti

    embed = Embed(title="New Vouch Created!!", color=discord.Color.blue())  # Imposta il colore dell'embed

    vouched_info = f"**Vouched by:** {vouched_by}\n**User ID:** {user_id} ({vouched})"  # Aggiungi il riferimento all'utente e l'ID

    # Aggiungi spaziatura per separare le sezioni dell'embed
    spacer = "\n" + "-"*25 + "\n\n"  # Aggiungi uno spazio extra dopo la linea orizzontale

    embed.description = f"**Vouch:**\n+rep {vouched} | {text}{spacer}{vouched_info}{spacer}**Vouched at:**{spacer}{publish_date}\n\n**Image/Video Proof:**\n"

    # Controllo se l'avatar dell'autore è disponibile
    if ctx.author.avatar:
        avatar_url = ctx.author.avatar.with_size(64).url  # Ottieni l'URL dell'avatar con dimensioni ridotte
        embed.set_thumbnail(url=avatar_url)  # Imposta l'avatar dell'autore nell'angolo in alto a sinistra
    else:
        embed.set_thumbnail(url="https://example.com/default_avatar.jpg")  # Imposta un'immagine predefinita

    # Gestione degli allegati delle immagini
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.content_type.startswith('image'):
                image_url = attachment.url
                embed.set_image(url=image_url)  # Imposta l'immagine allegata nell'embed

    await ctx.send(embed=embed)
    await ctx.message.delete()  # Cancella il messaggio contenente il comando

bot.run('MTIzMDk5OTE1NzAzNzIwMzU0Nw.GbdJOc.LkrN4VMcGvKdl9VttH1c30UUGqEBbXcGpZprKA')
