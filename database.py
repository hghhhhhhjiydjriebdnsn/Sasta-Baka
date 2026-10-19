from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY
from datetime import datetime, timezone, timedelta

# Supabase initialize
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- USER FUNCTIONS ---
def get_user(user_id: int):
    """User ka pura data nikalta hai"""
    response = supabase.table("users").select("*").eq("user_id", user_id).execute()
    if response.data:
        return response.data[0]
    return None

def create_user(user_id: int, username: str, first_name: str):
    """Agar user database mein nahi hai, toh naya banata hai"""
    data = {
        "user_id": user_id,
        "username": username or "NoUsername",
        "first_name": first_name,
        "balance": 0,
        "kills": 0,
        "robs": 0
    }
    supabase.table("users").insert(data).execute()
    return get_user(user_id)

def update_balance(user_id: int, amount: int):
    """User ka balance badhata ya ghatata hai"""
    user = get_user(user_id)
    if user:
        new_balance = user["balance"] + amount
        if new_balance < 0: new_balance = 0 # Balance 0 se niche nahi jayega
        
        supabase.table("users").update({"balance": new_balance}).eq("user_id", user_id).execute()
        
        # Transaction log save karna (Audit ke liye)
        if amount != 0:
            log_type = "deposit" if amount > 0 else "withdraw"
            supabase.table("transactions").insert({
                "sender_id": user_id if amount < 0 else None,
                "receiver_id": user_id if amount > 0 else None,
                "amount": abs(amount),
                "type": log_type
            }).execute()
        return new_balance
    return 0

def claim_daily(user_id: int):
    """Daily reward check aur claim karta hai"""
    user = get_user(user_id)
    if not user: return False, "User not found. Start the bot first."
    
    now = datetime.now(timezone.utc)
    last_daily = user.get("last_daily")
    
    if last_daily:
        last_daily_dt = datetime.fromisoformat(last_daily.replace("Z", "+00:00"))
        time_diff = now - last_daily_dt
        if time_diff < timedelta(days=1):
            remaining = timedelta(days=1) - time_diff
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            return False, f"⏳ You already claimed daily!\nCome back in {hours}h {minutes}m."

    # Reward dena
    reward = 2000
    xp_reward = 50
    supabase.table("users").update({
        "balance": user["balance"] + reward,
        "xp": user["xp"] + xp_reward,
        "last_daily": now.isoformat()
    }).eq("user_id", user_id).execute()
    
    # Reset daily limits
    supabase.table("users").update({"daily_kills": 0, "daily_robs": 0}).eq("user_id", user_id).execute()
    
    return True, f"🎁 You claimed your daily reward!\n💰 +${reward}\n✨ +{xp_reward} XP"

def check_protection(user_id: int):
    """Check karta hai ki user protected hai ya nahi"""
    user = get_user(user_id)
    if not user or not user.get("protection_expiry"): return False
    
    expiry = datetime.fromisoformat(user["protection_expiry"].replace("Z", "+00:00"))
    if datetime.now(timezone.utc) < expiry:
        return True
    return False

def buy_protection(user_id: int, days: int):
    """User ko protection shield deta hai"""
    user = get_user(user_id)
    cost = 5000 * days # Example price
    if user["balance"] < cost: return False, "Not enough balance!"
    
    expiry = datetime.now(timezone.utc) + timedelta(days=days)
    supabase.table("users").update({
        "balance": user["balance"] - cost,
        "protection_expiry": expiry.isoformat()
    }).eq("user_id", user_id).execute()
    return True, f"🛡️ Protection activated for {days} days!"