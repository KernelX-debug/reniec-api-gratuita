import discord
from discord.ext import commands
from discord import app_commands
import requests
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
RENIEC_TOKEN = os.getenv("RENIEC_TOKEN")

API_URL = "https://api.decolecta.com/v1/reniec/dni"


intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"[+] Bot conectado como {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"[+] Slash commands sincronizados: {len(synced)}")
    except Exception as e:
        print(f"[ERROR] {e}")

def consultar_dni(numero_dni):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {RENIEC_TOKEN}"
    }

    params = {
        "numero": numero_dni
    }

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        return None

    except Exception as e:
        print(f"[ERROR API] {e}")
        return None

@bot.tree.command(
    name="dni",
    description="Consulta información ciudadana"
)
@app_commands.describe(numero="Número de DNI")
async def dni(interaction: discord.Interaction, numero: str):

    # Validación
    if not numero.isdigit() or len(numero) != 8:

        await interaction.response.send_message(
            "❌ DNI inválido.",
            ephemeral=True
        )
        return

    await interaction.response.defer()

    data = consultar_dni(numero)

    if not data:

        await interaction.followup.send(
            "❌ No se encontraron resultados."
        )
        return


    embed = discord.Embed(
        title="🛡️ SISTEMA NACIONAL DE IDENTIFICACIÓN",
        description=(
            "```"
            "INFORMACIÓN CONFIDENCIAL\n"
            "ACCESO AUTORIZADO\n"
            "NIVEL DE SEGURIDAD: RESERVADO"
            "```"
        ),
        color=0x0f0f0f
    )

    embed.add_field(
        name="📌 DNI",
        value=f"```{data.get('document_number', 'N/A')}```",
        inline=False
    )

    embed.add_field(
        name="👤 NOMBRES",
        value=f"```{data.get('first_name', 'N/A')}```",
        inline=False
    )

    embed.add_field(
        name="🧾 APELLIDO PATERNO",
        value=f"```{data.get('first_last_name', 'N/A')}```",
        inline=False
    )

    embed.add_field(
        name="🧾 APELLIDO MATERNO",
        value=f"```{data.get('second_last_name', 'N/A')}```",
        inline=False
    )

    embed.add_field(
        name="📂 IDENTIDAD COMPLETA",
        value=f"```{data.get('full_name', 'N/A')}```",
        inline=False
    )

    embed.set_footer(
        text="Sistema Integrado de Verificación"
    )

    await interaction.followup.send(embed=embed)

bot.run(DISCORD_TOKEN)