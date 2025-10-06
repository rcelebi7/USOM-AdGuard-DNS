import requests
import json
import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

USOM_URL = "https://www.usom.gov.tr/url-list.txt"
OUTPUT_FILENAME = "USOM-AdGuard-DNS.txt"
SCRAPINGANT_API_KEY = "4ed372b18b5942e5b3bab7c8144baec6"

def download_list():
    print(f"'{USOM_URL}' adresinden proxy ile liste indiriliyor...")
    proxy_url = f"https://api.scrapingant.com/v2/general?url={USOM_URL}&browser=false&x-api-key={SCRAPINGANT_API_KEY}"
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        status_forcelist=[429, 500, 502, 503, 504],
        backoff_factor=1
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount('https://', adapter)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = session.get(proxy_url, timeout=60, headers=headers)
        response.raise_for_status()
        data = response.json()
        content = data.get('content')
        if content is None:
            print("HATA: Proxy'den gelen cevapta 'content' alani bulunamadi.")
            raise SystemExit("Proxy'den bos cevap geldi.")
        print("Liste basariyla indirildi.")
        return content.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"HATA: Liste birden cok denemeye ragmen indirilemedi. Hata: {e}")
        raise SystemExit(e)

def convert_to_adguard(lines):
    print("Liste AdGuard formatina cevriliyor...")
    domains_to_block = []
    for line in lines:
        domain = line.strip()
        if domain and not domain.startswith(('#', '!')):
            domains_to_block.append(f"||{domain}^")
            
    domain_count = len(domains_to_block)
    
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    last_modified = utc_now.strftime("%d %b %Y %H:%M UTC")
    version = utc_now.strftime("%Y%m%d.%H%M")

    header_lines = [
        "! Title: USOM Phishing and Malware Domain Blocklist",
        "! Description: Blocks domains published by the Turkish National Cyber Incident Response Center (USOM).",
        "! Homepage: https://www.usom.gov.tr",
        "! Source: Data is obtained from usom.gov.tr via proxy",
        "! Expires: 1 day (Daily update recommended)",
        f"! Last modified: {last_modified}",
        f"! Version: {version}",
        f"! Number of entries: {domain_count}",
        "!"
    ]
    
    header = "\n".join(header_lines)
    full_content = header + "\n" + "\n".join(domains_to_block)
    print(f"{domain_count} adet domain islendi.")
    return full_content

def save_list(content):
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Liste basariyla '{OUTPUT_FILENAME}' dosyasina kaydedildi.")

if __name__ == "__main__":
    raw_lines = download_list()
    adguard_list_content = convert_to_adguard(raw_lines)
    save_list(adguard_list_content)
    print("Islem tamamlandi.")
