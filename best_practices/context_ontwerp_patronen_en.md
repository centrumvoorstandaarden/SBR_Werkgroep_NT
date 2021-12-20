 
# Context design patterns
(copied from wiki, not yet checked/rewritten. Last modification on wiki 2016)

## Summary

Context information (reporting entity, period, dimensions, ...) may not be part of an XBRL element name.

In addition a number of dimensions is modelled that have to be followed by all Dutch Taxonomy parners.

## Best Practice
Modelling templates can be addressed from a report or from the form that underlies the report. An important aspect of standardisation is that the XBRL context information that may NOT be present in the elements. Context information is: the reporting entity (usually a company), the period that is being reported, and the entity in which a report is made EACH ELEMENT and potentially dimensionally modelled parts. Examples of semantic terms that therefore may NOT be used in the XBRL element names are:

- Holding
- Subsidiary
- Previous year/period * End of the year/period
- In Euros
- In kilos

In addition there are now a number of dimensions modelled in the Dutch Taxonomy that HAVE to be followed by all Dutch Taxonomy partners:

- Basis of the valuation (with the commercial and tax members)
- Reporting format (with the consolidated and separate members)(ConsolidatedAndSeparateFinancialStatements)
