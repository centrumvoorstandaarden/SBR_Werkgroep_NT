 
# Refereren aan niet-standaard linkbases
(overgenomen van wiki, nog niet herschreven.)

## Samenvatting

Niet-standaard linkbases (xxx specific resources en generic linkbases tussen resources) worden gerefereerd in het entrypoint schema. De xxx specific resource linkbases kunnen alternatief gerefereerd worden in het schema waarin de eigen domein specifieke concepten gedefinieerd worden. 

## Best Practice
Linkbases worden gerefereerd vanuit een XML Schema.
De 'standaard' linkbases worden gerefereerd vanuit het schema waarin de concepten gedefinieerd worden waarnaar deze linkbases refereren. Er zijn echter twee categorieën niet-standaard linkbases waarbij dit niet mogelijk is:

1. Linkbases met domain/entity/industry specific labels en references worden gedefinieerd in een domein dat concepten uit een ander domein hergebruikt. Het schema in dat andere domein kan daarvoor uiteraard niet worden aangepast.
2. De (generic) linkbases die resources relateren aan resources (uit een andere linkbase) hebben geen 'concept' schema waaruit ze gerefereerd worden. Dit geldt met name voor resources in de Formula en Table linkbases.

De best practice is dergelijke niet-standaard linkbases te refereren in het entrypoint schema. Dit schema refereert al de overige linkbases die de DTS vormen.
Beide categorieën linkbases kunnen op deze manier gerefereerd worden.

Voor de xxx specific resources is nog een alternatief mogelijk: deze kunnen eventueel ook gerefereerd worden vanuit het schema waarin de eigen domein specifieke concepten gedefinieerd worden.
Daarmee zijn dan alle linkbases met betrekking tot de definitie van concepten in hetzelfde schema opgenomen. 
