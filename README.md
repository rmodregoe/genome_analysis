# Genome Analysis Using Markov Chains

## Project Description
This project analyzes genome sequences of viruses using Markov chain models. The analysis aims to determine similarities between virus families and simulate mutations using transition matrices. Key methodologies include:
- Analyzing base distributions (G, T, A, C) using histograms.
- Generating transition matrices for first- and second-order Markov chains.
- Simulating mutations of virus genomes based on transition probabilities.

The project includes Python scripts for data processing, statistical analysis, and visualization.

## Motivation
This project was part of my academic training and focuses on applying computational models to solve complex biological problems. The study explores how Markov chains can be used to infer genetic relationships and simulate realistic genome sequences.

## Features
- **Base Distribution Analysis**: Calculates and visualizes the frequency of nucleotides in viral genomes.
- **Markov Chain Models**: Generates transition matrices to analyze first- and second-order dependencies in genome sequences.
- **Genome Simulation**: Simulates mutations of virus genomes using Markov chain models.
- **Visualizations**: Creates histograms and other visual tools for data analysis.

## Included Files
- `genome.py`: Main script for analyzing genome sequences and generating Markov chain transition matrices.
- `genome_generation.py`: Script for simulating mutations using second-order Markov chains.
- Supporting data files:
  - `A.txt`, `B.txt`, `C.txt`, `D.txt`: Genome sequences for different viruses.

## Requirements
- Python 3.6 or higher.
- Libraries:
  - NumPy
  - Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/rmodregoe/genome_analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd genome_analysis
   ```
3. Run the scripts:
   - Analyze genome sequences:
     ```bash
     python genome.py
     ```
   - Simulate genome mutations:
     ```bash
     python genome_generation.py
     ```

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
Created by Ricardo Modrego. For questions or comments, contact me at r.modrego.e@gmail.com
