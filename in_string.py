def check_vowels(): #
    nombre = input( )
    nombremin = nombre.lower()
    verdad = "a" in nombremin
    verded = "e" in nombremin
    verdid = "i" in nombremin
    verdod = "o" in nombremin
    verdud = "u" in nombremin
    print(f"Contiene a: {verdad}")
    print(f"Contiene e: {verded}")
    print(f"Contiene i: {verdid}")
    print(f"Contiene o: {verdod}")
    print(f"Contiene u: {verdud}")
