︠db6bff5f-ad58-45b6-9b09-1605f4827f1d︠
%typeset_mode True

#Program ma za zadanie znalezc nowy wierzcholek dla metody sympleks.
#Zakladam, ze dostajemy program w postaci normalnej (w p.p. mamy algorytm z zad.4/lab.3)

#Dzialanie programu:
#1. Program otrzymuje macierz A, wektor b (ograniczenia), wektor c (funkcja celu).
#2. Program dodaje nowe zmienne, nastepnie tworzymy problem minimalizacji sumy ujemnych wartosci tych zmiennych

#Wczytanie danych

n=int(raw_input("Liczba zmiennych: "))
m=int(raw_input("Liczba ograniczen: "))
A=[]    #macierz wspolczynnikow przy zmiennych przy ograniczeniach
b=[]    #wektor ograniczen
c=[]    #wektor funkcji celu
print "Funkcja celu"

    for i in range(0,n):
        c.append(int(raw_input("Podaj wspolczynnik przy x" + str(i+1) + " ")))

    for i in range (0,m):
      z = []    #zmienna pomocnicza
          print "Ograniczenie " + str(i+1)

          for j in range(0,n):      #wczytujemy dane dla danego ograniczenia
                z.append(int(raw_input("Podaj wspolczynnik przy x" + str(j + 1) + " ")))
              b.append(int(raw_input("Podaj liczbe po prawej stronie nierownosci ")))

          for j in range(0,m):      #dodajemy po jednej zmiennej dla danego ograniczenia (dla innych kladziemy 0)
              if i==j
                  z.append(1)
              else
                  z.append(0)
      A.append(z)                  #dodajemy ograniczenie o numerze i do macierzy ograniczen
      c.append(0)                  #do funkcji celu takze dodajemy zmienne, by wymiary sie zgadzaly


c2=[]                              #nowa funkcja celu (dla zadania pomocniczego)
      for i in range (0,len(c)):
          if i<n
              c2.append(0)         #gdy zmienna nalezy do "wymiaru" zadania poczatkowego, to nowa funkcja celu sie nia nie zajmuje
          else
              c2.append(-1)        #gdy nalezy, to minimalizujemy sume tych zmiennych, czyli dodajemy do wektora -1

P=InteractiveLPProblem(A,b,c2,'x', constraint_type="==", variable_type=">=")
view(P)
D=P.standard_form()
print "Optymalne rozwiazanie to" + str(P.optimal_solution())
