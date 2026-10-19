from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.menus import get_features_menu, get_start_menu

router = Router()

# 1. Baka Features Button Click
@router.callback_query(F.data == "baka_features")
async def show_features_menu(callback: CallbackQuery):
    text = (
        "ℹ️ <b>About Baka</b>\n\n"
        "Click the buttons below to know more about Baka features."
    )
    # Menu update karega 13 buttons ke saath
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 2. Back Button (Wapas Start par)
@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery):
    text = (
        f"💙 Hieeeee <b>{callback.from_user.first_name}</b> I'm Baka - a gaming and chatting girl having lots of features to engage your group.\n\n"
        f"👇 Choose an option below :"
    )
    await callback.message.edit_text(text, reply_markup=get_start_menu(), parse_mode="HTML")
    await callback.answer()

# ---------------------------------------------------------
# 3. Whisper
@router.callback_query(F.data == "feat_whisper")
async def show_whisper(callback: CallbackQuery):
    text = (
        "Do you know qts? 🫶\n\n"
        "You can whisper any text to anyone using baka 🫀\n\n"
        "<b>How to whisper in a group or DM?</b>\n\n"
        "just type this : <code>@im_bakabot &lt;username/userid&gt; &lt;your whisper text&gt;</code>\n\n"
        "If you send a whisper in a group using baka, only that particular user can read the message.\n\n"
        "Enjoy your privacy in groups too 😊"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 4. Management
@router.callback_query(F.data == "feat_management")
async def show_management(callback: CallbackQuery):
    text = (
        "✅ Manage your group with some amazing group management commands of baka!\n\n"
        "<code>.res &lt;user&gt; +-power_name</code> - restrict a member with given power\n\n"
        "<code>.add &lt;user&gt; &lt;power&gt;</code> - add given power for an admin\n"
        "<code>.remove &lt;user&gt; &lt;power&gt;</code> - remove given power for an admin\n\n"
        "<code>.promote &lt;user&gt; 0/1/2/3</code> - Promote user to admin\n"
        "<code>.demote &lt;user&gt;</code> - Demote admin\n\n"
        "<code>.demote_all</code> - demote all baka promoted admins\n\n"
        "<code>.title &lt;user&gt; &lt;title&gt;</code> - Set custom title\n\n"
        "<code>.warns &lt;user&gt;</code> - Get all warnings\n"
        "<code>.warn &lt;user&gt;</code> - Warn a user (3 = ban)\n"
        "<code>.unwarn &lt;user&gt;</code> - Remove 1 warning\n\n"
        "<code>.mute &lt;user&gt; 30m</code> - Mute temp/permanent\n"
        "<code>.dmute &lt;reply&gt; &lt;time&gt;</code> - delete replied message and mute user\n"
        "<code>.smute &lt;user&gt;</code> - silently mute the user\n"
        "<code>.unmute &lt;user&gt;</code> - Unmute the user\n\n"
        "<code>.ban &lt;user&gt;</code> - Ban user\n"
        "<code>.dban reply</code> - delete replied msg and ban user\n"
        "<code>.sban &lt;user&gt;</code> - silently ban the user\n"
        "<code>.unban &lt;user&gt;</code> - Unban user\n"
        "<code>.kick &lt;user&gt;</code> - Kick from group\n"
        "<code>.skick &lt;user&gt;</code> - silently kick the user\n\n"
        "<code>.pin &lt;reply&gt;</code> - Pin replied message\n"
        "<code>.unpin</code> - Unpin the current message\n"
        "<code>.d</code> - delete a message\n"
        "<code>.help</code> - Show this help\n\n"
        "<b>Note:</b>\n"
        "1) You can use '.' or '!' as prefix.\n"
        "2) &lt;user&gt; = reply/username/userid"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 5. Merge Account
@router.callback_query(F.data == "feat_merge")
async def show_merge(callback: CallbackQuery):
    text = (
        "✅ assets recovery system\n\n"
        "using this feature, your deleted account’s coins, gems, and premium can be added to your current — but only if you had set a password on your deleted account before it was deleted.\n\n"
        "🔒 <b>how to use:</b>\n\n"
        "<code>/setpass &lt;password&gt;</code> — set a recovery password.\n"
        "<code>/mpass</code> — check your password in dm.\n"
        "<code>/cpass &lt;old_pass&gt; &lt;new_pass&gt;</code> — change your password.\n"
        "<code>/merge &lt;old_id&gt; &lt;deleted_account_password&gt;</code> — add your deleted account’s coins, gems, and premium to your current account.\n\n"
        "⚙️ <b>important:</b>\n\n"
        "1) /merge only works if your old account is actually deleted.\n"
        "2) you must have set a password before the account was deleted.\n"
        "3) never share your password with anyone.\n"
        "4) only coins, gems, and premium will be added. gaming stats, levels, kills, experience, etc. will not be transferred.\n\n"
        "stay safe and keep playing! 👀"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 6. Premium (Sirf short info, kyunki image nahi hai)
@router.callback_query(F.data == "feat_premium")
async def show_premium(callback: CallbackQuery):
    text = (
        "👑 <b>Baka Premium</b>\n\n"
        "Premium users get higher limits, better rewards and additional benefits compared to normal users.\n\n"
        "Use <code>/pay</code> to buy Premium."
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 7. Gems
@router.callback_query(F.data == "feat_gems")
async def show_gems(callback: CallbackQuery):
    text = (
        "KNOW ABOUT BAKA GEMS 💎\n\n"
        "1 gem = $10000 coins = ₹8\n"
        "Check your gems : /pfp\n\n"
        "convert gems into coins : /convert \n\n"
        "1) you can convert baka gems into coins using /convert command - only premium users can convert baka gems into coins.\n\n"
        "2) you can use baka gems for playing baka games like card, bomb, hack, roulette and bluff too. \n\n"
        "3) whether it's a premium user or a normal user they can buy baka gems but for using gems you will need the baka premium subscription.\n\n"
        "4) you can buy an unlimited number of gems but you can only use 50 gems per day.\n\n"
        "6) you can't give or rob baka gems like baka coins.\n\n"
        "<b>How to use gems in baka mini games?</b> \n\n"
        "👉 in card game use /bet amount gems \n\n"
        "User A starts the game using : /card 1000\n\n"
        "You have two choices \n\n"
        "/bet 1000 coins\n"
        "/bet 1000 gems - 0.1 gem used 💎"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 8. Power
@router.callback_query(F.data == "feat_power")
async def show_power(callback: CallbackQuery):
    text = (
        "🐺 <b>Some Special Powers</b>\n\n"
        "- You can purchase these special powers using gems to unlock extra benefits and enhance your experience.\n\n"
        "<b>Power Commands:</b>\n\n"
        "/powers - Check the complete list of available powers.\n"
        "/pinfo &lt;power name&gt; - Check detailed information about a specific power.\n"
        "/act &lt;power name&gt; &lt;days&gt; - Activate a power for the specified number of days.\n"
        "/mypowers or /mp - Check your active powers \n"
        "/ph - Open the power help menu and check all available commands.\n\n"
        "<b>Note:</b>\n\n"
        "1. You can use multiple powers at the same time.\n"
        "2. There are currently 3 powers available. check by typing /powers"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 9. Economy
@router.callback_query(F.data == "feat_economy")
async def show_economy_info(callback: CallbackQuery):
    text = (
        "💰 <b>BAKA ECONOMY SYSTEM</b>\n\n"
        "Baka has a virtual money system where you can earn money, gain XP, rob or kill other users, protect your balance, and compete for the highest ranks globally.\n\n"
        "━━━━━━━━━━━━━━━\n\n"
        "📜 <b>ECONOMY COMMANDS</b>\n\n"
        "/daily - Claim your daily reward.\n"
        "• Normal: $2000 + 50 xp\n"
        "• Premium: $5000 + 200 XP\n\n"
        "/bal reply or without reply - Check balance \n\n"
        "/pfp - check your daily kills, robs, gems and wallet balance.\n\n"
        "/wallet - deposit or widthraw balance into wallet \n\n"
        "/rob &lt;reply&gt; &lt;amount&gt; - Rob another user and receive coins + XP.\n"
        "• Normal: Up to $10k + 0–50 XP\n"
        "• Premium: Up to $50k + 0–100 XP\n\n"
        "/kill &lt;reply&gt; - Kill another user and receive coins + XP.\n"
        "• Normal: $100–200 + 0-10 XP\n"
        "• Premium: $200–400 + 10–20 XP\n\n"
        "/revive &lt;reply/without reply&gt; - Revive yourself or another user.\n\n"
        "/protect 1d/2d - Buy protection to prevent other users from robbing you.\n"
        "• Normal: 1 day protection \n"
        "• Premium: 1/2 day protection \n\n"
        "/give &lt;reply&gt; - Give money to user.\n"
        "• Normal: 10% tax\n"
        "• Premium: 5% tax\n\n"
        "/close - close gaming commands \n"
        "/open - open gaming commands \n\n"
        "/claim - add baka in a group and claim the reward \n\n"
        "/toprich -See the Top 10 richest users.\n"
        "/topkill - See the Top 10 killers.\n\n"
        "/economy - get this paragraph \n\n"
        "💓 <b>PREMIUM-ONLY</b>\n"
        "/check - Check another user's protection status.\n"
        "/setemoji - Set your custom Premium emoji.\n\n"
        "━━━━━━━━━━━━━━\n"
        "💓 <b>PREMIUM, GEMS AND POWERS</b>\n\n"
        "/pay - Buy a Premium subscription for Baka.\n\n"
        "/gems - buy gems for playing games or purchasing special powers \n\n"
        "/powers - purchase special powers using gems \n\n"
        "Premium users get: premium features \n\n"
        "About gems : know about gems \n\n"
        "About powers: know about powers \n\n"
        "━━━━━━━━━━━━━━ \n\n"
        "✅ Premium users get higher limits, better rewards and additional benefits compared to normal users.\n\n"
        "✅ Build your balance, compete with others, reach the top.\n\n"
        "✅ The money you earn through the economy system can be used to play Baka games and buy or gift items to other users."
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 10. Games (Main info)
@router.callback_query(F.data == "feat_games")
async def show_games_info(callback: CallbackQuery):
    # Yahan aap games ka menu bana sakte hain, abhi ke liye text
    text = (
        "🎮 <b>Baka Games</b>\n\n"
        "Baka Hack Game \nBaka Bluff Game \nBaka Roulette Game \nBaka Card Game \nBaka Bomb Game"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 11. Friends
@router.callback_query(F.data == "feat_friends")
async def show_friends(callback: CallbackQuery):
    text = (
        "I have added some new commands\n\n"
        "/addf tag_name - add friend \n"
        "/tag tag/all - tag your friend \n"
        "/t tag/all - tag your friend \n"
        "/ctag - change tag of your friend \n"
        "/delf - delete a friend\n"
        "/allf - all friend's list\n"
        "/friend - show friends count \n"
        "/friends  - show all friendship commands\n\n"
        "What are the benefits of these commands? \n\n"
        "Now you can easily tag your friends in any group by typing /tag jinu archi - this will tag jinu and archi both in that particular group.\n\n"
        "Also i have updated /setemoji command now you can set premium emoji for you as well as for your friends too by replying them /setemoji \n\n"
        "Also some other commands \n\n"
        "/admin - check adminlist \n"
        "/admins - check adminlist\n"
        "/report - tag all admins silently to report them"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 12. Coupons
@router.callback_query(F.data == "feat_coupons")
async def show_coupons(callback: CallbackQuery):
    text = (
        "Now, guys, you can create coupon codes for your group members.\n\n"
        "What is the use of coupons?\n\n"
        "Any group member can claim coupons using '/coupon code' for receiving coupon balance.\n\n"
        "Commands?\n\n"
        "/create_coupon - create coupon\n"
        "/del_coupon - delete coupon\n"
        "/coupon - redeem the coupon\n"
        "/status - check the status of the coupon code\n"
        "/coupons - get all command list\n\n"
        "Instructions?\n\n"
        "1. A group can have only one coupon code.\n"
        "2. You can create coupons in a group if you are both an admin and a premium user.\n"
        "3. To create coupons, you must have enough balance in your account."
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 13. Interaction
@router.callback_query(F.data == "feat_interaction")
async def show_interaction(callback: CallbackQuery):
    text = (
        "🥳 <b>INTERACTIVE COMMANDS</b>\n\n"
        "Have fun with your friends using Baka's interaction commands. Reply to someone and use different actions to interact or show your feelings with them\n\n"
        "━━━━━━━━━━━━━━\n\n"
        "💚 <b>FUN INTERACTIONS</b>\n\n"
        "/kiss (reply) — Kiss someone.\n"
        "/hug (reply) — Hug someone.\n"
        "/slap (reply) — Slap someone.\n"
        "/punch (reply) — Punch someone.\n"
        "/bite (reply) — Bite someone.\n"
        "/murder (reply) - murder someone \n"
        "/love (reply) — Show love to someone.\n"
        "/crush (reply) — check replied user's crush \n"
        "/look (reply) — Look at someone.\n"
        "/brain (reply) — Check someone's brain.\n"
        "/stupid_meter (reply) — Check how stupid someone is.\n\n"
        "/couples — Choose random couples from the group.\n\n"
        "━━━━━━━━━━━━━━━\n\n"
        "🎲 <b>QUESTIONS & CHALLENGES</b>\n\n"
        "/truth — Get a random truth question.\n"
        "/dare — Get a random dare.\n"
        "/puzzle — Get a random puzzle.\n\n"
        "━━━━━━━━━━━━━━\n"
        "<b>INTRODUCE YOURSELF</b> \n\n"
        "/setintro &lt;your intro text&gt;\n"
        "/intro me/reply  - introduce urself \n\n"
        "━━━━━━━━━━━━━━━\n"
        "😄 Use these commands with your friends and have fun!"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()

# 14. Utilities
@router.callback_query(F.data == "feat_utilities")
async def show_utilities(callback: CallbackQuery):
    text = (
        "🛠️ <b>UTILITY COMMANDS</b>\n\n"
        "Useful commands to get information, manage groups & use various utilities.\n\n"
        "• /detail — Check past names & usernames\n"
        "• /q - quote a photo/video/gif/text into sticker \n"
        "• /voice - change a text into voice \n"
        "• /font 1/2/3/4 - convert ur text into diff diff font styles\n"
        "• /own - make your own sticker pack \n"
        "• /tr &lt;language&gt; - translate any text \n"
        "• /admins — Show all group admins\n"
        "• /report — Report a user to admins\n"
        "• /owner — Tag group owner\n"
        "• /id — Check user/group ID\n"
        "• /truth — Pick a truth\n"
        "• /dare — Pick a dare\n"
        "• /puzzle - get random puzzle \n"
        "• /intro - reply to check intro \n"
        "• /isdeleted &lt;user id&gt;- check if an account is deleted or not\n"
        "• /help - check all group management commands\n\n"
        "• /calc &lt;math query&gt; or /c &lt;math query&gt;\n\n"
        "/calc 20+10\n"
        "/calc 10*10 \n"
        "/calc 200/10 \n"
        "/calc 200-10 \n"
        "/calc 1000 ka 30% kitna hota \n\n"
        "✅ Try them out and make your groups more fun & convenient!"
    )
    await callback.message.edit_text(text, reply_markup=get_features_menu(), parse_mode="HTML")
    await callback.answer()