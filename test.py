G = {"a": ["c"],
     "b": ["c", "e"],
     "c": ["a", "b", "d", "e"],
     "d": ["c"],
     "e": ["c", "b"],
     "f": []
     }

if __name__ == "__main__":
    keys = list(G.keys())
    values = list(G.values())
    for i in keys:
        print(f"Entrada: {i} y G Salida: {len(G[i])} ")

