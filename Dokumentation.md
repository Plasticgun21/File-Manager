# File-Manager Dokumentation

## 1. Informieren

### 1.1 Anforderungen

| An-№ | Typ           | Beschreibung                                                              |
| ---- | ------------- | ------------------------------------------------------------------------ |
| 1    | Funktional    | Die Applikation soll eine Suchfunktion für Dateien und Ordner bieten.  |
| 2    | Funktional    | Die Applikation soll Dateien und Ordner löschen können.                |
| 3    | Funktional    | Die Applikation soll Dateien in einen gewählten Ordner verschieben können. |
| 4    | Funktional    | Die Applikation soll eine Benutzeroberfläche für einfache Bedienung bieten. |
| 5    | Funktional    | Die Applikation soll das Löschen bestätigen lassen, um Datenverluste zu vermeiden. |
| 6    | Qualitativ    | Die Applikation soll eine hohe Performance bieten.                     |
| 7    | Qualitativ    | Die Applikation soll mit verschiedenen Betriebssystemen kompatibel sein. |
| 8    | Qualitativ    | Die Applikation soll eine einfache und intuitive Bedienung ermöglichen. |
| 9    | Randbedingung | Die Applikation muss in Python 3.8 oder höher lauffähig sein.          |

### 1.2 User-Storys

| US-№ | An-№ | Verbindlichkeit | Beschreibung                                                   |
| ---- | ---- | -------------- | ------------------------------------------------------------- |
| 1.1  | 1    | muss           | Als User möchte ich Dateien und Ordner suchen können, um schnell auf sie zuzugreifen. |
| 2.1  | 2    | muss           | Als User möchte ich Dateien und Ordner löschen können, um Speicherplatz freizugeben. |
| 3.1  | 3    | muss           | Als User möchte ich Dateien in Ordner verschieben können, um meine Daten besser zu organisieren. |
| 4.1  | 5    | muss           | Als User möchte ich vor dem Löschen eine Bestätigung erhalten, um versehentliches Löschen zu vermeiden. |

## 2. Planen

### 2.1 Arbeitspakete

| AP-№ | Zuständig  | Frist       | Beschreibung                                               | Geplante Zeit |
| ----- | ---------- | ----------- | ---------------------------------------------------------- | ------------- |
| 1     | Luca J.W   | 17.01.25    | Anforderungen und User-Stories schreiben.                  | 60 min        |
| 2     | Luca J.W   | 17.01.25    | Testfälle schreiben.                                       | 60 min        |
| 3     | Luca J.W   | 24.01.25    | Systemarchitektur und UI-Design entwerfen.                 | 120 min       |
| 4     | Luca J.W   | 31.01.25    | Implementierung der Suchfunktion für Dateien und Ordner.   | 180 min       |
| 5     | Luca J.W   | 07.02.25    | Implementierung der Löschfunktion mit Bestätigung.         | 180 min       |
| 6     | Luca J.W   | 21.02.25    | Implementierung der Verschiebefunktion für Dateien.        | 180 min       |
| 7     | Luca J.W   | 28.02.25    | Fehlerbehebung und Optimierung.                            | 180 min       |
| 8     | Luca J.W   | 07.03.25    | Durchführung von Tests, Dokumentation und Portfolio schreiben. | 180 min       |

### 2.2 Testfälle
| **TC-№** | **Ausgangslage**               | **Eingabe**                                         | **Erwartete Ausgabe**                              |
|---------|--------------------------------|----------------------------------------------------|--------------------------------------------------|
| **1.1**  | Applikation ist geöffnet       | Nach einem existierenden File suchen               | Datei wird korrekt gefunden und angezeigt.      |
| **1.2**  | Applikation ist geöffnet       | Nach einem nicht existierenden File suchen         | Fehlermeldung: „Datei nicht gefunden“.          |
| **1.3**  | Applikation ist geöffnet       | Nach einer existierenden Datei mit Gross-/Kleinschreibung suchen | Datei wird korrekt gefunden (Suche ist case-insensitive). |
| **1.4**  | Applikation ist geöffnet       | Nach einem Ordner suchen                           | Ordner wird korrekt gefunden und angezeigt.      |
| **1.5**  | Applikation ist geöffnet       | Suchbegriff mit Sonderzeichen eingeben (`test_file@123`) | Falls vorhanden, Datei wird korrekt gefunden. |
| **1.6**  | Applikation ist geöffnet       | Suchfeld leer lassen und Suche starten            | Fehlermeldung: „Bitte Suchbegriff eingeben!“.   |
| **1.7**  | Applikation ist geöffnet       | Suche in leerem Ordner durchführen                | Meldung: „Keine Ergebnisse gefunden.“           |
| **2.1**  | Applikation ist geöffnet       | Eine Datei auswählen und löschen                   | Datei wird nach Bestätigung gelöscht.           |
| **2.2**  | Applikation ist geöffnet       | Eine Datei ohne Bestätigung löschen                | Datei bleibt bestehen.                           |
| **2.3**  | Applikation ist geöffnet       | Versuch, eine bereits gelöschte Datei zu löschen  | Fehlermeldung: „Datei existiert nicht mehr!“.  |
| **2.4**  | Applikation ist geöffnet       | Versuch, einen schreibgeschützten Ordner zu löschen | Fehlermeldung: „Löschen fehlgeschlagen: Zugriff verweigert.“ |
| **2.5**  | Applikation ist geöffnet       | Versuchen, eine Datei zu löschen, die vom System verwendet wird | Fehlermeldung: „Datei kann nicht gelöscht werden, da sie in Verwendung ist.“ |
| **3.1**  | Applikation ist geöffnet       | Eine Datei in einen anderen Ordner verschieben     | Datei wird in den gewählten Ordner verschoben.  |
| **3.2**  | Applikation ist geöffnet       | Datei in denselben Ordner verschieben              | Fehlermeldung: „Datei befindet sich bereits im Zielordner.“ |
| **3.3**  | Applikation ist geöffnet       | Datei in einen schreibgeschützten Ordner verschieben | Fehlermeldung: „Verschieben fehlgeschlagen: Zugriff verweigert.“ |
| **3.4**  | Applikation ist geöffnet       | Datei in einen nicht existierenden Ordner verschieben | Fehlermeldung: „Zielordner existiert nicht.“    |
| **3.5**  | Applikation ist geöffnet       | Datei überschreiben (Zieldatei existiert bereits) | Meldung zur Bestätigung: „Datei existiert bereits. Überschreiben?“ |
| **4.1**  | Applikation ist geöffnet       | Mehrere Dateien gleichzeitig auswählen und verschieben | Alle gewählten Dateien werden korrekt verschoben. |
| **4.2**  | Applikation ist geöffnet       | Applikation während einer laufenden Aktion schliessen | Bestätigungsabfrage: „Möchten Sie wirklich beenden?“ |
| **4.3**  | Applikation ist geöffnet       | Suche nach einer versteckten Datei                | Falls erlaubt, versteckte Datei wird gefunden.  |


## 3. Entscheiden

Da die Kernfunktionalitäten essenziell für einen File-Manager sind, wird zuerst das Backend entwickelt, bevor die Benutzeroberfläche erstellt wird. Dies erleichtert das Testen und die Fehlerbehebung.

## 4. Realisieren

### 4.1 Fortschritt

| AP-№ | Datum     | Zuständig  | Geplante Zeit | Tatsächliche Zeit |
| ---- | --------- | ---------- | ------------- | ----------------- |
| 1    | 17.01.25 | Luca J.W   | 60 min        | 60 min             |
| 2    | 17.01.25 | Luca J.W   | 60 min        | 60 min             |
| 2    | 24.01.25 | Luca J.W   | 120 min       | 120 min            |
| 3    | 31.01.25 | Luca J.W   | 180 min       | 180 min            |
| 4    | 07.02.25 | Luca J.W   | 180 min       | 180 min            |
| 5    | 21.02.25 | Luca J.W   | 180 min       | 180 min            |
| 6    | 28.02.25 | Luca J.W   | 180 min       | 180 min            |
| 7    | 07.03.25 | Luca J.W   | 180 min       | 180 min            |

## 5. Kontrollieren

### 5.1 Testprotokolle

| TC-№ | Ergebnis     | Bemerkungen                                     |
| ---- | ----------- | --------------------------------------------- |
| 1.1  | TBD         | TBD                                           |
| 1.2  | TBD         | TBD                                           |
| 2.1  | TBD         | TBD                                           |
| 2.2  | TBD         | TBD                                           |
| 3.1  | TBD         | TBD                                           |

### 5.2 Testbericht

Nach Abschluss der Implementierung werden Tests durchgeführt, um sicherzustellen, dass die Kernfunktionen stabil laufen. Falls erforderlich, werden Optimierungen und Fehlerkorrekturen vorgenommen.
