# Bioinfo QC Pipeline

A Windows-compatible bioinformatics QC workflow for automated FASTQ quality control using **Snakemake**, **Python**, and **FastQC**.

---

## Overview

This workflow:

* processes single-end and paired-end FASTQ files
* reads sample metadata from `samples.csv`
* runs FastQC automatically
* stores results inside each project folder
* supports multiple independent projects
* works natively in Windows PowerShell

The repository is organized to separate:

* workflow code
* project configuration
* raw sequencing data
* QC results

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
│       ├── samples.csv
│       ├── data/
│       └── results/
├── README.md
└── .gitignore
```

---

## Install Requirements

Install Python packages:

```powershell
pip install snakemake pandas multiqc
```

---

## Install FastQC on Windows

### 1. Download FastQC

Download FastQC from the official site:

https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

Extract it to a permanent folder, for example:

```text
C:\Tools\FastQC\
```

---

### 2. Test FastQC manually

Run:

```powershell
C:\Tools\FastQC\run_fastqc.bat
```

If installed correctly, FastQC should start.

---

### 3. Configure FastQC path

Edit:

```text
projects/demo_project/config.yaml
```

Example:

```yaml
project: demo_project

samples: samples.csv

tools:
  fastqc: "C:/Tools/FastQC/run_fastqc.bat"
  multiqc: "multiqc"
```

Use forward slashes in the path on Windows or escape backslashes.

---

## Example Test Data

The demo project uses small public FASTQ files from ENA.

| Sample       | Type       | Download                                                                         |
| ------------ | ---------- | -------------------------------------------------------------------------------- |
| ERR458493    | Single-end | https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR458/ERR458493/ERR458493.fastq.gz         |
| SRR1039508   | Single-end | https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR103/008/SRR1039508/SRR1039508.fastq.gz   |
| SRR1770413_1 | Paired-end | https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_1.fastq.gz |
| SRR1770413_2 | Paired-end | https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_2.fastq.gz |

---

## Download Example Data

Create the data folder:

```powershell
mkdir projects\demo_project\data
```

Download the files:

```powershell
Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR458/ERR458493/ERR458493.fastq.gz" -OutFile "projects\demo_project\data\ERR458493.fastq.gz"

Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR103/008/SRR1039508/SRR1039508.fastq.gz" -OutFile "projects\demo_project\data\SRR1039508.fastq.gz"

Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_1.fastq.gz" -OutFile "projects\demo_project\data\SRR1770413_1.fastq.gz"

Invoke-WebRequest -Uri "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR177/003/SRR1770413/SRR1770413_2.fastq.gz" -OutFile "projects\demo_project\data\SRR1770413_2.fastq.gz"
```

---

## Generate `samples.csv` Automatically

Instead of writing `samples.csv` manually, generate it automatically.

Run:

```powershell
python scripts/build_samplesheet.py
```

This creates:

```text
projects/demo_project/samples.csv
```

Example:

```csv
sample,file1,file2
ERR458493,ERR458493.fastq.gz,
SRR1039508,SRR1039508.fastq.gz,
SRR1770413,SRR1770413_1.fastq.gz,SRR1770413_2.fastq.gz
```

---

## Run the Pipeline

From the repository root:

```powershell
snakemake --cores 1
```

For multiple cores, previewing commands and parallelism:

```powershell
snakemake --cores 4 --printshellcmds
snakemake -n -p    # dry-run, show what will run
snakemake --cores 4 --rerun-incomplete    # rerun incomplete/failed jobs
```

---

## Preview Without Running

To preview the workflow:

```powershell
snakemake -n -p
```

Useful for debugging.

---

## Output and Logs

Results are written to:

```text
projects/demo_project/results/qc/
```

Structure:

```text
results/qc/
├── single/
├── paired/
└── multiqc_report.html
```

Each sample produces:

- `*_fastqc.html`
- `*_fastqc.zip`

Execution logs (stdout/stderr captured) are stored under:

```text
projects/demo_project/results/logs/
├── fastqc_single/{sample}.log
├── fastqc_paired/{sample}.log
└── multiqc.log
```
These logs help with debugging failed runs and reproducing command invocations.

---

## Create a New Project

Create a new project:

```powershell
mkdir projects\my_project
mkdir projects\my_project\data
```

Copy config:

```powershell
copy projects\demo_project\config.yaml projects\my_project\config.yaml
```

Add FASTQ files to:

```text
projects/my_project/data/
```

Generate sample sheet:

```powershell
python scripts/build_samplesheet.py
```

Run:

```powershell
snakemake --cores 4
```

---

## Current Features

* Windows-compatible Snakemake workflow
* FastQC integration
* automatic sample sheet generation
* single-end support
* paired-end support
* metadata-driven processing
* project-based organization

---

## Current Features & Notes

* FastQC integration (single & paired)
* MultiQC summary report generation (requires `multiqc`)
* Per-rule logs written to `results/logs/`
* The pipeline expects FASTQ inputs in `projects/<project>/data/` and writes deterministic outputs into `projects/<project>/results/` so Snakemake can track them reliably.

If your FastQC version doesn't support `-o/--outdir`, the workflow runs FastQC from the target output folder so FastQC writes outputs directly into `results/qc/*`.

Planned future features:

- adapter trimming
- alignment
- optional per-rule conda environments
- benchmarking and cluster support

---

## License

For research and educational use.
