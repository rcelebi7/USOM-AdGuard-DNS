import requests
import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

USOM_URL = "https://www.usom.gov.tr/url-list.txt"
OUTPUT_FILENAME = "USOM-AdGuard-DNS.txt"

def download_list():
    print(f"'{USOM_URL}' adresinden liste indiriliyor...")

    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        status_forcelist=[429, 500, 502, 503, 504],  # 429 (rate limit) eklendi
        allowed_methods=["GET"],  # method_whitelist yerine allowed_methods (yeni API)
        backoff_factor=2  # 1'den 2'ye çıkardım (2, 4, 8, 16, 32 saniye bekler)
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount('https://', adapter)
    session.mount('http://', adapter)  # HTTP için de ekledim

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive"
    }

    try:
        response = session.get(USOM_URL, timeout=300, headers=headers)  # 300 saniye = 5 dakika
        response.raise_for_status()
        print(f"Liste başarıyla indirildi. ({len(response.text.splitlines())} satır)")
        return response.text.splitlines()
    except requests.exceptions.Timeout:
        print(f"HATA: 5 dakikalık timeout süresi doldu. USOM sunucusu yanıt vermiyor.")
        raise SystemExit("Timeout error")
    except requests.exceptions.RequestException as e:
        print(f"HATA: Liste birden çok denemeye rağmen indirilemedi. Hata: {e}")
        raise SystemExit(e)

def convert_to_adguard(lines):
    print("Liste AdGuard formatına çevriliyor...")
    domains_to_block = []
    skipped = 0
    
    for line in lines:
        domain = line.strip()
        if not domain or domain.startswith(('#', '!')):
            skipped += 1
            continue
        
        # Boş veya geçersiz domain kontrolü
        if len(domain) < 3 or ' ' in domain:
            skipped += 1
            continue
            
        domains_to_block.append(f"||{domain}^")
    
    if skipped > 0:
        print(f"{skipped} geçersiz/yorum satırı atlandı.")
            
    domain_count = len(domains_to_block)
    
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    last_modified = utc_now.strftime("%d %b %Y %H:%M UTC")
    version = utc_now.strftime("%Y.%m%d.%H%M")

    header_lines = [
        "! Title: USOM Phishing and Malware Domain Blocklist",
        "! Description: Blocks domains published by the Turkish National Cyber Incident Response Center (USOM) primarily used for phishing and malware distribution.",
        "! Homepage: https://www.usom.gov.tr",
        "! Source: Data is obtained from usom.gov.tr",
        "! License: Not specified (Publicly available data).",
        "! Expires: 7 days (Daily update recommended)",
        f"! Last modified: {last_modified}",
        f"! Version: {version}",
        "! Syntax: AdBlock",
        f"! Number of entries: {domain_count}",
        "!"
    ]
    
    header = "\n".join(header_lines)
    full_content = header + "\n" + "\n".join(domains_to_block)
    print(f"{domain_count} adet domain işlendi.")
    return full_content

def save_list(content):
    try:
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Liste başarıyla '{OUTPUT_FILENAME}' dosyasına kaydedildi.")
    except IOError as e:
        print(f"HATA: Dosya kaydedilemedi. Hata: {e}")
        raise SystemExit(e)

if __name__ == "__main__":
    try:
        raw_lines = download_list()
        adguard_list_content = convert_to_adguard(raw_lines)
        save_list(adguard_list_content)
        print("İşlem tamamlandı.")
    except SystemExit as e:
        print(f"Program sonlandırıldı: {e}")
        exit(1)
