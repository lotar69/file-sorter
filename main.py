from pathlib import Path

my_download_path = input("Enter the path directory to clean: ")

my_download_path

downloads = Path(str(my_download_path))

iter_down = downloads.iterdir()

dirs = {".png": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".zip": "Archives",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".json": "Documents",
        ".mp3": "Musiques",
        ".xlsx": "Documents",
        ".ipynb": "Code",
        "^.py": "Code",
        ".exe": "Executables"}

files = [i for i in iter_down if i.is_file()]
for f in files:
    output_dir = downloads / dirs.get(f.suffix, "Others")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)