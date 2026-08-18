#!/usr/bin/env python3
# utils.py - RXIND Utility Functions

import re
import uuid
import random
import string
import urllib.parse
import time
import requests
from useragents import USER_AGENTS

# ============ PROXY SUPPORT (OPSIONAL) ============
PROXY_LIST = [
    # "http://proxy1:8080",
    # "socks5://proxy2:1080",
]

def get_proxy():
    """Dapatkan proxy random dari daftar"""
    return random.choice(PROXY_LIST) if PROXY_LIST else None

def get_session_with_proxy(proxy=None):
    """Buat session dengan proxy & retry"""
    session = requests.Session()
    
    # Retry logic
    retries = requests.adapters.Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = requests.adapters.HTTPAdapter(max_retries=retries, pool_connections=25, pool_maxsize=25)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    # Proxy
    if proxy is None:
        proxy = get_proxy()
    if proxy:
        session.proxies = {'http': proxy, 'https': proxy}
    
    return session

# ============ NORMALIZE & VALIDATE ============
def normalize(phone):
    """Normalisasi nomor telepon ke format 62"""
    n = phone.strip().replace(' ', '').replace('-', '').replace('+', '')
    if n.startswith('08'):
        return '62' + n[1:]
    if n.startswith('8'):
        return '62' + n
    if n.startswith('62'):
        return n
    return ''

def validate_phone(phone):
    """Validasi nomor telepon (minimal 10 digit)"""
    n = re.sub(r'\D', '', phone)
    return len(n) >= 10 and len(n) <= 15

# ============ FORMAT FUNCTIONS ============
def fmt_08(p):
    """Format ke 08"""
    return '0' + p[2:] if p.startswith('62') else p

def fmt_nocode(p):
    """Format tanpa kode negara"""
    return p[2:] if p.startswith('62') else p

def fmt_plus(p):
    """Format ke +62"""
    return '+' + p if not p.startswith('+') else p

def fmt_phone_only(p):
    """Format nomor saja tanpa kode"""
    if p.startswith('62'):
        return p[2:]
    if p.startswith('+62'):
        return p[3:]
    if p.startswith('0'):
        return p[1:]
    return p

# ============ IP & NETWORK ============
def get_public_ip():
    """Mendapatkan IP publik dengan fallback"""
    services = [
        'https://api.ipify.org',
        'https://icanhazip.com',
        'https://ident.me',
    ]
    for service in services:
        try:
            resp = requests.get(service, timeout=5)
            if resp.status_code == 200:
                return resp.text.strip()
        except:
            continue
    return '127.0.0.1'

# ============ CSRF EXTRACTION ============
def extract_csrf(html, cookies=None):
    """Ekstrak CSRF token dari HTML atau cookie"""
    patterns = [
        r'<meta name="csrf-token" content="([^"]+)"',
        r'<meta name="csrf_token" content="([^"]+)"',
        r'<input type="hidden" name="_token" value="([^"]+)"',
        r'<input type="hidden" name="csrf_token" value="([^"]+)"',
        r'<input type="hidden" name="_csrf" value="([^"]+)"',
        r'csrf_token\s*=\s*"([^"]+)"',
        r'var\s+csrfToken\s*=\s*"([^"]+)"',
        r'"csrfToken":"([^"]+)"',
    ]
    for p in patterns:
        m = re.search(p, html, re.I)
        if m:
            return m.group(1)
    
    # Coba dari cookie
    if cookies:
        for cookie in cookies:
            if cookie.name in ['XSRF-TOKEN', 'csrf_token', '_csrf']:
                return urllib.parse.unquote(cookie.value)
    
    return None

# ============ MULTIPART ============
def generate_multipart(data, boundary):
    """Generate multipart form data"""
    body = ""
    for key, val in data.items():
        body += f"--{boundary}\r\n"
        body += f'Content-Disposition: form-data; name="{key}"\r\n\r\n'
        body += f"{val}\r\n"
    body += f"--{boundary}--\r\n"
    return body

# ============ USER-AGENT ============
def get_random_user_agent():
    """Dapatkan user agent random"""
    return random.choice(USER_AGENTS)

def get_headers_with_random_ua(custom_headers=None):
    """Dapatkan headers dengan user agent random"""
    headers = {
        'User-Agent': get_random_user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
    }
    if custom_headers:
        headers.update(custom_headers)
    return headers

# ============ DELAY & JITTER ============
def random_delay(min_sec=0.3, max_sec=1.5):
    """Delay acak biar gak ketauan bot"""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay

def jitter_delay(base=0.5, jitter=0.3):
    """Delay dengan jitter (lebih natural)"""
    delay = base + random.uniform(-jitter, jitter)
    if delay < 0.1:
        delay = 0.1
    time.sleep(delay)
    return delay

# ============ GENERATORS ============
def generate_random_name():
    """Generate random name"""
    prefixes = ['User', 'Test', 'Demo', 'Sample', 'Guest']
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return random.choice(prefixes) + suffix

def generate_random_email():
    """Generate random email"""
    domains = ['gmail.com', 'yahoo.com', 'mailnesia.com', 'tempmail.com', 'outlook.com']
    name = generate_random_name().lower()
    return f"{name}{random.randint(100, 999)}@{random.choice(domains)}"

def generate_random_password():
    """Generate random password"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return 'Pass' + ''.join(random.choices(chars, k=8)) + '1'

# ============ RESPONSE CHECKER ============
def check_success(response, keywords):
    """Cek apakah response mengandung keyword sukses"""
    if not response:
        return False
    try:
        text = response.text.lower() if hasattr(response, 'text') else str(response).lower()
        for kw in keywords:
            if kw.lower() in text:
                return True
    except:
        pass
    return False

# ============ TESTING ============
if __name__ == "__main__":
    print("=== RXIND UTILS TEST ===")
    
    # Test normalize
    test_numbers = ['081234567890', '6281234567890', '+6281234567890', '81234567890']
    for num in test_numbers:
        print(f"normalize('{num}') -> '{normalize(num)}'")
    
    # Test format functions
    print(f"\nfmt_08('6281234567890') -> '{fmt_08('6281234567890')}'")
    print(f"fmt_nocode('6281234567890') -> '{fmt_nocode('6281234567890')}'")
    print(f"fmt_plus('6281234567890') -> '{fmt_plus('6281234567890')}'")
    print(f"fmt_phone_only('6281234567890') -> '{fmt_phone_only('6281234567890')}'")
    
    # Test IP
    print(f"\nIP Publik: {get_public_ip()}")
    
    # Test random functions
    print(f"\nRandom Name: {generate_random_name()}")
    print(f"Random Email: {generate_random_email()}")
    print(f"Random Password: {generate_random_password()}")