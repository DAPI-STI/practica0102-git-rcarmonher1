from src.strings import shout

def test_shout_basico():
    assert shout("hola") == "HOLA"

def test_shout_mantiene_espacios():
    assert shout("hola mundo") == "HOLA MUNDO"

def test_shout_texto_ya_en_mayus():
    assert shout("REDES") == "REDES"
