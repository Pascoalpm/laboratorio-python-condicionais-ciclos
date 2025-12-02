import math

# Точность вычислений
EPS = 1e-10

if __name__ == "__main__":
    x = float(input("Value of x? "))

    # a0 = x / ((2*0+1)*(2*0+1)!) = x / (1*1) = x
    a = x
    S = a
    n = 0

    while abs(a) > EPS:
        # Формула из третьей картинки:
        # a_{n+1} = a_n * x^2 / ( (2n+3)^2 * (2n+2) )
        a = a * ((x*x)*(2*n+1)) / ( (2*n + 3)*(2*n + 3) * (2*n + 2) )
        S += a
        n += 1

    print(f"Shi({x}) = {S:.12f}")