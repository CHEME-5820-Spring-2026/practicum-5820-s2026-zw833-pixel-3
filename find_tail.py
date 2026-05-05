import json
from pathlib import Path

path = Path(r'c:\Users\zipengwang\Documents\GitHub\practicum-5820-s2026-zw833-pixel-3\CHEME-5820-Practicum-Student-S2026.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
for i, cell in enumerate(nb['cells'][-40:], start=len(nb['cells'])-40):
    if cell['cell_type'] in ('markdown', 'code'):
        text = ''.join(cell['source'])
        print('CELL', i, cell['cell_type'])
        print(repr(text[:400]))
        print('---')
