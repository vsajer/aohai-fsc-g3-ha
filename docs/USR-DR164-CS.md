# USR-DR164: Modbus TCP přes Wi-Fi

Tato funkce je experimentální, nebyla ověřena na měniči ani převodníku. Výběr TCP je určen pro režim **Modbus TCP/RTU Protocol Conversion**, nikoliv transparentní RTU over TCP a nikoliv MQTT.

1. Napájejte převodník zdrojem 5–36 V DC podle jeho označení. Připojte RS485 A a B k odpovídajícím vývodům komunikačního portu měniče podle dokumentace konkrétního modelu a ověřte případné sdílení portu s BMS.
2. Připojte se k tovární Wi-Fi USR-DR164-xxxx, otevřete http://10.10.100.254 a přihlaste se admin/admin. Tovární údaje se mohou lišit. Změňte přístupové heslo a zabezpečte nebo po dokončení vypněte vlastní AP.
3. V Work Mode vyberte STA nebo dočasně AP+STA. V STA Setting připojte převodník k domácí Wi-Fi, uložte a restartujte. V routeru zjistěte IP adresu a ideálně rezervujte DHCP adresu.
4. V Serial Setting nastavte 9600 baud, 8 datových bitů, žádnou paritu, 1 stop bit, a ModBUS Enabled na Protocol Conversion. Jde o příklad dle protokolu V2.14; nastavení musí souhlasit s měničem.
5. V Net Setting nastavte Socket A jako TCP Server, například port 8899, Net heart OFF a Reg Set OFF. Socket B nepoužívejte. Port 8899 je příklad; v integraci nastavte stejný port jako v převodníku.
6. V Home Assistantu přidejte AOHAI FSC-G3, vyberte Wi-Fi / Ethernet (Modbus TCP), zadejte IP převodníku, TCP port a Modbus ID měniče (typicky 1). Přístup je přes místní síť, není třeba MQTT ani cloud.

Výrobce měniče uvádí odstup 850 ms mezi příkazy. Integrace tento odstup dodržuje, takže jednotlivé čtení mnoha registrů trvá déle než nastavený interval aktualizace. Nespouštějte jiný Modbus master na stejné RS485. Připojení a výsledky měření ověřte na konkrétním zařízení. Neotevírejte TCP port do internetu.

Dokumentace výrobce převodníku: https://www.pusr.com/uploads/20260108/b3e69e40904adb82d6cb31cfbebbcc36.pdf
