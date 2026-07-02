# FX Teller Publication System — Makefile
# Run the full publication pipeline from a single command.

.PHONY: all quick website pdf pptx clean assets help

PYTHON := python3

all: website pdf pptx assets
	@echo ""
	@echo "All publication outputs built."
	@echo "Outputs: build/"

quick: website pdf
	@echo ""
	@echo "Quick build complete (website + PDF)."

website:
	@echo "→ Building static website..."
	@cd ../.. && $(PYTHON) publication/generators/build_website.py

pdf:
	@echo "→ Building Founder Playbook PDF..."
	@cd ../.. && $(PYTHON) publication/generators/build_pdf.py

pptx:
	@echo "→ Building strategy deck..."
	@cd ../.. && $(PYTHON) publication/generators/build_pptx.py

assets:
	@echo "→ Bundling assets..."
	@cd ../.. && $(PYTHON) publication/generators/build_all.py --skip-website --skip-pdf --skip-pptx 2>&1 | tail -3

clean:
	@echo "→ Cleaning build output..."
	@cd ../.. && rm -rf publication/build

help:
	@echo "FX Teller Publication System"
	@echo ""
	@echo "Targets:"
	@echo "  make all      - build website + PDF + PPTX + assets bundle"
	@echo "  make quick    - build website + PDF only"
	@echo "  make website  - build static website only"
	@echo "  make pdf      - build Founder Playbook PDF only"
	@echo "  make pptx     - build strategy deck (PPTX) only"
	@echo "  make clean    - remove build/ directory"
	@echo "  make help     - show this help"
