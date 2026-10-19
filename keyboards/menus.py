from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_menu():
    """Start command ka 6-button menu"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🐺 Baka Features", callback_data="baka_features")],
        [InlineKeyboardButton(text="📊 Groups", callback_data="groups"), 
         InlineKeyboardButton(text="📢 Promoter", callback_data="promoter")],
        [InlineKeyboardButton(text="🔄 Updates", callback_data="updates"), 
         InlineKeyboardButton(text="🎮 Games", callback_data="games")],
        [InlineKeyboardButton(text="➕ Add Me To Your Group", url="https://t.me/im_bakabot?startgroup=true")]
    ])
    return keyboard

def get_features_menu():
    """Baka Features ka 13-button menu (7 lines)"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Whisper", callback_data="feat_whisper"), 
         InlineKeyboardButton(text="Management", callback_data="feat_management")],
        [InlineKeyboardButton(text="Merge Account", callback_data="feat_merge"), 
         InlineKeyboardButton(text="Premium", callback_data="feat_premium")],
        [InlineKeyboardButton(text="Gems", callback_data="feat_gems"), 
         InlineKeyboardButton(text="Power", callback_data="feat_power")],
        [InlineKeyboardButton(text="Economy", callback_data="feat_economy"), 
         InlineKeyboardButton(text="Games", callback_data="feat_games")],
        [InlineKeyboardButton(text="Friends", callback_data="feat_friends"), 
         InlineKeyboardButton(text="Coupons", callback_data="feat_coupons")],
        [InlineKeyboardButton(text="Interaction", callback_data="feat_interaction"), 
         InlineKeyboardButton(text="Utilities", callback_data="feat_utilities")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_start")]
    ])
    return keyboard