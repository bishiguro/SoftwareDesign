# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Bonnie Ishiguro
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    dna_seq = [] # creates an array of the amino acids coded in the DNA strand
    for i in range(len(dna)):       
        if i % 3 == 0:
            dna_seq.append(dna[i:i+3])
            
    aa_sequence = ""
    for i in dna_seq: # for each amino acid coded in the sequence
        for j in codons: # for each group of codons that synthesis a certain protein
            for k in codons[codons.index(j)]: # for each codon in each group
                if i == k:                              
                    aa_sequence = aa_sequence + aa[codons.index(j)]
    return aa_sequence # amino acid sequence
    
def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    print "input: AAA, expected output: K, actual output: " + coding_strand_to_AA("AAA")
    print "input: TTCCGC, expected output: FR, actual output: " + coding_strand_to_AA("TTCCGC")
    print "input: BBB, expected output: , actual output: " + coding_strand_to_AA("BBB") # invalid input
    print "input: TGGA, expected output: W, actual output: " + coding_strand_to_AA("TGGA") # number of nucleotides not a multiple of 3  
    
def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    rev_comp = ""
    for i in reversed(dna):
        if i == "T":
            rev_comp += "A"
        elif i == "A":
            rev_comp += "T"
        elif i == "C":
            rev_comp += "G"
        elif i == "G":
            rev_comp += "C"
    return rev_comp
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print "input: TGA, expected output: TCA, actual output: " + get_reverse_complement("TGA")
    print "input: CGCATG, expected output: CATGCG, actual output: " + get_reverse_complement("CGCATG")
    print "input: BAB, expected output: T, actual output: " + get_reverse_complement("BAB")  
    
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    dna_seq = [] # creates an array of the amino acids coded in the DNA strand
    for i in range(len(dna)):       
        if i % 3 == 0:
            dna_seq.append(dna[i:i+3])
    stop_codons = ["TAG", "TAA", "TGA"]    
    orf = ""
    
    for i in range(len(dna_seq)):
        for j in range(len(stop_codons)):
            if dna_seq[i] == stop_codons[j]:
                return orf
        orf += dna_seq[i]
    return orf

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    print "input: AAATAG, expected output: AAA, actual output: " + rest_of_ORF("AAATAG")
    print "input: AAATGA, expected output: AAA, actual output: " + rest_of_ORF("AAATAG")        
    print "input: AAATAA, expected output: AAA, actual output: " + rest_of_ORF("AAATAA")
    print "input: AAA, expected output: AAA, actual output: " + rest_of_ORF("AAA")
    print "input: TAG, expected output: , actual output: " + rest_of_ORF("TAG")
    
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    dna_seq = [] # creates an array of the amino acids coded in the DNA strand
    for i in range(len(dna)):       
        if i % 3 == 0:
            dna_seq.append(dna[i:i+3])  
    orf_oneframe = []
    start_codon = "ATG"
    
    i = 0
    while i < len(dna_seq):      
        if dna_seq[i] == start_codon:
            for j in range(i,len(dna_seq)):
                if dna_seq[j] == "TAG" or dna_seq[j] == "TAA" or dna_seq[j] == "TGA": # stop codons
                    orf_oneframe.append(dna_seq[i:j])                
                    i = j                    
                    break
        i+=1
        
    for x in range(len(orf_oneframe)):
        orf = ""
        for y in range(len(orf_oneframe[x])):      
            orf += orf_oneframe[x][y]
        orf_oneframe[x] = orf
    return orf_oneframe
    
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    print "input: ATGGCGTAG, expected output: ['ATGGCG'], actual output: "
    print find_all_ORFs_oneframe("ATGGCGTAG")
    
    print "input: CCCATGGCGTAG, expected output: ['ATGGCG'], actual output: "
    print find_all_ORFs_oneframe("CCCATGGCGTAG")    
    
    print "input: GCGTAG, expected output: [], actual output: " 
    print find_all_ORFs_oneframe("GCGTAG")
    
    print "input: ATGGAC, expected output: [], actual output: "
    print find_all_ORFs_oneframe("ATGGAC")
    
    print "input: ATGGCGTAGACGATGCGATAG, expected output: ['ATGGCG'],['ATGCGA'], actual output: "
    print find_all_ORFs_oneframe("ATGGCGTAGACGATGCGATAG") # AHH

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    dna_frame1 = find_all_ORFs_oneframe(dna[0:])
    dna_frame2 = find_all_ORFs_oneframe(dna[1:])
    dna_frame3 = find_all_ORFs_oneframe(dna[2:])      
    
    return dna_frame1 + dna_frame2 + dna_frame3    

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print "input: ATGGCGTAG, expected output: ['ATGGCG'], actual output: "
    print find_all_ORFs("ATGGCGTAG")
    
    print "input: AATGGCGTAG, expected output: ['ATGGCG'], actual output: "
    print find_all_ORFs("AATGGCGTAG")
    
    print "input: AAATGGCGTAG, expected output: ['ATGGCG'], actual output: "
    print find_all_ORFs("AAATGGCGTAG")

    print "input: AAATGGCGTAGATGGAACGTTAG, expected output: ['ATGGCG',ATGGAACGT'], actual output: "
    print find_all_ORFs("AAATGGCGTAGATGGAACGTTAG")
    
    print "input: AAA, expected output: [], actual output: "
    print find_all_ORFs("AAA")
    
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    dna_first_strand = find_all_ORFs(dna)
    dna_reverse_complement = find_all_ORFs(get_reverse_complement(dna))

    return dna_first_strand + dna_reverse_complement

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    print "input: ATGGCGTAG, expected output: ['ATGGCG'], actual output: "
    print find_all_ORFs_both_strands("ATGGCGTAG")
    
    print "input: CTACGCCAT, expected output: ['ATGGCG'], actual output: "
    print find_all_ORFs_both_strands("CTACGCCAT")
    
    print "input: ATGGCGTAGCTACGCCAA, expected output: ['ATGGCG'],['ATGGCG'], actual output: "
    print find_all_ORFs_both_strands("ATGGCGTAGCTACGCCAT")
    
def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    dna_seq = find_all_ORFs_both_strands(dna)   
    longest_orf = ""
    
    for i in range(len(dna_seq)):
        if len(dna_seq[i]) > len(longest_orf):
            longest_orf = dna_seq[i]
    return longest_orf

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    print "input: ATGGCGTAG, expected output: 'ATGGCG', actual output: "
    print longest_ORF("ATGGCGTAG")
    
    print "input: CATGGCGTAG, expected output: 'ATGGCG', actual output: "
    print longest_ORF("CATGGCGTAG")
    
    print "input: ATGGCGGCGTAGATGCGCTAGATGCGCCGCCGCCGCTAG, expected output: 'ATGCGCCGCCGCCGC', actual output: "
    print longest_ORF("ATGGCGGCGTAGATGCGCTAGATGCGCCGCCGCCGCTAG")

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    
    dna_list = list(dna)
    shuffles = []
    for i in range(0,num_trials):
        shuffle(dna_list)
        if longest_ORF(dna_list) != '':        
            shuffles.append(longest_ORF((dna_list)))

    longest_orf = ""
    for j in shuffles:  
        if len(j) > len(longest_orf):
            longest_orf = j
    return longest_orf
    
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    all_orfs = find_all_ORFs_both_strands(dna)
    all_orfs_over_threshold = []
    amino_acids = []
    
    for i in all_orfs:
        if len(i) > threshold:
            all_orfs_over_threshold.append(i)
    for i in all_orfs_over_threshold:
        amino_acids.append(coding_strand_to_AA(i))
    return amino_acids

def gene_finder_salmonella():
    from load import load_seq
    dna = load_seq("./data/X73525.fa")
    threshold = len(longest_ORF_noncoding(dna,1500))
    salmonella_aa = gene_finder(dna,threshold)
    return salmonella_aa