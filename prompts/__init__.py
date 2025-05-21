from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

def load_prompt(prompt_path: str):
    with open(SCRIPT_DIR / prompt_path, "r", encoding="utf-8") as f:
        return f.read()
