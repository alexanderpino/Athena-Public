from pypdf import PdfReader
import sys

reader = PdfReader('C:/repos/Athena-Public/books/Introduction To 3D Game Programming with DirectX 12.pdf')
ranges = [
    (158, 202, 'chapter_5_pipeline'),
    (396, 444, 'chapters_10_11_blending_stenciling'),
    (444, 538, 'chapters_12_13_14_shaders')
]

for start, end, name in ranges:
    with open(f'.context/data/deep-learning-lab/directx12/{name}.txt', 'w', encoding='utf-8') as f:
        for i in range(start, end):
            if i >= len(reader.pages): break
            f.write(f'--- Page {i+1} ---\n')
            text = reader.pages[i].extract_text()
            if text:
                f.write(text)
            f.write('\n')
