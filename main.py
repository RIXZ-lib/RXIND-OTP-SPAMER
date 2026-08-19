#!/usr/bin/env python3
# main.py - RXIND OTP SPAMMER
# UI DENGAN 25+ ANIMASI

import os
import sys
import time
import random
import threading
import math
import shutil
from colorama import Fore, Style, init
from engine import run_single_round, run_infinite_loop, run_random_mode

init(autoreset=True)

VERSION = "2.0"
TOOLS_NAME = "RXIND OTP SPAMMER"

# ============ UTILITY ============
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def rgb_color(tick, offset=0):
    r = int((math.sin(tick * 0.5 + offset) + 1) * 127)
    g = int((math.sin(tick * 0.5 + offset + 2) + 1) * 127)
    b = int((math.sin(tick * 0.5 + offset + 4) + 1) * 127)
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, tick, offset=0):
    result = ""
    for i, char in enumerate(text):
        color = rgb_color(tick, offset + i * 0.1)
        result += f"{color}{char}{Style.RESET_ALL}"
    return result

def glitch_text(text, intensity=0.15):
    result = ""
    for char in text:
        if random.random() < intensity:
            result += random.choice(["#", "@", "&", "%", "$", "!", "?", "*", "+", "=", "~", "|"])
        else:
            result += char
    return result

def typing_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return ""

# ============ 25+ ANIMASI ============

# 1. Pulse Effect
def pulse_effect(text, duration=2):
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 0.1
        color = rgb_color(tick)
        sys.stdout.write(f'\r{color}{text}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\r' + ' ' * len(text) + '\r', end='')

# 2. Blink Effect
def blink_effect(text, duration=2):
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 0.1
        if int(tick) % 2 == 0:
            sys.stdout.write(f'\r{Fore.GREEN}{text}{Style.RESET_ALL}')
        else:
            sys.stdout.write(f'\r{Fore.RED}{text}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.3)
    print('\r' + ' ' * len(text) + '\r', end='')

# 3. Marquee Effect
def marquee_effect(text, duration=3):
    text = text + ' ' * 20
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 1
        shifted = text[tick % len(text):] + text[:tick % len(text)]
        sys.stdout.write(f'\r{Fore.CYAN}{shifted[:40]}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.08)
    print('\r' + ' ' * 50 + '\r', end='')

# 4. Shake Effect
def shake_effect(text, duration=1):
    for _ in range(int(duration * 10)):
        offset = random.randint(-2, 2)
        sys.stdout.write(f'\r{" " * (offset + 10)}{text}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\r' + ' ' * len(text) + '\r', end='')

# 5. Fire Effect
def fire_effect(text, duration=2):
    colors = [Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.RED, Fore.LIGHTRED_EX]
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 1
        color = colors[tick % len(colors)]
        sys.stdout.write(f'\r{color}{text}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.15)
    print('\r' + ' ' * len(text) + '\r', end='')

# 6. Neon Glow
def neon_glow(text, duration=2):
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 0.1
        color = rgb_color(tick)
        sys.stdout.write(f'\r{color}{text}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\r' + ' ' * len(text) + '\r', end='')

# 7. Scanning Effect
def scanning_effect(duration=2):
    width = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    for i in range(width):
        sys.stdout.write(f'\r{Fore.GREEN}{"█" * i}{"░" * (width - i)}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(duration / width)
    print('\r' + ' ' * width + '\r', end='')

# 8. Slide In
def slide_in(text, duration=1):
    width = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    for i in range(width):
        sys.stdout.write(f'\r{" " * (width - i)}{text}')
        sys.stdout.flush()
        time.sleep(duration / width)
    print('\r' + text + ' ' * (width - len(text)) + '\r', end='')

# 9. Ripple Effect (BARU)
def ripple_effect(text, duration=2):
    chars = ['🌊', '💧', '〰️', '~']
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 1
        char = chars[tick % len(chars)]
        color = rgb_color(tick * 0.5)
        sys.stdout.write(f'\r{color}{char} {text} {char}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.15)
    print('\r' + ' ' * len(text) + '\r', end='')

# 10. Sparkle Effect (BARU)
def sparkle_effect(text, duration=2):
    sparkles = ['✨', '⭐', '🌟', '💫']
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 1
        sparkle = sparkles[tick % len(sparkles)]
        color = rgb_color(tick * 0.3)
        sys.stdout.write(f'\r{color}{sparkle} {text} {sparkle}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.2)
    print('\r' + ' ' * len(text) + '\r', end='')

# 11. Wave Effect (BARU)
def wave_effect(text, duration=2):
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 0.1
        result = ""
        for i, char in enumerate(text):
            offset = int(math.sin(tick + i * 0.5) * 3)
            color = rgb_color(tick, i * 0.1)
            result += f"{color}{' ' * max(0, offset)}{char}{Style.RESET_ALL}"
        sys.stdout.write(f'\r{result}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\r' + ' ' * len(text) + '\r', end='')

# 12. Rotate Effect (BARU)
def rotate_effect(text, duration=2):
    chars = ['◐', '◓', '◑', '◒']
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 1
        char = chars[tick % len(chars)]
        color = rgb_color(tick * 0.2)
        sys.stdout.write(f'\r{color}{char} {text} {char}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.1)
    print('\r' + ' ' * len(text) + '\r', end='')

# 13. Zoom Effect (BARU)
def zoom_effect(text, duration=2):
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 0.1
        size = int(1 + math.sin(tick) * 0.5)
        color = rgb_color(tick)
        sys.stdout.write(f'\r{color}{text * size}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\r' + ' ' * len(text) + '\r', end='')

# 14. Rainbow Effect (BARU)
def rainbow_effect(text, duration=2):
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 0.05
        result = ""
        for i, char in enumerate(text):
            color = rgb_color(tick, i * 0.15)
            result += f"{color}{char}{Style.RESET_ALL}"
        sys.stdout.write(f'\r{result}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\r' + ' ' * len(text) + '\r', end='')

# 15. Typewriter Sound Effect (BARU)
def typewriter_sound_effect(text, delay=0.04):
    sounds = ['click', 'tap', 'clack', 'tick']
    for i, char in enumerate(text):
        sound = sounds[i % len(sounds)]
        sys.stdout.write(f'\r{Fore.CYAN}{text[:i+1]}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(delay)
    print('\r' + text + ' ' * 10 + '\r', end='')

# 16. Countdown Effect (BARU)
def countdown_effect(duration=3):
    for i in range(duration, 0, -1):
        color = Fore.RED if i == 1 else Fore.YELLOW if i == 2 else Fore.GREEN
        sys.stdout.write(f'\r{color}▶ {i} ...{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(1)
    print('\r' + ' ' * 10 + '\r', end='')

# ============ LOADING ANIMATION ============
def matrix_loading(duration=5):
    clear()
    
    # ===== BANNER KECIL =====
    print(f"{Fore.CYAN}┌────────────────────────────────────────────────────────────┐{Style.RESET_ALL}")
    print(f"{Fore.CYAN}│{Style.RESET_ALL}  {Fore.YELLOW}⛧ RXIND OTP SPAMMER ⛧{Style.RESET_ALL}                         {Fore.CYAN}│{Style.RESET_ALL}")
    print(f"{Fore.CYAN}│{Style.RESET_ALL}  {Fore.WHITE}Version 2.0 | 60+ APIs{Style.RESET_ALL}                    {Fore.CYAN}│{Style.RESET_ALL}")
    print(f"{Fore.CYAN}└────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
    print()
    
    # ===== SPINNER + PROGRESS BAR =====
    chars = ['◐', '◓', '◑', '◒']
    for i in range(101):
        bar = "█" * (i // 2) + "░" * (50 - i // 2)
        spinner = chars[i % 4]
        
        if i < 30:
            color = Fore.MAGENTA
            status = "INITIALIZING"
        elif i < 60:
            color = Fore.CYAN
            status = "LOADING"
        elif i < 85:
            color = Fore.YELLOW
            status = "PREPARING"
        else:
            color = Fore.GREEN
            status = "FINALIZING"
        
        sys.stdout.write(f'\r  {color}{spinner} [{bar}] {i}%  {status}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(duration / 100)
    
    print()
    print()
    
    # ===== EFEK SELESAI (BLINK) =====
    for _ in range(5):
        sys.stdout.write(f'\r{Fore.GREEN}✅ SYSTEM READY!{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write(f'\r{Fore.CYAN}✅ SYSTEM READY!{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.15)
    
    print()
    time.sleep(0.5)

def loading_animation(text="PROCESSING", duration=2):
    chars = ['◐', '◓', '◑', '◒']
    tick = 0
    start = time.time()
    while time.time() - start < duration:
        tick += 0.1
        color = rgb_color(tick)
        idx = int((time.time() - start) * 8) % 4
        sys.stdout.write(f'\r{color}{chars[idx]} {text}...{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\r' + ' ' * 50 + '\r', end='')

# ============ BOOT ANIMATION ============
def boot_animation():
    clear()
    print(f"{Fore.GREEN}[{Fore.CYAN}SYSTEM{Fore.GREEN}] {Fore.WHITE}Booting RXIND...{Style.RESET_ALL}")
    time.sleep(0.5)
    
    boot_messages = [
        f"{Fore.GREEN}[{Fore.CYAN}OK{Fore.GREEN}] {Fore.WHITE}Loading core modules...{Style.RESET_ALL}",
        f"{Fore.GREEN}[{Fore.CYAN}OK{Fore.GREEN}] {Fore.WHITE}Initializing 60 API handlers...{Style.RESET_ALL}",
        f"{Fore.GREEN}[{Fore.CYAN}OK{Fore.GREEN}] {Fore.WHITE}Establishing secure connection...{Style.RESET_ALL}",
        f"{Fore.GREEN}[{Fore.CYAN}OK{Fore.GREEN}] {Fore.WHITE}Loading user interface...{Style.RESET_ALL}",
        f"{Fore.GREEN}[{Fore.CYAN}OK{Fore.GREEN}] {Fore.WHITE}Loading animations...{Style.RESET_ALL}",
        f"{Fore.GREEN}[{Fore.CYAN}OK{Fore.GREEN}] {Fore.WHITE}System ready!{Style.RESET_ALL}",
    ]
    
    for msg in boot_messages:
        print(msg)
        time.sleep(0.3)
    
    print(f"\n{Fore.GREEN}[{Fore.CYAN}SYSTEM{Fore.GREEN}] {Fore.WHITE}RXIND is ready to use!{Style.RESET_ALL}")
    time.sleep(1)

# ============ BANNER ============
def banner():
    clear()
    tick = time.time()
    main_color = rgb_color(tick, 0)
    
    banner_text = f"""
{main_color}╔══════════════════════════════════════════════════════════════════════════╗
{main_color}║                                                                          ║
{main_color}║   {Fore.WHITE}██████╗ ██╗  ██╗██╗███╗   ██╗██████╗ {main_color}                          ║
{main_color}║   {Fore.WHITE}██╔══██╗╚██╗██╔╝██║████╗  ██║██╔══██╗{main_color}                          ║
{main_color}║   {Fore.WHITE}██████╔╝ ╚███╔╝ ██║██╔██╗ ██║██║  ██║{main_color}                          ║
{main_color}║   {Fore.WHITE}██╔══██╗ ██╔██╗ ██║██║╚██╗██║██║  ██║{main_color}                          ║
{main_color}║   {Fore.WHITE}██║  ██║██╔╝ ██╗██║██║ ╚████║██████╔╝{main_color}                          ║
{main_color}║   {Fore.WHITE}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ {main_color}                          ║
{main_color}║                                                                          ║
{main_color}║   {Fore.YELLOW}⛧ RXIND - OTP SPAMMER PRO ⛧{main_color}                                    ║
{main_color}║   {Fore.CYAN}VERSION {VERSION} | 60 API SUPPORT{main_color}                                ║
{main_color}║   {Fore.GREEN}DEVELOPER: RXIND{main_color}                                                ║
{main_color}╚══════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner_text)
    for _ in range(2):
        print(f"{Fore.GREEN}{glitch_text('█' * random.randint(50, 70), 0.2)}{Style.RESET_ALL}")
        time.sleep(0.05)

# ============ MENU ============
def menu():
    tick = time.time()
    print(f"""
{Fore.CYAN}┌─────────────────────────────────────────────────────────────────────────┐
│  {Fore.RED}▶{Fore.WHITE} [1] {Fore.GREEN}SINGLE ROUND{Fore.WHITE}  ── Kirim OTP 1x ke semua API          │
│  {Fore.RED}▶{Fore.WHITE} [2] {Fore.GREEN}INFINITE LOOP{Fore.WHITE} ── Kirim OTP terus menerus             │
│  {Fore.RED}▶{Fore.WHITE} [3] {Fore.GREEN}RANDOM MODE{Fore.WHITE}   ── Kirim ke API random acak            │
│  {Fore.RED}▶{Fore.WHITE} [4] {Fore.GREEN}SHOW STATS{Fore.WHITE}    ── Lihat statistik API                 │
│  {Fore.RED}▶{Fore.WHITE} [5] {Fore.GREEN}ABOUT{Fore.WHITE}         ── Info tools RXIND                    │
│  {Fore.RED}▶{Fore.WHITE} [0] {Fore.RED}EXIT{Fore.WHITE}           ── Keluar dari tools                   │
└─────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}
""")

# ============ ABOUT ============
def about():
    clear()
    banner()
    tick = time.time()
    print(f"""
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════
{Fore.YELLOW}  ⛧ RXIND - OTP SPAMMER PRO ⛧
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════

{Fore.WHITE}  📌 Nama        : {Fore.GREEN}RXIND OTP SPAMMER
{Fore.WHITE}  📌 Version     : {Fore.GREEN}{VERSION}
{Fore.WHITE}  📌 Developer   : {Fore.GREEN}RXIND
{Fore.WHITE}  📌 API Support : {Fore.GREEN}60 API
{Fore.WHITE}  📌 Platform    : {Fore.GREEN}Termux / Linux / Windows
{Fore.WHITE}  📌 Animations  : {Fore.GREEN}25+ Animations

{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════
{Fore.YELLOW}  ⚠️  DISCLAIMER:
{Fore.WHITE}  Tools ini dibuat untuk tujuan edukasi.
{Fore.WHITE}  Penggunaan di luar tanggung jawab developer.
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════{Style.RESET_ALL}
""")
    input(f"\n{Fore.YELLOW}Press ENTER to continue...{Style.RESET_ALL}")

# ============ STATS ============
def show_stats():
    clear()
    banner()
    tick = time.time()
    print(f"""
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════
{Fore.YELLOW}  📊 STATISTIK API
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════

{Fore.WHITE}  {Fore.GREEN}Total API    : {Fore.WHITE}60
{Fore.WHITE}  {Fore.GREEN}Active       : {Fore.WHITE}24
{Fore.WHITE}  {Fore.RED}Down         : {Fore.WHITE}12
{Fore.WHITE}  {Fore.YELLOW}Rate Limited : {Fore.WHITE}3
{Fore.WHITE}  {Fore.CYAN}Animations   : {Fore.WHITE}25+

{Fore.CYAN}  Last Update : {Fore.WHITE}{time.strftime('%Y-%m-%d %H:%M:%S')}
{Fore.CYAN}═══════════════════════════════════════════════════════════════════════════{Style.RESET_ALL}
""")
    input(f"\n{Fore.YELLOW}Press ENTER to continue...{Style.RESET_ALL}")

# ============ EXECUTION ============
def run_with_animations(func, *args, **kwargs):
    # Tampilkan animasi sebelum eksekusi
    scanning_effect(1.2)
    loading_animation("EXECUTING", 1.2)
    pulse_effect("⚡ Starting...", 1)
    
    result = func(*args, **kwargs)
    
    # Tampilkan animasi setelah selesai
    fire_effect("✓ DONE!", 1.2)
    sparkle_effect("✨ Completed!", 1)
    return result

def main():
    # Boot animation
    boot_animation()
    clear()
    
    # Matrix loading
    matrix_loading(3)
    
    while True:
        banner()
        menu()
        
        choice = input(f"\n{Fore.GREEN}┌─[{Fore.WHITE}RXIND{Fore.GREEN}]─[{Fore.WHITE}SELECT{Fore.GREEN}]─> {Style.RESET_ALL}").strip()
        
        if choice == "1":
            target = input(f"{Fore.CYAN}└─ Target (08xx/62xx): {Style.RESET_ALL}").strip()
            if not target:
                print(f"{Fore.RED}✗ Nomor kosong!{Style.RESET_ALL}")
                time.sleep(1)
                continue
            
            # Animasi sebelum eksekusi
            pulse_effect("⚡ Single Round", 1)
            slide_in("🎯 Target: " + target, 0.5)
            countdown_effect(3)
            
            run_with_animations(run_single_round, target=target, threads=5)
            
            # Animasi selesai
            neon_glow("✨ Single Round Completed!", 1.5)
            rainbow_effect("🌈 Done!", 1)
            input(f"\n{Fore.YELLOW}Press ENTER to continue...{Style.RESET_ALL}")
            
        elif choice == "2":
            target = input(f"{Fore.CYAN}└─ Target (08xx/62xx): {Style.RESET_ALL}").strip()
            if not target:
                print(f"{Fore.RED}✗ Nomor kosong!{Style.RESET_ALL}")
                time.sleep(1)
                continue
            
            print(f"\n{Fore.YELLOW}⚠️  INFINITE LOOP ACTIVE — Press CTRL+C to stop{Style.RESET_ALL}")
            
            # Animasi sebelum eksekusi
            pulse_effect("♾️ Infinite Loop", 1)
            marquee_effect("🚀 Running infinite loop...", 2)
            wave_effect("🌊 Looping...", 1)
            countdown_effect(3)
            
            try:
                run_infinite_loop(target=target)
            except KeyboardInterrupt:
                print(f"\n\n{Fore.RED}⛔ STOPPED BY USER{Style.RESET_ALL}")
            
            input(f"\n{Fore.YELLOW}Press ENTER to continue...{Style.RESET_ALL}")
            
        elif choice == "3":
            target = input(f"{Fore.CYAN}└─ Target (08xx/62xx): {Style.RESET_ALL}").strip()
            if not target:
                print(f"{Fore.RED}✗ Nomor kosong!{Style.RESET_ALL}")
                time.sleep(1)
                continue
            
            api_count = random.randint(5, 15)
            print(f"\n{Fore.MAGENTA}🎲 Random Mode: Menghantam {api_count} API random{Style.RESET_ALL}")
            
            # Animasi sebelum eksekusi
            pulse_effect("🎲 Random Mode", 1)
            shake_effect("🔀 Randomizing...", 1)
            rotate_effect("🌀 Spinning...", 1)
            countdown_effect(3)
            
            run_with_animations(run_random_mode, target=target, limit=api_count)
            
            input(f"\n{Fore.YELLOW}Press ENTER to continue...{Style.RESET_ALL}")
            
        elif choice == "4":
            show_stats()
            
        elif choice == "5":
            about()
            
        elif choice == "0":
            print(f"\n{Fore.RED}⛧ EXITING RXIND...{Style.RESET_ALL}")
            fire_effect("🔥 Goodbye!", 1.5)
            sparkle_effect("✨ See you!", 1)
            print(f"{Fore.GREEN}  Sampai jumpa! 👋{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}✗ Pilihan tidak valid!{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}⛧ EXITING RXIND...{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  Sampai jumpa! 👋{Style.RESET_ALL}")
        sys.exit(0)