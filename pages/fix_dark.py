#!/usr/bin/env python3
import os
import re

# CSS для темной темы
DARK_STYLE = """
<style>
body {
    background-color: #0d1117 !important;
    color: #c9d1d9 !important;
}
html {
    background-color: #0d1117 !important;
}
h1, h2, h3, h4, h5, h6 {
    color: #58a6ff !important;
}
a {
    color: #58a6ff !important;
}
p, div, span, li, td, th {
    color: #c9d1d9 !important;
}
code {
    background-color: #161b22 !important;
    color: #79c0ff !important;
    padding: 2px 6px !important;
    border-radius: 3px !important;
}
pre {
    background-color: #161b22 !important;
    color: #79c0ff !important;
    padding: 16px !important;
    border-radius: 6px !important;
    border: 1px solid #30363d !important;
}
table {
    border-color: #30363d !important;
}
th {
    background-color: #161b22 !important;
}
</style>
"""

# Обработать все HTML файлы
for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
    
    print(f"Обработка {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Удалить все старые <style> блоки с белым фоном
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    
    # Заменить inline стили с белым фоном
    content = content.replace('background-color:white', 'background-color:#0d1117')
    content = content.replace('background-color:#fff', 'background-color:#0d1117')
    content = content.replace('background-color: white', 'background-color: #0d1117')
    content = content.replace('background: white', 'background: #0d1117')
    content = content.replace('background:#fff', 'background:#0d1117')
    content = content.replace('color:black', 'color:#c9d1d9')
    content = content.replace('color:#000', 'color:#c9d1d9')
    
    # Вставить темную тему после <head> или перед </head>
    if '<head>' in content:
        content = content.replace('<head>', f'<head>\n{DARK_STYLE}')
    elif '</head>' in content:
        content = content.replace('</head>', f'{DARK_STYLE}\n</head>')
    else:
        # Если нет head, вставить в начало body
        content = content.replace('<body>', f'<body>\n{DARK_STYLE}')
    
    # Сохранить
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ {filename} обработан")

print("\n✅ Все файлы стали темными!")
