import nltk

nltk.data.path.append("/usr/local/share/nltk_data")
nltk.download("punkt", download_dir="usr/local/share/nltk_data")
nltk.download("punkt_tab", download_dir="/usr/local/share/nltk_data")
nltk.download(
    "averaged_perceptron_tagger_eng", download_dir="/usr/local/share/nltk_data"
)
nltk.download("wordnet", download_dir="/usr/local/share/nltk_data")
nltk.download("stopwords", download_dir="/usr/local/share/nltk_data")
