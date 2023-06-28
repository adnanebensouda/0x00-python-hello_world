#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elim(elim):
        return (elim if elim != search else replace)
    return list(map(s_r_elim, my_list))
