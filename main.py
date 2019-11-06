import argparse
from algorithm import *

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser()
parser.add_argument("--s1", help="first sequence", type=str, default="")
parser.add_argument("--s2", help="second sequence", type=str, default="")
parser.add_argument("--filename1", help="path to file with first sequence in FASTA format", type=str, required=False)
parser.add_argument("--filename2", help="path to file with second sequence in FASTA format", type=str, required=False)
parser.add_argument("--type", type=str, help="global or local", default=GLOBAL)
parser.add_argument('--scores', nargs='+', type=int, help="weights of score function: [match, mismatch, gap]",
                    default=[1, -1, -2])
args = parser.parse_args()


def read_sequence_from_file(filename):
    for seq_record in SeqIO.parse(filename, "fasta"):
        return Seq(str(seq_record.seq), IUPAC.unambiguous_dna)


s1 = args.s1
s2 = args.s2
if args.s1 == "":
    s1 = read_sequence_from_file(args.filename1)
    s2 = read_sequence_from_file(args.filename2)

line, alingment_char_number, score = calculate_alignment(s1, s2, args.scores, args.type)
print(str(s1))
print(str(line))
print("score: ", score)
print("start place in sequence: ", str(alingment_char_number))
with open("results.txt", "w") as f:
    f.write(str(s1) + "\n")
    f.write(line + "\n")
    f.write("score: " + str(score) + "\n")
    f.write("start place in sequence: " + str(alingment_char_number))
