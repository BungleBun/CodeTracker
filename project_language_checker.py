from pathlib import Path
import math

supported_languages = {
    ".cpp" : 0,
    ".py" : 0,
    ".js" : 0,
    ".md" : 0,
    ".html" : 0,
    ".css" : 0,
}


from pathlib import Path

def count_lines(path: Path) -> int:
    """Return the number of lines in a text file."""
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        return sum(1 for _ in f)


folder_path = Path("/mnt/mydrive/Scrap/CodeStatTest1")

for path in folder_path.rglob("*"):
    if path.is_file():
        extension = path.suffix

        if extension in supported_languages:
            count_lines(path)
            supported_languages[extension] += count_lines(path)

def lang_percent():
    total = sum(supported_languages.values())
    for language, value in supported_languages.items():
        percent = value * 100 / total
        print(f"{language}: %{math.trunc(percent)}")

lang_percent()

