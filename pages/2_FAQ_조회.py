import streamlit as st

from data.faq_sample import load_faq_data


st.set_page_config(page_title="FAQ 조회", page_icon="?", layout="wide")

st.title("FAQ 조회")

df = load_faq_data()

COLUMN_LABELS = {
    "company": "회사",
    "category": "카테고리",
    "question": "질문",
    "answer": "답변",
}

companies = ["전체"] + sorted(df["company"].unique())
categories = ["전체"] + sorted(df["category"].unique())

selected_company = st.sidebar.selectbox("회사", companies)
selected_category = st.sidebar.selectbox("카테고리", categories)
keyword = st.sidebar.text_input("질문/답변 검색어")

filtered = df.copy()

if selected_company != "전체":
    filtered = filtered[filtered["company"] == selected_company]

if selected_category != "전체":
    filtered = filtered[filtered["category"] == selected_category]

if keyword:
    filtered = filtered[
        filtered["question"].str.contains(keyword, case=False, na=False)
        | filtered["answer"].str.contains(keyword, case=False, na=False)
    ]

st.metric("검색 결과", f"{len(filtered)}건")

if filtered.empty:
    st.warning("검색 조건에 해당하는 FAQ가 없습니다.")
    st.stop()

for row in filtered.itertuples(index=False):
    with st.expander(f"[{row.company} / {row.category}] {row.question}"):
        st.write(row.answer)

st.divider()
st.dataframe(
    filtered.rename(columns=COLUMN_LABELS),
    use_container_width=True,
    hide_index=True,
)
