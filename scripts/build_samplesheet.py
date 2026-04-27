from pathlib import Path
import csv

data_folder = Path("projects/demo_project/data")
output_file = Path("projects/demo_project/samples.csv")

samples = {}

for f in sorted(data_folder.glob("*.fastq.gz")):
    name = f.name

    if name.endswith("_1.fastq.gz"):
        sample = name.replace("_1.fastq.gz", "")
        samples.setdefault(sample, {"file1": "", "file2": ""})
        samples[sample]["file1"] = name

    elif name.endswith("_2.fastq.gz"):
        sample = name.replace("_2.fastq.gz", "")
        samples.setdefault(sample, {"file1": "", "file2": ""})
        samples[sample]["file2"] = name

    else:
        sample = name.replace(".fastq.gz", "")
        samples.setdefault(sample, {"file1": "", "file2": ""})
        samples[sample]["file1"] = name

with open(output_file, "w", newline="") as fh:
    writer = csv.writer(fh)
    writer.writerow(["sample", "file1", "file2"])

    for sample, info in sorted(samples.items()):
        writer.writerow([sample, info["file1"], info["file2"]])

print(f"Samplesheet written to {output_file}")