# 📊 데이터 시각화 실습 (Maewon_DS)

고등학생을 위한 3시간 데이터 시각화 실습 수업입니다.

## 🎯 학습 목표

1. **Jupyter Notebook**에서 matplotlib으로 데이터 탐색 및 시각화
2. **Streamlit**으로 인터랙티브 대시보드 제작
3. **Streamlit Cloud**에 배포하여 포트폴리오 완성

## 📚 수업 진행

### Part 1: 전처리 & 시각화 (60분)
- 파일: `notebooks/preprocessing.ipynb`
- 데이터 로드, 결측치 처리, 파생변수 생성
- matplotlib으로 4개 그래프 생성

### Part 2: Streamlit 대시보드 (90분) ⬅️ 15분 추가!
- 파일: `app.py`
- **TODO 13개** 완성 (기본 8개 + 인터랙티브 4개 + 인사이트 1개) 🆕
- Plotly로 인터랙티브 그래프 제작

### Part 3: 배포 (30분) ⬅️ 15분 단축
- GitHub에 푸시
- Streamlit Cloud 배포
- 링크 공유

## 🚀 실행 방법

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. Jupyter Notebook 실행
```bash
cd notebooks
jupyter notebook preprocessing.ipynb
```

### 3. Streamlit 앱 실행
```bash
streamlit run app.py
```

## 📊 데이터셋

- **Netflix Titles**: 8,807개 영화/TV쇼 정보
- **출처**: Kaggle Netflix Shows Dataset
- **위치**: `data/netflix_titles.csv`

## 📝 파일 구조

```
Maewon_DS/
├── data/
│   ├── netflix_titles.csv          # 원본 데이터
│   └── netflix_cleaned.csv         # 전처리 후 (자동 생성)
├── notebooks/
│   └── preprocessing.ipynb         # Part 1: 전처리 & 시각화
├── app.py                          # Part 2: Streamlit (TODO)
├── app_complete.py                 # 정답 파일
├── README.md                       # 이 파일
├── TODO_LIST.md                    # 과제 상세 가이드
├── requirements.txt                # 패키지 목록
└── .gitignore                      # Git 제외 파일
```

## ✅ TODO 목록

총 13개 과제 (난이도: ⭐~⭐⭐) 🆕

### 기본 과제 (TODO 1-9)

| # | 제목 | 난이도 | 내용 |
|---|------|--------|------|
| 1 | 제목 추가 | ⭐ | Streamlit 제목 입력 |
| 2 | 데이터 로드 | ⭐ | 파일 경로 입력 |
| 3 | 데이터프레임 표시 | ⭐ | head(10) 사용 |
| 4 | 히스토그램 | ⭐⭐ | Jupyter → Streamlit 변환 |
| 5 | 빈도수 계산 1 | ⭐⭐ | value_counts() 사용 |
| 6 | 막대그래프 | ⭐⭐ | Jupyter → Streamlit 변환 |
| 7 | 빈도수 계산 2 | ⭐⭐ | value_counts() 사용 |
| 8 | 파이차트 | ⭐⭐ | Jupyter → Streamlit 변환 |
| 9 | 인사이트 작성 | ⭐ | 텍스트 입력 (이미 완성) |

### 인터랙티브 과제 (TODO 10-13) 🆕

| # | 제목 | 난이도 | 내용 |
|---|------|--------|------|
| 10 | 콘텐츠 유형 필터 | ⭐⭐ | multiselect로 Movie/TV Show 선택 |
| 11 | 연도 범위 슬라이더 | ⭐⭐ | 개봉 연도 범위 선택 |
| 12 | 제목 검색 | ⭐ | 텍스트 입력으로 제목 검색 |
| 13 | 상위 N개 국가 | ⭐⭐ | 슬라이더로 상위 N개 국가 선택 |

자세한 가이드: `TODO_LIST.md` 참고

## 🎓 학습 포인트

### Jupyter → Streamlit 변환 패턴

| matplotlib | Plotly Express | Streamlit |
|-----------|---------------|-----------|
| `plt.hist()` | `px.histogram()` | `st.plotly_chart()` |
| `plt.bar()` | `px.bar()` | `st.plotly_chart()` |
| `plt.pie()` | `px.pie()` | `st.plotly_chart()` |

### 주요 학습 내용

1. **데이터 전처리**
   - 결측치 처리 (fillna, dropna)
   - 파생변수 생성 (feature engineering)

2. **데이터 시각화**
   - matplotlib으로 정적 그래프
   - Plotly로 인터랙티브 그래프

3. **웹 대시보드**
   - Streamlit 기초
   - 레이아웃 (탭, 컬럼 등)
   - 인터랙티브 요소 (selectbox, multiselect, slider, text_input 등) 🆕
   - 사용자 필터링 및 실시간 데이터 업데이트 🆕

4. **배포**
   - GitHub 연동
   - Streamlit Cloud

## 📖 코드 예시

### Jupyter (app.py 완성 전)
```python
import matplotlib.pyplot as plt

# 히스토그램
plt.hist(df['title_length'], bins=30)
plt.show()
```

### Streamlit (app.py 완성 후)
```python
import streamlit as st
import plotly.express as px

# 히스토그램
fig = px.histogram(df, x='title_length', nbins=30)
st.plotly_chart(fig, use_container_width=True)
```

## 🎬 수업 시나리오

### **60분 (Part 1: Jupyter)**
- 데이터 로드 및 탐색 (10분)
- 결측치 처리 (15분)
- 파생변수 생성 (15분)
- matplotlib 시각화 (20분)

### **90분 (Part 2: Streamlit)** ⬅️ 15분 추가! 🆕
- 기본 설정 및 TODO 1-3 (15분)
- Jupyter 코드 변환 및 TODO 4-8 (45분)
- 인터랙티브 필터 추가 및 TODO 10-13 (30분) 🆕
- 인사이트 작성 및 TODO 9 (15분 - 마지막)

### **30분 (Part 3: 배포)** ⬅️ 15분 단축
- GitHub 저장소 생성 및 푸시 (10분)
- Streamlit Cloud 배포 (15분)
- 링크 테스트 및 공유 (5분)

## 💾 저장된 파생변수

preprocessing.ipynb 실행 후 생성되는 6개 파생변수:

1. **decade** - 연대 (1920년대부터 2020년대)
2. **is_korean** - 한국 콘텐츠 여부 (True/False)
3. **title_length** - 제목 길이 (글자 수)
4. **content_age** - 콘텐츠 나이 (2024년 기준)
5. **is_recent** - 최근 5년 콘텐츠 (2019년 이후, True/False)
6. **has_cast** - 출연진 정보 유무 (True/False)

## 🔧 트러블슈팅

### 한글 폰트 오류
- Windows: `plt.rcParams['font.family'] = 'Malgun Gothic'` 설정됨
- Mac: `plt.rcParams['font.family'] = 'DejaVu Sans'` 로 변경
- Linux: `plt.rcParams['font.family'] = 'Noto Sans CJK JP'` 로 변경

### Streamlit 실행 오류
```bash
# 캐시 삭제
streamlit cache clear

# 포트 변경
streamlit run app.py --server.port 8502
```

### 데이터 로드 오류
- 경로 확인: `data/netflix_cleaned.csv` 존재 여부
- Jupyter 먼저 실행: preprocessing.ipynb로 netflix_cleaned.csv 생성

## 📚 추가 자료

- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [Plotly 공식 문서](https://plotly.com/python/)
- [pandas 공식 문서](https://pandas.pydata.org/docs/)
- [matplotlib 공식 문서](https://matplotlib.org/)

## 📝 라이센스

MIT License - 교육 목적 자유 사용

## 👨‍🏫 제작자

고등학교 데이터 시각화 실습 수업용 프로젝트

---

**이 수업으로 Jupyter, Streamlit, 웹 배포까지 한 번에 배울 수 있습니다!** 🚀
