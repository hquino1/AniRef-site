"""Builds the AniRef website.

    python scripts/build.py

Pages are written to the repo root, where GitHub Pages serves them.

  src/pages/*.html   page bodies. Each starts with a comment block giving its
                     title, description and which nav item to highlight.
  src/legal/*.txt    the Privacy Policy and Terms of Use as plain text — the same
                     files the app's legal text comes from. Replace a file and
                     rebuild to publish a new version; nothing else needs editing.

The shared header and footer live in this file, so a nav change is one edit here.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

SITE_URL = "https://hquino1.github.io/AniRef-site"
CONTACT_EMAIL = "app.aniref@gmail.com"
# Paste the App Store link here once the listing is live. While it is empty,
# every download button reads "Coming soon" and links nowhere.
APP_STORE_URL = ""

NAV = [
    ("about", "About", "about.html"),
    ("faq", "FAQ", "faq.html"),
    ("support", "Support", "support.html"),
    ("privacy", "Privacy", "privacy.html"),
    ("terms", "Terms", "terms.html"),
]

APPLE_ICON = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.62c-.02-2.3 '
    "1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8-1.41-.14-2.76.83-3.47.83-.72 0-1.82-.81-3-.79-1.54.02-2.96.9-3.76 "
    "2.27-1.6 2.78-.41 6.9 1.15 9.15.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 "
    "1.23-.02 2.01-1.12 2.76-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.39-.92-2.41-3.65zM14.1 5.86c.63-.77 "
    '1.06-1.83.94-2.89-.91.04-2.01.61-2.66 1.37-.58.67-1.09 1.75-.96 2.79 1.02.08 2.05-.52 2.68-1.27z"/></svg>'
)


def app_store_button(css_class="btn-white"):
    if APP_STORE_URL:
        return (
            f'<a class="btn {css_class}" href="{APP_STORE_URL}">{APPLE_ICON}'
            "Download on the App Store</a>"
        )
    return f'<span class="btn {css_class}" aria-disabled="true">{APPLE_ICON}Coming soon to the App Store</span>'


def render_page(*, slug, title, description, nav, body):
    full_title = "AniRef — Drawing practice with references" if slug == "index" else f"{title} · AniRef"
    url = f"{SITE_URL}/" if slug == "index" else f"{SITE_URL}/{slug}.html"
    current = ' aria-current="page"'
    links = "\n".join(
        f'                <li><a href="{href}"{current if key == nav else ""}>{label}</a></li>'
        for key, label, href in NAV
    )
    body = body.replace("{{APP_STORE_BUTTON}}", app_store_button()).replace(
        "{{APP_STORE_BUTTON_PRIMARY}}", app_store_button("btn-primary")
    ).replace("{{EMAIL}}", CONTACT_EMAIL)

    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>{html.escape(full_title)}</title>
    <meta name="description" content="{html.escape(description)}">
    <meta name="theme-color" content="#C0392B">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AniRef">
    <meta property="og:title" content="{html.escape(full_title)}">
    <meta property="og:description" content="{html.escape(description)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITE_URL}/assets/img/app-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
    <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
    <link rel="preload" href="assets/fonts/Poppins_600SemiBold.ttf" as="font" type="font/ttf" crossorigin>
    <link rel="stylesheet" href="assets/css/style.css">
    <script>try{{var t=localStorage.getItem("aniref-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
</head>
<body>
    <a class="skip-link" href="#main">Skip to content</a>

    <header class="site-header">
        <nav class="container nav" aria-label="Main">
            <a class="brand" href="index.html" aria-label="AniRef home">
                <img class="logo-red" src="assets/img/logo-red.png" alt="AniRef" width="480" height="158">
                <img class="logo-white" src="assets/img/logo-white.png" alt="AniRef" width="480" height="158">
            </a>
            <ul class="nav-links" id="nav-links">
{links}
            </ul>
            <div class="nav-actions">
                <button class="icon-btn" type="button" data-theme-toggle aria-label="Toggle dark mode">
                    <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
                    <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
                </button>
                <button class="icon-btn menu-toggle" type="button" data-menu-toggle aria-controls="nav-links" aria-expanded="false" aria-label="Open menu">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
                </button>
            </div>
        </nav>
    </header>

    <main id="main">
{body.rstrip()}
    </main>

    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <img class="logo-red" src="assets/img/logo-red.png" alt="AniRef" width="480" height="158">
                    <img class="logo-white" src="assets/img/logo-white.png" alt="AniRef" width="480" height="158">
                    <p>Find the reference, draw it stage by stage, and watch your practice add up.</p>
                </div>
                <div>
                    <h2>AniRef</h2>
                    <ul>
                        <li><a href="index.html#features">Features</a></li>
                        <li><a href="index.html#pricing">Pricing</a></li>
                        <li><a href="about.html">About</a></li>
                    </ul>
                </div>
                <div>
                    <h2>Help</h2>
                    <ul>
                        <li><a href="faq.html">FAQ</a></li>
                        <li><a href="support.html">Support</a></li>
                        <li><a href="mailto:{CONTACT_EMAIL}">Contact us</a></li>
                    </ul>
                </div>
                <div>
                    <h2>Legal</h2>
                    <ul>
                        <li><a href="privacy.html">Privacy Policy</a></li>
                        <li><a href="terms.html">Terms of Use</a></li>
                        <li><a href="support.html#delete-account">Delete your account</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; <span data-year>2026</span> AniRef. All rights reserved.</span>
                <span>Not affiliated with Pinterest, DeviantArt, Pexels, Unsplash, Apple, or Google.</span>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# Plain-text legal documents -> HTML
# --------------------------------------------------------------------------

# Phrases that open a paragraph or bullet as a label in the source text. Listed
# explicitly because no rule tells "Removal." apart from an ordinary short sentence.
LEAD_INS = [
    # Terms
    "Your drawings are yours.", "Your uploads stay private.", "Only upload what you have the right to use.",
    "Reference images belong to their creators.", "Subscriptions renew automatically.",
    "Copyright owners can reach us.", "What counts as your content.", "You own your content.",
    "Your promises about your content.", "The permission you give us.", "Keep your own copies.", "Removal.",
    "Free and paid plans.", "Billing through app stores.", "Automatic renewal.", "Free trials.",
    "How to cancel.", "Refunds.", "Price changes.", "Taxes.", "What happens next.",
    "If your content was removed.", "Repeat infringers.", "Talk to us first.", "Governing law.",
    "Where claims are brought.", "Consumers outside the United States.", "Entire agreement.",
    "Severability.", "No waiver.", "Assignment.", "Events outside our control.", "Electronic notices.",
    "Export and sanctions.",
    # Privacy
    "Questions or concerns?", "Questions?", "What personal information do we process?",
    "Do we process any sensitive personal information?", "Do we collect any information from third parties?",
    "How do we process your information?",
    "In what situations and with which types of parties do we share personal information?",
    "Is your information transferred internationally?", "How do we keep your information safe?",
    "What are your rights?", "How do you exercise your rights?", "Personal Information Provided by You.",
    "Content You Provide.", "Sensitive Information.", "Payment Data.", "Social Media Login Data.",
    "Application Data.", "Mobile Device Access.", "Reminder Notifications.", "Log and Usage Data.",
    "Analytics Data.", "Session Replay.", "Apple and Google sign-in.", "Pinterest and DeviantArt.",
    "To facilitate account creation and authentication and otherwise manage user accounts.",
    "To deliver and facilitate delivery of services to the user.",
    "To respond to user inquiries/offer support to users.", "To send administrative information to you.",
    "To fulfill and manage your orders.", "To understand and improve our Services.",
    "To save or protect an individual's vital interest.", "Consent.", "Performance of a Contract.",
    "Legal Obligations.", "Vital Interests.", "Vendors, Consultants, and Other Third-Party Service Providers.",
    "Services you choose to connect.", "Image search providers.", "Business Transfers.",
    "European Commission's Standard Contractual Clauses:", "Withdrawing your consent:",
]
LEAD_INS.sort(key=len, reverse=True)

HEADING_RE = re.compile(r"^(?:(\d+)\. )?([A-Z][A-Z0-9 ,'?()/\-]+)$")
BULLET_RE = re.compile(r"^\s+- (.*)$")
NUMBERED_RE = re.compile(r"^\s+\d+\. (.*)$")
CATEGORY_RE = re.compile(r"^([A-L])\. (.+)$")
URL_RE = re.compile(r"(https?://[^\s<]*[^\s<.,;:)])")
EMAIL_RE = re.compile(r"\b([\w.+-]+@[\w-]+\.[\w.]+[a-z])\b")


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def sentence_case(text):
    out = text.capitalize()
    for proper in ("AniRef", "United States", "Do-Not-Track"):
        out = re.sub(re.escape(proper), proper, out, flags=re.I)
    return out


def is_subheading(line, has_more):
    s = line.strip()
    return (
        has_more
        and len(s) < 60
        and s == line
        and not s.endswith((".", ":", ","))
        and not HEADING_RE.match(s)
        and not CATEGORY_RE.match(s)
        and s != "AniRef"
    )


class LegalDoc:
    def __init__(self, text):
        lines = text.replace("\r\n", "\n").split("\n")
        self.updated = lines[1].strip()
        self.blocks = [b for b in re.split(r"\n\s*\n", "\n".join(lines[2:]).strip()) if b.strip()]
        self.anchors = {}  # heading text (as quoted in the document) -> id
        self.toc = []

    def inline(self, text):
        out = html.escape(text, quote=False)
        for lead in LEAD_INS:
            esc = html.escape(lead, quote=False)
            if out.startswith(esc + " ") or out == esc:
                out = f"<strong>{esc}</strong>{out[len(esc):]}"
                break
        if out.startswith("In Short:"):
            out = "<strong>In Short:</strong>" + out[len("In Short:"):]
        out = URL_RE.sub(lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>', out)
        out = EMAIL_RE.sub(lambda m: f'<a href="mailto:{m.group(1)}">{m.group(1)}</a>', out)
        out = out.replace("ico.org.uk/make-a-complaint", '<a href="https://ico.org.uk/make-a-complaint">ico.org.uk/make-a-complaint</a>')

        def link_ref(m):
            key = m.group(1).rstrip(".")
            anchor = self.anchors.get(key)
            return f'<a href="#{anchor}">"{m.group(1)}"</a>' if anchor else m.group(0)

        return re.sub(r'"([^"<>]{4,90})"', link_ref, out)

    def collect_anchors(self):
        for i, block in enumerate(self.blocks):
            first = block.split("\n")[0]
            m = HEADING_RE.match(first) if "\n" not in block else None
            if m and first != "TABLE OF CONTENTS":
                num, name = m.groups()
                anchor = f"section-{num}" if num else slugify(name)
                self.anchors[name] = anchor
                if num:
                    self.toc.append((anchor, f"{num}. {sentence_case(name)}"))
            elif is_subheading(first, "\n" in block or i + 1 < len(self.blocks)):
                self.anchors[first] = slugify(first)

    def render(self):
        self.collect_anchors()
        parts = []
        i = 0
        while i < len(self.blocks):
            block = self.blocks[i]
            lines = block.split("\n")
            first = lines[0]

            if first == "TABLE OF CONTENTS":
                i += 2  # the heading and its numbered list; the sidebar replaces them
                continue

            if len(lines) == 1 and HEADING_RE.match(first):
                num, name = HEADING_RE.match(first).groups()
                parts.append(f'<h2 id="{self.anchors[name]}">{html.escape(first)}</h2>')
                i += 1
                continue

            if CATEGORY_RE.match(first):
                rows = []
                while i < len(self.blocks) and CATEGORY_RE.match(self.blocks[i].split("\n")[0]):
                    cat = self.blocks[i].split("\n")
                    letter, name = CATEGORY_RE.match(cat[0]).groups()
                    fields = dict(
                        (k.strip(), v.strip()) for k, v in (l.split(":", 1) for l in cat[1:] if ":" in l)
                    )
                    rows.append(
                        f"<tr><td>{letter}. {html.escape(name)}</td>"
                        f"<td>{html.escape(fields.get('Examples', ''))}</td>"
                        f"<td>{html.escape(fields.get('Collected', ''))}</td></tr>"
                    )
                    i += 1
                parts.append(
                    '<div class="category-table-wrap"><table class="category-table">'
                    "<thead><tr><th>Category</th><th>Examples</th><th>Collected</th></tr></thead>"
                    f"<tbody>{''.join(rows)}</tbody></table></div>"
                )
                continue

            if is_subheading(first, len(lines) > 1 or i + 1 < len(self.blocks)):
                parts.append(f'<h3 id="{self.anchors[first]}">{html.escape(first)}</h3>')
                lines = lines[1:]

            parts.extend(self.render_lines(lines))
            i += 1

        return "\n".join(parts)

    def render_lines(self, lines):
        out, para, items, kind = [], [], [], None

        def flush_para():
            if para:
                text = "<br>\n".join(self.inline(l.strip()) for l in para)
                letters = [c for c in text if c.isalpha()]
                classes = []
                if para[0].startswith("In Short:"):
                    classes.append("in-short")
                if len(letters) > 60 and sum(c.isupper() for c in letters) / len(letters) > 0.8:
                    classes.append("caps")
                cls = f' class="{" ".join(classes)}"' if classes else ""
                out.append(f"<p{cls}>{text}</p>")
                para.clear()

        def flush_items():
            nonlocal kind
            if items:
                out.append(f"<{kind}>" + "".join(f"<li>{self.inline(t)}</li>" for t in items) + f"</{kind}>")
                items.clear()
            kind = None

        for line in lines:
            bullet, numbered = BULLET_RE.match(line), NUMBERED_RE.match(line)
            if bullet or numbered:
                flush_para()
                new_kind = "ul" if bullet else "ol"
                if kind and kind != new_kind:
                    flush_items()
                kind = new_kind
                items.append((bullet or numbered).group(1))
            else:
                flush_items()
                para.append(line)
        flush_para()
        flush_items()
        return out


def legal_body(doc, title, intro):
    content = doc.render()
    toc = "\n".join(f'                    <li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in doc.toc)
    return f"""        <section class="container page-hero">
            <span class="eyebrow">Legal</span>
            <h1>{html.escape(title)}</h1>
            <p>{intro}</p>
            <p class="legal-meta">{html.escape(doc.updated)}</p>
        </section>
        <div class="container legal">
            <aside class="card legal-toc" aria-label="Contents">
                <h2>Contents</h2>
                <ol>
{toc}
                </ol>
            </aside>
            <article class="card legal-body">
{content}
            </article>
        </div>
"""


# --------------------------------------------------------------------------

META_RE = re.compile(r"^<!--(.*?)-->\s*", re.S)


def parse_page(path):
    raw = path.read_text(encoding="utf-8")
    m = META_RE.match(raw)
    meta = dict(
        (k.strip(), v.strip()) for k, v in (l.split(":", 1) for l in m.group(1).strip().splitlines() if ":" in l)
    )
    return meta, raw[m.end():]


def write(name, content):
    (ROOT / name).write_text(content, encoding="utf-8", newline="\n")
    print(f"  wrote {name}")


def main():
    for path in sorted((SRC / "pages").glob("*.html")):
        meta, body = parse_page(path)
        slug = path.stem
        write(
            f"{slug}.html",
            render_page(slug=slug, title=meta["title"], description=meta["description"], nav=meta.get("nav"), body=body),
        )

    legal = [
        ("privacy", "Privacy Policy", "How AniRef collects, uses and protects your information.",
         "privacy.txt", "How AniRef collects, uses, shares and protects your personal information, and the choices you have."),
        ("terms", "Terms of Use", "The terms that apply when you use the AniRef app.",
         "terms.txt", "The agreement between you and AniRef when you use the app. The summary covers the key points; the full terms below control."),
    ]
    for slug, title, description, source, intro in legal:
        doc = LegalDoc((SRC / "legal" / source).read_text(encoding="utf-8"))
        write(f"{slug}.html", render_page(slug=slug, title=title, description=description, nav=slug, body=legal_body(doc, title, intro)))


if __name__ == "__main__":
    main()
