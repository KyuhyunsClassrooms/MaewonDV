import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# 🎬 Netflix 테마 CSS 스타일링
# =========================================

st.markdown("""
<style>
    /* 전체 배경을 Netflix 다크 모드로 */
    .stApp {
        background-color: #141414;
    }
    
    /* 메인 컨텐츠 영역 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: #141414;
    }
    
    /* 제목 스타일 - Netflix 빨간색 */
    h1 {
        color: #E50914 !important;
        font-family: 'Netflix Sans', 'Helvetica Neue', Arial, sans-serif;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* 서브 제목 - 밝은 회색 */
    h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Netflix Sans', 'Helvetica Neue', Arial, sans-serif;
        font-weight: 500;
    }
    
    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1a1a1a;
        border-radius: 5px;
        padding: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #2a2a2a;
        color: #ffffff;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #E50914 !important;
        color: white;
    }
    
    /* 사이드바 스타일 */
    section[data-testid="stSidebar"] {
        background-color: #1a1a1a;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #1a1a1a;
    }
    
    /* 사이드바 텍스트 */
    section[data-testid="stSidebar"] .element-container {
        color: #ffffff;
    }
    
    /* 데이터프레임 스타일 */
    .dataframe {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
    }
    
    /* 메트릭 카드 스타일 */
    [data-testid="stMetricValue"] {
        color: #E50914;
        font-size: 2rem;
        font-weight: 700;
    }
    
    [data-testid="stMetricLabel"] {
        color: #ffffff;
        font-weight: 500;
    }
    
    /* 일반 텍스트 */
    p, li, span {
        color: #d0d0d0 !important;
    }
    
    /* 구분선 */
    hr {
        border-color: #E50914;
        opacity: 0.3;
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #b20710;
        transform: scale(1.05);
    }
    
    /* 입력 필드 */
    .stTextInput>div>div>input {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #404040;
    }
    
    /* 슬라이더 */
    .stSlider>div>div>div>div {
        background-color: #E50914;
    }
    
    /* 멀티셀렉트 */
    .stMultiSelect>div>div>div {
        background-color: #2a2a2a;
        color: #ffffff;
    }
    
    /* Plotly 차트 배경 */
    .js-plotly-plot {
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================================
# 📊 Netflix 데이터 시각화 대시보드
# =========================================

# TODO 1: 제목을 입력하세요 ⭐
# 정답: "📊 Netflix 데이터 시각화 대시보드"
st.title("___여기에_제목_입력___")

# 사이드바 설정
st.sidebar.header("⚙️ 설정")

# TODO 2: 파일 경로를 입력하세요 ⭐
# 정답: "data/netflix_cleaned.csv"
df_original = pd.read_csv("___파일_경로___")
df = df_original.copy()

# =========================================
# 인터랙티브 필터 (TODO 10-12)
# =========================================

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 데이터 필터")

# TODO 10: 콘텐츠 유형 필터 ⭐⭐
# 정답: default=["Movie", "TV Show"]
content_type_filter = st.sidebar.multiselect(
    "콘텐츠 유형 선택",
    options=___,
    default=___
)

# TODO 11: 연도 범위 슬라이더 ⭐⭐
# 정답: int(df_original['release_year'].min()), int(df_original['release_year'].max())
year_range = st.sidebar.slider(
    "개봉 연도 범위",
    min_value=___,
    max_value=___,
    value=(___, ___)
)

# TODO 12: 제목 검색 ⭐
# 정답: st.sidebar.text_input
search_query = ___(
    "제목 검색 (Enter 후 검색)",
    value=""
)

# =========================================
# 필터 적용 (TODO 10-12 연동)
# =========================================

# 콘텐츠 유형 필터
if content_type_filter:
    df = df[df['type'].isin(content_type_filter)]

# 연도 범위 필터
df = df[(df['release_year'] >= year_range[0]) & (df['release_year'] <= year_range[1])]

# 제목 검색 필터
if search_query:
    df = df[df['title'].str.contains(search_query, case=False, na=False)]

# 필터 결과 안내
if len(df) == 0:
    st.warning("⚠️ 선택한 필터에 맞는 데이터가 없습니다. 필터를 조정해주세요.")
    st.stop()
else:
    st.info(f"🔍 필터 결과: **{len(df):,}개** 콘텐츠")

# TODO 3: df.head()에 몇 개의 행을 표시할지 입력하세요 ⭐
# 정답: df.head(10)
st.subheader("📋 데이터 미리보기")
st.dataframe(df.___)

# =========================================
# 📊 기본 통계
# =========================================

st.subheader("📊 기본 통계")
col1, col2, col3, col4 = st.columns(4)
col1.metric("총 콘텐츠 수", f"{len(df):,}")
col2.metric("영화", f"{(df['type'] == 'Movie').sum():,}")
col3.metric("TV 쇼", f"{(df['type'] == 'TV Show').sum():,}")
col4.metric("제작 국가", f"{df['country'].nunique():,}")

# =========================================
# 탭 생성 (3개 탭)
# =========================================

tab1, tab2, tab3 = st.tabs(["📊 기본 분석", "🎬 콘텐츠 유형", "💡 인사이트"])

# =========================================
# 탭 1: 기본 분석
# =========================================

with tab1:
    st.header("📊 기본 분석")
    
    # --------- TODO 4: 제목 길이 히스토그램 ---------
    st.subheader("📏 제목 길이 분포")
    
    # TODO 4: x 파라미터에 컬럼 이름을 입력하세요 ⭐⭐
    # 정답: 'title_length'
    fig = px.histogram(
        df, 
        x=___, 
        nbins=30,
        title="제목 길이 분포",
        labels={'title_length': '제목 길이 (글자 수)', 'count': '개수'},
        color_discrete_sequence=['#E50914']
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # --------- TODO 5-6: 연대별 막대그래프 ---------
    st.subheader("📅 연대별 콘텐츠 제작량")
    
    # TODO 5: 빈도수를 계산하는 메서드를 입력하세요 ⭐⭐
    # 정답: value_counts()
    decade_counts = df['decade'].___().sort_index().tail(10)
    
    # TODO 6: x, y 파라미터를 입력하세요 ⭐⭐
    # 정답: x=decade_counts.index, y=decade_counts.values
    fig = px.bar(
        ___, ___,
        title="연대별 콘텐츠 수",
        labels={'x': '연대', 'y': '콘텐츠 수'},
        color_discrete_sequence=['#E50914']
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # --------- TODO 13: 상위 N개 국가 분석 ---------
    st.subheader("🌍 국가별 콘텐츠 제작량")
    
    # TODO 13: 슬라이더로 상위 N개 선택 ⭐⭐
    # 정답: st.slider, default값은 10
    top_n = ___(
        "상위 N개 국가 선택",
        min_value=___,
        max_value=___,
        value=___
    )
    
    country_counts = df['country'].___().head(top_n)
    
    fig = px.bar(
        x=country_counts.values,
        y=country_counts.index,
        orientation='h',
        title=f"상위 {top_n}개 국가별 콘텐츠 수",
        labels={'x': '콘텐츠 수', 'y': '국가'},
        color_discrete_sequence=['#E50914']
    )
    st.plotly_chart(fig, use_container_width=True)

# =========================================
# 탭 2: 콘텐츠 유형
# =========================================

with tab2:
    st.header("🎬 콘텐츠 유형 분석")
    
    # --------- TODO 7-8: 콘텐츠 유형 파이차트 ---------
    st.subheader("Movie vs TV Show")
    
    # TODO 7: 빈도수를 계산하는 메서드를 입력하세요 ⭐⭐
    # 정답: value_counts()
    type_counts = df['type'].___()
    
    # TODO 8: values, names 파라미터를 입력하세요 ⭐⭐
    # 정답: values=type_counts.values, names=type_counts.index
    fig = px.pie(
        ___, ___,
        title="콘텐츠 유형 비율",
        color_discrete_sequence=['#E50914', '#564d4d']
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 통계 정보
    st.write(f"**영화**: {type_counts.get('Movie', 0):,}개")
    st.write(f"**TV 쇼**: {type_counts.get('TV Show', 0):,}개")

# =========================================
# 탭 3: 인사이트
# =========================================

with tab3:
    st.header("💡 나만의 인사이트")
    
    # TODO 9: 텍스트 입력 ⭐ (이미 완성 - 학습용)
    insight = st.text_area(
        "데이터에서 발견한 흥미로운 점을 작성해보세요:",
        height=150
    )
    
    if insight:
        st.success("✅ 인사이트가 저장되었습니다!")
        st.info(f"**작성한 내용**: {insight}")

# =========================================
# 푸터
# =========================================

st.markdown("---")
st.markdown("**Made with ❤️ using Streamlit & Plotly**")
