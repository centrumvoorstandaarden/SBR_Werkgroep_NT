# Context ontwerp patronen 
(overgenomen van wiki, nog niet herschreven)

## Samenvatting
Context informatie (rapporterende eenheid, periode, dimensies, ...) mag niet in XBRL elementnamen voor komen.

Er is daarnaast een aantal dimensies gemodelleerd die door alle NT partners gevolgd moeten worden. 

## Best practice

Modelleer patronen kunnen benaderd worden vanuit een rapportage of vanuit het formulier dat de rapportage vorm geeft. Een belangrijke normaliseringsslag is de XBRL context informatie die NIET aanwezig mag zijn in de elementen. Context informatie is: de rapporterende eenheid (meestal een bedrijf), de periode waarover gerapporteerd wordt, en de eenheid waarin gerapporteerd wordt PER ELEMENT en eventuele dimensioneel gemodelleerde onderdelen. Voorbeelden van semantische begrippen die dus NIET in de XBRL elementnamen mogen voorkomen zijn:

- Holding
- Dochter
- Vorig rapportage jaar / periode
- Eind van het rapportage jaar / periode
- In Euro
- In kilo's

Daarnaast is er inmiddels een aantal dimensies in de NT gemodelleerd die door alle NT partners gevolgd MOETEN worden:

- Waarderingsgrondslag (met de leden commercieel en fiscaal)
- Rapportagevorm (met de leden geconsolideerd en enkelvoudig)(ConsolidatedAndSeparateFinancialStatements)
