# USOM AdGuard DNS Blocklist

[![Update USOM Blocklist](https://github.com/rcelebi7/USOM-AdGuard-DNS/actions/workflows/update.yml/badge.svg)](https://github.com/rcelebi7/USOM-AdGuard-DNS/actions/workflows/update.yml)

Bu proje, Türkiye Ulusal Siber Olaylara Müdahale Merkezi (USOM) tarafından yayınlanan zararlı bağlantılar listesini, AdGuard Home, AdGuard DNS ve diğer DNS tabanlı engelleyicilerle uyumlu hale getiren otomatik bir sistemdir.

This project is an automated system that converts the malicious domain list published by the Turkish National Cyber Incident Response Center (USOM) into a compatible format for AdGuard Home, AdGuard DNS, and other DNS-based blockers.

---

## 🇹🇷 Türkçe

### Bu Liste Nedir?

Bu liste, USOM'un genellikle oltalama (phishing), dolandırıcılık ve zararlı yazılım dağıtımı amacıyla kullanıldığını tespit ettiği alan adlarını (domain) içerir. Bu depo, USOM'un ham listesini her hafta otomatik olarak alıp AdGuard'ın anlayacağı `||domain.com^` formatına çevirir ve kullanıma sunar.

**Amacı:** Türkiye'deki kullanıcıları hedef alan güncel siber tehditlere karşı ek bir koruma katmanı sağlamaktır.

### Nasıl Kullanılır?

Aşağıdaki linki, kullandığınız DNS engelleyicinin "Filtre Listeleri" veya "Blocklists" bölümüne eklemeniz yeterlidir.

> **https://raw.githubusercontent.com/rcelebi7/USOM-AdGuard-DNS/main/USOM-AdGuard-DNS.txt**

#### AdGuard Home / AdGuard DNS

1.  `Filtreler` -> `DNS Yasaklama Listeleri` bölümüne gidin.
2.  `Yasaklama listesi ekle` butonuna basın.
3.  `Özel bir liste ekle` seçeneğini seçin.
4.  Listeye bir isim verin (Örn: `USOM Blocklist`).
5.  URL olarak yukarıdaki linki yapıştırın.
6.  Kaydedin. Liste bir sonraki güncellemede aktif olacaktır.

#### Diğer AdGuard Uygulamaları (iOS, Android, Windows, Mac)

1.  `Ayarlar` -> `DNS Koruması` -> `DNS Filtreleme` -> `DNS Filtreleri` bölümüne gidin.
2.  `+` butonuyla yeni bir filtre ekleyin.
3.  URL olarak yukarıdaki linki yapıştırın ve kaydedin.

### Listenin İçeriği ve Güncelliği

* **Kaynak:** [USOM Zararlı Bağlantılar](https://www.usom.gov.tr/url-list.txt)
* **Format:** AdGuard DNS `||domain.com^`
* **Güncelleme Sıklığı:** 3 saatte bir otomatik olarak güncellenir.
* **Otomasyon:** Süreç, [GitHub Actions](https://github.com/rcelebi7/USOM-AdGuard-DNS/actions) ile tamamen otomatiktir.

---

## 🇬🇧 English

### What is this list?

This list contains domains identified by USOM (Turkish National Cyber Incident Response Center) as being used for phishing, fraud, and malware distribution. This repository automatically fetches the raw list from USOM every week, converts it into the AdGuard-compatible `||domain.com^` format, and makes it available for public use.

**Purpose:** To provide an additional layer of protection against current cyber threats targeting users in Turkey.

### How to Use

Simply add the URL below to the "Filter Lists" or "Blocklists" section of your preferred DNS blocker.

> **https://raw.githubusercontent.com/rcelebi7/USOM-AdGuard-DNS/main/USOM-AdGuard-DNS.txt**

#### AdGuard Home / AdGuard DNS

1.  Go to `Filters` -> `DNS blocklists`.
2.  Click `Add blocklist`.
3.  Choose `Add a custom list`.
4.  Give the list a name (e.g., `USOM Blocklist`).
5.  Paste the URL provided above.
6.  Save the list. It will become active on the next update cycle.

#### Other AdGuard Apps (iOS, Android, Windows, Mac)

1.  Go to `Settings` -> `DNS Protection` -> `DNS Filtering` -> `DNS Filters`.
2.  Add a new filter using the `+` button.
3.  Paste the URL provided above and save.

### List Content and Update Frequency

* **Source:** [USOM Malicious Links](https://www.usom.gov.tr/url-list.txt)
* **Format:** AdGuard DNS `||domain.com^`
* **Update Frequency:** Automatically updated every 3 hours.
* **Automation:** The process is fully automated using [GitHub Actions](https://github.com/rcelebi7/USOM-AdGuard-DNS/actions).

---

### Sorumluluk Reddi / Disclaimer

Bu liste, USOM tarafından sağlanan kamuya açık veriler kullanılarak otomatik olarak oluşturulmuştur ve "olduğu gibi" sunulmaktadır. Listenin kullanımıyla ilgili tüm sorumluluk kullanıcıya aittir. Hatalı engelleme (false positive) olasılığı mevcuttur. Bu depo, listenin içeriğinden sorumlu değildir; yalnızca veriyi dönüştüren ve sunan bir aracıdır.

This list is generated automatically using publicly available data from USOM and is provided "as is". The user assumes all responsibility for its use. The possibility of false positives exists. This repository is not responsible for the content of the list; it is merely a tool that converts and serves the data.
