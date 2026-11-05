#!/usr/bin/env python3
"""seo_quickcheck: controleer de SEO-basis van een pagina.

Gebruik:
    python3 seo_quickcheck.py https://www.example.nl
    python3 seo_quickcheck.py https://www.example.nl/diensten --json

Controleert: status, https, title, meta description, H1, canonical, noindex,
robots.txt, sitemap.xml en JSON-LD. Alleen standaardbibliotheek.
Gemaakt door Joepify (https://www.joepify.nl), MIT-licentie.
"""
import argparse, json, re, sys, urllib.error, urllib.parse, urllib.request
from html.parser import HTMLParser

UA = {"User-Agent": "seo-quickcheck/1.0 (+https://github.com/Joepify/seo-checklist-mkb)"}


def get(url, timeout=15):
    req = urllib.request.Request(url, headers=UA)
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        return r.status, r.geturl(), r.read(2_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception:
        return 0, url, ""


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.h1, self.meta, self.canonical = "", [], {}, None
        self.jsonld, self._tag, self._buf, self._ld = [], None, "", False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("name"):
            self.meta[a["name"].lower()] = a.get("content", "")
        elif tag == "link" and "canonical" in (a.get("rel") or "").lower().split():
            self.canonical = a.get("href")
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._ld, self._buf = True, ""
        elif tag in ("title", "h1"):
            self._tag, self._buf = tag, ""

    def handle_data(self, data):
        if self._tag or self._ld:
            self._buf += data

    def handle_endtag(self, tag):
        if tag == "script" and self._ld:
            self.jsonld.append(self._buf)
            self._ld = False
        elif tag == self._tag:
            text = re.sub(r"\s+", " ", self._buf).strip()
            if tag == "title" and not self.title:
                self.title = text
            elif tag == "h1":
                self.h1.append(text)
            self._tag = None


def schema_types(blocks):
    types = []
    def walk(x):
        if isinstance(x, dict):
            t = x.get("@type")
            if t:
                types.extend(t if isinstance(t, list) else [t])
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for b in blocks:
        try:
            walk(json.loads(b))
        except ValueError:
            types.append("(ongeldige JSON-LD)")
    return sorted(set(types))


def run(url):
    if not re.match(r"https?://", url):
        url = "https://" + url
    status, final, html = get(url)
    res = []
    def add(level, msg):
        res.append({"niveau": level, "bericht": msg})
    add("OK" if status == 200 else "FAIL", f"Status {status}")
    add("OK" if final.startswith("https://") else "WARN", "https gebruikt" if final.startswith("https://") else "Geen https")
    if status != 200:
        return final, res
    p = Page()
    p.feed(html)
    n = len(p.title)
    if not p.title: add("FAIL", "Titel ontbreekt")
    elif 20 <= n <= 65: add("OK", f"Titel ({n} tekens): {p.title}")
    else: add("WARN", f"Titel ({n} tekens), richtlijn 50 tot 60: {p.title}")
    d = p.meta.get("description", "")
    if not d: add("FAIL", "Meta description ontbreekt")
    elif 70 <= len(d) <= 160: add("OK", f"Meta description ({len(d)} tekens)")
    else: add("WARN", f"Meta description ({len(d)} tekens), richtlijn 120 tot 155")
    if len(p.h1) == 1: add("OK", f"Eén H1: {p.h1[0]}")
    elif not p.h1: add("FAIL", "Geen H1")
    else: add("WARN", f"{len(p.h1)} H1-koppen")
    add("OK" if p.canonical else "WARN", f"Canonical: {p.canonical}" if p.canonical else "Canonical ontbreekt")
    robots = p.meta.get("robots", "").lower()
    add("FAIL" if "noindex" in robots else "OK", "noindex gevonden" if "noindex" in robots else "Geen noindex")
    base = "{0.scheme}://{0.netloc}".format(urllib.parse.urlsplit(final))
    s, _, txt = get(base + "/robots.txt")
    if s != 200: add("WARN", "robots.txt niet bereikbaar")
    elif re.search(r"(?im)^\s*disallow:\s*/\s*$", txt) and re.search(r"(?im)^\s*user-agent:\s*\*", txt):
        add("WARN", "robots.txt bevat 'Disallow: /' voor alle bots, controleer of dat bedoeld is")
    else: add("OK", "robots.txt bereikbaar (geen 'Disallow: /')")
    s, _, _ = get(base + "/sitemap.xml")
    add("OK" if s == 200 else "WARN", "sitemap.xml bereikbaar" if s == 200 else "sitemap.xml niet gevonden op /sitemap.xml")
    t = schema_types(p.jsonld)
    add("OK" if t else "WARN", "Structured data: " + ", ".join(t) if t else "Geen JSON-LD gevonden")
    return final, res


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("url")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    final, res = run(a.url)
    if a.json:
        print(json.dumps({"url": final, "checks": res}, indent=2, ensure_ascii=False))
    else:
        print(f"URL: {final}")
        for r in res:
            print(f"{r['niveau']:<5} {r['bericht']}")
    sys.exit(1 if any(r["niveau"] == "FAIL" for r in res) else 0)


if __name__ == "__main__":
    main()
