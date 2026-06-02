from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[1]
exclude_parts = {'.git', '__pycache__', '.ipynb_checkpoints', 'node_modules'}
rows = []
for path in sorted(root.rglob('*')):
    if not path.is_file():
        continue
    if any(part in exclude_parts for part in path.parts):
        continue
    rel = path.relative_to(root)
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    rows.append((str(rel), path.stat().st_size, h))

out = root / 'FILE_MANIFEST_SHA256.tsv'
with out.open('w', encoding='utf-8') as f:
    f.write('path\tsize_bytes\tsha256\n')
    for rel, size, sha in rows:
        f.write(f'{rel}\t{size}\t{sha}\n')
print(f'Wrote {out}')
