import json

# 1. Put the name of your broken downloaded notebook here
input_filename = 'HW5_script_GraduateTask.ipynb' 
output_filename = 'HW5_repaired_script_GraduateTask.ipynb'

with open(input_filename, 'r', encoding='utf-8') as f:
    nb = json.load(f)

try:
    # Navigate to the broken widget section
    widgets_meta = nb['metadata']['widgets']['application/vnd.jupyter.widget-state+json']
    
    # If the 'state' key is missing, we restructure it
    if 'state' not in widgets_meta:
        print("Missing 'state' key found. Repairing...")
        
        # Grab all the existing widget IDs (this is the actual state data)
        actual_state_data = widgets_meta.copy()
        
        # Rebuild the dictionary with the correct Jupyter specification
        nb['metadata']['widgets']['application/vnd.jupyter.widget-state+json'] = {
            "version_major": 2,
            "version_minor": 0,
            "state": actual_state_data
        }
        
        # Save the repaired notebook
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=2)
            
        print(f"Success! Repaired file saved as: {output_filename}")
        print("You can now run nbconvert on this new file.")
        
    else:
        print("The 'state' key is already present. No repair needed.")

except KeyError:
    print("Could not find the widget metadata. Are you sure this is the right file?")