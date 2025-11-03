
# AI-RAG Chatbot

## Projenin Amacı
Bu proje, Wikipedia AI Glossary veri setini kullanarak bir Retrieval-Augmented Generation (RAG) Chatbot geliştirmeyi amaçlamaktadır. Chatbot, kullanıcıların AI ve makine öğrenmesi ile ilgili terimleri doğal dilde sorabilmesini sağlar. Veri setindeki en ilgili bilgiler önce seçilir ve ardından doğal dil modeli ile anlamlı yanıtlar üretilir. Böylece hem doğru hem de anlaşılır bilgi sunulur ve AI terimlerini öğrenmek isteyenler için etkileşimli bir eğitim aracı oluşturulur.

## Geliştirme Ortamı
**Github:** AI-RAG Chatbot

**Programlama Dili:** Python 3.x

**Kütüphaneler:** streamlit, pandas, sentence-transformers, chromadb, transformers, openai, vb.

**Sanal Ortam:** rag_env (virtualenv)

## Veri Seti
**Kullanılan veri seti:** [Wikipedia AI Glossary](https://www.kaggle.com/datasets/antoinebourgois2/wikipedia-ai-glossary)  
**İçerik:** Yapay zekâ ile ilgili terimlerin açıklamaları
**Not:** Veri seti GitHub reposuna dahil edilmez, Kaggle API üzerinden indirilir

**Toplama/Hazırlama:** Hazır veri seti kullanılmıştır; ek veri toplama veya temizleme yapılmamıştır.

**Kullanım:** Uygulama çalıştırılırken Kaggle API üzerinden indirilir, GitHub reposuna eklenmez.

## Kullanılan Yöntemler
- **Embedding Oluşturma:** Wikipedia AI Glossary’den alınan metinler vektör uzayına dönüştürülür.
  
- **Retrieval (Sorgulama) Mekanizması:** Kullanıcının sorusu embedding’e dönüştürülür ve veri setindeki en benzer terimler bulunur.
  
- **OpenAI API ile Yanıt Üretme:** Seçilen terim açıklamaları kullanılarak doğal dil yanıtı üretilir.
  
- **Streamlit Kullanımı:** Chatbot arayüzü Streamlit ile hazırlanmıştır.  

## Çözüm Mimarisi
Problem: Kullanıcının AI ile ilgili teknik terim sorularına doğal dilde doğru yanıt vermek.

**Mimari:**

**Embedding Oluşturma:** Wikipedia AI Glossary metinleri embedding’e dönüştürülür.

**Retrieval (Sorgulama):** Kullanıcının sorusu embedding’e dönüştürülür ve veri setindeki en benzer terimler seçilir.

**Yanıt Üretme:** OpenAI API kullanılarak doğal dil yanıtı oluşturulur.

**Web Arayüzü:** Streamlit ile kullanıcı etkileşimi sağlanır.

## Elde Edilen Sonuçlar
- Kullanıcı sorularına doğru ve anlamlı yanıtlar üretebilen bir chatbot oluşturulmuştur.  
- Teknik terimler ve AI ile ilgili kavramlar hakkında bilgi sunabilmektedir.  
- Uygulama hem yerel ortamda hem de internette Streamlit üzerinden çalıştırılabilir.


## Canlı Web Uygulaması
[AI-RAG Chatbot Web](https://ai-rag-chatbot-yusraazrademirel.streamlit.app)

---

## 🖥️ Uygulama Demo


https://github.com/user-attachments/assets/438335e5-39db-4c0d-bfa1-cbaebc052469




## 🛠️ Kurulum

1. Reposu klonlayın:
```bash
git clone https://github.com/azraksk/AI-RAG-Chatbot.git
cd AI-RAG-Chatbot
```

2. Gerekli kütüphaneleri yükleyin.
```bash
pip install -r requirements.txt
```

3. Kaggle API anahtarınızı bilgisayarınıza ekleyin:
Kaggle’dan kaggle.json dosyasını indirin.
Terminalde şu komutları çalıştırın:

```bash
mkdir -p ~/.kaggle
mv ~/Desktop/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

4. Streamlit uygulamasını çalıştırın:

```bash
streamlit run app.py
```

5. Jupyter Notebook’u çalıştırmak için:

```bash
jupyter notebook
```
Notebook kernel’i rag_env olmalıdır.


📁 Dosya Yapısı:

```bash
AI-RAG-Chatbot/
├── data/
│   ├── Wikipedia_AI_Glossary.csv
│   └── wikipedia-ai-glossary.zip
├── .gitignore
├── AI-RAG-Notebook.ipynb
├── README.md
├── app.ipynb
├── app.py
└── requirements.txt
```

Notlar
Chatbot arayüzü, kullanıcı ve asistan mesajlarını balonlar içinde gösterir
Dark/Light mod desteklenir

Web Uygulaması: https://ai-rag-chatbot-yusraazrademirel.streamlit.app
