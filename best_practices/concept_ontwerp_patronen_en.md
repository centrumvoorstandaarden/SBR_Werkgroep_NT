 
# Concept design patterns
(copied from wiki, not yet checked/rewritten. Last modification on wiki 2016)

## Summary

Concepts are not standardized by means of their hierarchical path. In dimensional modelling meaning is transferred to the dimension. This will only be done when standardisation can be used in seeral reportable elements.

Based on 'common practice' a number of standardized values for dimensions is used. 
## Best Practice
An important criterion of XBRL (in contrast with the modelling standard) is that the elements are NOT standardised by means of their hierarchical path. The meaning of an element is given in the @name of an element and is therefore NOT (partially) transferred to a potentially older element (in XSD a complexType, in XBRL a tuple).

In XBRL dimensional modelling, part of the meaning that is expressed in the @name IS transferred to the dimension and the domain member. Therefore in this latter method, in extreme circumstances these are standardised to such an extent that ultimately only a set of datatypes remain as an element. The dimensional modelling that is scoring a hit in Europe -Data Point Modelling (DPM)- is not being adopted in its entirety. This method primarily works in a 'closed community', such as the central banks with their commercial banks. The community is limited in size and all parties know exactly what has to be reported and speak to one another about this in code as table codes and cell codes. In such a situation, 'self-explanatory' element names, which are required by XBRL, are no longer necessary. XBRL modelling is based on a large community (all companies) that have to report but which are far from familiar with the exact data set that is requested. Furthermore, these parties can design their own extensions. In this type of community, the elements that are used have to be clarified simply (the @name) and not by taking several dimensional relationships together (such as in DPM).

Based on common practice in the world of financial annual reporting for commercial companies, a number of dimensions have also been identified by the IASB, FASB and JFSA, which each GAAP report should contain:

- Components of tangible fixed assets (ClassesOfAssets)
- Components of intangible fixed assets (ClassesOfIntangibleAssets)
- Components of financial fixed assets (ClassesOfFinancialAssets)
- Components of fixed assets (ClassesOfPropertyPlantAndEquipment)
- Components of liabilities (ClassesOfLiabilities)

Unfortunately the standardisation is not yet so advanced that similar element names are used for the dimensions. SBR-NL follows IFRS insofar as applicable. Because balance sheet information is often part of a financial accounting report, it is expected that every Dutch Taxonomy partner will try to concur with the views expressed by the GAAP reports in this respect.

- The Dutch Taxonomy Architecture follows the XBRL method of modelling in which tuples are NOT part of the standardisation of elements.
- The Dutch Taxonomy Architecture sets as a limit to the XBRL dimensional way of modelling that domain members can ONLY be considered to be standardisation based on an element @name IF this domain member can be used in several reportable elements.
