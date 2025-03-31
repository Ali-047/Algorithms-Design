def jacard_similatary(set1,set2):
    intersection  = len(set(set1).intersection(set2))
    union = len(set(set1).union(set2))
    return intersection / union