"""
FX Teller Publication — Master Build Script
Runs the entire publication pipeline from one entry point.

Usage:
    python3 generators/build_all.py           # build everything
    python3 generators/build_all.py --quick    # website + PDF only
    python3 generators/build_all.py --clean   # clear build/ first
"""
import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path

REPO_ROOT = Path("/mnt/d/FX Teller")
PUB_ROOT = REPO_ROOT / "publication"
OUT_DIR = PUB_ROOT / "build"
GEN_DIR = PUB_ROOT / "generators"

sys.path.insert(0, str(GEN_DIR))
sys.path.insert(0, str(PUB_ROOT))


def step(name, fn):
    print(f"\n=== {name} ===")
    fn()


def build_assets():
    """Generate SVG diagrams."""
    from diagrams.library import render_diagram
    out = PUB_ROOT / "diagrams"
    out.mkdir(exist_ok=True)
    n = 0
    for name in [
        "revenue-pyramid", "flywheel", "lifecycle", "roadmap",
        "org-chart", "kpi-dashboard", "growth-curve", "risk-heatmap", "brand-pyramid",
    ]:
        svg = render_diagram(name)
        path = out / f"{name}.svg"
        path.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + svg)
        n += 1
    print(f"  {n} SVG diagrams generated")


def build_index():
    """Build the content index."""
    from content_loader import build_index as ci
    index = ci()
    print(f"  {index['total_docs']} docs · {index['total_words']:,} words · {len(index['sections'])} sections")


def build_website():
    """Build the static website."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_website", GEN_DIR / "build_website.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def build_pdf():
    """Build the Founder Playbook PDF."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_pdf", GEN_DIR / "build_pdf.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def build_pptx():
    """Build the strategy deck."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_pptx", GEN_DIR / "build_pptx.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def build_asset_bundle():
    """Create a ZIP bundle of all assets."""
    import zipfile
    zip_path = OUT_DIR / "assets.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Add all SVG diagrams
        for f in (PUB_ROOT / "diagrams").glob("*.svg"):
            zf.write(f, arcname=f"svg/{f.name}")
        # Add theme
        for f in (PUB_ROOT / "theme").glob("*"):
            if f.is_file():
                zf.write(f, arcname=f"theme/{f.name}")
        # Add index
        idx = OUT_DIR / "index.json"
        if idx.exists():
            zf.write(idx, arcname="index.json")
    size_kb = os.path.getsize(zip_path) // 1024
    print(f"  Bundle: {zip_path} ({size_kb} KB)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="Website + PDF only (no PPTX)")
    parser.add_argument("--clean", action="store_true", help="Clean build/ first")
    parser.add_argument("--skip-website", action="store_true")
    parser.add_argument("--skip-pdf", action="store_true")
    parser.add_argument("--skip-pptx", action="store_true")
    args = parser.parse_args()

    if args.clean and OUT_DIR.exists():
        print(f"Cleaning {OUT_DIR}...")
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"FX Teller Publication Builder")
    print(f"Source: docs/ ({REPO_ROOT / 'docs'})")
    print(f"Output: {OUT_DIR}/")

    step("1. Generating SVG diagrams", build_assets)
    step("2. Building content index", build_index)
    if not args.skip_website:
        step("3. Building static website", build_website)
    if not args.skip_pdf:
        step("4. Building Founder Playbook PDF", build_pdf)
    if not args.quick and not args.skip_pptx:
        step("5. Building strategy deck (PPTX)", build_pptx)
    step("6. Bundling assets", build_asset_bundle)

    print("\n=== Build complete ===")
    print(f"Outputs in: {OUT_DIR}/")
    if (OUT_DIR / "Founder_Playbook.pdf").exists():
        size = os.path.getsize(OUT_DIR / "Founder_Playbook.pdf") // 1024
        print(f"  Founder_Playbook.pdf: {size} KB")
    if (OUT_DIR / "Founder_Playbook.html").exists():
        size = os.path.getsize(OUT_DIR / "Founder_Playbook.html") // 1024
        print(f"  Founder_Playbook.html: {size} KB")
    if (OUT_DIR / "Deck.pptx").exists():
        size = os.path.getsize(OUT_DIR / "Deck.pptx") // 1024
        print(f"  Deck.pptx: {size} KB")
    if (OUT_DIR / "website").exists():
        size = sum(f.stat().st_size for f in (OUT_DIR / "website").rglob("*") if f.is_file()) // 1024
        print(f"  website/: {size} KB")
    if (OUT_DIR / "assets.zip").exists():
        size = os.path.getsize(OUT_DIR / "assets.zip") // 1024
        print(f"  assets.zip: {size} KB")


if __name__ == "__main__":
    main()
