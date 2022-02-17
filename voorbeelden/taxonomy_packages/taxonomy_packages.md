# Taxonomy packages
Een Taxonomy Package (TP) is een ZIP bestand met daarin een XBRL taxonomy. Een TP bevat gestandaardiseerde metadata waarmee het XBRL processors op eenvoudige wijze de gehele taxonomie kunnen inlezen. Ook bevat deze metadata extra informatie dat niet in de taxonomie zelf is te vinden.

De onderliggende specificaties zijn te vinden op de website van XBRL International:
https://www.xbrl.org/Specification/taxonomy-package/REC-2016-04-19/taxonomy-package-REC-2016-04-19.html


Onderstaand voorbeeld is een greep uit een taxonomyPackage.xml bestand zoals gebruikt in de NT:
```xml
    <?xml version="1.0" encoding="UTF-8"?>
        <tp:taxonomyPackage xml:lang="nl" xmlns:tp="http://xbrl.org/2016/taxonomy-package" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://xbrl.org/2016/taxonomy-package http://xbrl.org/2016/taxonomy-package.xsd">
        <tp:identifier>nt16</tp:identifier>
        <tp:name>Nederlandse Taxonomie 16</tp:name>
        <tp:description>De Nederlandse Taxonomie bevat de rapportages binnen Standard Business Reporting in Nederland.</tp:description>
        <tp:version>20220128</tp:version>
        <tp:publisher>SBR Programma</tp:publisher>
        <tp:publisherURL>http://www.nltaxonomie.nl</tp:publisherURL>
        <tp:publisherCountry>NL</tp:publisherCountry>
        <tp:publicationDate>2022-01-28</tp:publicationDate>
	<tp:entryPoints>
        <tp:entryPoint>
                <tp:name>JenV: Besluit actuele waarde</tp:name>
                <tp:description>Besluit actuele waarde</tp:description>
                <tp:version>20211208</tp:version>
                <tp:entryPointDocument href="http://www.nltaxonomie.nl/nt16/jenv/20211208/entrypoints/jenv-rpt-bw2-besluit-actuele-waarde.xsd"/>
            </tp:entryPoint>
            <tp:entryPoint>
                <tp:name>JenV: Besluit artikel 10 overnamerichtlijn</tp:name>
                <tp:description>Besluit artikel 10 overnamerichtlijn</tp:description>
                <tp:version>20211208</tp:version>
                <tp:entryPointDocument href="http://www.nltaxonomie.nl/nt16/jenv/20211208/entrypoints/jenv-rpt-bw2-besluit-artikel-10-overnamerichtlijn.xsd"/>
            </tp:entryPoint>
            <tp:entryPoint>
                <tp:name>BD: Omzetbelasting 2022</tp:name>
                <tp:description>Omzetbelasting 2022</tp:description>
                <tp:version>20211208</tp:version>
                <tp:entryPointDocument href="http://www.nltaxonomie.nl/nt16/bd/20211208/entrypoints/bd-rpt-ob-aangifte-2022.xsd"/>
            </tp:entryPoint>
            <tp:entryPoint>
                <tp:name>BD: Suppletie Omzetbelasting 2022</tp:name>
                <tp:description>Suppletie Omzetbelasting 2022</tp:description>
                <tp:version>20211208</tp:version>
                <tp:entryPointDocument href="http://www.nltaxonomie.nl/nt16/ bd/20211208/entrypoints/bd-rpt-ob-suppletie-2022.xsd"/>
            </tp:entryPoint>
        </tp:entryPoints>
    </tp:taxonomyPackage>
```

Binnen de NT is de naam en omschrijving per entrypoint is niet beschikbaar binnen de taxonomie zelf. Ook is de versie alleen af te leiden van delen van namespaces of uit de directorystructuur. Dit meta-bestand levert daarom waardevolle informatie. Ook informatie over de aanwezige talen is niet (direct) uit de taxonomie op te maken.

## Remappings
Een functie van taxonomy packages dat enigsinds onderbelicht blijft in de orginele specificaties is het toepassen van remappings. Een taxonomy package kan namelijk extra (externe) taxonomie informatie bevatten. Omdat er vanuit de taxonomie middels absolute paden naar wordt gerefereerd, moet deze worden geremapped naar relatieve paden. Een taxonomie processor/parser moet hiermee om kunnen gaan.
