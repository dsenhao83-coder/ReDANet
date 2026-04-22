import fitz  # PyMuPDF
import os

pdf_path = "E:\\BaiduNetdiskDownload\\qwen-8b\\123456\\showpage\\static\\images\\comparision.pdf"
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

doc = fitz.open(pdf_path)

for i, page in enumerate(doc):
    pix = page.get_pixmap()
    output_path = os.path.join(output_folder, f"page_{i+1}.png")
    pix.save(output_path)

print("转换完成！")
