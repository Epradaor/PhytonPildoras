miLista=["María", "Pepe", "Marta", "Antonio"]
miLista.append("Sandra")
miLista.insert (2,"Sandrita")
miLista.extend (["Ana", 78.35, "Calixto"])
print(miLista[0:])
print(miLista.index("Antonio"))
miLista.remove("Pepe")
print("Pepe" in miLista)
miLista.pop()
miLista2 = ["Camila", "Lucía"] * 2
miLista3 = miLista+miLista2
print(miLista3[:])
