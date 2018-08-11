# StatsWordResultResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** | The number of times a word appears in the entire corpus | 
**lemma** | **str** | A lemma of the word (e.g., wordforms \&quot;lay\&quot;, \&quot;laid\&quot; and \&quot;laying\&quot; have all lemma \&quot;lay\&quot;) | [optional] 
**lexical_category** | **str** | A lexical category such as &#39;verb&#39; or &#39;noun&#39; | [optional] 
**match_count** | **int** | The number of database records that matched the query params (stated frequency is the sum of the individual frequencies) | 
**normalized_frequency** | **int** | The number of times a word appears on average in 1 million words | 
**true_case** | **str** | A given written realisation of a an entry (e.g., \&quot;lay\&quot;) usually lower case | [optional] 
**wordform** | **str** | A given written realisation of a an entry (e.g., \&quot;Lay\&quot;) preserving case | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


