# Szkript_EncrypterApp
Készítette: Kiss Krisztofer Béla - F5EVU6

Az általam készített EncrypterApp-al a számítógépen bármilyen általunk válaszott fájlt titkosíthatunk, és visszafejthetünk. 
A titkosításhoz egy, a program által generált kulcsot használunk, amelyet el kell mentenünk magunknak, hogyha később a titkosított fájlt szeretnénk visszafejteni.
A megvalósítás folyán a felhasználó folyamatosan kap visszajelzést, akár hibázott akár nem.

Az általam használt modulok:
- Tkinter: ezek a modul felel a megjelenítésért.
- Tkinter.messagebox: ezzel a modullal lehetséges üzenet és hiba ablakokat megjeleníteni a felhasználónak.
- Tkinter.filedialog: ezzel a modullal lehet egy fájlkezelő ablakot megnyitni, és vele fájlt kiválasztani.
- cryptography.fernet: ez egy titkosítást lehetővé tevő modul egy key segítségével. Ezt építettem bele a függvényeimbe.

Az általam elkészített függvények:
main:
Itt dolgoztam ki a UI megjelenését, illetve itt kezeljük a kommunikációt a felhasználó, és az encrypting között.
Itt valósulnak meg az eseménykezelések:
- select_file: itt válasszuk ki, hogy mely fájlt akarjuk titkosítani/visszafejteni
- set_key: itt állítjuk be a titkosítás/visszafejtés során a kulcsot, amelyet beilleszthetünk mi, vagy a Fernet is legenerálhat alapértelmezetten.
- encrypt_file: a kiválasztott fájlt titkosítjuk
- decrypt_file: a kiválasztott fájlt visszafejtjük

EncryptionFileHandler:
Itt végezzük el a fájlkezelést és a titkosítást/visszafejtést.
Fügvényei:
- setFile: a kiválasztott fájl adatait és elérését betölti az osztálynak
- createFile: titkosított(encrypted) nevezetű paramétere alapján behívja a titkosítást(encrypt), vagy a visszafejtés(decrypt) függvényt, majd az új 
  fájlt elmenti a forrás fájl mellé átnevezve.
- encrypt: a Fernet modult felhasználva titkosítja a forrás szöveget
- decrypt: a Fernet modult felhasználva visszafejti a forrás szöveget
