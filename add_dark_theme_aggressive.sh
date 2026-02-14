#!/bin/bash

# Очень агрессивная темная тема (перебивает все стили)
SUPER_DARK_CSS='<style>
html {
    filter: invert(0.9) hue-rotate(180deg) !important;
    background: #0d1117 !important;
}
img, video, iframe {
    filter: invert(1) hue-rotate(180deg) !important;
}
</style>

<style>
body, html {
    background: #0d1117 !important;
    color: #c9d1d9 !important;
}
* {
    color: #c9d1d9 !important;
}
*:not(pre):not(code) {
    background: #0d1117 !important;
}
h1, h2, h3, h4, h5, h6 {
    color: #58a6ff !important;
}
a {
    color: #58a6ff !important;
}
code, pre {
    background: #161b22 !important;
    color: #79c0ff !important;
    border: 1px solid #30363d !important;
}
.notion-page,
.notion-page-content,
.notion-scroller,
[class*="notion"],
[class*="page"],
div, span, p, section, article {
    background: #0d1117 !important;
}
</style>'

for file in *.html; do
    echo "Применение супер-темной темы к $file..."
    
    if grep -q "filter: invert" "$file"; then
        echo "  Уже обработан"
        continue
    fi
    
    # Вставить в начало <head> или после <head>
    if grep -q "<head>" "$file"; then
        sed -i "/<head>/a $SUPER_DARK_CSS" "$file"
    else
        echo "$SUPER_DARK_CSS" | cat - "$file" > temp && mv temp "$file"
    fi
    
    echo "  ✓ Готово"
done

echo "✅ Все файлы темные!"
