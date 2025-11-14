import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from transformers import pipeline

# -------------------------------
# 1️⃣ Dataset
# -------------------------------
df = pd.read_csv('./data/Wikipedia_AI_Glossary.csv')
df = df.dropna(subset=["Title", "Wikipedia_page_description"])
df["Wikipedia_page_description"] = df["Wikipedia_page_description"].apply(lambda x: x.replace("\n", " ").strip())
texts = df["Wikipedia_page_description"].tolist()

<<<<<<< HEAD
st.title("AI RAG Chatbot 🌐")
st.write("Ask questions about AI, ML, Deep Learning, or related topics.")

# -------------------------------
# 2️⃣ Embeddings
# -------------------------------
@st.cache_data
=======
# -------------------------------
# 2️⃣ Embeddings
# -------------------------------
@st.cache_data(ttl=3600)
>>>>>>> c60be98 (Update app.py, notebook, and requirements with latest changes)
def get_embeddings(texts):
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = embedder.encode(texts, show_progress_bar=True)
    return embedder, embeddings

embedder, embeddings = get_embeddings(texts)

# -------------------------------
# 3️⃣ Chroma Vector Store
# -------------------------------
@st.cache_resource
def create_vector_store(texts, embeddings):
    client = chromadb.Client(Settings(anonymized_telemetry=False))
<<<<<<< HEAD
    # Eğer koleksiyon varsa sil
=======
>>>>>>> c60be98 (Update app.py, notebook, and requirements with latest changes)
    if "ai_glossary" in [c.name for c in client.list_collections()]:
        client.delete_collection("ai_glossary")
    collection = client.create_collection("ai_glossary")
    for i, (text, emb) in enumerate(zip(texts, embeddings)):
        collection.add(documents=[text], embeddings=[emb.tolist()], ids=[str(i)])
    return collection

collection = create_vector_store(texts, embeddings)

# -------------------------------
<<<<<<< HEAD
# 4️⃣ QA Model (Tiny Flan-T5)
# -------------------------------
@st.cache_resource
def load_qa_model():
    return pipeline("text2text-generation", model="google/flan-t5-small", tokenizer="google/flan-t5-small")
=======
# 4️⃣ QA Model
# -------------------------------
@st.cache_resource
def load_qa_model():
    return pipeline("text2text-generation", model="google/flan-t5-base", tokenizer="google/flan-t5-base")
>>>>>>> c60be98 (Update app.py, notebook, and requirements with latest changes)

qa_model = load_qa_model()

# -------------------------------
# 5️⃣ RAG Query
# -------------------------------
def rag_query(question, top_k=3):
    query_vec = embedder.encode([question])
    results = collection.query(query_embeddings=query_vec.tolist(), n_results=top_k)
    top_docs = results["documents"][0]

<<<<<<< HEAD
    # Contexti birleştir ve token sınırlaması (~300 token)
    context = " ".join(top_docs)
    context = context[:3000]  # Daha uzun context

    prompt = f"""
You are an AI expert. Answer the question using the following context.
Provide a detailed explanation in 3-5 sentences.
=======
    top_docs = list(dict.fromkeys(top_docs))
    context = " ".join(top_docs)[:1200]

    prompt = f"""
You are an AI expert. Answer the question in 3-5 sentences in simple, beginner-friendly terms. 
Use the context below if needed, but do not just repeat it.
>>>>>>> c60be98 (Update app.py, notebook, and requirements with latest changes)

Context: {context}

Question: {question}
Answer:
"""
<<<<<<< HEAD
    answer = qa_model(prompt, max_new_tokens=600, do_sample=True, temperature=0.7)[0]["generated_text"]
    return answer.strip()

# -------------------------------
# 6️⃣ Streamlit UI
# -------------------------------
user_input = st.text_input("Your question:")
if user_input:
    with st.spinner("Generating answer..."):
        answer = rag_query(user_input)
    st.success(answer)
=======
    answer = qa_model(prompt, max_new_tokens=250, do_sample=False)[0]["generated_text"]
    return answer.strip()

# -------------------------------
# 6️⃣ Streamlit UI (ChatGPT tarzı sağ-sol balon)
# -------------------------------
st.set_page_config(
    page_title="AI RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Gece modu seçimi
# -------------------------------
# Streamlit'in varsayılan ayarlarını kullanarak kenar çubuğunda tema seçimi
mode = st.sidebar.selectbox("Theme", ["Light Mode", "Dark Mode"])

if mode == "Light Mode":
    user_bg = "#4facfe"
    user_color = "#fff"
    assistant_bg = "#e0e0e0"
    assistant_color = "#000"
    body_bg = "#fff"
    sidebar_bg = "#f0f2f5"
    header_footer_bg = "#ffffff"
    header_footer_color = "#000000"
    input_bg = "#fff"
    input_color = "#000"
    placeholder_color = "#888888"

else:
    user_bg = "#2a9df4"
    user_color = "#000000"
    assistant_bg = "#333"
    assistant_color = "#f0f0f0"
    body_bg = "#121212"
    sidebar_bg = "#1a1a1a"
    header_footer_bg = "#000000"
    header_footer_color = "#ffffff"
    input_bg = "#000"
    input_color = "#fff"
    placeholder_color = "#ffffff"

# --- Modern ve yumuşak görünüm için CSS ---
st.markdown(f"""
<style>

/* GENEL UYGULAMA YAPISI */
body, .css-18e3th9, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
    background-color: {body_bg} !important;
    color: {assistant_color} !important;
    font-family: 'Segoe UI', sans-serif;
}}

/* ÜST ÇUBUK */
[data-testid="stHeader"], [data-testid="stToolbar"] {{
    background-color: {header_footer_bg} !important;
    color: {header_footer_color} !important;
    box-shadow: none !important;
    border: none !important;
}}

/* SIDEBAR */
[data-testid="stSidebar"], [data-testid="stSidebarNav"], .css-1d391kg {{
    background-color: {sidebar_bg} !important;
    color: #FFFFFF !important;
}}

/* MESAJ BALONLARI */
.chat-message.user {{
    background: {user_bg};
    color: {user_color};
    padding: 10px 16px;
    border-radius: 18px 18px 0 18px;
    margin: 6px 0;
    display: inline-block;
    float: right;
    clear: both;
    max-width: 70%;
    word-wrap: break-word;
}}
.chat-message.assistant {{
    background: {assistant_bg};
    color: {assistant_color};
    padding: 10px 16px;
    border-radius: 18px 18px 18px 0;
    margin: 6px 0;
    display: inline-block;
    float: left;
    clear: both;
    max-width: 70%;
    word-wrap: break-word;
}}

/* ALT CHAT GİRİŞ BARI */
[data-testid="stBottomBlockContainer"],
[data-testid="stChatInputContainer"],
section[data-testid="stChatInput"],
div[data-testid="stChatInput"] {{
    background-color: {input_bg} !important;
    color: {input_color} !important;
    border: none !important;
    padding: 10px 20px !important;
    margin: 0 auto !important;
    border-top: 1px solid rgba(255,255,255,0.08) !important;
}}

/* INPUT ALANI (textarea) */
[data-testid="stChatInputContainer"] textarea {{
    background-color: {input_bg} !important;
    color: {input_color} !important;
    border: 1px solid #333 !important;
    border-radius: 14px !important;
    font-size: 15px !important;
    padding: 10px 14px !important;
    resize: none !important;
    height: 60px !important;
}}

[data-testid="stChatInputContainer"] textarea::placeholder {{
    color: {placeholder_color} !important;
    opacity: 0.8;
}}

/* BUTON */
div[data-testid="stChatInputContainer"] button {{
    background-color: #ff6b6b !important;
    color: #fff !important;
    border-radius: 8px !important;
    font-weight: bold;
    margin-left: 8px !important;
    transition: all 0.2s ease-in-out;
}}
div[data-testid="stChatInputContainer"] button:hover {{
    background-color: #e63946 !important;
    transform: scale(1.05);
}}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# Başlık ve açıklama
# -------------------------------
st.title("AI RAG Chatbot 🌐")
st.write("Ask questions about AI, ML, Deep Learning, or related topics.")

# -------------------------------
# Sohbet geçmişi
# -------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# Kullanıcı input
# -------------------------------
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    placeholder = st.empty()
    answer = rag_query(user_input, top_k=3)
    st.session_state.history.append({"role": "assistant", "content": answer})
    placeholder.empty()

# -------------------------------
# Sohbeti göster
# -------------------------------
for chat in st.session_state.history:
    role = chat["role"]
    content = chat["content"]
    if role == "user":
        st.markdown(f'<div class="chat-message user">{content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message assistant">{content}</div>', unsafe_allow_html=True)
>>>>>>> c60be98 (Update app.py, notebook, and requirements with latest changes)
