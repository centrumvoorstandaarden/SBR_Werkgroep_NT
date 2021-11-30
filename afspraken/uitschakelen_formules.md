# Uitzetten van formules in NT taxonomiën

## Aanleiding
Binnen diverse XBRL stelsels is het gebruikelijk om een mechanisme toe te passen waarmee formules na publicatie kunnen worden uitgezet. 
Dit omdat deze soms voor ongewenste situaties kunnen zorgen bij het valideren van berichten. 
Om in zo'n geval niet een volledig nieuwe taxonomie uit te hoeven brengen, gebruikt men oplossingen die in de architectuur zijn beschreven. 
Middels deze RfC stellen we een dergelijk mechanisme voor om toe te passen binnen SBR Nederland.

## Behandeling
Op 15 September hebben een aantal SBR EGG leden enkele manieren besproken waarop formules binnen de NT na publicatie kunnen worden uitgezet. 
Hierbij staan drie principes centraal:

-	De taxonomie dient niet opnieuw te worden gepubliceerd;
-	De gekozen oplossing(en) brengen geen grote impact met zich mee;
-	De gekozen oplossing(en) zijn gebaseerd op (internationale) best practices.

Als basis hebben we gekeken naar de volgende oplossingen:

Eurofiling: http://eurofiling.info/portal/taxonomiesmechxml-blacklist/

SBR Nexus: https://support.sbrnexus.nl/hc/nl/articles/360015479799-Uitgeschakelde-formulas-op-de-BIV-blacklist-

Ook is er gekeken naar een combinatie van beide, waarbij de oplossing van Eurofiling enigszins is aangepast. 
In het originele voorstel wordt een dummy linkbase tijdens de initiële publicatie toegevoegd. 
We stellen voor om dit niet te doen. Dit zodat de gebruiker zelf kan kiezen of de DTS opnieuw opgebouwd dient te worden, 
of dat de handeling handmatig wordt doorgevoerd. 
Voor die tweede optie bieden we ook een lijst aan met uit te schakelen formules, zoals SBR Nexus al doet. 

Deze combinatie leek als winnaar uit de bus te komen, maar na de bijeenkomst op 17 September, 
en in mailcontact hierna bleek dit toch lastig uitvoerbaar te zijn. 
Op 3 November heeft de Werkgroep NT dit onderwerp nogmaals besproken en is uitgekomen op een mechanisme zoals SBR-Nexus gebruikt; 
een simpele CSV lijst met alleen een combinatie van bestand en de uit te schakelen formula ID.

Op 2 februari is een concept RfC voorgelegd aan de Expertgroep Gegevens. De opmerkingen zijn verwerkt in dit document.
In april 2021 is de definitieve RfC voorgelegd aan de Expertgroep gegevens, hierop zijn nog enkele toevoegingen gedaan.

## Voorgestelde oplossing
Zoals gezegd stelt de Expertgroep Gegevens voor om de aanpak van SBR-Nexus te hanteren: 
Een csv bestand met een combinatie van het bestand waar de uit te schakelen formule zich bevindt, 
de localname van de formule en de datum waarop de formule uitgeschakeld dient te worden.

De header van het document ziet er als volgt uit:
Bestand, Formula localname, roleuri, entrypoint, datum buiten gebruik CRLF

Een uitgeschakelde formule wordt als volgt beschreven:
http://www.nltaxonomie.nl/nt15/kvk/20201209/validation/kvk-balance-sheet-banks-for.xml, 
valueAssertion_BalanceSheetBanks_PrtFST1SumOfChildrenDParentDebit1, 
kvk-rpt-jaarverantwoording-2020-nlgaap-banken.xsd,
20210101 
CRLF

| Bestand | Formula localname | roleuri |entrypoint | datum buiten gebruik |
|-----------|-------------------|------------|----------------------|
|http://www.nltaxonomie.nl/nt15/kvk/20201209/validation/kvk-balance-sheet-banks-for.xml|valueAssertion_BalanceSheetBanks_PrtFST1SumOfChildrenDParentDebit1|"urn:kvk:linkrole:balance-sheet-banks"|kvk-rptjaarverantwoording-2020-nlgaap-banken.xsd|20210101|



Een scheiding van kolommen wordt aangegeven met een komma "," zoals beschreven in https://tools.ietf.org/html/rfc4180

## Publicatiemethoden
De lijst wordt alleen gepubliceerd als er daadwerkelijk formules zijn uitgezet. 
Er wordt dus geen lege lijst gepubliceerd voor elke gepubliceerde taxonomie. 
Zodra er wijzigingen zijn zal deze lijst worden gepubliceerd op:
https://www.nltaxonomie.nl/disabled_formulas/{NT versie}/{domein}/disabled_formulas.csv

Marktpartijen kunnen op de hoogte blijven door (geautomatiseerd) wijzigingen in deze bestanden te volgen. 
De markt wordt daarnaast via de gebruikelijke kanalen op de hoogte gesteld. 

