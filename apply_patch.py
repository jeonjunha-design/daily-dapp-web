import json, re

with open('title_ko_patch.json', 'r') as f:
    patch = json.load(f)

with open('DailyArt.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = 0
for fname, title_ko in patch.items():
    # image_file:"met_xxx.jpg" 가 있는 항목에 title_ko 추가
    # 이미 title_ko 있는 건 스킵
    old = f'image_file:"{fname}"'
    if old not in html:
        continue
    # 해당 항목에 title_ko가 없는 경우만 추가
    idx = html.find(old)
    # 해당 줄 찾기
    line_start = html.rfind('{', 0, idx)
    line_end = html.find('}', idx) + 1
    entry = html[line_start:line_end]
    if 'title_ko' in entry:
        continue
    # title: 뒤에 title_ko 삽입
    new_entry = entry.replace(
        f'image_file:"{fname}"',
        f'title_ko:"{title_ko}", image_file:"{fname}"'
    )
    html = html[:line_start] + new_entry + html[line_end:]
    count += 1
    print(f'OK {fname} -> {title_ko}')

with open('DailyArt.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\n완료! {count}개 title_ko 추가됨')
