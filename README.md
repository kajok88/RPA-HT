# RPA-HT
Ohjelmistorobotiikka -kurssin harjoitustyö

Tämän harjoitustyön aiheena oli tehdä yksinkertainen ohjelmistorobotti, joka
hakee tuotteiden/tavaroiden hinnan verrkosivustolta ja lähettää siitä
ilmoituksen Telegram sovellukseen, mikäli hinta on alempi kuin asetettu hintaraja.

Ideana oli asettaa tuotetiedot SQLite tietokantaan, josta löytyvät
    - URL
    - Hintaraja
    - Alekenttä: True/False, riippuen onko tuoteen hinta alle hintarajan
    - Lähetyskenttä: True/False, riippuen onko ilmoitus lähetetty

Tuotteesta lähetetään Telegram viesti, mikäli lähetyskenttä on False ja 
tuotteen hinta on alempi kuin asetettu hintaraja, eli Alekenttä on True.
Viestin lähettämisen jälkeen Lähetyskenttä muutetaan True:ksi.  
Mikäli tuotteen hinta on ylempi, kuin hintaraja, asetetaan alekenttä False:ksi ja lähetyskenttä False:ksi.

Koodia voidaan suorittaa päivittäin, jolloin saadaan ajantasaista tietoa mahdollisista alennuksista.




Huom. Tämä toteutus vaatii yksilöllisen Telegram botin tekemisen botfather:illa.