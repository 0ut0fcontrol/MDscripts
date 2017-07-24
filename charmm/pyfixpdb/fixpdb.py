import sys
import os
usage="""fix PDB format to CHARMM input format.
    usage:
        fixpdb.py input.pdb output.pdb chainID 
    example:
        fixpdb.py 1AKI1.pdb  protein1.pdb A 
    """
if len(sys.argv) < 4:
    print(usage)
    sys.exit(0)

inpf = open(sys.argv[1], 'r')
outf = open(sys.argv[2], 'w')
chainID = sys.argv[3]


def split_pdb_line(line):
    fields = []
    idx = 0
    # fields: 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
    for i in (6, 5, 1, 4, 1, 3, 1, 1, 4, 1, 3, 8, 8, 8, 6, 6, 6, 4, 2, 2):
        fields.append(line[idx:idx+i]) 
        idx += i
    return fields

atomno = 1
for line in inpf:
    fields = split_pdb_line(line)
    if fields[0] == "HEADER":
        outf.write('REMARK' + line[6:])
    if fields[0] in ["ATOM  ", "HETATM"]:
        if fields[4] != " " and fields[4] != "A":
            continue # go to next line
        if ( fields[7] == chainID or (fields[7] == ' ' and fields[0] != "HETATM")):
            if fields[5] == "HOH":
                fields[3] = " OH2"
                fields[5] = "TIP"
                fields[6] = '3'
            if fields[0] == "HETATM": fields[0] = "ATOM  "
            if fields[5] == "HIS": fields[5] = "HSD"
            if fields[5] == "ILE" and fields[3] == " CD1":
                fields[3] = " CD "
            if fields[3] == " OXT" or fields[3] == "OCT1": fields[3] == " OT1"
            if fields[3] == "OCT2": fields[3] == " OT2"
            fields[1] = atomno
            fields[2] = " "
            fields[4] = " "
            fields[7] = " "
            fields[9] = " "
            fields[10] = "   "
            fields[16] = "      "
            fields[17] = "    "
            fmt = "%6s%5d%1s%4s%1s%3s%1s%1s%4s%1s%3s%8s%8s%8s%6s%6s%6s%4s%2s\n"
            outf.write(fmt%tuple(fields[:19]))
            atomno += 1
outf.write("END")
