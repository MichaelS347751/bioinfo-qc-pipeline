from pathlib import Path
import csv

data_folder = Path("data")

fastq_files = list(data_folder.rglob("*.fastq.gz"))

samples = {}

# ---------------------------
# Group files by sample
# ---------------------------
for f in fastq_files:
    organism = f.parts[-2]            # selects the 2nd last part of the path which is the organism foldername
    sample_id = f.name.split("_")[0]  # takes the samplename without fwd (_1) or rev (_2) identifier 

    if sample_id not in samples:
        samples[sample_id] = {
            "organism": organism,
            "read1": "",
            "read2": ""
        }

    if "_1" in f.name:
        samples[sample_id]["read1"] = str(f)
    elif "_2" in f.name:
        samples[sample_id]["read2"] = str(f)
    else:
        samples[sample_id]["read1"] = str(f)

# ---------------------------
# Write CSV
# ---------------------------
output_file = Path("samples.csv")

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sample", "organism", "read1", "read2"])

    for sample, info in samples.items():
        writer.writerow([
            sample,
            info["organism"],
            info["read1"],
            info["read2"]
        ])

print(f"Samplesheet written to {output_file}")