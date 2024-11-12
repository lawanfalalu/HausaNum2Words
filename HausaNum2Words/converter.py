class HausaNumConverter:
    def __init__(self):
        self.alifiyya = ["", " dubu ", " miliyan ", " biliyan ", " tiriliyan ", " kwadiliyan ", " kwintilayan ", " sektiliyan ", " seftiliyan ", " oktiliyan ", " noniiliyan ", " desiliyan "]
        self.gomiya = ["", "", " ashirin", " talatin", " arba'in", " hamsin", " sittin", " saba'in", " tamanin", " casa'in"]
        self.daidai = ["", " ɗaya", " biyu", " uku", " huɗu", " biyar", " shida", " bakwai", " takwas", " tara"]
        self.sha = [" goma", " goma sha-ɗaya", " goma sha-biyu", " goma sha-uku", " goma sha-huɗu", " goma sha-biyar", " goma sha-shida", " goma sha-bakwai", " goma sha-takwas", " goma sha-tara"]

    def _convert_hundreds(self, num):
        result = ""
        remaining = num % 100
        if remaining < 10:
            result += self.daidai[remaining]
        elif remaining < 20:
            result += self.sha[int(remaining % 10)]
        else:
            connector = " da" if num % 10 > 0 else ""
            result += self.gomiya[int(remaining / 10)] + connector + self.daidai[int(remaining % 10)]

        if num >= 100:
            result = "ɗari" + self.daidai[int(num / 100)] + (" da" if remaining > 0 else "") + result
        return result

    def _convert_without_decimal(self, num):
        if num == 0:
            return "sifili"

        words = ""
        group = 0
        while num > 0:
            remainder = num % 1000
            if remainder != 0:
                part = self._convert_hundreds(remainder)
                connector = " da " if group > 0 else ""
                words = self.alifiyya[group] + part + connector + words
            group += 1
            num //= 1000
        return " ".join(words.split())
    
    def _convert_decimal(self, num):
        result = "".join("sifili" if digit == '0' else self.daidai[int(digit)] for digit in num).strip()
        return ' '.join(result.split())
    
    def to_words(self, num):
        # Check if the input is a number (int or float)
        if not isinstance(num, (int, float)):
            raise ValueError("Input must be a number (int or float).")
        
        if isinstance(num, float):
            integer_part, decimal_part = str(num).split('.')
            integer_part_words = self._convert_without_decimal(int(integer_part))
            decimal_part_words = self._convert_decimal(decimal_part)
            return f"{integer_part_words} da ɗigo {decimal_part_words}".strip()
        return self._convert_without_decimal(num).strip()
