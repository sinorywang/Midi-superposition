# MIDI Superposition Generator

This project provides a Python tool to generate **three versions** of any given MIDI file:

- **Original** : The input file, unchanged.  
- **Consonant**: Each track is duplicated with a consonant interval (randomly chosen from minor/major third, perfect fifth, or octave).  
- **Dissonant**: Each track is duplicated with a dissonant interval (randomly chosen from minor second, tritone, or major seventh).  

This can be used for **music cognition experiments**, **music composition**, or simply exploring how consonance and dissonance change perception.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/midi-superposition.git
   cd midi-superposition

2. Install dependencies:

pip install -r requirements.txt

# Usage

Put your MIDI file (e.g., input.mid) in the project folder, then run:

python midi_superposition.py


The script will generate three new MIDI files:

Original.mid

Consonant.mid

Dissonant.mid
