import json

# Load contributors.json
with open("contributors.json", "r", encoding="utf-8") as f:
    contributors = json.load(f)

# Build contributors table
rows = []
row = []

for i, person in enumerate(contributors, start=1):
    if not person["name"].strip():
        continue

    block = f'''
<td align="center">
  <a href="{person["github"]}">
    <img src="{person["avatar"]}" width="100" style="border-radius:50%"/><br/>
    <sub><b>{person["name"]}</b></sub><br/>
    <p>{person["role"]}</p>
  </a>
</td>
'''
    row.append(block)

    # if row filled 6 columns, push it
    if i % 6 == 0:
        rows.append("<tr>" + "".join(row) + "</tr>")
        row = []

# leftover contributors if less than 6
if row:
    rows.append("<tr>" + "".join(row) + "</tr>")

# Build markdown section
table_html = "<table>\n" + "\n".join(rows) + "\n</table>"

# Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace between markers
start_marker = "<!-- CONTRIBUTORS START -->"
end_marker = "<!-- CONTRIBUTORS END -->"

before = readme.split(start_marker)[0]
after = readme.split(end_marker)[1] if end_marker in readme else ""

new_section = start_marker + "\n\n" + table_html + "\n\n" + end_marker

# Write updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(before + new_section + after)

print("✅ README.md updated with contributors table.")
