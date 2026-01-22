import discord
from discord.ext import commands
import random , os 
from config  import token

intents = discord.Intents.default()
intents.message_content = True
bot =commands.Bot(command_prefix='!', intents=intents) 
a = {
    'petsise.jpg': 'Plastik şişeler doğada 450-1000 yil arasinda çözünür. Deniz canlılarını öldürür, toprağı kirletir ve mikro plastik oluşturur.',
    'camsise.jpg': 'Cam şişeler doğada 4000 yildan fazla sürede çözünür. Kırıldığında canlılara zarar verir ve geri dönüşümü enerji gerektirir.',
    'kagit.jpg': 'Kağit atiklar ormanlarin yok olmasına neden olur. Çürürken metan gazı salar ve su kaynaklarını kirletir.',
    'pil.jpg': 'Piller içerdikleri ağır metallerle toprağı ve suyu zehirler. Kadmiyum, kurşun ve cıva gibi toksik maddeler içerir.',
    'AlüminyumFolyo.jpeg': 'Alüminyum folyo üretimi çok fazla enerji tüketir. Doğada çözünmez ve geri dönüşümü zordur.'
}
@bot.command()
async def kirlilik(ctx):
    img = random.choice([f for f in os.listdir('images') if f.endswith(('.jpg', '.jpeg', '.png'))])
    await ctx.send(file=discord.File(f'images/{img}'))
    await ctx.send(a.get(img, 'Bu atik doğaya zararlidir ve geri dönüşüme gönderilmelidir.'))
bot.run(token)































































