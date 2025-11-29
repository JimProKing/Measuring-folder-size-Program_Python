# 폴더 크기 분석기 (Directory Size Analyzer)

`pathlib`를 활용한 순수 파이썬 기반 디렉터리 용량 분석
- 작업일: 2025.11.29. (부산 가는 기차 안)
- "혼자 만들면서 공부하는 파이썬" 책 예제 연계

| Python | License | Dependencies |
|--------|---------|--------------|
| 3.9+   | MIT     | None         |

## 프로젝트 개요

본 프로젝트는 외부 의존성 없이 표준 라이브러리만을 사용하여 특정 디렉터리 내의 모든 하위 디렉터리에 대해 재귀적으로 파일 크기를 계산하고, 그 결과를 구조화된 JSON 형식으로 저장하는 실습용 도구입니다.

`pathlib.Path` 객체를 중심으로 한 현대적인 파일 시스템 조작 기법을 학습할 수 있으며, 모듈화와 함수형 프로그래밍 원칙을 준수한 설계로 구성되어 있습니다.

## 파일 구성 및 역할

| 단계 | 파일명                          | 주요 기능                                            |
|------|--------------------------------|-----------------------------------------------------|
| 1    | `step1_폴더생성.py`             | 결과물 저장을 위한 `output/` 디렉터리 자동 생성       |
| 2    | `step2_크기측정.py`             | 지정된 경로 내 모든 파일의 총합 바이트 계산 함수 제공 |
| 3    | `step3_폴더목록JSON.py`         | 대상 디렉터리의 하위 디렉터리 목록 추출 및 JSON 저장  |
| 4    | `step4_폴더크기측정실행.py`     | 3번에서 추출된 각 디렉터리의 용량 계산 및 결과 저장   |

## 실행 방법

```bash
git clone https://github.com/your-username/directory-size-analyzer.git
cd directory-size-analyzer

# 순차 실행
python step1_폴더생성.py
python step3_폴더목록JSON.py      # 필요 시 분석 대상을 여기서 변경
python step4_폴더크기측정실행.py
```

실행이 완료되면 `output/step4_폴더크기측정실행.json` 파일에 다음과 유사한 결과가 기록됩니다:

```json
{
  "/Users/username/Documents": 1298472938,
  "/Users/username/Downloads": 42849203421,
  "/Users/username/Desktop":   8923749238,
  "/Users/username/Projects": 15728493721
}
```

## 분석 대상 디렉터리 변경 방법

`step3_폴더목록JSON.py` 파일 하단의 다음 줄을 수정합니다:

```python
if __name__ == "__main__":
    # 기본값: 사용자 홈 디렉터리
    dump_dirnames(Path.home())

    # 예시 1: 특정 절대 경로 지정
    # dump_dirnames(Path("/Volumes/ExternalDrive/Data"))

    # 예시 2: 현재 프로젝트 디렉터리 기준
    # dump_dirnames(Path(__file__).parent)
```

## 학습 목표 및 특징

- `pathlib.Path`를 활용한 플랫폼 독립적 경로 처리
- 재귀 패턴 매칭 (`**/*`)과 `glob`·`iterdir`의 적절한 사용
- 모듈 간 명확한 의존성 관리 및 재사용 가능한 함수 설계
- JSON을 이용한 데이터 직렬화 및 지속성 확보
- 외부 패키지 의존성 제로 (Zero External Dependency)

> 파이썬 표준 라이브러리의 강력함을 몸소 체험할 수 있는 실습 프로젝트입니다.  
> 디스크 용량 분석이 필요한 모든 상황에서 유용하게 활용하시기 바랍니다.