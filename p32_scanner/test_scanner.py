from scanner import Scanner

TOKENS = [ ("^def",                         "DEF" ),
           ("^[a-zA-Z_][a-zA-Z0-9_]*",      "NAME"),
            ("^[0-9]+",                     "INTEGER"),
            ("^\(",                     "LPAREN"),
            ("^\)",                     "RPAREN"),
            ("^[a-zA-Z0-9_][a-zA-Z0-9_]*",      "PARAM"),
            ("^\+",                     "PLUS"),
            ("^:",                      "COLON"),
            ("^,",                      "COMMA"),
            ("^\s+",                    "INDENT")
           ]


def test_01():
    scanner = Scanner(TOKENS)

    line = 'def hellow(x, y):'
    #line = input ()
    token_n = scanner.scan(line)

    assert (token_n > 0)
