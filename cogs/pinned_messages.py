# What this modules does:
# listens for reactions on server;
# if a message has n-CONST 📌 reactions, it gets pinned.

#TODO CONST should be changed with moulinette input on discord

import discord
from discord.ext import commands

CONST = 4

class Pinned(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		if str(payload.emoji) == "📌":
			channel = self.client.get_channel(payload.channel_id)
			message = await channel.fetch_message(payload.message_id)
			for reaction in message.reactions:
				if reaction.emoji == "📌" and reaction.count >= CONST:
					await message.pin()


async def setup(client):
	await client.add_cog(Pinned(client))
