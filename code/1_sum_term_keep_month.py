# create dictionary that collects all unique terms
keep = {}

list_of_months = ['2020-06','2020-07']

for tmp_month in list_of_months:
# load csv
    with open("data/clean_terms_all2_5.csv", 'r') as f:
        # skip header
        for i, line in enumerate(f):
            if i == 0:
                continue
            id_, term, impressions, visits, month = line.strip().split(',')
            # remove quotemarks and cast to integers
            id_ = id_[1:-1]
            term = term[1:-1]
            impressions = int(impressions[1:-1])
            visits = int(visits[1:-1])
            month = month[1:-1]
            print(month)
            print(tmp_month)
            if month == tmp_month:
                # loop over every term and add to dictionary if not already in
                if term not in keep.keys():
                    keep[term] = [id_, impressions, visits, month]
                # if term is already in dictionary, don't add, but sum up the impression and visit count to existing occurence
                else:
                    fid, imp, vis, mon = keep[term]
                    imp += impressions
                    vis += visits
                    keep[term] = [fid, imp, vis, mon]
        f.close()
        
        # save dictionary to new csv
        with open('data/all_months/processed_al5/1_sum_term_keep_months.csv', 'a') as newf:
            for term in keep.keys():
                fid, imp, vis, mon = keep[term]
                # add term to csv only if it has at least 2 impressions
                if imp > 4:
                    newf.write(f"{fid},{term},{imp},{vis},{mon}\n")
            f.close()
        keep = {}