def to_rna(dna_strand):
    dna_rna= dict(
        G = 'C',
        C = 'G',
        T = 'A',
        A = 'U')

    rna_eq=[]
    for i in dna_strand:
        rna_eq.append(dna_rna[i])

    return ''.join(rna_eq)