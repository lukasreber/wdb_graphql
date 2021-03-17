# Mini Challenge 3: Report

**wdb @ FHNW BSc Data Science** \
**Autor: Lukas Reber**

## Umsetzung

Für die Mini Challenge 3 der Kompetenz Web Datenbeschaffung (wdb) wurde ein GraphQL API mittels [Django](https://www.djangoproject.com) und [Graphene](https://graphene-python.org) umgesetzt. Die API dient als Schnittstelle um die in der Mini Challenge 4 von wdb gescrapten Daten entsprechend in eine Datenbank abzulegen. (Weitere Informationen zur Umsetzung der Mini Challenge 4 sind [hier](https://github.com/lukasreber/wdb_scraper) zu finden).

Das Datenmodell besteht aus den Tabellen 'User' und 'Ad'. In der Tabelle 'Ad' sind die gescrapten Tutti Inserate hinterlegt. Die Tabelle 'User' beinhaltet die Tutti Benutzer, also Usernamen der Inserenten. Da ein User mehrere Inserate aufgeben kann, wurden die Userinformationen in eine separate Tabelle ausgelagert und über die User ID verknüpft. Da es sich hierbei lediglich um einen "Proof of concecpt" handelt, wurde darauf verzichtet eine richtige Datenbankanbindung zu realisieren. Stattdessen wurde die interne, filebasierte SQLite3 Datenbank von Django verwendet.

In der API wurde sämtliche CRUD Funktionen implementiert. Somit lassen sich über die API alle Daten der Datenbank abrufen, veränder und löschen sowie neue Daten einfügen. Die API lässt sich nach dem ausführen über die URL [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql) mittels einer graphischen Oberfläche benutzen. GraphQL erstellt zudem eine automatische Dokumentation, somit ist dort ersichtlich, welche Queries und Mutations verfügbar sind.

Um die Schnittstelle zu testen wurden diverse Tests mit pytests realisiert.

Der Data Science Aspekt ist insofern gegeben, dass die Erstellung einer GraphQL API in relativ kurzer Zeit realisierbar ist und dies somit eine einfache und schnelle Lösung bietet, Daten zur Verfügung zu stellen. Da das Datenmodell sehr einfach ist und die Daten nicht weiter verarbeitet werden sehe ich hierbei jedoch keine weiteren explizite Data Science Aspekte.

## GraphQL vs REST

Ein oft genanntes Problem betreffend REST APIs ist das Over- oder Underfetching von Daten. Da bei eine REST Endpoint fixe Datenstrukturen zurückgegeben werden, fürht dies je nach Requirement dazu, dass mehrere Request gemacht werden müssen um die benötigten Daten zu erhalten, oder aber dass nur ein kleiner Teil der übermittelten Daten benötigt wird. Ich hab mich deshalb bei der Umsetzung der Schnittstelle aus folgenden Gründen für GraphQL entschieden:

1. **Vielseitige Anwendung**: Die gescrapten Tutti Daten können einen vielseitigen Anwendungszweck haben. Da zum aktuellen Zeitpunkt jedoch noch nicht klar ist, welche Daten und in welcher Zusammenstellung die Daten benötigt werden, sind durch die API keine restriktionen gesetzt. Die benötigten Daten können frei mittels entsprechendem JSON Syntax definiert werden. Dass heisst, kommt zu einem späteren Zeitpunkt ein neuer Use Case hinzu, welcher die Daten in anderer Weise aggregiert oder filtert, kann dies mit grosser Wahrscheinlichkeit auf der bestehenden API bereits genutzt werden.

2. **Einfache Erweiterung**: Da sich bei der Entwicklung der Mini Challenge 4 die Datenstruktur mehrmals verändert hat, lässt sich dank der einfachen Struktur der GraphQL API, diese leicht anpassen. Es sind keine zusätzlichen Endpoints einzurichten. Sobald das Schema erweitert ist, können die neuen Attribute verwendet werden.

3. **Zukunftsfähig**: Kein technischer Grund, aber ein persönlicher: Ich bin der Meinung, in Zukunft wird vermehrt GraphQL zum Einsatz kommen, aus diesem Grund war es für mich interessant diese Technologie zu lernen.

## Weiterentwicklung

Die API sowie das darunterliegende Datenmodell lassen sich grundsätzlich beliebig weiterentwickeln. Zustäzliche Tabellen oder Attribute können ohne grossen Aufwand impelementiert werden ohne dass die bestehenden Funktionalitäten verloren gehen. Für einen produktiven Einsatz, gerade wenn mit einer grösseren Datenmenge zu rechnen ist, ist zu empfehlen eine full featured Datenbank Anbindung zu realisieren.
