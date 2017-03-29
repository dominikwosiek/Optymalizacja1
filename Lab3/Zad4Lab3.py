import numpy
import itertools


# wybor kolumny z macierzy
def get_column(array, col_idx):
    return array[:, [col_idx]]


# dodanie kolumny na koniec macierzy
def append_column(array, column):
    if array is None:
        return column
    else:
        return numpy.append(array, column, 1)


# wybor wszystkich mozliwych kolumn, z ktorych stworzymy macierz kwadratowa
def get_possible_columns(n, m):
    for columns in itertools.permutations(range(m + n), m):
        if columns == tuple(sorted(columns)):
            yield columns


#sprawdzenie, czy wszystkie wpolrzedne sa nieujemne
def is_non_negative(v):
    is_non_negative = True
    for i in v:
        if i <= 0:
            is_non_negative = False
    return is_non_negative


print 'UWAGA: Program zaklada, ze:'
print '1. Wprowadzany problem jest juz w postaci normalnej (ograniczenia maja postac Ax<=b, zas x>=0);'
print '2. Przestrzen, na ktorej badamy funkcje jest ograniczonym wieloscianem;'
print '3. Podana funkcje MAKSYMALIZUJEMY (jesli chcemy minimalizowac, nalezy wpisac wspolczynniki o przeciwnych znakach)'
print '4. Program podaje jedno rozwiazanie, nie wszystkie'

liczba_zmiennych = int(raw_input('Podaj liczbe zmiennych: '))

c = []

#tworzenie funkcji, ktora chcemy zamksymalizowac
for i in range(liczba_zmiennych):
    c.append(float(raw_input('Podaj wspolczynnik przy x' + str(i + 1) + ': ')))

# zakladam ze ograniczenia maja zawsze postac ax1+bx2...<=k i x1,x2...>=0
liczba_ograniczen = int(raw_input('Podaj liczbe ograniczen: '))

A = []
b = []

#tworzenie ograniczen (rowniez macierzy A oraz wektorow b i c)
for i in range(liczba_ograniczen):
    print 'ograniczenie', i + 1
    a = []
    for j in range(liczba_zmiennych):
        a.append(float(raw_input('Podaj wspolczynnik przy x' + str(j + 1) + ': ')))
    b.append(float(raw_input('Podaj liczbe po prawej stronie nierownosci: ')))
    for j in range(liczba_ograniczen):
        if i == j:
            a.append(1.0)
        else:
            a.append(0.0)
    A.append(a)
    c.append(0.0)

A = numpy.array(A)
b = numpy.array(b)
c = numpy.array(c)

maxV = float('-inf')
maxX = []
for columns in get_possible_columns(liczba_zmiennych, liczba_ograniczen):
    a = None
    for i in columns:
        a = append_column(a, get_column(A, i))
    if numpy.linalg.det(a) != 0.0:
        v = numpy.linalg.inv(a).dot(b)
        if is_non_negative(v):
            V = [0] * (liczba_zmiennych + liczba_ograniczen)
            j = 0
            for i in columns:
                V[i] = v[j]
                j += 1
            if c.dot(V) >= maxV:
                maxV = c.dot(V)
                maxX = V[:liczba_zmiennych]

if maxX == []:
    print 'Nie istnieja nieujemne wartosci zmiennych, bedace rozwiazaniem problemu.'
else:
    print ('Funkcja przyjmuje maksimum w punkcie: ' + str(maxX))
print ('Maksimum funkcji wynosi ' + str(maxV))
