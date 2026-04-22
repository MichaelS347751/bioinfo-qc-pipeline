from pathlib import Path
import argparse

data_folder = Path("data")

# ---------------------------
# Argument handling
# ---------------------------
parser = argparse.ArgumentParser()
parser.add_argument(
    "--organism",
    help="Filter by organism folder (ecoli, yeast, human)",
    default=None
)

args = parser.parse_args()


# ---------------------------
# Find files
# ---------------------------
fastq_files = list(data_folder.rglob("*.fastq.gz"))

if args.organism:
    fastq_files = [
        f for f in fastq_files
        if args.organism in f.parts
    ]



# ---------------------------
# Output
# ---------------------------
if not fastq_files:
    print("No FASTQ files found.")
else:
    print("\nDetected samples:\n")

    for f in sorted(fastq_files):
        organism = f.parts[-2]
        sample = f.name
        print(f"{organism}: {sample}")

