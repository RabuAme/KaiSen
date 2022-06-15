import keep_alive
import re
import pandas as pd
from pandas import DataFrame
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('目前登入身份：', client.user)
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ID'):
        str = message.content
        tmp = re.split('：|\n|:', str)
        if len(tmp) == 4:
          count = int(tmp[3])
          data = pd.read_excel('KaiSen.xlsx', index_col='ID')
          data.loc[tmp[1], 'Count'] = count
          df = DataFrame(data)
          df.to_excel('KaiSen.xlsx')
        else:
          await message.channel.send('格式錯誤')
          return
    if message.content.startswith('總和'):
        data = pd.read_excel('KaiSen.xlsx')
        df = DataFrame(data)
        await message.channel.send(df['Count'].sum())
    if message.content.startswith('清單'):
        data = pd.read_excel('KaiSen.xlsx')
        await message.channel.send(data)

if __name__ == "__main__":
    keep_alive.keep_alive()
    client.run(
        'OTg2NTE3MzE3NzA4MDUwNDMy.GNEDQ-.gfMOu6zg0Bh1o4RZ9z6U0DQHcIqkpV0mgdw3ng'
    )