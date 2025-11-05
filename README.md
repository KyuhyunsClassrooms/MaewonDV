# 🎬 Netflix 데이터 시각화 실습

**환영합니다!** 오늘은 Netflix 데이터를 활용해서 나만의 대시보드를 만들고 인터넷에 배포까지 해볼 거예요! 🚀

> 🎨 **특별 기능**: Netflix 공식 다크 테마로 멋진 웹페이지를 만들어요!

## 🎯 오늘 뭐 할 거예요?

1. **1교시 (60분)**: Jupyter로 데이터 분석하고 그래프 그리기
2. **2교시 (90분)**: Streamlit으로 Netflix 스타일 웹페이지 만들기
3. **3교시 (30분)**: 내가 만든 사이트 인터넷에 배포하기

> 💡 **완성하면?** 친구들에게 자랑할 수 있는 나만의 Netflix 스타일 웹사이트!

---

## 📂 오늘 사용할 파일들

```
📁 code/
  ├── 📁 notebooks/
  │   └── preprocessing.ipynb    ⬅️ 1교시: 여기서 시작!
  ├── 📁 data/
  │   └── netflix_titles.csv     ⬅️ Netflix 데이터 (8,807개)
  ├── app.py                     ⬅️ 2교시: TODO 채우기!
  ├── app_complete.py            ⬅️ 정답 파일 (막히면 참고)
  └── README.md                  ⬅️ 지금 보는 파일
```

---

## � 시작하기

### ✅ STEP 0: 준비 확인

이 화면이 보이면 준비 완료! 아래 명령어는 **이미 실행되었어요**.

```bash
pip install -r requirements.txt  # ✅ 이미 설치됨
```

---

## 📚 1교시: Jupyter로 데이터 분석 (60분)

### 🎯 목표
- Netflix 데이터 살펴보기
- 결측치(빈 데이터) 정리하기
- 그래프 4개 그려보기

### 📝 따라하기

#### 1️⃣ Jupyter Notebook 열기 (5분)

1. 왼쪽 탐색기에서 `notebooks` 폴더 클릭
2. `preprocessing.ipynb` 파일 더블클릭
3. 노트북이 열리면 준비 완료!

#### 2️⃣ 셀 실행하기 (55분)

```
💡 팁: 각 셀 왼쪽의 ▶️ 버튼을 누르면 코드가 실행돼요!
      또는 Shift + Enter 키를 누르세요.
```

**실습 순서:**
1. **Section 1**: 데이터 불러오기 (10분)
2. **Section 2**: 데이터 탐색하기 (10분)
3. **Section 3**: 결측치 처리하기 (15분)
4. **Section 4**: 새로운 컬럼 만들기 (10분)
5. **Section 5**: 그래프 그리기 (20분)
   - 히스토그램 📊
   - 막대그래프 📈
   - 파이차트 🥧
   - 비교 막대그래프 📉

#### 3️⃣ 데이터 저장 (자동)

마지막 셀을 실행하면 `data/netflix_cleaned.csv` 파일이 자동으로 생성돼요!

---

## 💻 2교시: Streamlit 웹페이지 만들기 (90분)

### 🎯 목표
- Jupyter 코드를 Streamlit으로 변환하기
- **TODO 13개** 완성하기
- 인터랙티브 필터 추가하기

### 📝 따라하기

#### 1️⃣ app.py 파일 열기 (5분)

1. 왼쪽 탐색기에서 `app.py` 파일 클릭
2. 파일 안에 `___여기에___` 표시가 있는 곳을 찾으세요
3. 이게 바로 **TODO**예요!

#### 2️⃣ TODO 완성하기 (70분)

**기본 과제 (TODO 1-9)**

| TODO | 제목 | 난이도 | 힌트 |
|------|------|--------|------|
| 1 | 페이지 제목 | ⭐ | `st.title("Netflix 데이터 분석")` |
| 2 | 데이터 불러오기 | ⭐ | 경로: `data/netflix_cleaned.csv` |
| 3 | 데이터 보여주기 | ⭐ | `st.dataframe(df.head(10))` |
| 4 | 히스토그램 | ⭐⭐ | Jupyter 그래프를 복사해서 수정 |
| 5-6 | 막대그래프 | ⭐⭐ | `value_counts()` 사용 |
| 7-8 | 파이차트 | ⭐⭐ | 한국 콘텐츠 비율 계산 |
| 9 | 인사이트 작성 | ⭐ | 분석 결과 정리 (나중에!) |

**인터랙티브 과제 (TODO 10-13)** 🆕

| TODO | 제목 | 난이도 | 무엇을 하나요? |
|------|------|--------|--------------|
| 10 | 콘텐츠 유형 필터 | ⭐⭐ | Movie/TV Show 선택 기능 |
| 11 | 연도 슬라이더 | ⭐⭐ | 원하는 연도 범위 선택 |
| 12 | 제목 검색 | ⭐ | 제목으로 콘텐츠 찾기 |
| 13 | 상위 국가 선택 | ⭐⭐ | Top 10 또는 Top 20 선택 |

> 💡 **막히면?** `app_complete.py` 파일을 열어서 정답을 확인하세요!

#### 3️⃣ Streamlit 실행하기 (5분)

아래 **터미널**에 명령어 입력:

```bash
streamlit run app.py
```

웹브라우저가 자동으로 열리고 **Netflix 스타일의 다크 모드**로 여러분이 만든 페이지가 나타나요! 🎉

```
🎨 Netflix 테마 특징:
- ⚫ 다크 배경 (#141414)
- 🔴 Netflix 빨강 강조색 (#E50914)
- ✨ 부드러운 애니메이션
- 🎯 깔끔한 버튼과 슬라이더
```

#### 4️⃣ 실시간 수정 (10분)

```
💡 꿀팁: app.py를 수정하고 저장(Ctrl+S)하면
        웹페이지가 자동으로 새로고침돼요!
```

---

## 🌐 3교시: 인터넷에 배포하기 (30분)

### 🎯 목표
- GitHub에 코드 올리기
- Streamlit Cloud로 배포하기
- 친구들에게 공유할 링크 받기

### 📝 따라하기

#### 1️⃣ GitHub에 저장 (10분)

터미널에서 순서대로 입력:

```bash
git add .
git commit -m "Netflix 대시보드 완성!"
git push origin main
```

#### 2️⃣ Streamlit Cloud 배포 (15분)

1. [streamlit.io/cloud](https://streamlit.io/cloud) 접속
2. **Sign up with GitHub** 클릭
3. **New app** 클릭
4. 설정:
   - Repository: `여러분의저장소/MaewonDV`
   - Branch: `main`
   - Main file path: `app.py`
5. **Deploy!** 클릭

#### 3️⃣ 완성! (5분)

2-3분 기다리면 여러분만의 웹사이트 주소가 생성돼요!

```
🎉 완성된 주소 예시:
https://여러분이름-maewondv.streamlit.app
```

이 주소를 친구들에게 공유하세요! 📱


---

## � 자주 묻는 질문 (FAQ)

### Q1: 코드를 실행했는데 오류가 나요!
**A**: 당황하지 마세요! 오류 메시지를 잘 읽어보거나 선생님께 질문하세요.

### Q2: TODO를 어떻게 채워야 할지 모르겠어요.
**A**: 세 가지 방법이 있어요!
1. Jupyter Notebook의 비슷한 코드를 참고하기
2. `app_complete.py` 정답 파일 확인하기
3. 선생님께 질문하기

### Q3: Streamlit이 실행이 안 돼요.
**A**: 터미널에서 실행했나요?
```bash
streamlit run app.py
```

### Q4: 그래프가 안 보여요.
**A**: `data/netflix_cleaned.csv` 파일이 있나요?
   → Jupyter Notebook을 먼저 끝까지 실행하세요!

### Q5: 배포가 실패했어요.
**A**: GitHub에 코드가 잘 올라갔나요?
   → `git push origin main` 명령어를 다시 실행해보세요.

---

## 🎓 배운 내용 정리

### 1교시에서 배운 것
- ✅ pandas로 데이터 불러오기 (`read_csv`)
- ✅ 결측치 처리하기 (`fillna`, `dropna`)
- ✅ 새로운 컬럼 만들기 (파생변수)
- ✅ matplotlib으로 그래프 그리기

### 2교시에서 배운 것
- ✅ Streamlit 기본 문법 (`st.title`, `st.dataframe`)
- ✅ Plotly로 인터랙티브 그래프 만들기
- ✅ 사용자 입력 받기 (`multiselect`, `slider`, `text_input`)
- ✅ 데이터 필터링 (조건에 맞는 데이터 찾기)

### 3교시에서 배운 것
- ✅ Git으로 코드 관리하기
- ✅ GitHub에 코드 올리기
- ✅ Streamlit Cloud로 웹사이트 배포하기

---

## 🎉 수고하셨습니다!

오늘 여러분은:
1. **8,807개의 Netflix 데이터**를 분석했어요
2. **13개의 TODO**를 완성했어요
3. **나만의 웹사이트**를 인터넷에 배포했어요

이제 여러분은 **데이터 과학자**가 되기 위한 첫 걸음을 떼었어요! 👏

---

## 📚 더 공부하고 싶다면?

- [Streamlit 튜토리얼](https://docs.streamlit.io/get-started/tutorials)
- [Plotly 예제](https://plotly.com/python/)
- [pandas 10분 완성](https://pandas.pydata.org/docs/user_guide/10min.html)

---