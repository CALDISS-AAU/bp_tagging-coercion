# CALDISS Bridging Project: Tagging Coercion

*Sidst opdateret 3. februar 2021*



## Om projektet

| **Key**                       | **Value**             |
| ----------------------------- | --------------------- |
| Projektets interne titel      | Tagging Coercion (TC) |
| Varighed af bridging projekt  | Februrar-Juni 2021    |
| Aftalt deadline for leverance | 11. juni 2021         |



## Parter i projektet

Projektet er et samarbejde mellem CALDISS og Institut for Politik og Samfund.

**Deltagere fra Institut for Politik og Samfund**

| **Navn**                 | **E-mail**         |
| ------------------------ | ------------------ |
| Johan Heinsen            | heinsen@dps.aau.dk |
| Anders Dyrborg Birkemose |                    |

**Deltagere fra CALDISS**

| **Navn**               | **E-mail**     |
| ---------------------- | -------------- |
| Kristian Gade Kjelmann | kgk@adm.aau.dk |

**Andre deltagere**

| **Navn** | **E-mail** | **Tilhør**                        |
| -------- | ---------- | --------------------------------- |
| TBD      |            | TRoS (Rolfs studentermedhjælpere) |



## Beskrivelse

En central udfordring i historieforskning er at spore de samme mennesker gennem tiden. I tilfældet med tvangsarbejde findes en del materiale, hvor de samme personer går igen; herunder i bortløbningsannonncer samt i retssagsmateriale. For lettere at kunne identificere personer på tværs af materialet, er der brug for automatiserede metoder.

Formålet med projektet er at udvikle en model, der kan identificere forskellige kategorier i tekstmateriale fra 1700-tallet. Modellen skal som minimum kunne identificere steder og navne i tekst, men muligheder for at kunne identificere bestemte beskrivelser undersøges også (fx beskrivelser af ansigt).

I dette projekt trænes en eksisterende sprogmodel til at kunne identificere disse kategorier i tekstmaterialet. Formålet er at blive bekendt med mulighederne inden for brug af disse sprogmodeller. Det taggede materiale overføres til en ElasticSearch database for samtidig at undersøge potentialer med brug af søgemaskineteknologi i kombination med de identificerede kategorier.

Projektet er tænkt som et pilotprojekt, der skal danne grundlag for en større projektansøgning, hvis værktøjerne har potentiale. 



## Betingelser

Der henvises til betingelserne for CALDISS bridging projekt, som beskrevet på: https://www.caldiss.aau.dk/services/samarbejde/samarbejdsbetingelser/



## Data evaluering

**Risikoskala:**

0: Offentlig, ingen problemer

1: Et potentielt problem (personlig og/eller proprietær)

2: To potentielle problemer (personlig og proprietær)

3: Et faktisk problem (personlig og/eller proprietær)

4: To faktiske problemer (personlig og proprietær)

| Kilde                         | **Risiko** | **Opbevaring** | **Note**                                                     |
| ----------------------------- | ---------- | -------------- | ------------------------------------------------------------ |
| Billeder af retssagsmateriale | 1          |                | OCR-scanningerne af billedet bruges i projektet og ikke selve billederne. |



## Leverance

Det aftales, at CALDISS i dette bridging projekt leverer følgende: 

- En trænet sprogmodel til at identificere personer og steder i retssagsmateriale samt bortløbningsannoncer fra Danmark i 1700-tallet
- En evaluering af mulighederne med sprogmodellen generelt
- En evaluering af mulighederne med sprogmodellen for at identificere specifikke beskrivelser af ansigt, tøj o.l. specifikt
- En demoudgave af en ElasticSearch instans, der gør det mulig at anvende de identificerede kategorier i søgninger
- En workshop der introducerer de anvendte værktøjer (relevant Python-kode, brug af spacy, brug af prodi.gy, brug af ElasticSearch)



### Delleverancer

Der er i øjeblikket ingen delleverancer aftalt.



### Projektdeltagernes bidrag

Deltagere fra Institut for Politik og Samfund bidrager med domæneviden samt løbende test, feedback og kommentering. 

Deltagere fra TRoS bidrager i udviklingsarbejdet (manuel træning af sprogmodellen).



## Opfølgningsmøder

Der planlægges månedlige opfølgningsmøder indtil projektets afslutning.