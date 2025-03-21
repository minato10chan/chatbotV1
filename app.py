import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import sqlite3

# sqlite3のバージョンを確認
if sqlite3.sqlite_version_info < (3, 35, 0):
    raise RuntimeError("Your system has an unsupported version of sqlite3. Chroma requires sqlite3 >= 3.35.0.")

from chromadb import ChromaDB
import openai
import os

# OpenAI APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# LangChainとChromaDBの初期化
vectorizer = TfidfVectorizer()
chromadb = ChromaDB()

# アップロードされたテキストファイルを処理する関数
def process_uploaded_file(uploaded_file):
    text = uploaded_file.read().decode("utf-8")
    vectors = vectorizer.fit_transform([text]).toarray()
    chromadb.save_vectors(vectors)
    return text

# StreamlitアプリケーションのUI
st.title("LangChain Chatbot")
uploaded_file = st.file_uploader("テキストファイルをアップロードしてください", type=["txt"])

if uploaded_file is not None:
    text = process_uploaded_file(uploaded_file)
    st.write("アップロードされたテキスト:")
    st.write(text)

    # チャットボットの応答を生成する関数
    def generate_response(query):
        results = chromadb.query(query)
        response = "応答生成機能は未実装です"  # 応答生成機能の仮実装
        return response

    query = st.text_input("質問を入力してください")
    if query:
        response = generate_response(query)
        st.write("チャットボットの応答:")
        st.write(response)

# ログ管理
if "logs" not in st.session_state:
    st.session_state["logs"] = []

if query and response:
    st.session_state["logs"].append({"query": query, "response": response})

st.write("ログ:")
st.write(st.session_state["logs"])

# デバッグ用のprint文
print("アップロードされたテキスト:", text if uploaded_file else "なし")
print("質問:", query if query else "なし")
print("応答:", response if query else "なし")
