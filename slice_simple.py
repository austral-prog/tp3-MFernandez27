def slice_simple(): #
    palabra = "Awesome"
    texto = palabra.lower()

    tex1 = texto[0:3]
    tex2 = texto[2:5]
    tex3 = texto[0:5]
    tex4 = tex3 + texto[-2:]

    print(tex1)
    print(tex2)
    print(tex4)

