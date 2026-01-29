from pathlib import Path
import json


def load_json(file: Path) -> dict | list:
    with open(file, mode='r', encoding='utf-8') as fp:
        return json.load(fp)


def save_json(file: Path, data: dict | list):
    Path(file).parent.mkdir(parents=True, exist_ok=True)
    with open(file, mode='w', encoding='utf-8') as fp:
        json.dump(data, fp, indent='    ')
