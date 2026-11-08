# EEM305SimLab derleme betiği
# Kaynak HTML'e (src/EEM305SimLab.src.html) kütüphaneleri, yazı tiplerini ve ikonları gömer;
# sonucu depo kökünde tek bir dosya olarak üretir: EEM305SimLab.html
# Kullanım: build klasöründe "npm ci" ve ardından "npm run build"
import base64, json, re, os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NM = os.path.join(HERE, "node_modules") + os.sep
SRC = os.path.join(ROOT, "src", "EEM305SimLab.src.html")
OUT = os.path.join(ROOT, "EEM305SimLab.html")

src = open(SRC, encoding="utf-8").read()

def b64(path):
    return base64.b64encode(open(path, "rb").read()).decode()

# Yazı tipleri: Latin + Latin Extended (Türkçe karakterler dahil)
LAT = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
EXT = "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
fonts = ""
for fam, pkg, pre in [("Inter Var", "@fontsource-variable/inter", "inter"),
                      ("JetBrains Mono Var", "@fontsource-variable/jetbrains-mono", "jetbrains-mono")]:
    for sub, rng in [("latin", LAT), ("latin-ext", EXT)]:
        f = NM + pkg + "/files/" + pre + "-" + sub + "-wght-normal.woff2"
        fonts += '@font-face{font-family:"%s";font-style:normal;font-display:swap;font-weight:100 900;src:url(data:font/woff2;base64,%s) format("woff2");unicode-range:%s}\n' % (fam, b64(f), rng)

# İkonlar: yalnızca kaynakta kullanılan Lucide ikonları gömülür
names = sorted(set(re.findall(r'ic\("([a-z0-9-]+)"', src)) | set(re.findall(r'icon: "([a-z0-9-]+)"', src)))
icons = {}
for n in names:
    svg = open(NM + "lucide-static/icons/" + n + ".svg", encoding="utf-8").read()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    icons[n] = re.sub(r"\s+", " ", inner).strip()
src = src.replace("/*@@ICONS@@*/{}", json.dumps(icons))

def safe(js):
    return js.replace("</script", "<\\/script")

libs = ""
for title, path in [("CodeMirror 6 (MIT) — bundled with esbuild", os.path.join(HERE, "cm.min.js")),
                    ("Chart.js 4.6.1 (MIT)", NM + "chart.js/dist/chart.umd.min.js"),
                    ("GSAP 3.15.1 (GSAP Standard License)", NM + "gsap/dist/gsap.min.js"),
                    ("GSAP MotionPathPlugin 3.15.1", NM + "gsap/dist/MotionPathPlugin.min.js")]:
    libs += "<script>/* " + title + " */\n" + safe(open(path, encoding="utf-8").read()) + "\n</script>\n"

src = src.replace("<style>", "<style>\n" + fonts, 1)
i = src.index("<script>\n// Dosyanın değiştirilmemiş hâli")
src = src[:i] + libs + src[i:]
open(OUT, "w", encoding="utf-8", newline="\n").write(src)

digest = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
print("Built:", OUT, "(%d KB)" % (os.path.getsize(OUT) // 1024))
print("SHA-256:", digest)
