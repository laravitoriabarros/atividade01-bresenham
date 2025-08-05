#Aluna: Lara Vitória Silva Santos Barros

def bresenham(x0, y0, x1, y1):
    pontos = []

    dx = x1 - x0
    dy = y1 - y0

    d = 2 * dy - dx
    y = y0

    for x in range(x0, x1 + 1):
        pontos.append((x, y))

        if d > 0:
            y += 1
            d += 2 * (dy - dx)
        else:
            d += 2 * dy

    return pontos

if __name__ == "__main__":
    resultado = bresenham(1, 1, 8, 5)
    print("Pontos rasterizados:")
    for p in resultado:
        print(p)