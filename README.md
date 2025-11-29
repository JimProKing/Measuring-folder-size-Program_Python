# 폰더 크기 분석기 (Directory Size Analyzer)

`pathlib`를 활용한 순수 파이썬 기반 재귀적 디렉터리 용량 분석 도구  
— 2025.11.29. 부산행 KTX 2호차 12C석에서 완성

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pathlib Master](https://img.shields.io/badge/pathlib-master-green)
![Zero Deps](https://img.shields.io/badge/Dependencies-0-success)
![Made on KTX](https://img.shields.io/badge/Made%20on-KTX_%20Busan%20Line-orange)

> “혼자 만들면서 공부하는 파이썬” 책 참고

## 프로젝트 개요

본 프로젝트는 외부 패키지 없이 **표준 라이브러리만을 사용**하여 지정된 루트 디렉터리 내의 **하위 디렉터리를 재귀적으로 탐색**하고, 각 디렉터리가 차지하는 총 파일 용량을 계산하여 JSON으로 저장하는 실습용 분석 도구입니다.

`pathlib.Path`의 현대적 API와 재귀 패턴 매칭(`glob('**/')`, `rglob`)을 깊이 있게 다루며, 모듈화와 함수 재사용성을 철저히 지킨 설계를 통해 파이썬 중급 문법을 자연스럽게 체득할 수 있도록 구성하였습니다.

## 파일 구성 및 기능

| 단계 | 파일명                          | 핵심 기능                                             |
|------|--------------------------------|-------------------------------------------------------|
| 1    | `step1_폴더생성.py`             | `output/` 디렉터리 자동 생성                           |
| 2    | `step2_크기측정.py`             | 재귀적 파일 크기 합계 계산 함수 (`glob("**/*")`)       |
| 3    | `step3_폴더목록JSON.py`         | **재귀적** 하위 디렉터리 수집 → JSON 저장         |
| 4    | `step4_폴더크기측정실행.py`     | 수집된 모든 폴더에 대해 용량 계산 → 최종 결과 저장      |

**핵심 변경점 (v2.0)**:  
`step3`에서 기존 `iterdir()` → `Path.glob('**/')`로 변경하여 **진정한 재귀 탐색** 구현

## 실행 방법

```bash
git clone https://github.com/JimProKing/directory-size-analyzer.git
cd directory-size-analyzer

python step1_폴더생성.py
python step3_폴더목록JSON.py     # ← 여기서 분석 대상을 설정
python step4_폴더크기측정실행.py