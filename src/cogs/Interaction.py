import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class Interaction(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dankr8"])
    async def dankrater(self, ctx):
        v = ["100%",
             "99%",
             "98%",
             "95%",
             "87%",
             "85%",
             "82%",
             "80%",
             "76%",
             "74%",
             "70%",
             "69%",
             "65%",
             "54%",
             "57%",
             "50%",
             "49%"
             "45%",
             "47%",
             "42%",
             "40%",
             "36%",
             "35%",
             "25%",
             "23%",
             "18%",
             "15%",
             "13%",
             "10%",
             "7%",
             "5%",
             "3%",
             "2%",
             "1%"]
        embed=discord.Embed(color=0x0338b5)
        embed.add_field(name="Dank r8 machine", value=f"Il tuo potenziale memetico è: **{random.choice(v)}**", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, arg):
        if (arg) == "Sono stupido":
            await ctx.send("Lo sappiamo.")
        elif (arg) == "sono stupido":
            await ctx.send("Lo sappiamo.")
        elif (arg) == "Sono uno stupido":
            await ctx.send("Lo sappiamo.")
        elif (arg) == "sono uno stupido":
            await ctx.send("Lo sappiamo.")
        else:
            await ctx.send(f"{arg} \n\n\n- **{ctx.author}**")

    # Command of questions. The bot send a random response for any type of question
    @commands.command(aliases=["8ball", "oracolo", "predizione", "domanda"])
    async def erdubbio(self, ctx, *, question):
        responses = ["E' certo.",
                     "E' stato deciso così.",
                     "Senza dubbio.",
                     "Già....indubbiamente.",
                     "Contaci.",
                     "Per come la vedo io, si.",
                     "Preferibilmente.",
                     "Vedila così.",
                     "Sì.",
                     "Un punto in più per il 'Sì'.",
                     "uhm... Sono un po' confuso, potresti ripetere la domanda?",
                     "Chiedimelo più tardi..",
                     "E' meglio non dirtelo ora.",
                     "Mi risulta difficile predirlo ora.",
                     "Concentrati e chiedimelo di nuovo.",
                     "Non ci contare.",
                     "La mia risposta è no.",
                     "Le mie fonti dicono di no.",
                     "Pessima prospettiva.",
                     "Dubito."]
        embed = discord.Embed(color=0xa7c7fb)
        embed.add_field(name="(?) ErDubbio (?)", value="*Poni le tue più strambe domande a questo magnifico oracolo dotato di tanta saggezza e righe di codice", inline=False)
        embed.add_field(name=":question: Domandona:", value=f"{question}", inline=True)
        embed.add_field(name=":speech_left: Risposta epica:", value=f"{random.choice(responses)}", inline=True)
        embed.set_footer(text="Leonardus Project")
        await ctx.send(embed=embed)

    @commands.command(aliases=["hack"])
    async def akeraggio(self, ctx, member: commands.MemberConverter):
        message = await ctx.send(f"Sto hackerando con paint {member}...")
        await asyncio.sleep(2)
        await message.edit(content='Sono penetrato nel sistema!')
        await asyncio.sleep(3)
        await message.delete()
        await asyncio.sleep(0.2)
        message = await ctx.send("[▙] Eseguo un leak dell'email discord...(2fa Bypass)")
        await asyncio.sleep(3)
        await message.edit(content="[▛] **Gotcha!**")
        email = await ctx.send(f"**EMAIL:** `{member}@email.net` \n**PASSWORD:** `PASSW0RD`")
        await asyncio.sleep(4)
        await message.delete()
        await email.delete()
        await asyncio.sleep(0.1)
        message = await ctx.send("[▟] Spio i messaggi recenti...")
        await asyncio.sleep(2)
        dms = ["send nudes",
               "Ammetto che adoro i canditi",
               "Napoli merda",
               "Tifo Juve",
               "Ieri ho rubato 2 orologi",
               "Cyca mala criminale",
               "mlmlml, che belli i bimbi neri"]
        await message.edit(content=f"**Leak degli ultimi dms**: '`{random.choice(dms)}`'")
        await asyncio.sleep(3)
        await message.edit(content=f"[▙] Rubo le credenziali di steam...")
        await asyncio.sleep(3)
        await message.edit(content=f"[▛] Credenziali di steam rubate :)")
        await asyncio.sleep(2)
        await message.edit(content=f"[▜] Traccio l'IP...")
        await asyncio.sleep(3)
        await message.edit(content=f"[▟] **IP TROVATO:** `127.0.0.1`")
        await asyncio.sleep(2)
        await message.edit(content=f"[▙] Scopro la cronologia...")
        await asyncio.sleep(3)
        await message.edit(content=f"**CRONOLOGIA TROVATA** \n*Lista:* \n`How to buil a bomb`\n`How to kidnapp`\n`Come dichiarare le variabili in HTML`")
        await asyncio.sleep(5)
        await message.edit(content=f"*Rivendo i dati al governo...*")
        await asyncio.sleep(3)
        await message.edit(content=f"*Rendo {member} ricercato in 5 paesi differenti...*")
        await asyncio.sleep(4)
        await message.edit(content=f"*Infetto il computer di {member} con diversi virus...*")
        await asyncio.sleep(2)
        await message.edit(content=f"Fine. *{member}* è stato hackerato!")
        await ctx.send("Processo di hackeraggio **100%** *reale* e *pericoloso* terminato.")







def setup(client):
    client.add_cog(Interaction(client))