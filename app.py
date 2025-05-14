
import streamlit as st
import pandas as pd

# Đọc dữ liệu câu hỏi - trả lời
@st.cache_data
def load_data():
    df = pd.read_excel("Mau_CauHoi_CauTraLoi_PCCC.xlsx")
    return df

def find_best_match(user_input, data):
    # Tìm câu hỏi chứa nhiều từ khóa nhất so với input
    scores = []
    for idx, row in data.iterrows():
        question = row["Câu hỏi"].lower()
        match_score = sum([1 for word in user_input.lower().split() if word in question])
        scores.append(match_score)
    best_idx = scores.index(max(scores))
    return data.iloc[best_idx]["Câu trả lời"], data.iloc[best_idx]["Nguồn"]

def main():
    st.title("🤖 Chatbot AI PCCC & CNCH")
    st.write("Hỏi tôi về Phòng cháy chữa cháy và Cứu nạn cứu hộ!")

    data = load_data()

    user_input = st.text_input("Nhập câu hỏi của bạn:")

    if user_input:
        answer, source = find_best_match(user_input, data)
        st.success(f"**Trả lời:** {answer}")
        st.caption(f"Nguồn: {source}")

if __name__ == "__main__":
    main()
