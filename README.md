# Open Data Berlin - Search terms

This repository contains scripts for processing the open dataset of search terms in the [Open Data Portal Berlin](https://daten.berlin.de).

The original dataset and its documentation can be found here: https://daten.berlin.de/datensaetze/zugriffsstatistik-datenberlinde. It contains all search terms and their impressions and visits per month.

## Usage

#### Step 1:
Run the *odis_keywords.r* script with the original dataset as input data. The script applies the following sub-steps to the data:
- splitting search terms
- removing spaces and punctuation
- stemming
- merging of similiar terms

#### Step 2:
Use [this web application](https://lab.technologiestiftung-berlin.de/projects/csv-string-optimization/de/) from Technologiestiftung Berlin for phonetic fingerprinting on results.
Run *sum_terms_after_fingerprinting.py* to sum up impressions and visits of terms.

#### Step 3:
Run *assign_categories.py* to assign categories of the open data portal to the terms.
Terms that have been assigned in a previous run, will be assigned automatically to the same category.
For all other terms: Type in the ID to assign the word to the appropriate category.
The results are saved automatically in *terms_categories.csv*.
