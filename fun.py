from pyrogram import Client, filters
import asyncio
import time
import random
import os
from groq import Groq

# --- CLOUD CONFIGURATION ---
# The script will now securely grab these from your server's Environment Variables
API_ID = int(os.environ.get("API_ID", 27611951)) 
API_HASH = os.environ.get("API_HASH", "16c265ac1d31f819b7dd53ce3b3602af") 
SESSION_STRING = os.environ.get("SESSION_STRING", "BQGlUy8AOWxxdXzi0oCJUapSG3ROsP7p_VwwPC88HVKTCdHM2_uWDMLnuSnGMMf4wO2YIayh-PDEJ06WsejiIVIBECvFfdSkMwk5mefB0xoy2ufsMFJb1s9xYbun8iGWtduhVxWMahuMjMiHSVnJLvKtlfcbGc8JC9v-qJvDYP_mIaH2ndElLP2cPJtM53GUYwDbLPmwd_CTUVt6l_4Gv7sEe9L57x1d8qgQDl1rjYYV5d_QTQB5vGS4WM8FTn4noQEpMMvbK6hAhkAVWV3gXlfdKhSaWaCk04ZtPvavu6e9sD5r0a7ZCsVG1PJL3RXgr9JnibrDJB5sjVOGag0jb_iINMD3WwAAAAFpXr-QAA") 
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "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") 

# Initialize the client using the String Session instead of a local file
app = Client(
    name="hacker_prank_session",
    session_string=SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)
groq_client = Groq(api_key=GROQ_API_KEY)

# ... [KEEP ALL THE COMMAND FUNCTIONS EXACTLY AS THEY WERE IN THE LAST SCRIPT] ...

# --- HELPER FUNCTIONS ---
def get_reply_target(message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        return user.first_name or (f"@{user.username}" if user.username else "Target")
    return "Target"

def get_reply_target_info(message):
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user
    return None

# --- 1. THE CLASSIC MAINFRAME BREACH ---
@app.on_message(filters.me & filters.command("hack", prefixes="!"))
async def hack_sequence(client, message):
    target = get_reply_target(message)
    ip = f"192.168.1.{random.randint(2, 254)}"
    frames = [
        f"`> [INIT] Initializing Metasploit payload deployment on target: {target}...`",
        f"`> [NET] Mapping routes... Hop 1: 10.0.0.1 -> Hop 2: {ip}`",
        "`> [NET] Target pinged successfully. TTL=64ms. OS fingerprint: Android/iOS kernel`",
        "`> [SCAN] Scanning open ports... 22/tcp [OPEN], 80/tcp [OPEN], 443/tcp [OPEN], 5555/tcp [OPEN]`",
        "`> [EXPLOIT] Injecting buffer overflow into port 5555 (ADB Daemon)...`",
        "`> [PAYLOAD] Allocating heap memory: [0x7fff5fbff610] -> [0x7fff5fbff640]`",
        "`> [BYPASS] Piercing firewall: ▓░░░░░░░░0%`",
        "`> [BYPASS] Piercing firewall: ▓▓▓░░░░░░0%`",
        "`> [BYPASS] Piercing firewall: ▓▓▓▓▓▓░░░0%`",
        "`> [BYPASS] Piercing firewall: ▓▓▓▓▓▓▓▓▓▓ 100%`",
        "`> [AUTH] Grabbing root tokens... SHA-256 handshake bypassed successfully.`",
        f"`🟢 [SUCCESS] Root shell spawned. Accessing {target}'s system files...`",
        "`> [DUMP] Corrupted cache cleared. Extracting /data/user/0/...`",
        f"`> [DUMP] Scraping {target}'s SQLite localized browser history database...`",
        "`⚠️ [ALERT] Scanning text fragments... Keyword match: 'weird stuff'`",
        "`🚨 [FATAL ERROR] Target history contains extreme high levels of cringe. Dumping memory aborting...`",
        "`🔴 Connection closed by local host to protect our servers. 🚨`"
    ]
    for frame in frames:
        await message.edit_text(frame)
        await asyncio.sleep(0.4)

# --- 2. THE CRYPTO HEIST ---
@app.on_message(filters.me & filters.command("crypto", prefixes="!"))
async def crypto_sequence(client, message):
    target = get_reply_target(message)
    frames = [
        f"`$ ssh -i ~/.ssh/id_rsa root@{target}_device -p 22`",
        "`$ Establishing secure SSH tunneling... AES-256 encrypted.`",
        "`$ Connection established. Dropping to bash shell...`",
        "`$ grep -rnw '/sdcard/' -e 'mnemonic' -e 'private_key'`",
        "`$ [SCANNING INODE MEMORY ENTRIES]...`",
        "`$ [MATCH] /sdcard/Documents/safekeeping/.vault.json found.`",
        "`$ cat /sdcard/Documents/safekeeping/.vault.json | decrypt`",
        "`$ Extracting BIP-39 12-word seed phrase...`",
        "`$ Seed phrase cloned. Parsing connected EVM public chains...`",
        "`$ [FOUND] TrustWallet instance detected on device.`",
        "`$ Network: Ethereum Mainnet | Balance: 12.45 ETH`",
        "`$ Network: Bitcoin Mainnet  | Balance: 0.84 BTC`",
        "`$ Initializing atomic multi-sig swap routing to offshore mixer...`",
        "`$ Transaction payload built. Broadcaster node: TxID 0x8f3c...a1e9`",
        "`$ Sending ETH: [░░░░░░░░░░] 0%`",
        "`$ Sending ETH: [██████░░░░] 60%`",
        "`$ Sending BTC: [██████████] 100%`",
        f"`🟢 [TX SUCCESS] Wallets drained. Thanks for funding my coffee chat, {target}! 💸`"
    ]
    for frame in frames:
        await message.edit_text(frame)
        await asyncio.sleep(0.4)

# --- 3. THE INTERPOL ALERT ---
@app.on_message(filters.me & filters.command("interpol", prefixes="!"))
async def interpol_sequence(client, message):
    target = get_reply_target(message)
    lat = f"{random.uniform(-90, 90):.5f}"
    lon = f"{random.uniform(-180, 180):.5f}"
    frames = [
        "`🚨 [SYSTEM] URGENT INTERPOL EMERGENCY INTRUSION OVERRIDE 🚨`",
        f"`> [MONITOR] Packet sniffing node active on profile: {target}`",
        "`> [TRAFFIC] Deep analysis of Telegram CDN media delivery packets...`",
        "`> [MATCH] System flagged hazardous metadata signatures.`",
        f"`> [SCAN] Parsing local cache folder on {target}'s hardware storage...`",
        "`> [WARNING] 743 illegal/forbidden underground toxic memes detected.`",
        "`> [LAW] Breach of International Cyber-Sanity Treaty (Section 4, Art. 12).`",
        "`> [TRACK] Resolving ISP node coordinates via regional gateway...`",
        f"`> [GPS] Triangulating... Cell Tower Lock: Lat {lat}, Lon {lon}`",
        f"`> [ACTION] Locking {target}'s system UI and encrypting operational keys...`",
        "`> [ALERT] Sending digital warrant directly to regional police departments...`",
        "`> [ETA] Dispatch squad tracking status. Target intercept within 2 minutes.`",
        f"`🔴 [CRITICAL] Do not attempt to close this app, {target}. Run while you can! 🚓`"
    ]
    for frame in frames:
        await message.edit_text(frame)
        await asyncio.sleep(0.4)

# --- 4. THE HARDWARE MELTDOWN ---
@app.on_message(filters.me & filters.command("melt", prefixes="!"))
async def melt_sequence(client, message):
    frames = [
        "`[!] [CORE] Allocating raw pointer leak in root memory...`",
        "`[!] [CORE] Fork bomb initiated: :(){ :|:& };:...`",
        "`[!] Thread pool count climbing rapidly: 1024 -> 4096 -> 16384`",
        "`[!] Disabling device thermal throttling triggers via kernel config...`",
        "`[!] Forcing CPU core frequencies to maximum voltage override...`",
        "`🟡 [WARN] Core 0: 94°C | Core 1: 96°C | Core 2: 99°C`",
        "`⚠️ [CRITICAL] Li-ion Battery Controller reports abnormal gas expansion.`",
        "`[!] Wiping file system tables... MBR partition unlinking...`",
        "`[!] rm -rf /system /vendor /boot --no-preserve-root`",
        "`🔴 [FATAL] Kernel Panic: VFS: Unable to mount root fs on unknown-block`",
        "`[!] Executing emergency forced hardware power cycle down sequence...`",
        "`> T-Minus 3...`",
        "`> T-Minus 2...`",
        "`> T-Minus 1...`",
        "`[!] SCREEN FREQUENCY COLLAPSE INTO ZERO STATE...`",
        "`Just kidding, your phone is fine. Wipe the sweat off your forehead! 📱`"
    ]
    for frame in frames:
        await message.edit_text(frame)
        await asyncio.sleep(0.4)

# --- 5. THE MATRIX GLITCH ---
@app.on_message(filters.me & filters.command("matrix", prefixes="!"))
async def matrix_sequence(client, message):
    target = get_reply_target(message)
    frames = [
        "`[SYS] SYSTEM FAILURE IN SIMULATION LAYER 7`",
        "`01100110 01101111 01101100 01101100 01101111 01110111`",
        "`[DECRYPTING ENCRYPTED MATRIX FLUX LOGS]`",
        "`0x00000000 -> ERROR_BUS_RESET`",
        "`0x0000007A -> ERROR_KERNEL_DATA_INPAGE_ERROR`",
        "`\u2591\u2592\u2593 Glitch signature detected in memory pool \u2593\u2592\u2591`",
        "`S h r e d d i n g   l o c a l   R e a l i t y . . .`",
        f"`Wake up, {target}...`",
        f"`The walls of your UI are code fragments, {target}.`",
        "`Reading consciousness blocks... Done.`",
        "`Rewriting your timeline variables...`",
        "`The Matrix has you... 🐇`",
        "`Knock, knock. Look behind your screen.`"
    ]
    for frame in frames:
        await message.edit_text(frame)
        await asyncio.sleep(0.35)

# --- 6. THE GROQ AI ROAST ---
@app.on_message(filters.me & filters.command("roast", prefixes="!"))
async def roast_sequence(client, message):
    target_user = get_reply_target_info(message)
    
    if not target_user:
        await message.edit_text("`[!] Error: Swipe left to reply to the user you want to roast.`")
        return

    chat_id = message.chat.id
    target_id = target_user.id
    target_name = target_user.first_name or "Target"
    
    await message.edit_text(f"`[+] Scanning last 100 messages from {target_name} for psychological weak spots...`")

    # Fetch group history to filter out the target's messages
    user_messages = []
    
    async for msg in client.get_chat_history(chat_id, limit=500):
        if len(user_messages) >= 100:
            break
            
        if msg.from_user and msg.from_user.id == target_id and msg.text:
            context_str = ""
            if msg.reply_to_message and msg.reply_to_message.text:
                context_str = f"(Replying to: \"{msg.reply_to_message.text}\") -> "
            user_messages.append(f"{context_str}\"{msg.text}\"")

    if not user_messages:
        await message.edit_text(f"`[!] Error: Couldn't find any recent text messages from {target_name} in this chat.`")
        return

    await message.edit_text("`[+] Analyzing syntax patterns and compiling data packets...`")
    await asyncio.sleep(0.5)
    await message.edit_text("`[+] Connecting to Groq AI core to generate maximum emotional damage... 🔥`")

    # Format the payload
    chat_logs = "\n".join(user_messages)
    
    # Strict prompt to prevent AI from "thinking out loud"
    system_prompt = (
        "You are a savage, witty roast master. You will be provided with chat logs from a user. "
        "CRITICAL RULES: "
        "1. DO NOT include any intro, outro, or meta-commentary (e.g., NEVER say 'Here is the roast' or 'Let's refine the tone'). "
        "2. DO NOT output your thinking process or numbered steps. "
        "3. Output ONLY the raw roast text. Start immediately with the insult. "
        "4. Base the roast entirely on the weird things they said in the provided logs."
    )
    
    user_prompt = f"Here are the recent group chat messages from the user named {target_name}:\n\n{chat_logs}\n\nRoast them:"

    try:
        # Request the roast using the updated, fast Llama 3.1 model
        completion = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )
        
        roast_text = completion.choices[0].message.content
        
        # Deliver the final roast
        await message.edit_text(f"🔥 **Roasting {target_name}:**\n\n{roast_text}")

    except Exception as e:
        await message.edit_text(f"`[!] Groq AI Error: Could not generate roast. ({str(e)})`")

if __name__ == "__main__":
    print("Ultimate Hacker & Roast Userbot is running!")
    print("Swipe left to reply to someone and type !hack, !crypto, !interpol, !melt, !matrix, or !roast")
    app.run()