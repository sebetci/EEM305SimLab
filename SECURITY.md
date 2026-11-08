# Güvenlik Dokümanı / Security

**Proje:** EEM305SimLab — 8051 Mikrodenetleyici Simülasyon Laboratuvarı
**Sürüm:** 1.0.0 · **Tarih:** 8 Kasım 2026
**Hazırlayan:** Sercan Sebetçi · sercan.sebetci@ogr.sakarya.edu.tr
**Ders:** EEM305 Mikroişlemciler — Prof. Dr. Şuayb Çağrı Yener, Sakarya Üniversitesi

> English summary is at the end of this document.

---

## 1. Özet

EEM305SimLab, tarayıcıda açılan **tek bir HTML dosyasıdır**. Kurulum gerektirmez, bilgisayara hiçbir şey yüklemez ve **internete bağlanamaz**. Bu son özellik bir vaat değil, tarayıcı tarafından zorla uygulanan bir kuraldır (bkz. Bölüm 3).

| Özellik | Durum |
|---|---|
| Bilgisayara kurulum | Yok |
| İnternet bağlantısı | Teknik olarak engelli (CSP: `connect-src 'none'`) |
| Dışarıdan kod / yazı tipi / görsel yükleme | Teknik olarak engelli (CSP: `default-src 'none'`) |
| `eval` ve benzeri dinamik kod çalıştırma | Teknik olarak engelli (CSP'de `'unsafe-eval'` yok) |
| Dosya sistemine erişim | Yalnızca kullanıcı bir butona basıp dosyayı kendisi seçtiğinde |
| Kişisel veri toplama | Yok |
| Kaynak kodu | Açık (GitHub), yeniden derlenebilir |

## 2. Uygulama Ne Yapar, Ne Yapmaz

**Yapar:**
- 8051 komutlarını tarayıcı içinde simüle eder ve sonuçları ekranda gösterir.
- Code Lab'da yazılan assembly kodunu, JavaScript ile yazılmış bir assembler ve emülatörle **yorumlar**. Kullanıcının yazdığı kod hiçbir zaman JavaScript olarak çalıştırılmaz; yalnızca 8051 komutu olarak çözümlenir.
- Tercihleri (dil, tema vb.) ve Code Lab'daki kodu tarayıcının yerel depolamasında saklar (bkz. Bölüm 4).

**Yapmaz:**
- İnternete veri göndermez, internetten veri almaz.
- Çerez (cookie) kullanmaz, analiz/izleme aracı içermez.
- Kullanıcı seçmedikçe hiçbir dosyayı okumaz veya yazmaz.
- Başka program çalıştırmaz, eklenti veya uzantı yüklemez.

## 3. Ağ Erişiminin Kapatılması: İçerik Güvenliği Politikası (CSP)

Dosyanın en başında, `<head>` bölümünde şu satır bulunur:

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; font-src data:; img-src data: blob:; connect-src 'none'; media-src 'none'; object-src 'none'; frame-src 'none'; worker-src 'none'; manifest-src 'none'; form-action 'none'; base-uri 'none'">
```

Tarayıcı bu kuralları sayfa açılır açılmaz uygular; sayfadaki kod bunları değiştiremez.

| Kural | Anlamı |
|---|---|
| `default-src 'none'` | Açıkça izin verilmeyen hiçbir kaynak yüklenemez. |
| `script-src 'unsafe-inline'` | Yalnızca dosyanın içindeki kod çalışır; dışarıdan betik yüklenemez. `'unsafe-eval'` olmadığı için `eval()` ve `new Function()` da engellidir. |
| `style-src 'unsafe-inline'` | Yalnızca dosyanın içindeki stiller kullanılır. |
| `font-src data:` / `img-src data: blob:` | Yazı tipleri ve görseller yalnızca dosyanın içine gömülü veriden gelebilir. |
| `connect-src 'none'` | `fetch`, `XMLHttpRequest`, `WebSocket` vb. **tüm ağ bağlantıları engellidir.** |
| `frame-src`, `object-src`, `worker-src`, `media-src`, `manifest-src` `'none'` | Gömülü sayfa, eklenti, arka plan işçisi ve medya yüklenemez. |
| `form-action 'none'` | Hiçbir form bir sunucuya gönderilemez. |
| `base-uri 'none'` | Sayfanın bağlantı adresleri başka bir sunucuya yönlendirilemez. |

**Neden `'unsafe-inline'` var?** Uygulama tek dosyadan oluştuğu için tüm kod dosyanın içindedir; bu izin yalnızca dosyanın kendi kodunun çalışmasını sağlar. Dışarıdan gelen hiçbir içerik kod olarak çalıştırılmaz.

Bu kural, geliştirme sırasında otomatik testle doğrulanmıştır: sayfadan `https://example.com` adresine yapılan deneme isteği tarayıcı tarafından engellenmiş ve uygulama kullanımı boyunca dosya dışında hiçbir ağ isteği gözlenmemiştir.

## 4. Tarayıcıda Saklanan Veriler

Tüm veriler yalnızca kullanıcının kendi tarayıcısında kalır; hiçbir yere gönderilmez.

| Depolama | Anahtar | İçerik |
|---|---|---|
| localStorage | `eem305.settings` | Dil, tema, animasyon ve "kaldığın yerden devam" tercihleri |
| localStorage | `eem305.labCode` | Code Lab'da yazılan son assembly kodu |
| localStorage | `eem305.step.call-stack`, `eem305.step.code-lab` | Simülasyonlarda kalınan adım numarası |
| IndexedDB | `eem305` → `kv` → `fileHandle` | "Ayarları Dosyaya Kaydet" için kullanıcının seçtiği dosyanın tutamacı (yalnızca Chrome/Edge) |

Bu verileri silmek için: Ayarlar sayfasında "Dosyadaki Ayarlara Dön" ve "Dosya Bağlantısını Kaldır" butonları kullanılabilir ya da tarayıcının site verileri temizlenebilir.

## 5. Dosya Erişimi

Uygulama yalnızca şu durumlarda dosyalarla etkileşir; hepsi kullanıcının bir butona basmasıyla başlar:

| İşlem | Nasıl çalışır |
|---|---|
| Ayarları Dosyaya Kaydet | Chrome/Edge'de kullanıcı hedef HTML dosyasını kendisi seçer (File System Access API). Tarayıcı ayrıca düzenleme izni sorar. Diğer tarayıcılarda dosya indirilir. |
| .asm Dosyası Aç | Kullanıcının seçtiği tek dosya okunur. |
| .asm İndir | Yazılan kod indirme olarak kaydedilir. |

> **Not:** "Ayarları Dosyaya Kaydet" HTML dosyasının içindeki `FILE_SETTINGS` satırını değiştirir. Bu nedenle ayar kaydedilmiş bir kopyanın SHA-256 değeri yayınlanan değerle **eşleşmez**. Doğrulamayı her zaman GitHub'dan indirilen, değiştirilmemiş dosya üzerinde yapın.

## 6. Harici Bağlantılar

Hakkında sayfasındaki kütüphane ve kaynak bağlantıları ile e-posta adresi, yalnızca kullanıcı tıkladığında yeni sekmede açılır. Sayfa bu bağlantılardan otomatik olarak hiçbir şey yüklemez.

## 7. Gömülü Üçüncü Taraf Bileşenler

| Bileşen | Sürüm | Lisans | Kullanım |
|---|---|---|---|
| CodeMirror 6 | 6.0.2 | MIT | Code Lab kod editörü |
| Chart.js | 4.6.1 | MIT | Zaman çizelgesi grafiği |
| GSAP + MotionPathPlugin | 3.15.1 | GSAP Standard License | Animasyonlar |
| Lucide Icons | 1.70.0 | ISC | Arayüz ikonları |
| Inter | variable | SIL OFL 1.1 | Arayüz yazı tipi |
| JetBrains Mono | variable | SIL OFL 1.1 | Kod yazı tipi |

Tüm bileşenler npm üzerinden, `build/package-lock.json` dosyasında sabitlenmiş sürümlerle alınır. Lisans metinleri `THIRD_PARTY_LICENSES.md` dosyasındadır.

## 8. Dosyanın Doğrulanması

### 8.1 SHA-256 özet değeri

Yayınlanan değerler `SHA256SUMS.txt` dosyasındadır:

```
c0694fec27c4f6ac0f228ab42924799173675e510fcacba01d99c7c2c437d7f9  EEM305SimLab.html
```

Kendi bilgisayarınızda hesaplamak için:

| Sistem | Komut |
|---|---|
| Windows (PowerShell) | `Get-FileHash EEM305SimLab.html -Algorithm SHA256` |
| Windows (Komut İstemi) | `certutil -hashfile EEM305SimLab.html SHA256` |
| macOS | `shasum -a 256 EEM305SimLab.html` |
| Linux | `sha256sum EEM305SimLab.html` |

Çıkan değer yukarıdakiyle birebir aynıysa dosya değiştirilmemiştir.

### 8.2 VirusTotal taraması

Dosyanın bağımsız virüs taraması raporu: *(rapor bağlantısı README.md dosyasındadır)*

### 8.3 Ağ trafiğini kendiniz izleyin

1. Dosyayı tarayıcıda açın ve **F12** ile geliştirici araçlarını açın.
2. **Network (Ağ)** sekmesine geçin ve sayfayı yenileyin (F5).
3. Uygulamanın tüm sayfalarını gezin, simülasyonları çalıştırın.
4. Listede dosyanın kendisi dışında hiçbir istek görünmemelidir.

### 8.4 Güvenlik politikasını kendiniz görün

Dosyayı bir metin düzenleyicide (ör. Not Defteri) açın; ilk satırlarda Bölüm 3'teki `Content-Security-Policy` satırını göreceksiniz.

### 8.5 Dosyayı kaynak koddan kendiniz üretin

Kaynak kod (`src/`) ve derleme betiği (`build/`) depodadır. Node.js ve Python 3 kurulu bir bilgisayarda:

```bash
cd build
npm ci
npm run build
```

Bu işlem depo kökünde `EEM305SimLab.html` dosyasını üretir ve SHA-256 değerini ekrana yazar. Değer, yayınlanan değerle aynı olmalıdır (derleme tekrarlanabilir şekilde tasarlanmıştır ve bu durum temiz bir ortamda doğrulanmıştır).

## 9. Güvenlik Sorunu Bildirme

Bir güvenlik sorunu fark ederseniz lütfen **sercan.sebetci@ogr.sakarya.edu.tr** adresine e-posta gönderin ya da GitHub deposunda bir "Issue" açın.

---

## English Summary

EEM305SimLab is a **single, self-contained HTML file** that runs entirely in the browser sandbox. It installs nothing and **cannot access the network**: a Content Security Policy in the `<head>` (`default-src 'none'; connect-src 'none'; …`) is enforced by the browser and blocks all network requests, external resources, form submissions and `eval`. This was verified with an automated test in which a deliberate request to `https://example.com` was blocked.

- **Data storage:** only the browser's own localStorage/IndexedDB (preferences, last Code Lab program, last step, and an optional file handle for "Save Settings to File"). Nothing leaves the computer.
- **File access:** only when the user clicks a button and picks the file (save settings, open/download `.asm`).
- **User code:** 8051 assembly written in Code Lab is interpreted by the built-in emulator and is never executed as JavaScript.
- **Third-party components:** CodeMirror 6 (MIT), Chart.js 4.6.1 (MIT), GSAP 3.15.1 (GSAP Standard License), Lucide 1.70.0 (ISC), Inter and JetBrains Mono (SIL OFL 1.1), pinned in `build/package-lock.json`.
- **Verification:** compare the SHA-256 in `SHA256SUMS.txt`, check the VirusTotal report linked in `README.md`, watch the Network tab in DevTools, or rebuild the file from source with `npm ci && npm run build` in `build/` (the build is reproducible).
- **Note:** "Save Settings to File" rewrites the `FILE_SETTINGS` line, so a file with saved settings will no longer match the published hash.
- **Reporting:** sercan.sebetci@ogr.sakarya.edu.tr or a GitHub issue.
