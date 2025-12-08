import re

def clean_text(text):
    """
    Clean tweet text by removing links, mentions, and special characters.
    """

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)

    return text.strip()
