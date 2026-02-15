import os
import re

# Folders to scan
FOLDERS = ["Sorting", "Searching", "Data-Structures"]
README_PATH = "README.md"

def get_algo_info(filepath):
    """Extracts Name, Time, and Space from the file docstring."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    name = re.search(r"Name:\s*(.*)", content)
    time_comp = re.search(r"Time:\s*(.*)", content)
    space_comp = re.search(r"Space:\s*(.*)", content)

    if name and time_comp and space_comp:
        return f"| {name.group(1).strip()} | ${time_comp.group(1).strip()}$ | ${space_comp.group(1).strip()}$ |"
    return None

def update_readme():
    rows = []
    for folder in FOLDERS:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.endswith(".py") and file != "__init__.py":
                    row = get_algo_info(os.path.join(folder, file))
                    if row:
                        rows.append(row)

    # Sort rows alphabetically
    rows.sort()
    
    table_header = (
        "| Algorithm | Time Complexity | Space Complexity |\n"
        "| :--- | :--- | :--- |\n"
    )
    new_table = table_header + "\n".join(rows)

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Regex to replace the old table with the new one
    # It looks for the table headers and replaces everything until the next section
    updated_content = re.sub(
        r"\| Algorithm \|.*?(?=\n#|\Z)", 
        new_table + "\n\n", 
        readme_content, 
        flags=re.DOTALL
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print("✅ README.md updated successfully!")

if __name__ == "__main__":
    update_readme()