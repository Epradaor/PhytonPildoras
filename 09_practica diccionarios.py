midiccionario={"Alemania":"Berlín", "Francia":"París","Reino Unido":"Londres", "España":"Madrid"}
print(midiccionario["Francia"])
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)
midiccionario2={"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(midiccionario2)
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario = {mitupla[0]: "Madrid",
                 mitupla[1]: "París", mitupla[2]: "Londres", mitupla[3]: "Berlín"}
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))
print(midiccionario)
