import json
from pathlib import Path
from step1_폴더생성 import OUT_DIR

OUT_step3 = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_dirnames(base_dir: Path) -> None:
    #폴더 목록 저장하는 함수 * base_dir - 폴더 경로
    dirs=[]
    for path in base_dir.iterdir():
        if path.is_dir():
            dirs.append(path.as_posix())
    dirs_sorted = sorted(dirs)
    with open(OUT_step3,"w",encoding="utf-8") as fp:
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)

def load_dirnames() -> list[str]:
    if OUT_step3.is_file():
        with open(OUT_step3, encoding="utf-8") as fp:
            return json.load(fp)
    return []

if __name__ == "__main__":
    dump_dirnames(Path.home()) ## Path.home() 이기에, 
    # Path(__file__).parent 이건 현재 경로