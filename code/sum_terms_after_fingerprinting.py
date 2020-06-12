# create dictionary that collects all unique terms
keep = {}
# load csv
with open("data/clean_term_phon_fingerpr.csv", 'r') as f:
    # skip header
    for i, line in enumerate(f):
        if i == 0:
            continue
        id_, term, impressions, visits = line.strip().split(',')
        # remove quotemarks and cast to integers
        id_ = id_[1:-1]
        term = term[1:-1]
        impressions = int(impressions[1:-1])
        visits = int(visits[1:-1])
        # loop over every term and add to dictionary if not already in
        if term not in keep.keys():
            keep[term] = [id_, impressions, visits]
        # if term is already in dictionary, don't add, but sum up the impression and visit count to existing occurence
        else:
            fid, imp, vis = keep[term]
            imp += impressions
            vis += visits
            keep[term] = [fid, imp, vis]
    f.close()
# save dictionary to new csv
with open('data/summed_terms_after_fingerpr.csv', 'w') as newf:
    for term in keep.keys():
        fid, imp, vis = keep[term]
        newf.write(f"{fid},{term},{imp},{vis}\n")