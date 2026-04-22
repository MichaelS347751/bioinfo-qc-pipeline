# Bioinfo QC Pipeline

A beginner-friendly bioinformatics workflow for automated FASTQ quality control using Python and Snakemake on Windows.

---

## Overview

This project demonstrates a reusable sequencing workflow that:

* scans project folders automatically
* reads metadata from `samples.csv`
* processes multiple FASTQ files
* supports multiple independent projects
* stores outputs inside each project folder

The pipeline is designed to separate:

* workflow code
* project metadata
* raw sequencing data
* analysis results

---

## Repository Structure

bioinfo-qc-pipeline/
├── projects/
│   └── demo_project/
│       ├── data/
│       ├── results/
│       ├── samples.csv
│       └── config.yaml
├── scripts/
├── workflow/
└── README.md

---

## Example Test Data

The demo project contains example sequencing files from public databases.

Current datasets:

| Sample | Organism | Source     |
| ------ | -------- | ---------- |
| S1     | E. coli  | SRR1770413 |
| S2     | Human    | SRR1039508 |
| S3     | Yeast    | ERR458493  |

---

## Download Demo Data

Create the data folder:

```powershell
mkdir projects\demo_project\data
```

Download the same files used in this project:

### E. coli paired-end

```powershell
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_1.fastq.gz" -OutFile "projects\demo_project\data\SRR1770413_1.fastq.gz"
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_2.fastq.gz" -OutFile "projects\demo_project\data\SRR1770413_2.fastq.gz"
```

### Human single-end

```powershell
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR103/008/SRR1039508/SRR1039508_1.fastq.gz" -OutFile "projects\demo_project\data\SRR1039508_1.fastq.gz"
```

### Yeast single-end

```powershell
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR458/ERR458493/ERR458493.fastq.gz" -OutFile "projects\demo_project\data\ERR458493.fastq.gz"
```

---

## Install Dependencies

Install required Python packages:

```powershell
pip install snakemake pandas
```

---

## Run the Pipeline

From the project root folder:

```powershell
snakemake --cores 1 --config project=demo_project
```

---

## Output

Results are written to:

projects/demo_project/results/

Each sample generates a QC output file.

---

## Current Features

* project-based folder structure
* metadata-driven sample handling
* reusable Snakemake workflow
* automatic sample processing

---

## Planned Features

* FastQC integration
* MultiQC reports
* alignment support
* logging improvements
* configurable workflow steps
