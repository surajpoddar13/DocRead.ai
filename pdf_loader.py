import fitz
import os
import pytesseract
from PIL import Image
from langchain_core.documents import Document


class PdfLoader:

    def read_file(self, file_path):

        docs = []

        if not os.path.exists(file_path):
            raise ValueError("File not found.")

        pdf = fitz.open(file_path)

        for page_num in range(len(pdf)):

            page = pdf.load_page(page_num)

            text = page.get_text()

            # If text exists → use it
            if text.strip():
                docs.append(
                    Document(
                        page_content=text,
                        metadata={"page": page_num + 1}
                    )
                )

            else:
                # OCR fallback
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                ocr_text = pytesseract.image_to_string(img)

                if ocr_text.strip():
                    docs.append(
                        Document(
                            page_content=ocr_text,
                            metadata={"page": page_num + 1}
                        )
                    )

        pdf.close()

        if not docs:
            raise ValueError("No readable text found even after OCR.")

        return docs