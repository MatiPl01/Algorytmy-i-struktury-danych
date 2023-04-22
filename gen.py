import os
import re

def gen_section(title, parent_dir):
  res = []
  
  for file_name in sorted(os.listdir(parent_dir)):
    file_path = os.path.join(parent_dir, file_name)
    if os.path.isfile(file_path):
      item_name = re.sub(r"[()]", "", file_name.replace("Zadanie ", "").replace(".ipynb", "").replace(".py", ""))
      
      if len(item_name.split(". ")) == 1:
        parts = item_name.split(" ")
        item_name = f"{parts[0]}. {' '.join(parts[1:])}"
        
      item_name = item_name.title()
      
      res.append(f'''     <li>
        <a href="{file_path}">{item_name}</a>
      </li>
'''.rstrip())
      
  list_items = '\n'.join(res)

  return f'''
<li>
  <h3>{title}</h3>
  <ul>
{list_items}
  </ul>
</li>
'''.strip()

def gen_sections(section_title, parent_dir):
  res = []
  
  for dir_name in sorted(os.listdir(parent_dir), key=lambda x: x.split(".")[0]):
    dir_path = os.path.join(parent_dir, dir_name)
    if os.path.isdir(dir_path):
      res.append(gen_section(section_title, dir_path))
      
  return '<ol>\n' + '\n'.join(res) + '\n</ol>'

if __name__ == "__main__":
  print(gen_sections("Kolokwium", "./Kolokwia/2020-2021"))