 
# XBRL Formula best practices
(copied from wiki, not yet checked/rewritten. Last modification on wiki 2016)

## Summary

Several best practices about XBRL Formula on the use of the building blocks and naming conventions. 

## Best Practice


XBRL Formulas can be used to check the content of instances. It is also possible to create new instances in which results of calculations can be placed. The specification is based on building XPath expressions and uses the functions of XQuery. This is recorded as a whole as resources in a (generic) linkbase. For processing, a certified XBRL Formula engine is required.

The XBRL formula specification works with a so-called 'aspects model. This is a model where the reported fact is assumed (say: 2000) that has linked aspects in the instance. Some aspects are the unit, the @decimals, the concept name and the (content of the) context. By using, for example, the concept name, its type, label and place of presentation can be discovered. This information encompasses aspects that may or may not be of importance when determining the verification. An easy example is: add the values of A and B together and see if this totals more than zero. This verification is, of course, only worthwhile if the values of A and B have the same unit and context! 

### Bouwstenen
Formula, FormulaTuple, ConsistencyAssertion, ValueAssertion, ExistenceAssertion. These are the five start options of an XBRL formula. In the Dutch Taxonomy we only allow valueAssertion and ExistenceAssertion.
When a field is unconditionally mandatory the usage of a fn: exists () result as an @test of a value assertion, is discouraged. because the existenceAssertion is intended for this porpose. In a precondition in combination with a existenceAssertion problems can occur with the precondition. In that case, a value assertion with fn:exists() is preferred. Assertions that do not give a result are discouraged. Give the assertions a unique (in time) established identification, so that a refference can be added to the error message and any documentation.
GeneralVariable and FactVariable. These are the variables that will be filled with values. GeneralVariable has no aspects; these are 'bare' values. FactVariable are given all aspects that can be discovered.
Filters. For each aspect, the specification has its own filter, so that this can be used for the range of facts included in the instance. The 'inverse' can be used for each filter if that is more practical. The Dutch Taxonomy allows all filters.

Implicit filtering. This ensures that when a formula is evaluated sets are formed of FactVariables for which aspects have equal values. For example, only the amounts of the same unit are included in a calculation. If it is desirable to disable this mechanism for a particular aspect, that specific aspect has to be covered. Also, the inclusion of an explicit filter with a FactVariable leads to the covering of that aspect. Implicit filtering does still apply to all other aspects in this formula.
Fallback values. The pairing of a fallback value to a FactVariable ensures that an evaluation of a formula, in which implicit filtering is used, may also take place when not all FactVariabeles actually occur in an instance with a value. At least 1 FactVariable with a "true" value must be included in the instance in order to lead to the evaluation of the rule.

Preconditions and parameters. These are aids for effective formulas. The precondition first determines whether a basic condition is met before execution can take place. Parameters are actually the same as generalVariables, with the exception that they can be used on top of formulas. Because the values that represent parameters make the maintenance of formulas more arduous, it is recommended that the parameter values are stored outside of the formula in an XML file. The value can be addressed with a fn:doc() function in the formula.
Messages. An important part of a verification is the error message and how exact this is, in order to help resolve the problem. The Dutch Taxonomy states that every verification has to send a message in every case, otherwise it cannot be stated that the verification has helped. In the message, all aspects can be worked with that are involved in the evaluation.
Labels and References. Each formula can, of course, be given (generic) labels and references. The Dutch Taxonomy states that a reference is mandatory. This has to reference the documentation concerning exactly what the verification is trying to achieve. 

### Naming
The Dutch Taxonomy has not yet laid down any naming conventions for all components that are used. It is obvious that if the formulas are drawn up manually and have to be verified, it is useful to use a naming convention. It would, however, be wise to generate formulas using a tool. In that case, the names of the linked resources are less important.
Rules have been laid down for the names of the linkbase files and the folders. 
