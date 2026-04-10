import json
with open('d:/site/jinydev/Statistical/src/book/payload_c03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for item in data:
    with open(item['TargetFile'], 'r', encoding='utf-8') as f2:
        lines = f2.readlines()
    num = len(lines)
    print(f"{item['TargetFile']} : {num}")
