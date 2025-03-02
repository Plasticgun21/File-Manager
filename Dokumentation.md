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
| 1     | Entwickler | 15.03.25    | Anforderungen und User-Stories definieren.                 | 60 min        |
| 2     | Entwickler | 22.03.25    | Systemarchitektur und UI-Design entwerfen.                 | 120 min       |
| 3     | Entwickler | 05.04.25    | Implementierung der Suchfunktion für Dateien und Ordner.   | 180 min       |
| 4     | Entwickler | 12.04.25    | Implementierung der Löschfunktion mit Bestätigung.         | 180 min       |
| 5     | Entwickler | 19.04.25    | Implementierung der Verschiebefunktion für Dateien.        | 180 min       |
| 6     | Entwickler | 26.04.25    | Fehlerbehebung und Optimierung.                            | 180 min       |
| 7     | Entwickler | 03.05.25    | Durchführung von Tests und Dokumentation.                  | 180 min       |

### 2.2 Testfälle

| TC-№ | Ausgangslage                 | Eingabe                                          | Erwartete Ausgabe                             |
| ---- | ---------------------------- | ----------------------------------------------- | --------------------------------------------- |
| 1.1  | Applikation ist geöffnet     | Nach einem existierenden File suchen           | File wird korrekt gefunden und angezeigt.    |
| 1.2  | Applikation ist geöffnet     | Nach einem nicht existierenden File suchen     | Fehlermeldung: „Datei nicht gefunden“.       |
| 2.1  | Applikation ist geöffnet     | Eine Datei auswählen und löschen               | Datei wird nach Bestätigung gelöscht.        |
| 2.2  | Applikation ist geöffnet     | Eine Datei ohne Bestätigung löschen            | Datei bleibt bestehen.                        |
| 3.1  | Applikation ist geöffnet     | Eine Datei in einen anderen Ordner verschieben | Datei wird in den gewählten Ordner verschoben. |

## 3. Entscheiden

Da die Kernfunktionalitäten essenziell für einen File-Manager sind, wird zuerst das Backend entwickelt, bevor die Benutzeroberfläche erstellt wird. Dies erleichtert das Testen und die Fehlerbehebung.

## 4. Realisieren

### 4.1 Fortschritt

| AP-№ | Datum     | Zuständig  | Geplante Zeit | Tatsächliche Zeit |
| ---- | --------- | ---------- | ------------- | ----------------- |
| 1    | 15.03.25 | Entwickler | 60 min        | TBD               |
| 2    | 22.03.25 | Entwickler | 120 min       | TBD               |
| 3    | 05.04.25 | Entwickler | 180 min       | TBD               |
| 4    | 12.04.25 | Entwickler | 180 min       | TBD               |
| 5    | 19.04.25 | Entwickler | 180 min       | TBD               |
| 6    | 26.04.25 | Entwickler | 180 min       | TBD               |
| 7    | 03.05.25 | Entwickler | 180 min       | TBD               |

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
