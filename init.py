import argparse
from main import *

parser = argparse.ArgumentParser()
parser.add_argument("--s1", help="first sequence", type=str, default="")
parser.add_argument("--s2", help="second sequence", type=str, default="")
parser.add_argument("--filename1", help="path to file with first sequence in FASTA format", type=str, required=False)
parser.add_argument("--filename2", help="path to file with second sequence in FASTA format", type=str, required=False)
parser.add_argument("--type", type=str, help="global or local", default=GLOBAL)
parser.add_argument('--scores', nargs='+', type=int, help="weights of score function: [match, mismatch, gap]", default=[1, -1, -2])
args = parser.parse_args()

line, alingment_char_number = calculate_alignment(args.s1, args.s2,  args.scores, args.type)
print(line, alingment_char_number)
