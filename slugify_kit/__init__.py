import re
import unicodedata
__version__ = "1.4.0"

def slugify(text: str, sep: str = "-", lower: bool = False) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9]+", sep, text).strip(sep)
    return text.lower() if lower else text
