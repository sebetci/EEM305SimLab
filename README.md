# EEM305SimLab — 8051 Simülasyon Laboratuvarı

**EEM305 Mikroişlemciler** dersi (Prof. Dr. Şuayb Çağrı Yener, Sakarya Üniversitesi) kapsamında bir simülasyon aracı olarak **Sercan Sebetçi** tarafından hazırlanmıştır.

MCS-51 (8051) mimarisi için etkileşimli bir öğrenme ortamıdır. Komutları adım adım çalıştırarak program sayacı, stack pointer, register'lar, dahili RAM ve flash bellekteki değişimleri izleyebilir, kendi assembly programınızı yazıp simüle edebilirsiniz.

## Hemen Kullan

- **Tarayıcıda aç:** https://sebetci.github.io/EEM305SimLab/EEM305SimLab.html
- **İndir:** `EEM305SimLab.html` dosyasını indirip çift tıklayın. İnternet bağlantısı gerekmez.

## Özellikler

- **Alt Program Çağrıları:** ACALL / LCALL / RET; PC, SP, stack, flash ve RAM mikro adımlarla
- **Code Lab:** Sözdizimi renklendirmeli editör, tarayıcı içi 8051 assembler ve emülatör
- **Veri Akışı Diyagramı:** Flash ↔ CPU (PC, SP) ↔ RAM arasında animasyonlu veri paketleri
- **Zaman Çizelgesi:** SP ve A değerlerinin adım adım grafiği
- **Komut Seti:** 8051'in 111 komutunun tamamı; opcode, byte, çevrim ve bayrak bilgileriyle
- Türkçe / İngilizce arayüz, açık / koyu tema

## Güvenlik ve Doğrulama

Uygulama **internete bağlanamaz**: dosyanın başındaki İçerik Güvenliği Politikası (CSP) tüm ağ isteklerini tarayıcı düzeyinde engeller. Ayrıntılar için: [SECURITY.md](SECURITY.md)

| Doğrulama | |
|---|---|
| SHA-256 (`EEM305SimLab.html`) | `c0694fec27c4f6ac0f228ab42924799173675e510fcacba01d99c7c2c437d7f9` |
| VirusTotal raporu | VIRUSTOTAL_RAPOR_BAGLANTISI |
| Tüm özet değerleri | [SHA256SUMS.txt](SHA256SUMS.txt) |

Windows'ta doğrulamak için PowerShell'de:

```powershell
Get-FileHash EEM305SimLab.html -Algorithm SHA256
```

## Kaynak Koddan Derleme

Gereksinimler: Node.js 18+ ve Python 3.

```bash
cd build
npm ci
npm run build
```

Derleme, `src/EEM305SimLab.src.html` dosyasına kütüphaneleri, yazı tiplerini ve ikonları gömerek depo kökünde `EEM305SimLab.html` dosyasını üretir. Derleme tekrarlanabilirdir; aynı kaynak her zaman aynı SHA-256 değerini verir.

## Depo Yapısı

```
EEM305SimLab.html          Kullanıma hazır tek dosya (derlenmiş)
index.html                 GitHub Pages için yönlendirme sayfası
SHA256SUMS.txt             SHA-256 özet değerleri
SECURITY.md                Güvenlik dokümanı
THIRD_PARTY_LICENSES.md    Gömülü kütüphanelerin lisansları
src/EEM305SimLab.src.html  Okunabilir kaynak kod
build/                     Derleme betiği ve sabitlenmiş bağımlılıklar
```

## Kullanılan Kütüphaneler

CodeMirror 6 (MIT) · Chart.js 4.6.1 (MIT) · GSAP 3.15.1 (GSAP Standard License) · Lucide 1.70.0 (ISC) · Inter ve JetBrains Mono (SIL OFL 1.1). Lisans metinleri: [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)

## İletişim

sercan.sebetci@ogr.sakarya.edu.tr

---

## English

**EEM305SimLab** is an interactive 8051 (MCS-51) learning environment prepared by Sercan Sebetçi as a simulation tool for the EEM305 Microprocessors course taught by Prof. Dr. Şuayb Çağrı Yener at Sakarya University. It is a single, offline HTML file: open `EEM305SimLab.html` in any modern browser or use the GitHub Pages link above. Network access is blocked by a Content Security Policy; see [SECURITY.md](SECURITY.md) for details and verification steps.
