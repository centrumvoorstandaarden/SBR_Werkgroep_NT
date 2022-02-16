from pathlib import Path
import json

for child in Path('.').iterdir():
    if child.is_file() and ".py" not in child.name: # Otherwise, We'll also read the MD dir	
        nt_rule = str(child.name).replace('.json', '')
        print(f"Converting '{child.name}'")
        json_file = json.loads(child.read_text())
        
        md_str = f"# {nt_rule}\n\n"

        for k,v in json_file.items():
            md_str += (f"## {k}\n")
            md_str += (f"{v}\n\n")

        with open(f"md/{nt_rule}.md", 'w') as md_file:
            md_file.write(md_str)
            
            
        
