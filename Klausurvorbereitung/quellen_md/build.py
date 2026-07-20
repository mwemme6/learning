#!/usr/bin/env python3
"""Baut alle Vorlesungs-Zusammenfassungen (Markdown -> PDF) via pandoc + weasyprint.
Aufruf:  python3 build.py            (alle)
         python3 build.py 03 07      (nur bestimmte Nummern)
"""
import os, sys, subprocess, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.dirname(HERE)          # Klausurvorbereitung/
CSS  = os.path.join(HERE, "style.css")

def title_from(md_path):
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return re.sub(r"\s+", " ", line[2:].strip())
    return os.path.basename(md_path)

def build(md_path):
    base = os.path.splitext(os.path.basename(md_path))[0]
    pdf  = os.path.join(OUT, base + ".pdf")
    title = title_from(md_path)
    # pagetitle setzt nur das HTML <title> (befriedigt weasyprint), ohne im
    # Body eine zweite H1 zu erzeugen -> unsere '# ...'-Überschrift bleibt die einzige.
    cmd = ["pandoc", md_path, "-o", pdf,
           "--pdf-engine=weasyprint", "-c", CSS,
           "-V", f"pagetitle={title}"]
    env = dict(os.environ, PATH=os.environ.get("PATH","") + ":/sessions/clever-gallant-mayer/.local/bin")
    # In tmp-Verzeichnis ausführen, damit weasyprint keine Temp-Dateien im Ordner hinterlässt
    import tempfile
    r = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=tempfile.gettempdir())
    ok = os.path.exists(pdf)
    print(("OK  " if ok else "FAIL") + f" {base}.pdf")
    if not ok:
        print(r.stderr[-800:])
    return ok

def main():
    sel = sys.argv[1:]
    files = sorted(glob.glob(os.path.join(HERE, "[0-9][0-9]_*.md")))
    files += sorted(glob.glob(os.path.join(HERE, "Loesungen*.md")))
    if sel:
        files = [f for f in files if any(os.path.basename(f).startswith(s) for s in sel)]
    for f in files:
        build(f)

if __name__ == "__main__":
    main()
