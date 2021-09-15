#Zadanie 1
'''
Python jest językiem wysokopoziomowym, tzn., ze jest on czytelny i zrozumiały dla człowieka.
'''

#Zadanie 2
'''
Kontakencja to inaczej łączenie
1 + 1;  -  mozliwe
“str” + 1;  -  niemozliwe bez konwersji stringa wyrazonego liczbą na int
“str” + “ “ + “str”  -  mozliwe
'''

#Zadanie 3
'''
liczba1 = input('Podaj I składnik sumy ')
liczba2 = input('Podaj II składnik sumy ')
wynik = liczba1 + liczba2
print('Wynikiem sumy jest:', wynik)

Operacje nie są poprawne, poniewaz sklejają ze spobą podane liczby a nie dokonują działania.
'''

#Zadanie 4
'''
Nieprawidłowo nazwane zmienne to:
czy LubiPsy = False
'''

#Zadanie 5
'''
z = 5, z = -1, z = 0 - zmienna typu int
z = 0.0, z = -1.123 - zmienna typu float
z = “c”, z = ‘c’, z = “programowanie” - zmienna typu string
z = False, z = True - wartość logiczna (bool)
'''

#Zadanie 6
'''
a += 5 -> a = a + 5
a -= 5 -> a = 5 – a - niepoprawna kolejność zapisu odejmowania po znaku równości
a *= 5 -> a = 5 * a
a *= 5 -> a = a * 5
a /= 5 -> a = 5/a - niepoprawna kolejność zapisu dzielenia po znaku równości
'''

#Zadanie 7
'''
mojWzrost = 185
mojWiek = 21
print('Cześć, jestem Piotr. Mam ', mojWzrost, 'cm wzrostu i mam ', mojWiek, 'lat. Pozwól, ze obliczę twoje BMI')
waga = int(input('Podaj swoją wagę '))
wzrost = int(input('Podaj mi swój wzrost '))
bmi = waga/(wzrost**2)*10000 #nie wiem dlaczego bez pomnozenia wychodzi liczba po przecinku
print('Twoje BMI to ', bmi)
'''

#Zadanie 8
'''
(5 / 2) = 2.5 - typ float
(1 + 1) = 2
(1.0 + 1) = 2.0 - typ float
(2.0 + 2.0) = 4.0 - typ float
(“napis” + 1) = error
(“napis” + “napis”) = error
(True + True) = 2
(5 % 2) = 1
(10 % 2) = 0
(20 % 30) = 20
(100 % 3) = 1
(100 // 3) = 33
(5 // 3) = 1
(1 // 3) = 0
(3**3) = 27
(2**2) = 4
(2**0) = 1

Reszta wyników jest typu int
'''

#Zadanie 9
'''
napis = input()
napis1 = napis[-1]+napis[1:-1]+napis[0]
print(napis1)
'''

#Zadanie 10
'''
a = 5
b = 6
liczba = str(a)
liczba1 = str(b)
wynik = liczba + liczba1
print(wynik)
'''

#Zadanie 11
'''
imie1 = 'Kacper'
imie2 = 'Lucjan'
imie3 = imie1[0:3]+imie2[-3:]
print(imie3)
'''

#Zadanie 12
'''
tekst1 = tekst2[:]
Ten zapis oznacza kopię zawartości
'''

#Zadanie 13
'''
Kod ASCII jest niezbędny przy programowaniu, poniewaz jest to kod
maszynowy na który musi zostać przekonwertowane to co zapisaliśmy
w języku programowania zeby 'komputer to zrozumiał'
'''

#Zadanie 14
'''
1:
Przekształcić znak do zaszyfrowania na kod ASCII,
wykonanie jakiejś operacji arytmetycznej i powrót do pierwotnego typu

2:
Szyfrowanie za pomocą klucza

3:
Haszowanie - wykonywanie skomplikowanych obliczeń przez algorytm i zwracanie pozornie losowego ciągu znaków
'''

#Zadanie rozszerzone 1
'''
tekst = str(input('Wpisz dowolny tekst powyzej 7 znaków. '))
if len(tekst) >= 7:
 print(tekst)
 print(len(tekst))
 print(tekst[0],tekst[-1])
 print(tekst[int(len(tekst)/2) - 1:int(len(tekst)/2) + 2])
else:
 print('Zbyt krótki ciąg znaków, spróbuj jeszcze raz!')
 '''

 #Zadanie rozszerzone 2
'''
koty = int(input('Ile Ala ma kotów? '))
print('Dzisiaj Ala znalazła jeszcze 3 koty w stawie')
wynik = (f'Ala ma już {koty+3} kotów')
print(wynik)
print(wynik.split(' '))
print(f'Ala \nma \njuż \n{koty+3} \nkotów')
wynik1 = wynik.lower()
print(wynik1)
print(wynik1[0].upper() + wynik[1:])
'''

#Zadanie rozszerzone 3
'''
word = 'DOM'
word1 = (word.lower() + 'ek')
print(word1)
'''

#Zadanie rozszerzone 4
'''
dowolne = str(input('Podaj słowo: '))
zmiana = dowolne.upper()
print(zmiana)
'''

#Zadanie rozszerzone 5
'''
spacja = input('Wpisz dowolny napis z pięcioma spacjami na początku: ')
print(spacja)
print(spacja.lstrip())
'''

#Zadanie rozszerzone 6
'''
kolory = 'czarny, czerwony, zielony, granatowy, niebieski'
kolory2 = kolory.split()
print(kolory2[2])
'''


