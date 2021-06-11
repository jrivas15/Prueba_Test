G = {"a": ["c"],
     "b": ["c", "e"],
     "c": ["a", "b", "d", "e"],
     "d": ["c"],
     "e": ["c", "b"],
     "f": []
     }
def determinarAristas (entrada, grafo):
    aristas = len(grafo[entrada])
    return aristas

if __name__ == "__main__":
    print(determinarAristas("c", G))

