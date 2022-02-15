 
# XBRL Formule best practices
(overgenomen van wiki, nog niet herschreven.)

## Samenvatting

Diverse best practices m.b.t. XBRL Formule over het gebruik van bouwstenen en naamgeving. 

## Best Practice

Met XBRL Formules kunnen inhoudelijke controles op instances gemaakt worden. Het is tevens mogelijk nieuwe instances aan te maken waarin resultaten van berekeningen geplaatst worden. De specificatie is gebaseerd op het bouwen van XPath expressies en gebruikt de functies van XQuery. Het geheel wordt vastgelegd als resources in een (generic) linkbase. Voor de processing is een gecertificeerde XBRL Formule engine nodig.

De XBRL formule specificatie werkt met een zogenaamd aspecten model. Dit is een model waarbij uitgegaan wordt van het gerapporteerde feit (stel: 2000) die in de instance gekoppelde aspecten heeft. Aspecten zijn o.a. de unit, de @decimals, de conceptnaam en de (inhoud van de) context. Maar middels bijvoorbeeld de conceptnaam kunnen ook zijn type, label en presentatieplaats ontdekt worden. Al deze gegevens zijn aspecten die wel of niet van belang kunnen zijn bij het bepalen van de controle. Een gemakkelijk voorbeeld is: tel de waarden van A en B bij elkaar en kijk of dat meer dan nul is. Deze controle heeft natuurlijk alleen zin als de waarden van A en B wel dezelfde unit en context hebben!

### Bouwstenen
Formula, FormulaTuple, ConsistencyAssertion, ValueAssertion, ExistenceAssertion. Dit zijn de vijf start mogelijkheden van XBRL formules. In de NT staan we alleen de valueAssertion en existanceAssertion toe.

Wanneer een veld onconditioneel verplicht is wordt het gebruik van een fn:exists() resultaat als @test van een valueAssertion ontmoedigd, aangezien hiervoor de existenceAssertion bedoeld is. Bij een preconditie in combinatie met een existenceAssertion kunnen problemen met de preconditie optreden. In dat geval is een valueAssertion met fn:exists() te prefereren. Assertions die geen resultaat geven worden ook ontmoedigd.
Geef de assertions een uniek (in de tijd) vaststaande identificatie mee, zodat daarnaar in de foutmelding en eventuele documentatie verwezen kan worden.
GeneralVariable en FactVariable. Dit zijn de variabelen die gevuld gaan worden met waarden. GeneralVariable kennen geen aspecten, het zijn 'kale' waarden. FactVariabele krijgen alle aspecten die ontdekt kunnen worden.

Filters. De specificatie kent voor elk aspect een eigen filter zodat deze toegepast kan worden op het universum van feiten die in de instance staan. Van elk filter kan de 'inverse' aangewend worden als dat praktischer is. De NT staat alle filters toe.
Implicit filtering. Dit zorgt ervoor dat bij evaluatie van een formule setjes gevormd worden van FactVariables waarvoor de aspecten gelijke waarden hebben. Bij een berekening bijvoorbeeld worden alleen de bedragen met dezelfde unit meegenomen. Als het wenselijk is om dit mechanisme uit te schakelen voor een bepaald aspect, dan dient dat specifieke aspect gecoverd te worden. Ook het opnemen van een expliciet filter bij een FactVariable leidt tot het coveren van dat aspect. Implicit filtering blijft dan bij deze formule wel gelden voor alle overige aspecten.

Fallback values. Het koppelen van een fallback value aan een FactVariable zorgt ervoor dat evaluatie van een formule, waarbij gebruik wordt gemaakt van implicit filtering, ook plaats kan vinden wanneer niet alle FactVariabeles daadwerkelijk met een waarde in een instance voorkomen. Minimaal 1 FactVariable moet met een “echte” waarde in de instance zijn opgenomen om tot evaluatie van de regel te leiden.

Precondities en parameters. Dit zijn hulpjes voor effectieve formules. De preconditie stelt eerst vast of er aan een basisvoorwaarde is voldaan voordat executie plaats gaat vinden. Parameters zijn eigenlijk hetzelfde als generalVariables met de uitzondering dat ze over formules heen gebruikt kunnen worden. Omdat de waarden die parameters vertegenwoordigen het onderhoud op formules verzwaart wordt geadviseerd de parameter waarden buiten de formule in een XML bestand op te slaan. De waarde is met een fn:doc() functie in de formule te adresseren.

Messages. Een belangrijk onderdeel van een controle is de foutmelding en hoe precies deze is om te helpen het probleem op te lossen. De NT stelt dat elke controle in elk geval een signaal af moet geven, anders is niet te stellen dat de controle überhaupt gelopen heeft. In de message kan met alle aspecten gewerkt worden die bij de evaluatie betrokken zijn.

Labels en References. Elke formule kan natuurlijk uitgerust worden met (generic) labels en references. De NT stelt dat een reference verplicht is. Deze moet verwijzen naar de documentatie over wat de controle precies probeert te bereiken.

### Naamgeving
De NT heeft nog geen naamgevingsconventies vastgesteld voor alle gebruikte componenten. Het ligt voor de hand dat als de formules met de hand worden opgesteld en moeten worden gecontroleerd, het handig is een naamgevingsconventie te gebruiken. Het is echter verstandiger formules te genereren vanuit een tool. In dat geval zijn de namen van de gelinkte resources minder van belang.

Alleen op het gebied van de namen van de linkbase bestanden en de folders zijn wel regels gesteld. 
