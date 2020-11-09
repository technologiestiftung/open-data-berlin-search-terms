# create dictionary that collects all unique terms
keep = {}

list_of_months = [
    #'2019-02','2019-03','2019-04','2019-05','2019-06',
    #'2019-07','2019-08','2019-09','2019-10','2019-11','2019-12',
    '2020-01','2020-02','2020-03','2020-04','2020-05', '2020-06','2020-07',
     '2020-08','2020-09','2020-10']

for tmp_month in list_of_months:
# load csv
    with open("data/all_months/initial_cleaning/clean_terms_all.csv", 'r') as f:
        # skip header
        for i, line in enumerate(f):
            if i == 0:
                continue
            id_, term, impressions, visits, month = line.strip().split(',')
            # remove quotemarks and cast to integers
            #id_ = id_[1:-1]
            #term = term[1:-1]
            impressions = int(impressions)
            visits = int(visits)
            #month = month[1:-1]
           # print(month)
           # print(tmp_month)
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
        with open('data/all_months/processed_al5/1_sum_term_keep_months_2020.csv', 'a') as newf:
            for term in keep.keys():
                fid, imp, vis, mon = keep[term]
                # add term to csv only if it has at least 2 impressions
                if imp > 4:
                    newf.write(f"{fid},{term},{imp},{vis},{mon}\n")
            f.close()
        keep = {}