# Даны вещественные положительные числа a, b, c, d. Выясните, может ли прямоугольник со сторонами a,b
# уместиться внутри прямоугольника со сторонами c,d так, чтобы каждая сторона внутреннего прямоугольника
# была параллельна или перпендикулярна стороне внешнего прямоугольника.
import sys
a = int(input("Введите сторуну а прямоугольника "))
b = int(input("Введите сторуну b прямоугольника "))
c = int(input("Введите сторуну c прямоугольника "))
d = int(input("Введите сторуну d прямоугольника "))

if a < 0 or b < 0 or c < 0 or d < 0:
    print("Сторона прямоугольника не может быть отрицательной, проверьте данные")
    sys.exit(0)

if ((a < c and b < d)
    or (a < d and b < c)):
    print("Прямоугольник ", a, b, "сможет уместиться внутри прямоугольника (",c," ",d,")")
else:
    print("Прямоугольник ", a, b, "НЕ сможет уместиться внутри прямоугольника (",c," ",d,")")
# Считая, что прямоугольник уместится, только если одна из сторон строго больше. Например прямоугольник со сторонами 2, 3 не вместится в прямоугольник 2,4 так как одна из сторон будет равна.




