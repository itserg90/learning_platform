from rest_framework.exceptions import ValidationError


class URLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, url):
        url = url.get("url")
        if url:
            if not url.startswith("https://youtube.com"):
                raise ValidationError("URL должен начинаться с 'https://youtube.com'")
            return url
