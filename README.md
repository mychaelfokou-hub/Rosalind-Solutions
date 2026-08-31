# Rosalind Solutions 🧬

Questo repository contiene le mie soluzioni personali ai problemi di bioinformatica e programmazione della piattaforma [Rosalind](https://rosalind.info/).

[![Rosalind Profile](https://img.shields.io/badge/Rosalind-Profile-blue?style=flat-square&logo=dna)](https://rosalind.info/users/mychaelfokou-hub/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-brightgreen?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

---

## 📌 Panoramica

- **Linguaggio principale:** Python 3
- **Librerie utilizzate:** Standard library (`collections`, `itertools`), `Biopython` (se consentito/necessario)
- **Obiettivo:** Approfondire algoritmi per la genomica computazionale, trascrittomica e filogenesi, mantenendo un codice leggibile ed efficiente.

---

## 📂 Struttura del Repository

I file sono organizzati per traccia tematica e identificati tramite il codice ufficiale del problema su Rosalind:

```text
.
├── bioinformatics-stronghold/
│   ├── dna.py          # Counting DNA Nucleotides
│   ├── rna.py          # Transcribing DNA into RNA
│   ├── revc.py         # Complementing a Strand of DNA
│   └── fib.py          # Rabbits and Recurrence Relations
├── python-village/
│   ├── ini1.py         # Installing Python
│   └── ini2.py         # Variables and Some Arithmetic
├── requirements.txt
└── README.md

```

---

## 📊 Tabella dei Progressi

### Bioinformatics Stronghold

| ID | Titolo del Problema | Soluzione | Concetti Chiave / Algoritmo |
| :--- | :--- | :---: | :--- |
| **DNA** | Counting DNA Nucleotides | [dna.py](./bioinformatics-stronghold/dna.py) | Conteggio frequenze, String manipulation |
| **RNA** | Transcribing DNA into RNA | [rna.py](./bioinformatics-stronghold/rna.py) | String replacement |
| **REVC** | Complementing a Strand of DNA | [revc.py](./bioinformatics-stronghold/revc.py) | Reverse complement, Hash mapping |
| **FIB** | Rabbits and Recurrence Relations | [fib.py](./bioinformatics-stronghold/fib.py) | Dynamic Programming, Fibonacci |
| **GC** | Computing GC Content | [gc.py](./bioinformatics-stronghold/gc.py) | FASTA parsing, Percentuali |

### Python Village

| ID | Titolo del Problema | Soluzione | Note |
| :--- | :--- | :---: | :--- |
| **INI1** | Installing Python | [ini1.py](./python-village/ini1.py) | Setup ambiente |
| **INI2** | Variables and Some Arithmetic | [ini2.py](./python-village/ini2.py) | Operazioni matematiche base |

---

## ⚙️ Come Eseguire gli Script

1. **Clona il repository:**
   ```bash
   git clone [https://github.com/mychaelfokou-hub/rosalind-solutions.git](https://github.com/mychaelfokou-hub/rosalind-solutions.git)
   cd rosalind-solutions

```


2. **(Opzionale) Installa i requisiti:**
```bash
pip install -r requirements.txt

```


3. **Esegui uno script con il file di input scaricato:**
```bash
python bioinformatics-stronghold/dna.py < rosalind_dna.txt
pip install -r requirements.txt (correntemente non necessario)
python bioinformatics-stronghold/dna.py < rosalind_dna.txt
```



---

## ⚖️ Academic Integrity & Disclaimer

Le soluzioni qui presenti sono intese esclusivamente a scopo didattico, di studio e di archivio personale. Se stai partecipando attivamente alle sfide su Rosalind, ti incoraggio a risolvere i problemi in autonomia prima di consultare il codice.
