from datetime import date
import datetime

# lista klientów i samochodów
klienci = [
    {'id': 1, 'imie_nazwisko': 'Jan Nowak', 'data_prawa_jazdy': date(2021, 3, 4)},
    {'id': 2, 'imie_nazwisko': 'Agnieszka Kowalska', 'data_prawa_jazdy': date(1999, 1, 15)},
    {'id': 3, 'imie_nazwisko': 'Robert Lewandowski', 'data_prawa_jazdy': date(2010, 12, 18)},
    {'id': 4, 'imie_nazwisko': 'Zofia Plucińska', 'data_prawa_jazdy': date(2020, 4, 29)},
    {'id': 5, 'imie_nazwisko': 'Grzegorz Braun', 'data_prawa_jazdy': date(2015, 7, 12)}
]

samochody = [
    {'id': 1, 'marka': 'Škoda Citigo', 'segment': 'mini', 'rodzaj_paliwa': 'benzyna', 'cena_za_dobe': 70, 'status': 'dostępny'},
    {'id': 2, 'marka': 'Toyota Aygo', 'segment': 'mini', 'rodzaj_paliwa': 'benzyna', 'cena_za_dobe': 90, 'status': 'dostępny'},
    {'id': 3, 'marka': 'Fiat 500', 'segment': 'mini', 'rodzaj_paliwa': 'elektryczny', 'cena_za_dobe': 110, 'status': 'dostępny'},
    {'id': 4, 'marka': 'Ford Focus', 'segment': 'kompakt', 'rodzaj_paliwa': 'diesel', 'cena_za_dobe': 160, 'status': 'dostępny'},
    {'id': 5, 'marka': 'Kia Ceed', 'segment': 'kompakt', 'rodzaj_paliwa': 'benzyna', 'cena_za_dobe': 150, 'status': 'dostępny'},
    {'id': 6, 'marka': 'Volkswagen Golf', 'segment': 'kompakt', 'rodzaj_paliwa': 'benzyna', 'cena_za_dobe': 160, 'status': 'dostępny'},
    {'id': 7, 'marka': 'Hyundai Kona Electric', 'segment': 'kompakt', 'rodzaj_paliwa': 'elektryczny', 'cena_za_dobe': 180, 'status': 'dostępny'},
    {'id': 8, 'marka': 'Audi A6 Allroad', 'segment': 'premium', 'rodzaj_paliwa': 'diesel', 'cena_za_dobe': 290, 'status': 'dostępny'},
    {'id': 9, 'marka': 'Mercedes E270 AMG', 'segment': 'premium', 'rodzaj_paliwa': 'benzyna', 'cena_za_dobe': 320, 'status': 'dostępny'},
    {'id': 10, 'marka': 'Tesla Model S', 'segment': 'premium', 'rodzaj_paliwa': 'elektryczny', 'cena_za_dobe': 350, 'status': 'dostępny'}
]

def wyswietl_liste_klientow_i_samochodow():
    print('ID | Imę i Nazwisko | Data wydania prawa jazdy:')
    for klient in klienci:
        print(f"{klient['id']}: {klient['imie_nazwisko']} | {klient['data_prawa_jazdy']}")

    print('ID | Model | Segment | Rodzaj paliwa | Cena za dobę:')
    for samochod in samochody:
        print(f"{samochod['id']}: {samochod['marka']} | {samochod['segment']} | {samochod['rodzaj_paliwa']} | {samochod['cena_za_dobe']} PLN")


# minimalny czas posiadania prawa jazdy dla każdego segmentu samochodu w latach
samochod_minimalny_czas_prawa_jazdy = {
    'mini': 1,
    'kompakt': 3,
    'premium': 5
}

#wypożyczenie samochodu

def wypozycz_samochod():
    klient_id = int(input('Podaj ID klienta: '))
    samochod_id = int(input('Podaj ID samochodu: '))
    # wybór daty wypożyczenia i liczby dni
    ilosc_dni = int(input('Podaj liczbę dni wypożyczenia: '))

    for i in range(len(klienci)):
        if klienci[i]['id'] == klient_id:
            wybrany_klient = klienci[i]

    for i in range(len(samochody)):
        if samochody[i]['id'] == samochod_id:
            wybrany_samochod = samochody[i]


    # sprawdzanie czy samochód jest dostępny
    if wybrany_samochod['status'] != 'dostępny':
        print(f'Samochód o ID {samochod_id} jest niedostępny.')
        return


    # wybór daty wypożyczenia i liczby dni
    data_wypozyczenia = datetime.datetime.now().date()
    minimalny_czas_prawa_jazdy = samochod_minimalny_czas_prawa_jazdy.get(wybrany_samochod['segment'])

    if (data_wypozyczenia - wybrany_klient['data_prawa_jazdy']).days < minimalny_czas_prawa_jazdy * 365:
        print()

    # obliczanie kosztu wypożyczenia
    cena = wybrany_samochod['cena_za_dobe'] * ilosc_dni
    if (data_wypozyczenia + datetime.timedelta(days=ilosc_dni)) - data_wypozyczenia > datetime.timedelta(days=30):
        cena -= 3 * wybrany_samochod['cena_za_dobe']
    elif ilosc_dni > 7:
        cena -= wybrany_samochod['cena_za_dobe']

    if (data_wypozyczenia - wybrany_klient['data_prawa_jazdy']).days < 4 * 365 and wybrany_samochod['segment'] == 'premium':
        cena *= 1.2

    # wypożyczenie samochodu
    wybrany_samochod['status'] = 'niedostępny'
    wypozyczenie = {
        'klient': wybrany_klient,
        'samochod': wybrany_samochod,
        'ilosc_dni': ilosc_dni,
        'koszt': cena
    }
    
    print(f'Koszt wypożyczenia samochodu to: {cena} zł')
 
    
    
           
# pętla do wyświetlania menu i wywołania odpowiedniej funkcji
while True:
    print("WYBIERZ OPCJĘ:")
    print("1 => LISTA KLIENTÓW I SAMOCHODÓW")
    print("2 => WYPOŻYCZENIE SAMOCHODU")
    print("3 => ZAKOŃCZ PROGRAM")
    wybor = input("WYBIERZ 1, 2 LUB 3: ")

    if wybor == "1":
        wyswietl_liste_klientow_i_samochodow()
    elif wybor == "2":
        wypozycz_samochod()
    elif wybor == "3":
        print("Dziękujemy za skorzystanie z programu!")
        break
    else:
        print("Błędny wybór. Wybierz 1, 2 lub 3.")


