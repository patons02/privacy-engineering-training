import nbformat
import sys

def fix_notebook(path_in, path_out=None):
    # Open the notebook properly
    with open(path_in, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Patch every code cell
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            # Add missing outputs or execution_count if not present
            cell.setdefault('outputs', [])
            cell.setdefault('execution_count', None)
    
    # Save the patched notebook
    if path_out is None:
        path_out = path_in  # overwrite original
    with open(path_out, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"Fixed notebook saved at {path_out}")

# Usage
fix_notebook(sys.argv[1], sys.argv[1])

