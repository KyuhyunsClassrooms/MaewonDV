# ✅ app.py TODO 과제 목록

## 🎯 총 13개 과제

**전략**: Jupyter에서 만든 코드를 Streamlit으로 변환!

---

## 기본 설정 (15분, TODO 1-3)

### TODO 1: 제목 추가 ⭐

**위치**: Line ~15  
**과제**: 대시보드 제목 입력  
**난이도**: ⭐ (매우 쉬움)

**Streamlit 코드**:
```python
st.title("___여기에_제목_입력___")
```

**정답**:
```python
st.title("📊 Netflix 데이터 시각화 대시보드")
```

**해설**: `st.title()`은 페이지 제목을 표시합니다. 이모지를 포함할 수 있습니다.

---

### TODO 2: 데이터 로드 ⭐

**위치**: Line ~16  
**과제**: Netflix 파일 경로 입력  
**난이도**: ⭐ (매우 쉬움)

**Streamlit 코드**:
```python
df_original = pd.read_csv("___파일_경로___")
df = df_original.copy()
```

**정답**:
```python
df_original = pd.read_csv("data/netflix_cleaned.csv")
df = df_original.copy()
```

**해설**: 
- preprocessing.ipynb 실행 후 생성되는 파일 경로
- `data/` 디렉토리에 저장된 파일
- `df_original`은 필터용 원본, `df`는 필터링될 복사본

---

### TODO 3: 데이터프레임 표시 ⭐

**위치**: Line ~79  
**과제**: 처음 10개 행 표시  
**난이도**: ⭐ (매우 쉬움)

**Streamlit 코드**:
```python
st.subheader("📋 데이터 미리보기")
st.dataframe(df.___)
```

**정답**:
```python
st.subheader("📋 데이터 미리보기")
st.dataframe(df.head(10))
```

**해설**: `df.head(10)`은 처음 10개 행을 반환합니다.

---

## Jupyter → Streamlit 변환 (45분, TODO 4-8)

### TODO 4: 히스토그램 ⭐⭐

**위치**: Line ~87  
**과제**: Jupyter의 `plt.hist()` → `px.histogram()` 변환  
**난이도**: ⭐⭐ (중간)

**Jupyter 코드** (preprocessing.ipynb):
```python
plt.hist(df['title_length'], bins=30)
plt.show()
```

**Streamlit 코드** (app.py):
```python
fig = px.histogram(
    df, 
    x=___, 
    nbins=30,
    title="제목 길이 분포",
    labels={'title_length': '제목 길이 (글자 수)', 'count': '개수'},
    color_discrete_sequence=['#E50914']
)
st.plotly_chart(fig, use_container_width=True)
```

**정답**: `'title_length'`

**해설**:
- Plotly Express에서는 컬럼명을 **문자열**로 입력
- `x='title_length'` - x축 데이터
- `nbins=30` - 히스토그램 구간 수

---

### TODO 5: 빈도수 계산 ⭐⭐

**위치**: Line ~112  
**과제**: 연대별 빈도수 계산  
**난이도**: ⭐⭐ (중간)

**Jupyter 코드** (preprocessing.ipynb):
```python
decade_counts = df['decade'].value_counts().sort_index()
```

**Streamlit 코드** (app.py):
```python
decade_counts = df['decade'].___().sort_index().tail(10)
```

**정답**: `value_counts()`

**해설**:
- `value_counts()` - 각 값의 출현 빈도 계산
- `sort_index()` - 인덱스 순서대로 정렬
- `tail(10)` - 최신 10개 연대만 (1960~2020년대)

---

### TODO 6: 막대그래프 ⭐⭐

**위치**: Line ~117  
**과제**: Jupyter의 `plt.bar()` → `px.bar()` 변환  
**난이도**: ⭐⭐ (중간)

**Jupyter 코드** (preprocessing.ipynb):
```python
plt.bar(decade_counts.index, decade_counts.values)
plt.show()
```

**Streamlit 코드** (app.py):
```python
fig = px.bar(
    ___, ___,
    title="연대별 콘텐츠 수",
    labels={'x': '연대', 'y': '콘텐츠 수'},
    color_discrete_sequence=['#E50914']
)
st.plotly_chart(fig, use_container_width=True)
```

**정답**: `x=decade_counts.index, y=decade_counts.values`

**해설**:
- Plotly Express의 `px.bar()`는 `x=`, `y=` 파라미터 사용
- `decade_counts.index` - x축 (연대)
- `decade_counts.values` - y축 (콘텐츠 수)

---

### TODO 7: 빈도수 계산 2 ⭐⭐

**위치**: Line ~139  
**과제**: Movie vs TV Show 빈도수  
**난이도**: ⭐⭐ (중간)

**Jupyter 코드** (preprocessing.ipynb):
```python
type_counts = df['type'].value_counts()
```

**Streamlit 코드** (app.py):
```python
type_counts = df['type'].___()
```

**정답**: `value_counts()`

**해설**:
- TODO 6과 동일 방식
- 콘텐츠 유형(Movie, TV Show)의 빈도수 계산

---

### TODO 8: 파이차트 ⭐⭐

**위치**: Line ~144  
**과제**: Jupyter의 `plt.pie()` → `px.pie()` 변환  
**난이도**: ⭐⭐ (중간)

**Jupyter 코드** (preprocessing.ipynb):
```python
plt.pie(type_counts.values, labels=type_counts.index)
plt.show()
```

**Streamlit 코드** (app.py):
```python
fig = px.pie(
    ___, ___,
    title="콘텐츠 유형 비율",
    color_discrete_sequence=['#E50914', '#564d4d']
)
st.plotly_chart(fig, use_container_width=True)
```

**정답**: `values=type_counts.values, names=type_counts.index`

**해설**:
- `px.pie()`는 `values=`, `names=` 파라미터 사용
- `values=type_counts.values` - 크기 (개수)
- `names=type_counts.index` - 레이블 (Movie, TV Show)

---

## 인터랙티브 필터 (30분, TODO 10-12)

### TODO 10: 콘텐츠 유형 필터 ⭐⭐

**위치**: Line ~20  
**과제**: multiselect로 Movie/TV Show 선택  
**난이도**: ⭐⭐ (중간)

**Streamlit 코드**:
```python
content_type_filter = st.sidebar.multiselect(
    "콘텐츠 유형 선택",
    options=___,
    default=___
)
```

**정답**:
```python
content_type_filter = st.sidebar.multiselect(
    "콘텐츠 유형 선택",
    options=["Movie", "TV Show"],
    default=["Movie", "TV Show"]
)
```

**해설**:
- `st.sidebar.multiselect()` - 사이드바에 다중선택 메뉴 생성
- `options` - 선택 가능한 항목 리스트
- `default` - 기본 선택 항목 (전체 선택)

---

### TODO 11: 연도 범위 슬라이더 ⭐⭐

**위치**: Line ~30  
**과제**: 개봉 연도 범위를 슬라이더로 선택  
**난이도**: ⭐⭐ (중간)

**Streamlit 코드**:
```python
year_range = st.sidebar.slider(
    "개봉 연도 범위",
    min_value=___,
    max_value=___,
    value=(___, ___)
)
```

**정답**:
```python
year_range = st.sidebar.slider(
    "개봉 연도 범위",
    min_value=int(df['release_year'].min()),
    max_value=int(df['release_year'].max()),
    value=(int(df['release_year'].min()), int(df['release_year'].max()))
)
```

**해설**:
- `st.sidebar.slider()` - 범위 선택 슬라이더
- `min_value`, `max_value` - 데이터의 최소/최대값
- `value=(최소, 최대)` - 초기값 (전체 범위)

---

### TODO 12: 제목 검색 ⭐

**위치**: Line ~40  
**과제**: 제목 검색 입력창 추가  
**난이도**: ⭐ (매우 쉬움)

**Streamlit 코드**:
```python
search_query = ___(
    "제목 검색 (Enter 후 검색)",
    value=""
)
```

**정답**:
```python
search_query = st.sidebar.text_input(
    "제목 검색 (Enter 후 검색)",
    value=""
)
```

**해설**:
- `st.sidebar.text_input()` - 텍스트 입력창
- `value=""` - 초기값은 빈 문자열

---

## 국가별 분석 추가 (15분, TODO 13)

### TODO 13: 상위 N개 국가 슬라이더 ⭐⭐

**위치**: Line ~105  
**과제**: 슬라이더로 상위 N개 국가 선택  
**난이도**: ⭐⭐ (중간)

**Streamlit 코드**:
```python
top_n = ___(
    "상위 N개 국가 선택",
    min_value=___,
    max_value=___,
    value=___
)

country_counts = df['country'].___().head(top_n)
```

**정답**:
```python
top_n = st.slider(
    "상위 N개 국가 선택",
    min_value=5,
    max_value=20,
    value=10
)

country_counts = df['country'].value_counts().head(top_n)
```

**해설**:
- `st.slider()` - 단일 값 선택 슬라이더
- `min_value=5, max_value=20` - 5~20개 국가 선택 가능
- `value=10` - 기본값 10개
- `orientation='h'` - 가로 막대그래프

---

## 인터랙티브 필터 작동 원리

TODO 10-12를 완성하면 다음과 같이 필터가 적용됩니다:

```python
# 콘텐츠 유형 필터
if content_type_filter:
    df = df[df['type'].isin(content_type_filter)]

# 연도 범위 필터
df = df[(df['release_year'] >= year_range[0]) & (df['release_year'] <= year_range[1])]

# 제목 검색 필터
if search_query:
    df = df[df['title'].str.contains(search_query, case=False, na=False)]
```

**효과**: 필터를 변경하면 모든 그래프가 실시간으로 업데이트됩니다!

---

## 인사이트 작성 (15분, TODO 9)

### TODO 9: 텍스트 입력 ⭐

**위치**: Line ~171  
**과제**: 이미 완성 (학습용)  
**난이도**: ⭐ (매우 쉬움)

**설명**: 이 TODO는 이미 완성되어 있으며 수정할 필요 없습니다.

**코드**:
```python
insight = st.text_area(
    "데이터에서 발견한 흥미로운 점을 작성해보세요:",
    height=150
)

if insight:
    st.success("✅ 인사이트가 저장되었습니다!")
    st.info(f"**작성한 내용**: {insight}")
```

---

## 🎓 수업 가이드

### Part 1: preprocessing.ipynb (60분)
- 데이터 전처리
- matplotlib 시각화 4개 생성

### Part 2: app.py (90분) ⬅️ 15분 추가!
- TODO 1-3: 기본 설정 (15분)
- TODO 4-8: 코드 변환 (45분)
- TODO 10-13: 인터랙티브 기능 (30분) 🆕
- TODO 14: 인사이트 (15분) - 마지막에 작성

### Part 3: 배포 (30분) ⬅️ 15분 단축
- GitHub 푸시
- Streamlit Cloud 배포

---

## 💡 변환 패턴 정리

### 히스토그램 (TODO 4)
```
Jupyter: plt.hist(df['col'], bins=30)
↓
Streamlit: px.histogram(df, x='col', nbins=30)
```

### 막대그래프 (TODO 6)
```
Jupyter: plt.bar(index, values)
↓
Streamlit: px.bar(x=index, y=values)
```

### 파이차트 (TODO 8)
```
Jupyter: plt.pie(values, labels=names)
↓
Streamlit: px.pie(values=values, names=names)
```

### 인터랙티브 필터 (TODO 10-12) 🆕
```
sidebar.multiselect() → 다중선택
sidebar.slider() → 범위선택
sidebar.text_input() → 검색
```

---

## ✨ 완료 기준

- ✅ **필수**: TODO 1-6 (기본 + 2개 그래프)
- ✅ **권장**: TODO 1-8 (3개 그래프 전부)
- ✅ **완벽**: TODO 1-13 + 배포 완료 (인터랙티브 대시보드) 🆕

---

## 🔍 검증 체크리스트

모든 TODO를 완성하면 다음을 확인하세요:

**기본 기능 (TODO 1-9)**
- [ ] Streamlit 앱이 오류 없이 실행됨
- [ ] 제목이 대시보드에 표시됨
- [ ] 데이터프레임 미리보기가 표시됨 (10개 행)
- [ ] 3개 탭이 모두 보임 (📊 기본 분석, 🎬 콘텐츠 유형, 💡 인사이트)
- [ ] 제목 길이 히스토그램이 표시됨
- [ ] 연대별 막대그래프가 표시됨
- [ ] Movie vs TV Show 파이차트가 표시됨
- [ ] 인사이트 텍스트 입력창이 작동함

**인터랙티브 기능 (TODO 10-13)** 🆕
- [ ] 사이드바에 필터 3종이 표시됨 (콘텐츠 유형, 연도, 검색)
- [ ] 콘텐츠 유형 선택 시 그래프가 실시간 변경됨
- [ ] 연도 슬라이더 조정 시 데이터가 필터링됨
- [ ] 제목 검색 시 해당 콘텐츠만 표시됨
- [ ] 필터 결과 개수가 표시됨
- [ ] 상위 N개 국가 슬라이더가 작동함
- [ ] 국가별 가로 막대그래프가 표시됨

---

## 🚀 제출 방법

1. **app.py 저장**
   ```bash
   git add app.py
   git commit -m "Complete all TODO tasks"
   ```

2. **GitHub 푸시**
   ```bash
   git push origin main
   ```

3. **Streamlit Cloud 배포**
   - https://share.streamlit.io 접속
   - GitHub 연동
   - `app.py` 파일 선택

4. **배포 링크 제출**

---

## 🎯 학습 목표 달성 확인

이 과제를 완료하면 다음을 학습하게 됩니다:

✅ Pandas로 데이터 다루기  
✅ matplotlib/Plotly로 시각화하기  
✅ Streamlit 앱 만들기  
✅ 인터랙티브 대시보드 설계 🆕  
✅ 사용자 입력과 필터링 구현 🆕  
✅ 배포 및 공유  

**축하합니다! 당신은 이제 데이터 분석가입니다!** 🎉

---

## 🎁 보너스 챌린지 (선택)

시간이 남으면 다음을 시도해보세요:

1. **새로운 그래프 추가**: rating, duration 등 다른 컬럼 시각화
2. **색상 테마 변경**: Netflix 빨강 → 다른 브랜드 색상
3. **더 많은 필터**: 국가별 필터, rating 필터 추가
4. **통계 지표 추가**: 평균 제목 길이, 최다 제작 국가 등

---

## 📚 참고 자료

- [Streamlit 공식 문서](https://docs.streamlit.io)
- [Plotly Express 차트 예제](https://plotly.com/python/plotly-express/)
- [Pandas 치트시트](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
