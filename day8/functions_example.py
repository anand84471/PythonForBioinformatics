from function_example import calculate_gc_percent

seq="ATAAAA"
print(calculate_gc_percent(seq))


def calculate_avg_gc_percent(seq1,seq2):
    return (calculate_gc_percent(seq1)+calculate_gc_percent(seq2))/2


seq1="AAAA"
seq2="GCAA"
print(calculate_avg_gc_percent(seq1,seq2))





