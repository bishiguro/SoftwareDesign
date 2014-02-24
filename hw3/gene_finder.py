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

    #Nice commenting.

    dna_seq = [] # creates an array of the amino acids coded in the DNA strand
    for i in range(len(dna)):       
        if i % 3 == 0: #This is clumsy - increment by 3 with a third argument to range "range(0,len(dna),3)"
                       #The last argument is the equivalent of i+=3 in a Java for loop.
            dna_seq.append(dna[i:i+3])
            
    aa_sequence = ""
    for i in dna_seq: # for each amino acid coded in the sequence
        for j in codons: # for each group of codons that synthesis a certain protein
            for k in codons[codons.index(j)]: # for each codon in each group
            # So, unless I'm mistaken, codons[codons.index(j)] is the same thing as j in this instance. Something to keep in mind.
                if i == k:                              
                    aa_sequence = aa_sequence + aa[codons.index(j)] # += saves time and space
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
    for i in reversed(dna): # Beautiful.
        if i == "T":
            rev_comp += "A" # Likewise beautiful.
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
    
    for i in range(len(dna_seq)):   # Using "for i in dna_seq" would mean that later, dna_seq[i] gets truncated to i. 
                                    # Same goes for stop_codons. It saves time and space in two places.
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

    #As you may be aware, this function is bugged.

    dna_seq = [] # creates an array of the amino acids coded in the DNA strand
    for i in range(len(dna)):       
        if i % 3 == 0:  
            dna_seq.append(dna[i:i+3])  
    orf_oneframe = []
    start_codon = "ATG"
    
    i = 0
    while i < len(dna_seq):      
        if dna_seq[i] == start_codon:
            # for j in range(i,len(dna_seq)):
            #     if dna_seq[j] == "TAG" or dna_seq[j] == "TAA" or dna_seq[j] == "TGA": # stop codons
            #                                                                             #HERE IS YOUR BUG: you don't account for the case that you are at the end of your sequence.
            #                                                                             # There should be some variety of append statement outside the for j loop
            #                                                                              #Could be made more succinct with "if dna_seq[j] in ['TAG','TAA', 'TGA']:""
            #         orf_oneframe.append(dna_seq[i:j])   #Nice use of [:]. Its handy so keep it in mind for future projects             
            #         i = j
            #         break


            # This little bit of code is the one thing that kept 4 of your 7 testable functions from being correct
            # That makes me really sad. Please make sure your unit tests are robust enough to catch this in future, 
            # and test/debug early and often. Talk to me or the other ninjas if you get really hung up on a bug.
            # Functionality is the largest part of your grade, and this is heavily impairing that.
            j=i;
            while j<len(dna_seq) and dna_seq[j] not in ["TAG","TAA","TGA"]:
                j+=1;
            orf_oneframe.append(dna_seq[i:j])
            i=j
            # END Nick's Code PS. There's probably a more succinct and prettier way to do this too.

        i+=1
        
    for x in range(len(orf_oneframe)):
        orf = ""
        for y in range(len(orf_oneframe[x])): # Using ''.join() would render this for loop unecessary   
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
    print find_all_ORFs_oneframe("ATGGCGTAGACGATGCGATAG") # AHH Indeed.

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

    return dna_first_strand + dna_reverse_complement #This is perfectly fine, but you can also one-line this just as easily

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
    return longest_orf      #This is fine, but for an exercise, try one-lining this with a list-comprehension and max().

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
    return longest_orf          # Spoilers from my above comment - to one line this function you could use
                                # return len(max([longest_ORF(shuffle(list(dna))) for i in range(num_trials)]))

                                # Isn't that cool?! Admittedly, its getting a bit dense and you may not want to
                                # one line it, but the point is that there are functions available that can save you
                                # some for loops and the like here
    
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