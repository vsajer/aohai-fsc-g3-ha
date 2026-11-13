# AOHAI FSC-G3 Modbus pro Home Assistant

[🇵🇱 Instrukcja po polsku](README_PL.md)

Experimentální HACS integrace pro **AOHAI FSC-8/10/12K1P-BL-G3**, odvozená z [SANDISOLAR HA](https://github.com/vsajer/sandisolar-ha). Projekt zatím nemá potvrzený test se skutečným měničem FSC-G3. Kompatibilita jednotlivých verzí a firmwarů vyžaduje zpětnou vazbu testerů.

Obsahuje senzory, výpočty, nastavení baterie, přepínače a výběry převzaté z původní integrace a další FSC-G3 registry podle veřejné [ESPHome konfigurace pro 12 kW](https://github.com/bootuz-dinamon/Sandisolar-Aohai-FSC-12K1P-BL-G3-Home-Assistant-integration-via-RS485). U činného výkonu a hodnot sítě je třeba ověřit znaménko a skutečný význam. Položky převzaté z jiného měniče nemusí odpovídat FSC-G3.

## Instalace

1. V HACS → Integrace → Vlastní repozitáře přidejte `https://github.com/vsajer/aohai-fsc-g3-ha`, kategorii Integration.
2. Nainstalujte výchozí větev, restartujte Home Assistant a přidejte **AOHAI FSC-G3 Modbus**.
3. Nastavte sériový port, baud rate a Modbus ID podle svého připojení. Výchozí hodnoty jsou 9600, 1 a 8N1.

Používá se přímé sériové Modbus RTU připojení. Připojení ESPHome k UART originálního Wi-Fi modulu je samostatné řešení, které tato integrace přímo neposkytuje. Jeden sériový port nesdílejte současně s jiným masterem.

## Testování a ovládání

**Zápisové entity jsou při prvním přidání ve výchozím stavu vypnuté.** V Home Assistantu lze jednotlivé entity zapnout pro cílené testování. Před změnou porovnejte aktuální hodnotu, jednotku, hranice a funkci s displejem a dokumentací konkrétního zařízení. Uložte si původní nastavení. Nastavení baterie, zdrojů a výstupu může ovlivnit provoz instalace. Neověřené senzory nepoužívejte pro automatizace.

Hodnoty režimů vycházejí z protokolu výrobce V2.14 a musí být ověřeny na konkrétním firmwaru. Zápis do holding registrů 218, 220 a 226 je prozatím zablokovaný: registr 218 představuje jmenovitý výkon generátoru, 220 napětí zapnutí SecEPS pro olověnou baterii a 226 není v poskytnuté tabulce popsán. Význam senzoru AC Power To User a znaménka výkonů je třeba ověřit.

Protokol vyžaduje odstup nejméně 850 ms mezi příkazy. Protože integrace zatím čte registry jednotlivě, celý cyklus může trvat déle než zvolený interval aktualizace.

Snímky v `docs/images` pocházejí z původní integrace a slouží pouze jako ilustrační příklady.

## Co poslat při testování

V issue uveďte přesný model a verzi firmware, verzi HA a integrace, způsob připojení, nastavení rychlosti a ID, logy bez hesel, snímky displeje a porovnání jednotlivých entit. Pro neodpovídající údaj přidejte jednotku, znaménko, stav provozu a pokud možno surovou hodnotu registru. U zapisovatelných nastavení nejprve sdělte čtenou hodnotu; zápis testujte pouze po ověření významu.

## Licence

MIT, viz [LICENSE](LICENSE). Původní projekt a obrázky: vsajer/sandisolar-ha.
