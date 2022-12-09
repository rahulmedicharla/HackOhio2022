from Parser import TextToCode, CodeToText
from PyObjects import PyObjects, MyDict


def test():
    # tokens = ["while", "a", "<", "4"]
    # tokens2 = ["variable", "a", "=", "1"]
    # tokens3 = ["if", "x", ">", "5"]
    # tokens4 = ["call", "print", "x"]
    # tokens5 = ["for", "1", "until", "5"]
    # tokens6 = ["statement", "a", "+=", "1"]
    # tokens7 = ["close"]
    # tokens8 = ["close"]
    # tokens9 = ["close"]

    tokens = ["variable", "b", "=", "2"]
    tokens2 = ["function", "main", "x"]
    tokens3 = ["for", "i", "from", "2", "until", "5"]
    tokens4 = ["for", "j", "from", "5", "until", "10"]
    tokens5 = ["close"]
    tokens6 = ["close"]
    tokens7 = ["call", "print", "x"]
    tokens8 = ["close"]
    tokens9 = ["call", "main", "b"]

    code = MyDict()
    text = MyDict()

    TextToCode.parse(tokens, code, code.append)
    TextToCode.parse(tokens2, code, code.append)
    TextToCode.parse(tokens3, code, code.append)
    TextToCode.parse(tokens4, code, code.append)
    TextToCode.parse(tokens5, code, code.append)
    TextToCode.parse(tokens6, code, code.append)
    TextToCode.parse(tokens7, code, code.append)
    TextToCode.parse(tokens8, code, code.append)
    TextToCode.parse(tokens9, code, code.append)

    CodeToText.parse(code.scope, text, text.append)

    for key, value in text.items():
        print(f'{key}   {value}')


test()
