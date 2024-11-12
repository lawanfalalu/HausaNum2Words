# test_converter.py
from HausaNum2Words import HausaNumConverter

def test_to_words():
    converter = HausaNumConverter()

    # Test integers
    assert converter.to_words(0) == "sifili", "Test failed for 0"
    assert converter.to_words(10) == "goma", "Test failed for 10"
    assert converter.to_words(123) == "ɗari ɗaya da ashirin da uku", "Test failed for 123"
    assert converter.to_words(1001) == "dubu ɗaya da ɗaya", "Test failed for 1001"

    # Test floats
    assert converter.to_words(10.5) == "goma da ɗigo biyar", "Test failed for 10.5"
    assert converter.to_words(123.45) == "ɗari ɗaya da ashirin da uku da ɗigo huɗu biyar", "Test failed for 123.45"
    assert converter.to_words(190905.5) == "dubu ɗari ɗaya da casa'in da ɗari tara da biyar da ɗigo biyar", "Test failed for 190905.5"
    assert converter.to_words(1230099.45) == "miliyan ɗaya da dubu ɗari biyu da talatin da casa'in da tara da ɗigo huɗu biyar", "Test failed for 1230099.45"

    print("All tests passed.")

if __name__ == "__main__":
    test_to_words()