import os
import sys
import shutil

# Resolve user home directory dynamically
HOME = os.path.expanduser("~")

def get_target_paths():
    """
    Dynamically resolve target configuration paths:
    1. Global configuration (%USERPROFILE%/.gemini/config/AGENTS.md)
    2. Any active Antigravity workspace folders under %USERPROFILE%/Documents/antigravity/
    3. Local directory if running inside an active project.
    """
    targets = [
        (os.path.join(HOME, ".gemini", "config", "AGENTS.md"), True)
    ]
    
    # Scan Documents/antigravity for active project workspaces
    ag_doc_dir = os.path.join(HOME, "Documents", "antigravity")
    if os.path.exists(ag_doc_dir):
        for item in os.listdir(ag_doc_dir):
            item_path = os.path.join(ag_doc_dir, item)
            if os.path.isdir(item_path):
                agents_dir = os.path.join(item_path, ".agents")
                target_agents_file = os.path.join(agents_dir, "AGENTS.md")
                targets.append((target_agents_file, False))
                
    # Also include current working directory if inside an Antigravity project
    cwd = os.getcwd()
    cwd_agents = os.path.join(cwd, ".agents", "AGENTS.md")
    existing_paths = [t[0] for t in targets]
    if cwd_agents not in existing_paths and os.path.exists(os.path.join(cwd, ".agents")):
        targets.append((cwd_agents, False))

    return targets

# Source rule directory locations
GLOBAL_SOURCE_DIR = os.path.join(HOME, ".gemini", "config", ".agents")
LOCAL_SOURCE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".agents")

def find_rule_filepath(filename):
    """
    Look for filename in local repository .agents folder first, then global config .agents folder.
    """
    local_path = os.path.join(LOCAL_SOURCE_DIR, filename)
    if os.path.exists(local_path):
        return local_path
        
    global_path = os.path.join(GLOBAL_SOURCE_DIR, filename)
    if os.path.exists(global_path):
        return global_path
        
    return None

RULES_MAP = {
    "neon": "Neon_v4.3.md",
    "neon43": "Neon_v4.3.md",
    "jalapeno": "Neon_v4.3.md",
    "flash": "Gemini_3.5_Flash.md",
    "gemini35": "Gemini_3.5_Flash.md",
    "pro": "Gemini_3.1_Pro.md",
    "gemini31": "Gemini_3.1_Pro.md",
    "sonnet": "Claude_Sonnet_4.6.md",
    "opus": "Claude_Opus_4.6.md",
    "gpt": "GPT_OSS_120B.md",
    "oss": "GPT_OSS_120B.md"
}

ORDERED_MODELS = [
    ("Neon v4.3 (Universal Hardened / Deep Thinking)", "Neon_v4.3.md"),
    ("Gemini 3.5 Flash", "Gemini_3.5_Flash.md"),
    ("Gemini 3.1 Pro", "Gemini_3.1_Pro.md"),
    ("Claude Sonnet 4.6", "Claude_Sonnet_4.6.md"),
    ("Claude Opus 4.6", "Claude_Opus_4.6.md"),
    ("GPT-OSS 120B", "GPT_OSS_120B.md")
]

def combine_all_rules(target_file):
    combined_content = [
        "# Custom System Directives\n",
        "The following instructions are model-specific. Please locate and follow the section corresponding to your model identity:\n"
    ]
    
    for model_name, filename in ORDERED_MODELS:
        filepath = find_rule_filepath(filename)
        if filepath and os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            combined_content.append(f"\n## Directives for {model_name}\n")
            combined_content.append(content)
            combined_content.append("\n---\n")
        else:
            print(f"Warning: Source file for '{model_name}' ('{filename}') not found. Skipping...")
            
    try:
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("\n".join(combined_content))
        print(f"Successfully combined rules for ALL models into -> {target_file}")
    except Exception as e:
        print(f"Error combining rules for {target_file}: {e}")

def set_rules(model_key):
    targets = get_target_paths()
    
    if model_key == "all":
        print("Toggling rules to: Combined (ALL models)")
        for target_file, _ in targets:
            combine_all_rules(target_file)
        return
        
    if model_key not in RULES_MAP:
        print(f"Error: Unknown model key '{model_key}'.")
        print("Available options: all, " + ", ".join(sorted(RULES_MAP.keys())))
        return
        
    src_filename = RULES_MAP[model_key]
    src_filepath = find_rule_filepath(src_filename)
    
    if not src_filepath:
        print(f"Error: Source file '{src_filename}' does not exist in local or global .agents directory.")
        return
        
    print(f"Toggling rules to: {src_filename} (from {src_filepath})")
    for target_file, _ in targets:
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            shutil.copyfile(src_filepath, target_file)
            print(f"Successfully updated rule file -> {target_file}")
        except Exception as e:
            print(f"Error writing to {target_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python set-rules.py <model_name | all>")
        print("Example: python set-rules.py neon")
        print("Available models: all, " + ", ".join(sorted(set(RULES_MAP.keys()))))
    else:
        set_rules(sys.argv[1].lower())
