from pathlib import Path
import html
import re
import yaml
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "KITAP_METNI.md"
OUT = ROOT / "1_Eksi_3_Arti.pdf"

raw = SRC.read_text(encoding="utf-8")
meta = {}
body = raw
if raw.startswith("---\n"):
    _, front, body = raw.split("---\n", 2)
    meta = yaml.safe_load(front) or {}

# Internal HTML comments never enter the PDF.
body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()

def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text

parts = []
para = []

def flush_para():
    if para:
        text = " ".join(s.strip() for s in para).strip()
        if text:
            parts.append(f"<p>{inline(text)}</p>")
        para.clear()

for line in body.splitlines():
    s = line.rstrip()
    if not s.strip():
        flush_para()
        continue
    if s.strip() in {"***", "* * *", "---"}:
        flush_para()
        parts.append('<div class="scene-break">* * *</div>')
        continue
    if s.startswith("# "):
        flush_para()
        parts.append(f'<h1 class="chapter">{inline(s[2:].strip())}</h1>')
        continue
    if s.startswith("## "):
        flush_para()
        parts.append(f'<h2>{inline(s[3:].strip())}</h2>')
        continue
    if s.startswith("> "):
        flush_para()
        parts.append(f'<blockquote>{inline(s[2:].strip())}</blockquote>')
        continue
    para.append(s)
flush_para()

title = html.escape(str(meta.get("title", "1 Eksi 3 Artı")))
content = "\n".join(parts)

css = r'''
@font-face {
  font-family: "BookSerif";
  src: local("Noto Serif");
  font-weight: 400;
}
@font-face {
  font-family: "BookSerif";
  src: local("Noto Serif SemiBold"), local("Noto Serif");
  font-weight: 600;
}
@font-face {
  font-family: "BookSans";
  src: local("Noto Sans");
  font-weight: 400;
}
@font-face {
  font-family: "BookSans";
  src: local("Noto Sans SemiBold"), local("Noto Sans");
  font-weight: 600;
}

@page {
  size: A5;
  margin-top: 17mm;
  margin-bottom: 20mm;
}
@page :right {
  margin-left: 20mm;
  margin-right: 16mm;
  @bottom-right {
    content: counter(page);
    font-family: "BookSans";
    font-size: 8.5pt;
  }
}
@page :left {
  margin-left: 16mm;
  margin-right: 20mm;
  @bottom-left {
    content: counter(page);
    font-family: "BookSans";
    font-size: 8.5pt;
  }
}
@page titlepage {
  margin: 0;
  @bottom-left { content: none; }
  @bottom-right { content: none; }
}

html { lang: tr; }
body {
  margin: 0;
  font-family: "BookSerif", serif;
  font-size: 10.7pt;
  line-height: 1.48;
  color: #111;
  text-rendering: optimizeLegibility;
}
.title-page {
  page: titlepage;
  height: 210mm;
  width: 148mm;
  display: flex;
  align-items: center;
  justify-content: center;
  break-after: page;
}
.title-page h1 {
  font-family: "BookSans", sans-serif;
  font-size: 28pt;
  font-weight: 600;
  letter-spacing: 0.2pt;
  text-align: center;
  margin: 0 15mm;
}
.book-body:empty { display: none; }
p {
  margin: 0;
  text-indent: 5mm;
  text-align: justify;
  hyphens: auto;
  orphans: 3;
  widows: 3;
}
h1.chapter + p, h2 + p, .scene-break + p, blockquote + p {
  text-indent: 0;
}
h1.chapter {
  font-family: "BookSans", sans-serif;
  font-size: 19pt;
  line-height: 1.2;
  font-weight: 600;
  margin: 0 0 10mm 0;
  break-before: right;
  break-after: avoid;
}
h2 {
  font-family: "BookSans", sans-serif;
  font-size: 13.5pt;
  line-height: 1.25;
  font-weight: 600;
  margin: 7mm 0 3.5mm 0;
  break-after: avoid;
}
.scene-break {
  text-align: center;
  font-family: "BookSans", sans-serif;
  letter-spacing: 2pt;
  margin: 6mm 0;
}
blockquote {
  margin: 5mm 7mm;
  font-style: italic;
  orphans: 3;
  widows: 3;
}
'''

doc = f'''<!doctype html>
<html lang="tr">
<head><meta charset="utf-8"><style>{css}</style></head>
<body>
<section class="title-page"><h1>{title}</h1></section>
<main class="book-body">{content}</main>
</body>
</html>'''

HTML(string=doc, base_url=str(ROOT)).write_pdf(str(OUT))
print(OUT)
