# N ** 2
def strcounter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
        
# strcounter('яшалава')


# N * M

def strcounter2(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
        
                    
# strcounter2('яшалава')


#  N


def strcounter3(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
        
    for sym, count in syms_counter.items():
        print(sym, count)
        
strcounter3('яшалава')