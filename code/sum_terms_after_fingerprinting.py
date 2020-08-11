# create dictionary that collects all unique terms
keep = {}
# load csv
with open("data/all_months/categorized.csv", 'r') as f:
    # skip header
    for i, line in enumerate(f):
        if i == 0:
            continue
        id_, term, impressions, visits, cat, month = line.strip().split(';')
        # remove quotemarks and cast to integers
        #id_ = id_[1:-1]
        #term = term[1:-1]
        impressions = int(impressions)
        visits = int(visits)
        # loop over every term and add to dictionary if not already in
        if term not in keep.keys():
            keep[term] = [id_, impressions, visits, cat]
        # if term is already in dictionary, don't add, but sum up the impression and visit count to existing occurence
        else:
            fid, imp, vis, cat = keep[term]
            imp += impressions
            vis += visits
            keep[term] = [fid, imp, vis, cat]
    f.close()
    
# save dictionary to new csv
with open('data/all_months/categorized_summed.csv', 'w') as newf:
    for term in keep.keys():
        fid, imp, vis, cat = keep[term]
        # add term to csv only if it has at least 2 impressions
        if imp > 1:
            newf.write(f"{fid};{term};{imp};{vis};{cat}\n")