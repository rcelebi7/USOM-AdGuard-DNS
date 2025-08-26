import requests
import datetime
import os

# --- AYARLAR ---
# USOM'un yayınladığı güncel listenin URL'si
USOM_URL = "https://www.usom.gov.tr/url-list.txt"

# Oluşturulacak dosyanın adı
OUTPUT_FILENAME = "USOM-AdGuard-DNS.txt"

def download_list():
    """USOM'dan ham domain listesini indirir."""
    print(f"'{USOM_URL}' adresinden liste indiriliyor...")
    try:
        response = requests.get(USOM_URL, timeout=30)
        response.raise_for_status()
        print("Liste başarıyla indirildi.")
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"HATA: Liste indirilemedi. Hata: {e}")
        raise SystemExit(e)

def convert_to_adguard(lines):
    """
    Ham domain listesini AdGuard formatına çevirir ve
    profesyonel bir başlık ekler.
    """
    print("Liste AdGuard formatına çevriliyor...")
    domains_to_block = []
    for line in lines:
        domain = line.strip()
        if domain and not domain.startswith(('#', '!')):
            domains_to_block.append(f"||{domain}^")
            
    domain_count = len(domains_to_block)
    
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    last_modified = utc_now.strftime("%d %b %Y %H:%M UTC")
    version = utc_now.strftime("%Y.%m%d.%H%M")

    header_lines = [
        "! Title: USOM Phishing and Malware Domain Blocklist",
        "! Description: Blocks domains published by the Turkish National Cyber Incident Response Center (USOM) primarily used for phishing and malware distribution.",
        "! Homepage: https://www.usom.gov.tr",
        "! Source: Data is obtained from USOM.GOV.TR.",
        "! License: Not specified (Publicly available data).",
        "! Expires: 7 days (Weekly update recommended)",
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
    """Oluşturulan listeyi dosyaya yazar."""
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Liste başarıyla '{OUTPUT_FILENAME}' dosyasına kaydedildi.")

if __name__ == "__main__":
    raw_lines = download_list()
    adguard_list_content = convert_to_adguard(raw_lines)
    save_list(adguard_list_content)
    print("İşlem tamamlandı.")
