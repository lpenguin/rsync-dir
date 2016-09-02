from collections import Iterable


def flatten(ls):
    # type: (list)->list

    res = []
    for xs in ls:
        if not isinstance(xs, str) and isinstance(xs, Iterable):
            for x in xs:
                res.append(x)
        else:
            res.append(xs)
    return res
