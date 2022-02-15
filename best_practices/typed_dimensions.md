 
# XBRL Typed dimensions best practices
(overgenomen van wiki, nog niet herschreven.)

## Samenvatting

Gebruik typed dimensions voor het categoriseren van aspecten van een concept, met een domein met veel of onbekende waarden die semantisch betekenisvol zijn. Gebruik typed dimensions niet voor waarden die zelfstandig worden opgeslagen of als sleutel dienen.


## Best Practice

Met XBRL Formules kunnen inhoudelijke controles op instances gemaakt worden. Het is tevens mogelijk nieuwe instances aan te maken waarin resultaten van berekeningen geplaatst worden. De specificatie is gebaseerd op het bouwen van XPath expressies en gebruikt de functies van XQuery. Het geheel wordt vastgelegd als resources in een (generic) linkbase. Voor de processing is een gecertificeerde XBRL Formule engine nodig.

De XBRL formule specificatie werkt met een zogenaamd aspecten model. Dit is een model waarbij uitgegaan wordt van het gerapporteerde feit (stel: 2000) die in de instance gekoppelde aspecten heeft. Aspecten zijn o.a. de unit, de @decimals, de conceptnaam en de (inhoud van de) context. Maar middels bijvoorbeeld de conceptnaam kunnen ook zijn type, label en presentatieplaats ontdekt worden. Al deze gegevens zijn aspecten die wel of niet van belang kunnen zijn bij het bepalen van de controle. Een gemakkelijk voorbeeld is: tel de waarden van A en B bij elkaar en kijk of dat meer dan nul is. Deze controle heeft natuurlijk alleen zin als de waarden van A en B wel dezelfde unit en context hebben!

### Bouwstenen
Dimensions is een module die bovenop de core XBRL specificatie gebruikt kan worden. Hierdoor kunnen multi dimensionale tabellen (zgn. hypercubes) gedefinieerd worden in de XBRL taxonomie. Er zijn 2 soorten dimensions, Explicit en Typed.

**Een Typed Dimension wordt gebruikt voor het catagoriseren van aspecten van een concept, en niet voor het opnemen van concepten.**
Typed Dimensions kun je dus inzetten ten behoeve van een categorisatie. Voor nieuwe feiten moet een ‘concept’ gedefinieerd worden.

**In Typed Dimensions wordt een domain vastgelegd (obv een typering) van categorieën die:**

1. onbekend zijn voor de DTS auteur; en/of
2. dermate veel leden bevatten dat deze niet in de DTS op te nemen zijn.

Je kunt daarin dus ranges van toegestane waarden voor een bepaalde categorie opnemen. (b.v.: postcodes,tijd, temperatuur)

**Gebruik een Typed Dimension alleen voor waarden die semantisch betekenisvol zijn.**
Je kunt hierin sleutelwaarden opnemen om een set van andere feiten te adresseren. Maar niet: een volgnummer daarvoor moet een tuple gebruikt worden.


**Een Typed Dimension waarde die in een systeem als een op zichzelf staand gegeven opgeslagen wordt, is een indicatie dat het mogelijk geen Typed Dimension is.**

Een dergelijk gegeven is waarschijnlijk een feit dat als concept moet worden opgenomen.

**Een Typed Dimension waarde die in foutrapportages terug gecommuniceerd wordt om de unieke regel te adresseren is geen Typed Dimension waarde, maar een technische sleutel.**

Een foutmelding waarin wordt aangegeven dat van bestuurslid nummer ‘5’ de BSN onjuist is, is ‘5’, (een waarde in de range van toegestane nummers) een verkeerd gebruik van Typed dimension.
