 
# Concept ontwerp patronen
(overgenomen van wiki, nog niet herschreven)

## Samenvatting

Concepten worden niet uitgenormalisered middels hun hiërarchisch pad. Bij dimensioneel modelleren wordt wel betekenis overgeheveld naar de dimensie. Dit wordt alleen gedaan als normalisatie op meerdere rapporteerbare elementen gebruikt kan worden.

Op basis van 'common practice' zijn gestandaardiseerde waarden voor dimensies te onderkennen. 

## Best Practice
Belangrijk uitgangspunt van XBRL (in tegenstelling tot de norm binnen datamodellering) is dat elementen NIET uitgenormaliseerd worden middels hun hiërarchisch pad. De betekenis van een element staat in de @name van een element en wordt dus NIET (deels) overgeheveld naar een eventueel ouder element (in XSD een complexType, in XBRL een tuple).

Bij XBRL dimensioneel modelleren wordt WEL een deel van de betekenis, die verwoord is in de @name, overgeheveld naar de dimensie en het domeinlid. Bij deze laatste methodiek kan dus in extremis zo ver genormaliseerd worden dat er uiteindelijk alleen een set van datatypen als element overblijven. De dimensionele modellering die in Europa opgang maakt -Data Point Modelling (DPM)- wordt niet geheel overgenomen. Deze methodiek werkt voornamelijk bij een zogenaamde 'closed community', zoals de centrale banken met hun commerciële banken. De community is beperkt qua grootte en alle partijen weten exact wat er gerapporteerd moet worden en spreken hierover in coderingen als tabelcodes en celcodes met elkaar. In een dergelijke situatie zijn 'zelfverklarende' elementnamen zoals XBRL die vereist niet langer noodzakelijk. XBRL modellering gaat uit van een grote community (alle bedrijven) die moeten rapporteren maar lang niet allemaal bekend zijn met de exacte gegevensset die gevraagd wordt. Bovendien mogen deze partijen zelf uitbreidingen ontwerpen. In een dergelijk community moeten de gebruikte elementen duidelijk gemaakt worden op een simpele manier (de @naam) en niet door meerdere dimensionele relaties bij elkaar te nemen (zoals bij DPM).

Op basis van 'common practice' in de wereld van de financiële jaarrapportage voor commerciële bedrijven zijn er door de IASB, FASB en JFSA ook een aantal dimensies onderkend die elke GAAP rapportage behoort te bevatten:

- Componenten van materiële vaste activa (ClassesOfAssets)
- Componenten van immateriële vaste activa (ClassesOfIntangibleAssets)
- Componenten van financiële vaste activa (ClassesOfFinancialAssets)
- Componenten van vaste activa (ClassesOfPropertyPlantAndEquipment)
- Componenten van passiva (ClassesOfLiabilities)

Helaas is de standaardisatie nog niet zo ver gevorderd dat gelijkluidende elementnamen voor de dimensies worden gebruikt. SBR-NL volgt IFRS voor zo ver van toepassing. Omdat balans gegevens vaak een onderdeel uitmaken van een financiële verantwoordingsrapportage wordt verwacht dat elke NT partner probeert aan te sluiten bij de inzichten die de GAAP rapportages op dit punt verwoorden.

- De NTA volgt de XBRL modelleringwijze dat tuples GEEN onderdeel van de normalisatie van elementen zijn.
- De NTA stelt als limiet aan de XBRL dimensionele manier van modelleren dat domeinleden ALLEEN aangemaakt worden als normalisatie vanuit een element @name INDIEN een dergelijk domeinlid op meerdere rapporteerbare elementen gebruikt kan worden.
