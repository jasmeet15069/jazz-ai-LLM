from pathlib import Path

import fitz


PDF_PATH = Path(r"C:\Users\ACXIOM\Downloads\Advait AI Knowledge.pdf")
OUT_DIR = Path(__file__).resolve().parents[1] / "knowledge" / "rendered_pages"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(PDF_PATH))
    for index, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False)
        pix.save(str(OUT_DIR / f"advait_page_{index}.png"))
    print(f"Rendered {len(doc)} page(s) to {OUT_DIR}")


if __name__ == "__main__":
    main()
