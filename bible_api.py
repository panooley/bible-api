import requests
from enum import Enum

API_URL = "https://bible-api.com/"

class BibleType(Enum):
    CHEROKEE_NT = "cherokee"
    KRALICKA = "bkr"
    ASV_1901 = "asv"
    BASIC_ENGLISH = "bbe"
    DARBY = "darby"
    DOUAY_RHEIMS_1899 = "dra"
    KJV = "kjv"
    WEB = "web"
    YOUNGS_LITERAL = "ylt"
    OEB_CW = "oeb-cw"
    OEB_US = "oeb-us"
    WEB_BRITISH = "webbe"
    LATIN_VULGATE = "clementine"
    ALMEIDA = "almeida"
    CORNILESCU = "rccv"

class BibleReader:
    def __init__(self, translation: BibleType = BibleType.WEB):
        self.translation = translation
    
    def fetch_data(self, reference: str):
        try:
            url = API_URL + reference + f"?translation={self.translation.value}"
            res = requests.get(url)
            if res.status_code == 200:
                return res.json().get("text", "No text found").strip()
            else:
                return f"Error {res.status_code}: Unable to fetch verse. Check input or server."
        except requests.RequestException as e:
            return f"Request failed: {e}"

    def get_verse(self, book: str, chapter: int, verse: int):
        ref = f"{book} {chapter}:{verse}"
        return self.fetch_data(ref)

    def get_verse_range(self, book: str, chapter: int, verse_start: int, verse_end: int):
        if verse_start > verse_end:
            raise BaseException("verse_start cannot be greater than verse_end")
        ref = f"{book} {chapter}:{verse_start}-{verse_end}"
        return self.fetch_data(ref)