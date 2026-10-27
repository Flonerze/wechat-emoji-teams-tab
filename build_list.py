# -*- coding: utf-8 -*-
"""扫描 emoji/ 文件夹，生成 emoji.json（网页画廊用它来加载表情列表）。"""
import json
import os

IMG_EXT = {'.gif', '.png', '.jpg', '.jpeg', '.webp', '.bmp'}

here = os.path.dirname(os.path.abspath(__file__))
emoji_dir = os.path.join(here, 'emoji')
out_path = os.path.join(here, 'emoji.json')

files = []
if os.path.isdir(emoji_dir):
    for name in sorted(os.listdir(emoji_dir)):
        ext = os.path.splitext(name)[1].lower()
        if ext in IMG_EXT and not name.startswith('.'):
            files.append(name)

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({'emojis': files}, f, ensure_ascii=False, indent=2)

print(f'已扫描到 {len(files)} 个表情，写入 {out_path}')
for n in files:
    print(' -', n)
