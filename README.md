# Open Data Berlin - Search terms

This repository contains scripts for processing the open dataset of search terms in the [Open Data Portal Berlin](https://daten.berlin.de).

The original dataset and its documentation can be found here: https://daten.berlin.de/datensaetze/suchbegriffe-datenberlinde. It contains all search terms and their impressions and visits per month.

## Usage

#### Initial cleaning:
Run the *odis_keywords.r* script with the original dataset as input data. The script applies the following sub-steps to the data:
- splitting search terms
- removing spaces and punctuation
- stemming
- merging of equal terms

Combine data from diffrent months if needed and add month attribute with *merge_all_months.py*. We also filtered the data to terms with impressions of at least 5.

#### KNN/ Neighbour-Analysis:
Use [this web application](https://lab.technologiestiftung-berlin.de/projects/csv-string-optimization/de/) from Technologiestiftung Berlin for usage of KNN/ Neighbour-Analysis on results, to find more similiar but not equal terms, for example because of typos.
Run *1_sum_term_keep_months.py* to sum up impressions and visits of terms.

#### Assign categories of to terms:
Run *2_assign_categories.py* to assign categories of the open data portal to the terms.
Terms that have been assigned in a previous run, will be assigned automatically to the same category, because there are stored in *categories.json*.
For all other terms: Type in the ID to assign the word to the appropriate category.
The results are saved immediately in *2_categorized.csv*.

#### Prepare for analysis:
Use Python-Script 3a, 3b, 3c to generate diffrent information on occurence of searchterms by months and categories.
