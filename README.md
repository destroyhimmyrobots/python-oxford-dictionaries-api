# oxford-dictionaries-api
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.11.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import oxford_dictionaries_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import oxford_dictionaries_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import oxford_dictionaries_api
from oxford_dictionaries_api.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = oxford_dictionaries_api.DictionaryEntriesApi()
source_lang = 'source_lang_example' # str | IANA language code
word_id = 'word_id_example' # str | An Entry identifier. Case-sensitive.
filters = ['filters_example'] # list[str] | Separate filtering conditions using a semicolon. Conditions take values grammaticalFeatures and/or lexicalCategory and are case-sensitive. To list multiple values in single condition divide them with comma.
app_id = '' # str | App ID Authentication Parameter (default to )
app_key = '' # str | App Key Authentication Parameter (default to )

try:
    # Apply filters to response
    api_response = api_instance.entries_source_lang_word_id_filters_get(source_lang, word_id, filters, app_id, app_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryEntriesApi->entries_source_lang_word_id_filters_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://od-api.oxforddictionaries.com:443/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DictionaryEntriesApi* | [**entries_source_lang_word_id_filters_get**](docs/DictionaryEntriesApi.md#entries_source_lang_word_id_filters_get) | **GET** /entries/{source_lang}/{word_id}/{filters} | Apply filters to response
*DictionaryEntriesApi* | [**entries_source_lang_word_id_get**](docs/DictionaryEntriesApi.md#entries_source_lang_word_id_get) | **GET** /entries/{source_lang}/{word_id} | Retrieve dictionary information for a given word
*DictionaryEntriesApi* | [**entries_source_lang_word_id_regionsregion_get**](docs/DictionaryEntriesApi.md#entries_source_lang_word_id_regionsregion_get) | **GET** /entries/{source_lang}/{word_id}/regions&#x3D;{region} | Specify GB or US dictionary for English entry search
*LemmatronApi* | [**inflections_source_lang_word_id_filters_get**](docs/LemmatronApi.md#inflections_source_lang_word_id_filters_get) | **GET** /inflections/{source_lang}/{word_id}/{filters} | Apply optional filters to Lemmatron response
*LemmatronApi* | [**inflections_source_lang_word_id_get**](docs/LemmatronApi.md#inflections_source_lang_word_id_get) | **GET** /inflections/{source_lang}/{word_id} | Check a word exists in the dictionary and retrieve its root form
*LexiStatsApi* | [**stats_frequency_ngrams_source_lang_corpus_ngram_size_get**](docs/LexiStatsApi.md#stats_frequency_ngrams_source_lang_corpus_ngram_size_get) | **GET** /stats/frequency/ngrams/{source_lang}/{corpus}/{ngram-size}/ | Retrieve the frequency of ngrams (1-4) derived from a corpus
*LexiStatsApi* | [**stats_frequency_word_source_lang_get**](docs/LexiStatsApi.md#stats_frequency_word_source_lang_get) | **GET** /stats/frequency/word/{source_lang}/ | Retrieve the frequency of a word derived from a corpus.
*LexiStatsApi* | [**stats_frequency_words_source_lang_get**](docs/LexiStatsApi.md#stats_frequency_words_source_lang_get) | **GET** /stats/frequency/words/{source_lang}/ | Retrieve a list of frequencies of a word/words derived from a corpus.
*SearchApi* | [**search_source_lang_get**](docs/SearchApi.md#search_source_lang_get) | **GET** /search/{source_lang} | Retrieve possible matches to input
*SearchApi* | [**search_source_search_language_translationstarget_search_language_get**](docs/SearchApi.md#search_source_search_language_translationstarget_search_language_get) | **GET** /search/{source_search_language}/translations&#x3D;{target_search_language} | Retrieve possible translation matches to input
*TheSentenceDictionaryApi* | [**entries_source_language_word_id_sentences_get**](docs/TheSentenceDictionaryApi.md#entries_source_language_word_id_sentences_get) | **GET** /entries/{source_language}/{word_id}/sentences | Retrieve corpus sentences for a given word
*ThesaurusApi* | [**entries_source_lang_word_id_antonyms_get**](docs/ThesaurusApi.md#entries_source_lang_word_id_antonyms_get) | **GET** /entries/{source_lang}/{word_id}/antonyms | Retrieve words that mean the opposite
*ThesaurusApi* | [**entries_source_lang_word_id_synonyms_get**](docs/ThesaurusApi.md#entries_source_lang_word_id_synonyms_get) | **GET** /entries/{source_lang}/{word_id}/synonyms | Retrieve words that are similar
*ThesaurusApi* | [**entries_source_lang_word_id_synonymsantonyms_get**](docs/ThesaurusApi.md#entries_source_lang_word_id_synonymsantonyms_get) | **GET** /entries/{source_lang}/{word_id}/synonyms;antonyms | Retrieve synonyms and antonyms for a given word
*TranslationApi* | [**entries_source_translation_language_word_id_translationstarget_translation_language_get**](docs/TranslationApi.md#entries_source_translation_language_word_id_translationstarget_translation_language_get) | **GET** /entries/{source_translation_language}/{word_id}/translations&#x3D;{target_translation_language} | Retrieve translation for a given word
*UtilityApi* | [**domains_source_domains_language_target_domains_language_get**](docs/UtilityApi.md#domains_source_domains_language_target_domains_language_get) | **GET** /domains/{source_domains_language}/{target_domains_language} | Lists available domains in a bilingual dataset
*UtilityApi* | [**domains_source_language_get**](docs/UtilityApi.md#domains_source_language_get) | **GET** /domains/{source_language} | Lists available domains in a monolingual dataset
*UtilityApi* | [**filters_endpoint_get**](docs/UtilityApi.md#filters_endpoint_get) | **GET** /filters/{endpoint} | Lists available filters for specific endpoint
*UtilityApi* | [**filters_get**](docs/UtilityApi.md#filters_get) | **GET** /filters | Lists available filters
*UtilityApi* | [**grammatical_features_source_language_get**](docs/UtilityApi.md#grammatical_features_source_language_get) | **GET** /grammaticalFeatures/{source_language} | Lists available grammatical features in a dataset
*UtilityApi* | [**languages_get**](docs/UtilityApi.md#languages_get) | **GET** /languages | Lists available dictionaries
*UtilityApi* | [**lexicalcategories_language_get**](docs/UtilityApi.md#lexicalcategories_language_get) | **GET** /lexicalcategories/{language} | Lists available lexical categories in a dataset
*UtilityApi* | [**regions_source_language_get**](docs/UtilityApi.md#regions_source_language_get) | **GET** /regions/{source_language} | Lists available regions in a monolingual dataset
*UtilityApi* | [**registers_source_language_get**](docs/UtilityApi.md#registers_source_language_get) | **GET** /registers/{source_language} | Lists available registers in a  monolingual dataset
*UtilityApi* | [**registers_source_register_language_target_register_language_get**](docs/UtilityApi.md#registers_source_register_language_target_register_language_get) | **GET** /registers/{source_register_language}/{target_register_language} | Lists available registers in a bilingual dataset
*WordlistApi* | [**wordlist_source_lang_filters_advanced_get**](docs/WordlistApi.md#wordlist_source_lang_filters_advanced_get) | **GET** /wordlist/{source_lang}/{filters_advanced} | Retrieve list of words for category with advanced options
*WordlistApi* | [**wordlist_source_lang_filters_basic_get**](docs/WordlistApi.md#wordlist_source_lang_filters_basic_get) | **GET** /wordlist/{source_lang}/{filters_basic} | Retrieve a list of words in a category


## Documentation For Models

 - [ArrayOfRelatedEntries](docs/ArrayOfRelatedEntries.md)
 - [ArrayOfRelatedEntriesInner](docs/ArrayOfRelatedEntriesInner.md)
 - [Arrayofstrings](docs/Arrayofstrings.md)
 - [CategorizedTextList](docs/CategorizedTextList.md)
 - [CategorizedTextListInner](docs/CategorizedTextListInner.md)
 - [CrossReferencesList](docs/CrossReferencesList.md)
 - [CrossReferencesListInner](docs/CrossReferencesListInner.md)
 - [Entry](docs/Entry.md)
 - [ExamplesList](docs/ExamplesList.md)
 - [ExamplesListInner](docs/ExamplesListInner.md)
 - [Filters](docs/Filters.md)
 - [FiltersResults](docs/FiltersResults.md)
 - [GrammaticalFeaturesList](docs/GrammaticalFeaturesList.md)
 - [GrammaticalFeaturesListInner](docs/GrammaticalFeaturesListInner.md)
 - [HeadwordEntry](docs/HeadwordEntry.md)
 - [HeadwordLemmatron](docs/HeadwordLemmatron.md)
 - [HeadwordThesaurus](docs/HeadwordThesaurus.md)
 - [InflectionsList](docs/InflectionsList.md)
 - [InflectionsListInner](docs/InflectionsListInner.md)
 - [Languages](docs/Languages.md)
 - [LanguagesResults](docs/LanguagesResults.md)
 - [LanguagesSourceLanguage](docs/LanguagesSourceLanguage.md)
 - [LanguagesTargetLanguage](docs/LanguagesTargetLanguage.md)
 - [Lemmatron](docs/Lemmatron.md)
 - [LemmatronLexicalEntry](docs/LemmatronLexicalEntry.md)
 - [LexicalEntry](docs/LexicalEntry.md)
 - [NgramsResult](docs/NgramsResult.md)
 - [NgramsResultResults](docs/NgramsResultResults.md)
 - [PronunciationsList](docs/PronunciationsList.md)
 - [PronunciationsListInner](docs/PronunciationsListInner.md)
 - [Regions](docs/Regions.md)
 - [RetrieveEntry](docs/RetrieveEntry.md)
 - [Sense](docs/Sense.md)
 - [SentencesEntry](docs/SentencesEntry.md)
 - [SentencesLexicalEntry](docs/SentencesLexicalEntry.md)
 - [SentencesResults](docs/SentencesResults.md)
 - [StatsWordResult](docs/StatsWordResult.md)
 - [StatsWordResultList](docs/StatsWordResultList.md)
 - [StatsWordResultListResults](docs/StatsWordResultListResults.md)
 - [StatsWordResultResult](docs/StatsWordResultResult.md)
 - [SynonymsAntonyms](docs/SynonymsAntonyms.md)
 - [SynonymsAntonymsInner](docs/SynonymsAntonymsInner.md)
 - [Thesaurus](docs/Thesaurus.md)
 - [ThesaurusEntry](docs/ThesaurusEntry.md)
 - [ThesaurusLexicalEntry](docs/ThesaurusLexicalEntry.md)
 - [ThesaurusLink](docs/ThesaurusLink.md)
 - [ThesaurusSense](docs/ThesaurusSense.md)
 - [TranslationsList](docs/TranslationsList.md)
 - [TranslationsListInner](docs/TranslationsListInner.md)
 - [UtilityLabels](docs/UtilityLabels.md)
 - [UtilityLabelsResults](docs/UtilityLabelsResults.md)
 - [VariantFormsList](docs/VariantFormsList.md)
 - [VariantFormsListInner](docs/VariantFormsListInner.md)
 - [Wordlist](docs/Wordlist.md)
 - [WordlistResults](docs/WordlistResults.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



