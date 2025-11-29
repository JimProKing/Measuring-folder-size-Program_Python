from pathlib import Path

WORK_DIR = Path(__file__).parent # 소스코드 절대경로 지정
OUT_DIR = WORK_DIR / "output"

if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True) # 이미 output 폴더가 있어도 오류 안나게 하기 위해, exist_ok 설정