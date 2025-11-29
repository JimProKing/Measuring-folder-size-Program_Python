from pathlib import Path
from step1_폴더생성 import WORK_DIR #step1 모듈에서 WORK_DIR 불러옴

def get_total_filesize(base_dir: Path, pattern: str="*") -> int:
    total_bytes = 0 # 변수 초기화 (파일 크기 저장할 것임)
    for fullpath in base_dir.glob(pattern): # 글로브 패턴과 일치하는 파일명 리스트로 반환
        if fullpath.is_file(): # 파일이 유효한지 검사
            total_bytes += fullpath.stat().st_size # 파일 크기를 바이트 단위로 더함
    return total_bytes

if __name__ == "__main__":
    base_dir = WORK_DIR
    filesize = get_total_filesize(base_dir,pattern="*")
    print(f"{base_dir.as_posix()=}, {filesize=} bytes") #as.posix 함수가 Path 객체를 문자열로 바꿀 것임.

