# create dictionary that collects all unique terms
keep = {}

list_of_months = ['2019-02','2019-03','2019-04','2019-05','2019-06', '2019-07','2019-08','2019-09','2019-10','2019-11','2019-12','2020-01','2020-02','2020-03','2020-04','2020-05']

for tmp_month in list_of_months:
# load csv
    with open("data/all_months/categorized.csv", 'r') as f:
        # skip header
        for i, line in enumerate(f):
            if i == 0:
                continue
            id_, term, impressions, visits, cat, month = line.strip().split(';')
            # remove quotemarks and cast to integers
            impressions = int(impressions)
            visits = int(visits)
            print(month)
            print(tmp_month)
            if month == tmp_month:
                # loop over every cat and add to dictionary if not already in
                if cat not in keep.keys():
                    keep[cat] = [id_, impressions, visits, month]
                # if cat is already in dictionary, don't add, but sum up the impression and visit count to existing occurence
                else:
                    fid, imp, vis, mon = keep[cat]
                    imp += impressions
                    vis += visits
                    keep[cat] = [fid, imp, vis, mon]
        f.close()
        
        # save dictionary to new csv
        with open('data/all_months/summed_cat_by_month.csv', 'a') as newf:
            for cat in keep.keys():
                fid, imp, vis, mon = keep[cat]
                newf.write(f"{fid};{cat};{imp};{vis};{mon}\n")
            f.close()
        keep = {}