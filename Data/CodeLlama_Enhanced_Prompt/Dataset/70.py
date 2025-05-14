def strange_sort_list(lst):
    res = []
    while lst:
        if len(lst) == 1:
            res.append(lst.pop())
        else:
            if res:
                res.append(max(lst) if max(lst) > min(lst) else min(lst))
            else:
                res.append(min(lst))
            lst.remove(res[-1])
    return res
