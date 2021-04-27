def get_length(sequence):
    return len(sequence)


def get_gc_percentage(sequence):
    return 100*(sequence.count("G")+sequence.count("C"))/len(sequence)


