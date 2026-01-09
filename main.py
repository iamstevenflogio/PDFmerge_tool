import os
from pathlib import Path
from pypdf import PdfWriter  # make sure: python -m pip install pypdf

# Folder where your PDFs live
SOURCE_FOLDER = r"C:/Users/Steven/OneDrive/Desktop/Mix"
OUTPUT_NAME = "merged.pdf"
MAX_FILES = 20  # change if you ever want more/less


def merge_all_pdfs(folder: Path):
    # Get all PDFs in folder
    pdf_paths = [
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() == ".pdf"
    ]

    if not pdf_paths:
        print("No PDF files found in the folder.")
        return

    # Sort by filename
    pdf_paths.sort(key=lambda p: p.name)

    # Limit to MAX_FILES
    pdf_paths = pdf_paths[:MAX_FILES]

    writer = PdfWriter()

    try:
        for pdf_path in pdf_paths:
            print(f"Adding: {pdf_path.name}")
            with open(pdf_path, "rb") as f:
                writer.append(f)
    except Exception as e:
        print(f"Error while reading/merging '{pdf_path}': {e}")
        print("Stopping because a corrupt or unreadable file was encountered.")
        return

    output_path = folder / OUTPUT_NAME
    with open(output_path, "wb") as out_f:
        writer.write(out_f)

    writer.close()
    print(f"Successfully created: {output_path}")


if __name__ == "__main__":
    folder = Path(SOURCE_FOLDER)
    if not folder.is_dir():
        print(f"Folder not found: {folder}")
    else:
        merge_all_pdfs(folder)
