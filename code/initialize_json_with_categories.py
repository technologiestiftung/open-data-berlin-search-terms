import json

# Open the json file that includes already assigned lists of terms 
with open("code/categories.json", "r") as read_file:
    categories_list = json.load(read_file)


    term_dict = {}
    # load csv that includes the terms
    with open("data/test_2020-05/comparison_categories_2020-05.csv", 'r') as f:
        for line in f:
            id_, term, cat, diff = line.strip().split(';')
            for i, category in enumerate(categories_list.keys()):
                #print(i, term, category)
                if cat == category:
                    categories_list[category].append(term)
                    print(categories_list)
            

    # save assigned categories to json file
    with open("data/test_2020-05/categories_2020-05.json", "w") as write_file:
        json.dump(categories_list, write_file, indent =4)


