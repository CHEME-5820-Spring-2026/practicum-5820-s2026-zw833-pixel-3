import json
import re
from pathlib import Path

path = Path(r'c:\Users\zipengwang\Documents\GitHub\practicum-5820-s2026-zw833-pixel-3\CHEME-5820-Practicum-Student-S2026.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
found = False
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] in ('markdown', 'code'):
        text = ''.join(cell['source'])
        if re.search(r'DQ\s*1|DQ1|DQ\s*2|DQ2|DQ\s*3|DQ3|Discussion|discussion|Question', text):
            found = True
            print('CELL', i, cell['cell_type'])
            print(text)
            print('---')
if not found:
    print('NOT FOUND')
