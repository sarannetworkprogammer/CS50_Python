from twttr import shorten

def test_upper_case():
  assert shorten("SARANAEIOU") == "SRN"

def test_lower_case():
  assert shorten("Twitter") == "Twttr"

def test_mixed():
  assert shorten("What's your name?") == "Wht's yr nm?"

def test_num():
  assert shorten("CS50") == "CS50"

