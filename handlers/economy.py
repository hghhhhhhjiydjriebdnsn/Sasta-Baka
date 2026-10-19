import random
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime, timezone
from database import get_user, update_balance, claim_daily, check_protection, buy_protection

router = Router()

@router.message(Command("bal"))
async def balance_cmd(message: Message):
    target_id = message.reply_to_message.from_user.id if message.reply_to_message else message.from_user.id
    user = get_user(target_id)
    
    if not user:
        return await message.reply("User not found in database.")
    
    await message.reply(
        f"👤 **{user['first_name']}**'s Stats:\n"
        f"💰 Balance: **${user['balance']}**\n"
        f"💎 Gems: **{user['gems']}**\n"
        f"🔪 Kills: **{user['kills']}**\n"
        f"🔫 Robs: **{user['robs']}**",
        parse_mode="Markdown"
    )

@router.message(Command("daily"))
async def daily_cmd(message: Message):
    success, msg = claim_daily(message.from_user.id)
    await message.reply(msg)

@router.message(Command("protect"))
async def protect_cmd(message: Message):
    # Basic logic for 1 day protection
    success, msg = buy_protection(message.from_user.id, 1)
    await message.reply(msg)

@router.message(Command("rob"))
async def rob_cmd(message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ Reply to a user to rob them!\nUsage: /rob <amount>")
    
    target_user = message.reply_to_message.from_user
    target_id = target_user.id
    user_id = message.from_user.id
    
    if target_id == user_id:
        return await message.reply("❌ You cannot rob yourself!")
    
    # Amount check
    args = message.text.split()
    if len(args) < 2:
        return await message.reply("⚠️ Usage: /rob <amount>")
    
    try:
        amount = int(args[1])
        if amount <= 0 or amount > 10000:
            raise ValueError
    except ValueError:
        return await message.reply("⚠️ Invalid amount. Limit is up to $10,000.")
    
    # Protection check
    if check_protection(target_id):
        return await message.reply("🛡️ This user is protected! You cannot rob them.")
    
    target_data = get_user(target_id)
    user_data = get_user(user_id)
    
    if not target_data or not user_data:
        return await message.reply("User data not found.")
    
    if target_data["balance"] < amount:
        return await message.reply("❌ Target doesn't have that much balance.")
        
    # Success chance (Example: 70%)
    if random.random() > 0.7:
        # Fail logic
        penalty = amount // 2
        update_balance(user_id, -penalty)
        return await message.reply(f"🚨 You failed to rob {target_user.first_name} and got caught!\nYou paid a penalty of ${penalty}.")
    
    # Success logic
    update_balance(target_id, -amount)
    update_balance(user_id, amount)
    
    # Update robs count
    user_data["robs"] += 1
    from database import supabase
    supabase.table("users").update({"robs": user_data["robs"]}).eq("user_id", user_id).execute()
    
    await message.reply(f"🔪 You successfully robbed **${amount}** from {target_user.first_name}!", parse_mode="Markdown")

@router.message(Command("kill"))
async def kill_cmd(message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ Reply to a user to kill them!")
    
    target_user = message.reply_to_message.from_user
    target_id = target_user.id
    user_id = message.from_user.id
    
    if target_id == user_id:
        return await message.reply("❌ You cannot kill yourself!")
    
    if check_protection(target_id):
        return await message.reply("🛡️ This user is protected! You cannot kill them.")
        
    target_data = get_user(target_id)
    if not target_data:
         return await message.reply("User data not found.")
         
    if target_data["balance"] < 100:
        return await message.reply("❌ Target is too poor to kill.")
    
    # Random reward for kill
    reward = random.randint(100, 200)
    xp_reward = random.randint(0, 10)
    
    # Perform kill
    update_balance(target_id, -reward)
    update_balance(user_id, reward)
    
    from database import supabase
    user_data = get_user(user_id)
    supabase.table("users").update({
        "kills": user_data["kills"] + 1,
        "xp": user_data["xp"] + xp_reward
    }).eq("user_id", user_id).execute()
    
    await message.reply(f"🔪 You killed **{target_user.first_name}** and looted **${reward}**!\n✨ +{xp_reward} XP", parse_mode="Markdown")