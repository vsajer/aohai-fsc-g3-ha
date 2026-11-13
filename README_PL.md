# AOHAI FSC-G3 Modbus dla Home Assistant

Eksperymentalna integracja HACS dla AOHAI FSC-8/10/12K1P-BL-G3, oparta na projekcie [SANDISOLAR HA](https://github.com/vsajer/sandisolar-ha). Protokół Modbus RTU V2.14 został udostępniony przez producenta.

**Integracja nie została jeszcze przetestowana na rzeczywistym falowniku.** Różnice pomiędzy modelami i wersjami oprogramowania wymagają sprawdzenia przez testerów.

## Instalacja

1. W HACS → Integracje → Własne repozytoria dodaj `https://github.com/vsajer/aohai-fsc-g3-ha`, kategoria Integration.
2. Zainstaluj wybraną wersję, uruchom ponownie Home Assistant i dodaj integrację AOHAI FSC-G3 Modbus.
3. Wybierz port szeregowy i ustaw szybkość oraz adres zgodnie z urządzeniem. Domyślnie: 9600 baud, 8N1, adres 1.

Integracja używa szeregowego Modbus RTU. Połączenie ESPHome z UART oryginalnego modułu Wi-Fi nie jest częścią tej integracji. Nie podłączaj równocześnie dwóch urządzeń nadrzędnych do tej samej magistrali.

## Testowanie

Przy pierwszym dodaniu encje zapisujące ustawienia są domyślnie wyłączone. Przed włączeniem i zmianą wartości porównaj jednostki, zakres i funkcję z wyświetlaczem oraz dokumentacją falownika. Zapisz pierwotne ustawienia. Nie używaj niezweryfikowanych wartości w automatyzacjach.

Zapis do rejestrów 218, 220 i 226 jest zablokowany do czasu dalszej weryfikacji. Według protokołu 218 oznacza moc wejściową generatora, 220 napięcie włączenia SecEPS dla akumulatora ołowiowego; 226 nie został opisany w dostarczonej tabeli. Znaczenie mocy „AC Power To User” i znaków przepływu należy zweryfikować.

Protokół wymaga co najmniej 850 ms między poleceniami. Odczyt wielu rejestrów osobno może trwać dłużej niż wybrany interwał aktualizacji.

## Zgłoszenie wyników

W zgłoszeniu podaj model, wersje firmware, Home Assistant i integracji, sposób połączenia, szybkość, ID, logi bez haseł oraz porównanie wartości z wyświetlaczem. Podaj również jednostki i warunki pracy. Testy zapisu wykonuj dopiero po potwierdzeniu znaczenia ustawienia.

## Licencja

MIT, zobacz [LICENSE](LICENSE).
