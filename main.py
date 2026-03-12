import re

# Open input and output files
input_file = "data/orf_trans_all.fa"
output_file = "results/yeast_zinc_finger_orf.txt"

# Zinc Finger motif as a regex pattern
zinc_finger_pattern = re.compile(r"C.H.[LIVMFY]C.{2}C.[LIVMYA]")

# counter for proteins containing the motif
proteins_with_motif = 0

#looping thro each line in file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    protein_name = ""
    protein_seq = ""

    for line in infile:
        line = line.strip()
        if line.startswith(">"):
            if protein_name and protein_seq:
                matches = zinc_finger_pattern.findall(protein_seq)
                if matches:
                    proteins_with_motif += 1
                    outfile.write(f"{protein_name}\n")
                    for match in matches:
                        outfile.write(f"{match}\n")
            # Start a new protein
            protein_name = line[1:]  # remove  the ">"
            protein_seq = ""
        else:
            protein_seq += line

    #last protein in the file
    if protein_name and protein_seq:
        matches = zinc_finger_pattern.findall(protein_seq)
        if matches:
            proteins_with_motif += 1
            outfile.write(f"{protein_name}\n")
            for match in matches:
                outfile.write(f"{match}\n")

    # Write tp output file at the end
    outfile.write(f"\nNumber of proteins containing Zinc Finger Motif: {proteins_with_motif}\n")
print("DONE! check results folder")