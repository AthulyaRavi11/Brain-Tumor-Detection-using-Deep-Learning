import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Medical News", layout="wide")

# ---------------- CONFIG ----------------
API_KEY = "10007eae8ebf4fb8b72c41eb5ef49063"
QUERY = "brain tumor OR MRI OR artificial intelligence healthcare"
PAGE_SIZE = 8

# ---------------- UI ----------------
st.title("📰 Latest Medical & AI News")
st.markdown("""
Real-time news articles related to **brain tumors, medical imaging,
and artificial intelligence in healthcare**.
""")

st.markdown("---")

# ---------------- FETCH NEWS ----------------
@st.cache_data(ttl=600)
def fetch_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": QUERY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": PAGE_SIZE,
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

data = fetch_news()

# ---------------- DISPLAY ----------------
if data.get("status") != "ok":
    st.error("Unable to fetch news articles. Please check your API key.")
else:
    articles = data.get("articles", [])

    if not articles:
        st.warning("No recent articles found.")
    else:
        for article in articles:
            with st.container():
                st.subheader(article["title"])

                published = article.get("publishedAt", "")
                if published:
                    published = datetime.fromisoformat(
                        published.replace("Z", "")
                    ).strftime("%d %b %Y, %H:%M")

                st.caption(f"🕒 {published} | 📰 {article.get('source', {}).get('name', '')}")

                if article.get("description"):
                    st.write(article["description"])

                if article.get("url"):
                    st.markdown(
                        f"[🔗 Read full article]({article['url']})"
                    )

                st.markdown("---")

st.info("News is fetched live and refreshed every 10 minutes.")
