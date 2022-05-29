# Import the necessary packages
import requests  # pip install requests


class TranslateApi:

    # The default URL that we use to make requests for translations
    DEFAULT_URL = "https://libretranslate.de/"

    def __init__(self, url=None, api_key=None):
        """__init__(self, url=None, api_key=None) -> TranslateApi()
            TranslateApi constructor
            If no url attribute is supplied then the DEFAULT_URL will be used.
        """
        if url is not None:
            # Tests if the url has a trailing '/' character otherwise it's added
            self.url = url + '/' if len(url) > 0 and url[-1] != '/' else url
        else:
            self.url = TranslateApi.DEFAULT_URL
        self.api_key = api_key

    def test_url(self, url=None):
        """test_url(self, url=None)
            Tests url availability
            Returns '200' if it is available
            or 'NA' otherwise
        """
        try:
            if url is None:
                return requests.get(self.url).status_code
            else:

                return requests.get(url).status_code
        except Exception:
            return "NA"

    def translate(self, q: str, source="auto", target="en"):
        """translate(self, q: str, source="en", target="en") -> str
            Translates a string of text. If no languages are specified,
            the source language and target language will be english
            and german.
        """

        # If source language is not supplied
        if source == "auto":
            # Detects the language
            source = self.detect_lang(q, "en")
        url = self.url + 'translate'
        data = {"q": q, "source": source, "target": target,
                "format": "text"}
        if self.api_key is not None:
            data["api_key"] = self.api_key
        request = requests.post(url, data=data)
        translation = request.json()["translatedText"]
        return translation

    def detect_lang(self, q: str, target="en"):
        """detect_lang(self, q: str, target="en") -> str
                Returns the language detected in the text supplied.
        """
        url = self.url + 'translate'
        data = {"q": q, "source": "auto", "target": target}

        if self.api_key is not None:
            data["api_key"] = self.api_key
        request = requests.post(url, data=data)
        return request.json()['detectedLanguage']['language']

    def supported_languages(self):
        """supported_languages(self) -> list()
            Returns the supported languages
        """
        url = self.url + 'languages'
        request = requests.get(url)
        return request.json()


if __name__ == "__main__":
    pass
