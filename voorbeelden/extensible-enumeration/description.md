## Toelichting extensible enumeration

Om het gebruik van een Extensible Enumeration 2.0 te illustreren is een voorbeeld gemaakt waar gekozen is voor een enumeratie van landen onderverdeeld over de verschillende continenten. De taxonomie bestaat uit één tabel met twee concepten: een enumerationItemType (single select) en een enumerationSetItemType (multi select). Beide maken gebruik van dezelde set enumeratie waarden.

### Toelichting op relevante taxonomie bestanden

**taxonomie/<n/>www.nltaxonomie.nl/nt16/sbr/20210301/dictionary/sbr-data.xsd** definieerd de twee enumeratie concepten: CountrySingleSelect en CountryMultiSelect. Het type attribuut geeft aan dat het om een enumerationItemType (single select enumeratie) en een enumerationSetItemType (multi select enumeratie) gaat. De attributen enum2:domain en enum2:linkrole attributen leggen de link naar de enumeratie waardes. Dit zijn de domain(members) die gevonden worden door de definition arcs te volgen in de aangegeven linkrole met de aangegeven domain als root/head. Het attribuut enum2:headUsable geeft aan of de domain(member) gekozen in enum2:domain zelf als enumeratie waarde gebruikt mag worden.

**taxonomie/www.nltaxonomie.nl/nt16/sbr/20210301/validation/iso3166-countrycodes-2020-11-24-members-def.xml** bevat de relaties die leiden tot de set van enumeratie waarden. De relaties gaan van sbr-dm:M49_001 (world) naar continent naar land. sbr-dm:M49_001 komt overeen met het linkrole attribuut van de enumeratie concepten. Omdat de relaties van de sbr-dm:M49_001 (world) naar de continenten xbrldt:usable="false" als attribuut hebben kunnen de continenten zelf niet gekozen worden als enumeratie waarde. De continenten dienen ter aggregatie van de onderliggende landen. sbr-dm:M49_001 (world) zelf is geen enumeratie waarde omdat enum2:headUsable op false staat (zie sbr-data.xsd).

### Toelichting op instances
**instances/instance-valid.xml** - Een valide voorbeeld. CountrySingleSelect heeft CAF (Central African Republic (the)) als enumeratie waarde. CountryMultiSelect heeft CAF (Central African Republic (the)) én MAR (Morocco) als enumeratie waarden.

**instances/instance-invalid-1.xml** - Een invalide voorbeeld. De instance is invalide omdat M49_001 (world) en M49-009 (Oceania) geen correcte enumeratie waardes zijn (usable = "false"). 

**instances/instance-invalid-2.xml** - Een invalide voorbeeld. De instance is invalide omdat CountrySingleSelect twee enumeratie waardes als value heeft. Dit mag alleen als het type van CountrySingleSelect enumerationSetItemType is.
