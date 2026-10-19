from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from database import get_user, create_user
from keyboards.menus import get_start_menu

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    user_id = message.from_user.id
    user = get_user(user_id)
    
    # Agar user database mein nahi hai, toh banao
    if not user:
        user = create_user(user_id, message.from_user.username, message.from_user.first_name)

    text = (
        f"💙 Hieeeee <b>{message.from_user.first_name}</b> I'm Baka - a gaming and chatting girl having lots of features to engage your group.\n\n"
        f"📊 Your stats:\n"
        f"💰 Balance: {user['balance']}\n"
        f"🏆 Rank: 382741\n"
        f"💎 Gems: {user['gems']}\n"
        f"🔪 Kills: {user['kills']}\n\n"
        f"🕹️ How to play?\n"
        f"💰 /bal - check your stats\n"
        f"🎁 /daily - get free coins\n"
        f"⚔️ /kill & /rob - loot others"
    )
    await message.answer(text, reply_markup=get_start_menu(), parse_mode="HTML")

@router.message(Command("help"))
async def help_cmd(message: Message):
    help_text = (
        "✅ Manage your group with some amazing group management commands of baka!\n\n"
        "Here are the economy commands:\n"
        "/bal - Check balance\n"
        "/pfp - Check profile\n"
        "/daily - Claim daily reward\n"
        "/rob <reply> <amount> - Rob a user\n"
        "/kill <reply> - Kill a user\n"
        "/protect <days> - Buy protection\n\n"
        "Management commands coming soon..."
    )
    await message.answer(help_text)

# Callback query for the menu buttons
@router.callback_query(F.data == "baka_features")
async def show_features(callback: CallbackQuery):
    await callback.answer("Baka Features menu is under construction!", show_alert=True)

@router.callback_query(F.data == "groups")
async def show_groups(callback: CallbackQuery):
    await callback.answer("Top 5 Groups feature is coming soon!", show_alert=True)