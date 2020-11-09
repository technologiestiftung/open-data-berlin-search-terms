#### assign_categories.py

""" Run this script to assign categories of the open data portal to the terms.
Terms that have been assigned in a previous run, will be assigned automatically to the same category.
For all other terms: Type in the ID to assign the word to the appropriate category.
The results are saved automatically: 
terms_categories.csv is the input .csv, but with a new column that contains the categories.
categories.json stores your assigned words in lists
 """
 
import json

# Open the json file that includes already assigned lists of terms 
with open("code/categories.json", "r") as read_file:
    categories_list = json.load(read_file)

    # set new dictonairy to connect the categories with an id
    ids = {"1": "Arbeitsmarkt",
        "2": "Bildung",
        "3" : "Demographie",
        "4": "Geographie und Stadtplanung",
        "5": "Gesundheit",
        "6": "Jugend",
        "7": "Kunst und Kultur",
        "8": "Öffentliche Verwaltung, Haushalt und Steuern",
        "9": "Protokolle und Beschlüsse",
        "10": "Sonstiges",
        "11": "Sozialleistungen",
        "12": "Sport und Erholung",
        "13": "Tourismus",
        "14": "Umwelt und Klima",
        "15": "Ver- und Entsorgung",
        "16": "Verbraucherschutz",
        "17": "Verkehr",
        "18": "Wahlen",
        "19": "Wirtschaft",
        "20": "Wohnen und Immobilien"
        }

    term_dict = {}
    # load csv that includes the terms
    with open("data/all_months/processed_al5/1_sum_term_keep_months_2020.csv", 'r') as f:
        for line in f:
            id_, term, impressions, visits, mon = line.strip().split(',')
            for i, category in enumerate(categories_list.keys()):
                #print(i, term, category)
                if term in categories_list[category]:
                    term_dict[term,mon] = [id_, term, impressions, visits, category, mon]
                    print("The term '" + term +  "' is assigned to the category '" + category + "'")
                    break
                elif i == len(categories_list.keys())-1:
                    print("\n1 - Arbeitsmarkt , \n2 - Bildung , \n3 - Demographie, \n4 - Geographie und Stadtplanung, \n5 - Gesundheit, \n6 - Jugend, \n7 - Kunst und Kultur, \n8 - Öffentliche Verwaltung, Haushalt und Steuern, \n9 - Protokolle und Beschlüsse, \n10 - Sonstiges, \n11 - Sozialleistungen, \n12 - Sport und Erholung, \n13 - Tourismus, \n14 - Umwelt und Klima, \n15 - Ver- und Entsorgung, \n16 - Verbraucherschutz, \n17 - Verkehr, \n18 - Wahlen, \n19 - Wirtschaft, \n20 - Wohnen und Immobilien ")
                    print("\n'" + term +  "' has no category assigned yet.")
                    category_id = input("\nEnter category number to assign:")
                    print("\n")
                    while category_id not in ids.keys():
                        category_id = input("This is not a valid number. Please enter new number:")
                    category = ids[category_id] 
                    categories_list[category].append(term)
                    term_dict[term,mon] = [id_, term, impressions, visits, category, mon]
                    #print(categories_list)

            # save term with category to new csv
            with open('data/all_months/processed_al5/2_categorized_2020.csv', 'w') as newf:
                for term_mon in term_dict.keys():
                    fid, term, imp, vis, category, mon = term_dict[term_mon]
                    newf.write(f"{fid};{term};{imp};{vis};{category};{mon}\n")
            newf.close()

            # save assigned categories to json file
            with open("code/categories.json", "w") as write_file:
                json.dump(categories_list, write_file, indent =4)

