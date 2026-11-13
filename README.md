# AOHAI FSC-G3 Home Assistant – experimentální verze

Samostatná čtecí kopie [SANDISOLAR HA](https://github.com/vsajer/sandisolar-ha), připravovaná pro měniče AOHAI FSC-8/10/12K1P-BL-G3. Vychází z původní integrace a porovnání s [ESPHome konfigurací pro FSC-12K1P-BL-G3](https://github.com/bootuz-dinamon/Sandisolar-Aohai-FSC-12K1P-BL-G3-Home-Assistant-integration-via-RS485). Původní kód je šířen pod licencí MIT, viz LICENSE.

**Vývojová verze: nebyla ověřena na měniči FSC-G3.** Hodnoty a jejich znaménka je nutné porovnat s displejem a externím měřením. Registry se mohou lišit podle modelu a firmwaru. Nepoužívejte ji pro automatizace, dokud nejsou hodnoty ověřené.

Prozatím jsou aktivní pouze senzory. Ovládací entity typu switch, number a select nejsou načítány; zejména význam holding registru 220 se mezi dostupnými konfiguracemi liší. Některé výpočtové senzory používají výchozí nebo nedostupná nastavení a nemusí být přesné.

## Instalace pro testování

V HACS přidejte `https://github.com/vsajer/aohai-fsc-g3-ha` jako vlastní repozitář typu Integration. Nainstalujte výchozí větev, restartujte Home Assistant a přidejte integraci AOHAI FSC-G3 Modbus. Připojení je sériové Modbus RTU; původní nastavení je 9600 baud, slave 1, 8N1. Parametry a zapojení ověřte pro svůj měnič. Souběžný provoz s jiným Modbus masterem může narušit komunikaci.

Přímé připojení ESPHome k UART Wi-Fi modulu není součástí této integrace. Bez reálného testu není potvrzena kompatibilita 8kW ani 10kW varianty.
