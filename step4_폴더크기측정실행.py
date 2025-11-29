import json
from pathlib import Path
from step1_폴더생성 import OUT_DIR
from step2_크기측정 import get_total_filesize
from step3_폴더목록JSON import load_dirnames

OUT_step4 = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_filesize_from_dirnames():
    dirs = load_dirnames()
    result = {}
    for path_str in dirs:
        path = Path(path_str)
        filesize = get_total_filesize(path, pattern="**/*")
        result[path.as_posix()]=filesize
    with open(OUT_step4,"w",encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)

def load_filesize_per_dir() -> dict[str,int]:
    if OUT_step4.is_file():
        with open(OUT_step4,encoding="utf-8") as fp:
            return json.load(fp)
    return {}

if __name__ == "__main__":
    dump_filesize_from_dirnames()