import asyncio
import httpx
import random
import time
import threading

# URL siaran TikTok Live yang disasarkan (untuk pembelajaran)
LIVE_URL = "https://www.tiktok.com/@someuser/live"

# Senarai user-agent untuk mensimulasikan pelayar berbeza
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 9)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F)",
]

# Simulasi IP rawak (tidak menukar IP sebenar)
def fake_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

# Fungsi utama viewer bot
async def send_viewer_request():
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "X-Forwarded-For": fake_ip()
    }
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(LIVE_URL, headers=headers)
            print(f"[+] Viewer dihantar | Status: {response.status_code} | IP: {headers['X-Forwarded-For']}")
    except Exception as e:
        print(f"[-] Ralat sambungan: {e}")

# Fungsi untuk jalankan beberapa viewer sekaligus
async def simulate_viewers(total):
    tasks = []
    for _ in range(total):
        tasks.append(send_viewer_request())
        await asyncio.sleep(random.uniform(0.5, 1.2))  # Delay rawak setiap permintaan
    await asyncio.gather(*tasks)

# Wrapper dalam thread
def start_bot(viewer_count, delay):
    print(f"[•] Memulakan simulasi untuk {viewer_count} viewer...")
    while True:
        asyncio.run(simulate_viewers(viewer_count))
        print(f"[✓] Pusingan selesai. Menunggu {delay} saat...")
        time.sleep(delay)

# Antara muka pengguna
if __name__ == "__main__":
    print("╔═══════════════════════════════════════╗")
    print("║     TikTok Live Viewer Bot (EDU)     ║")
    print("╚═══════════════════════════════════════╝")
    jumlah = int(input("Masukkan bilangan viewer palsu: "))
    selang = int(input("Selang ulang setiap (saat): "))
    
    # Guna thread untuk multitasking
    thread = threading.Thread(target=start_bot, args=(jumlah, selang))
    thread.start()