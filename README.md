# Bioinfo QC Pipeline

A Windows-compatible bioinformatics QC workflow for automated FASTQ quality control using **Snakemake**, **Python**, **FastQC**, and **MultiQC**.

---

## Overview

This workflow provides automated FASTQ quality control with:

- support for single-end and paired-end data
- automatic detection of FASTQ files (optional CSV override)
- robust filename parsing (including `_R1/_R2`, `_1/_2`, and `_trimmed` suffixes)
- structured QC outputs per project
- per-rule logging for reproducibility
- MultiQC aggregation of all QC results

It is designed to be:
- modular
- reproducible
- Windows-compatible (PowerShell)

---

## Pipeline Features (Current)

- ✔ Automatic sample detection OR CSV-based input
- ✔ Paired-end inference from filenames
- ✔ Trim-aware filename parsing (`_trimmed`)
- ✔ Mixed naming validation (prevents R1/R2 mismatches)
- ✔ FastQC per-sample execution
- ✔ MultiQC summary report
- ✔ Structured logging per rule
- ✔ Project-based organization
- ✔ Deterministic Snakemake outputs

---

## Repository Structure

```text
bioinfo-qc-pipeline/
├── workflow/
│   └── Snakefile
├── scripts/
│   └── build_samplesheet.py
├── projects/
│   └── demo_project/
│       ├── config.yaml
       ├── samples.csv
       ├── data/
       └── results/
           ├── qc/
           └── logs/
├── README.md
└── .gitignore
```
Input Modes
1. CSV mode (recommended)

Provide:

projects/<project>/samples.csv

Required columns:

sample
file1

Optional:

file2 (legacy support; usually inferred automatically)
2. Automatic mode (no CSV required)

If samples.csv is missing, the pipeline:

scans data/ directory
detects FASTQ files automatically
infers pairing based on naming patterns

Supported formats:

sample.fastq.gz
sample_1.fastq.gz / sample_2.fastq.gz
sample_R1.fastq.gz / sample_R2.fastq.gz
sample_1_trimmed.fastq.gz
Output Structure
results/
├── qc/
│   ├── single/
│   ├── paired/
│   └── multiqc_report.html
└── logs/
    ├── fastqc_single/
    ├── fastqc_paired/
    └── multiqc.log

Each sample produces:

*_fastqc.html
*_fastqc.zip
Install Requirements
pip install snakemake pandas multiqc
Install FastQC (Windows)
1. Download FastQC

https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

Extract to:

C:\Tools\FastQC\
2. Configure FastQC path

Edit:

projects/demo_project/config.yaml

Example:

project: demo_project

samples: samples.csv

tools:
  fastqc: "C:/Tools/FastQC/run_fastqc.bat"
  multiqc: "multiqc"
Example Test Data
Sample	Type	Link
ERR458493	SE	https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR458/ERR458493/ERR458493.fastq.gz

SRR1039508	SE	https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR103/008/SRR1039508/SRR1039508.fastq.gz

SRR1770413_1	PE	https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_1.fastq.gz

SRR1770413_2	PE	https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_2.fastq.gz
Download Example Data
mkdir projects\demo_project\data
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR458/ERR458493/ERR458493.fastq.gz" -OutFile "projects\demo_project\data\ERR458493.fastq.gz"
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR103/008/SRR1039508/SRR1039508.fastq.gz" -OutFile "projects\demo_project\data\SRR1039508.fastq.gz"
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_1.fastq.gz" -OutFile "projects\demo_project\data\SRR1770413_1.fastq.gz"
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_2.fastq.gz" -OutFile "projects\demo_project\data\SRR1770413_2.fastq.gz"
Generate Sample Sheet
python scripts/build_samplesheet.py
Run Pipeline
snakemake --cores 4

Dry run:

snakemake -n -p

Debug run:

snakemake --cores 4 --printshellcmds

Recover incomplete runs:

snakemake --cores 4 --rerun-incomplete
Create New Project
mkdir projects\my_project\data
copy projects\demo_project\config.yaml projects\my_project\config.yaml

Run:

snakemake --cores 4
Key Design Notes
FastQC is executed without relying on --outdir
outputs are managed via post-processing and controlled file movement
filename parsing supports trimming and mixed naming conventions
sample identity can include suffixes (e.g. _trimmed) to allow parallel QC states
Planned Features
adapter trimming integration (fastp)
alignment module
modular workflow splitting (qc/, trim/, align/)
optional conda environments per rule
benchmarking and scaling improvements
License

For research and educational use.
