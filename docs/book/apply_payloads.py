import json

with open(r'd:\site\jinydev\Statistical\src\book\payloads.json', 'r', encoding='utf-8') as f:
    payloads = json.load(f)

count = 0
for chapter, instructions in payloads.items():
    for item in instructions:
        target = item['TargetFile']
        rep_content = item['ReplacementContent']
        
        with open(target, 'r', encoding='utf-8') as tf:
            lines = tf.readlines()
            
        # Ensure we only append if not already appended
        if "## Sub-Chapters" not in "".join(lines):
            # Replace the last line using target logic
            last_line = item['TargetContent']
            if lines[-1].strip() == last_line.strip():
                lines[-1] = rep_content
            else:
                # If exact last line didn't match, just append safely
                lines.append("\n" + rep_content[len(last_line):])
                
            with open(target, 'w', encoding='utf-8') as tf:
                tf.writelines(lines)
            count += 1
            
print(f"DONE! Evaluated exactly {count} sub-chapter TOC insertions from chapter 3 to 13.")
