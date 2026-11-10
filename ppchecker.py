from pathlib import Path

supported_languages = {
    ".cpp" : 0,
    ".py" : 0,
    ".js" : 0,
    ".md" : 0,
    ".html" : 0,
    ".css" : 0,
}

folder_path = Path("/mnt/mydrive/Scrap/CodeStatTest1")

for file in folder_path.iterdir():
    if file.is_file():
        extension = file.suffix

        if extension in supported_languages:
            supported_languages[extension] +=1

print(supported_languages)

