 
# Gebruik van labels
(overgenomen van wiki, nog niet herschreven.)
**Todo: gebruik Negated label en Guidance is toegestaan sinds het opstellen van deze tekst.**

## Samenvatting

Een lijst met de toegestane rollen uit de XBRL 2.1 specificatie en hun gebruiksdoel. 

## Best Practice
Een label wordt gevormd door een tekst, taalcode en labelrol. Meerdere taalcodes dienen door software als optie aan de gebruiker getoond te worden. Bij gebruik van meerdere labelrollen is het DOEL van het label van belang. XBRL International heeft een aantal labelrollen ter beschikking gesteld met de specificatie van XBRL 2.1. Niet alle labelrollen worden toegestaan in de NTA. Hieronder een lijst met de toegestane rollen en hun gebruiksdoel. 

label resource xlink:role attribute value | Betekenis | NTA
-----|------|------
(Omitted role attribute) | Standaard label rol | Standaard label geschikt voor presentatie doeleinden maar ook de menselijke interpretatie wat het concept betekent (is echter niet de definitie!)
http://www.xbrl.org/2003/role/label | Standaard label rol | Standaard label geschikt voor presentatie doeleinden maar ook de menselijke interpretatie wat het concept betekent (is echter niet de definitie!)
http://www.xbrl.org/2003/role/terseLabel | Verkorte versie van het standaard label | Aanvullend label ter verkorting van het standaard label voor presentatie doeleinden
http://www.xbrl.org/2003/role/verboseLabel | Uitgebreide versie van het standaard label | Niet toegestaan
http://www.xbrl.org/2003/role/positiveLabel |  | Positive is de default, label dus overbodig
http://www.xbrl.org/2003/role/positiveTerseLabel |  | Positive is de default, label dus overbodig
http://www.xbrl.org/2003/role/positiveVerboseLabel |  | Positive is de default, label dus overbodig
http://www.xbrl.org/2003/role/negativeLabel |  | Opgevolgd door negatedLabel
http://www.xbrl.org/2003/role/negativeTerseLabel |  | Opgevolgd door negatedTerseLabel
http://www.xbrl.org/2003/role/negativeVerboseLabel |  | Niet toegestaan
http://www.xbrl.org/2003/role/zeroLabel |  | Niet toegestaan
http://www.xbrl.org/2003/role/zeroTerseLabel |  | Niet toegestaan
http://www.xbrl.org/2003/role/zeroVerboseLabel |  | Niet toegestaan
http://www.xbrl.org/2003/role/totalLabel | Bij het totalLabel wordt een concept ingezet om zowel een detail als een totaal uit te drukken in de instance | Het totalLabel voegt geen semantiek toe maar moet gezien worden als gelijkend op een terseLabel of verboseLabel: een iets andere presentatie maar geen semantisch impact
http://www.xbrl.org/2003/role/periodStartLabel | Label die de factor tijd presentabel op het concept maakt. Veelal gebruikt in verloopoverzichten. | Gebruik van de periodStartLabel en periodEndLabel wordt ontraden. Advies is een tijd dimensie te gebruiken.
http://www.xbrl.org/2003/role/periodEndLabel | Label die de factor tijd presentabel op het concept maakt. Veelal gebruikt in verloopoverzichten. | Gebruik van de periodStartLabel en periodEndLabel wordt ontraden. Advies is een tijd dimensie te gebruiken.
http://www.xbrl.org/2003/role/documentation |  | Alternatief voor een referentie. Bevat de tekst waarnaar gerefereerd zou worden. Geldt als de definitie van het concept.
http://www.xbrl.org/2003/role/definitionGuidance |  | Niet toegestaan
http://www.xbrl.org/2003/role/disclosureGuidance |  | Niet toegestaan
http://www.xbrl.org/2003/role/presentationGuidance |  | Niet toegestaan
http://www.xbrl.org/2003/role/measurementGuidance |  | Niet toegestaan
http://www.xbrl.org/2003/role/commentaryGuidance |  | Aanvullend label tbv gebruikersinstructie
http://www.xbrl.org/2003/role/exampleGuidance |  | Niet toegestaan
http://www.xbrl.org/2009/role/deprecatedDateLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/deprecatedLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negatedLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negatedNetLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negatedPeriodEndLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negatedPeriodStartLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negatedTerseLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negatedTotalLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negativePeriodEndLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negativePeriodEndTotalLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negativePeriodStartLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/negativePeriodStartTotalLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/netLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/positivePeriodEndLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/positivePeriodEndTotalLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/positivePeriodStartLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/positivePeriodStartTotalLabel |  | Niet toegestaan
http://www.xbrl.org/2009/role/restatedLabel |  | Niet toegestaan 
