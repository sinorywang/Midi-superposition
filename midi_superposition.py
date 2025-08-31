import pretty_midi
import random

def add_intervals_to_midi(input_midi, output_filename, interval_list):
    midi_data = pretty_midi.PrettyMIDI(input_midi)
    new_midi = pretty_midi.PrettyMIDI()

    for instrument in midi_data.instruments:
        new_instrument = pretty_midi.Instrument(program=instrument.program, is_drum=instrument.is_drum)
        
        for note in instrument.notes:
            new_instrument.notes.append(note)

            interval = random.choice(interval_list)
            
            new_note = pretty_midi.Note(
                velocity=note.velocity,
                pitch=min(note.pitch + interval, 127),
                start=note.start,
                end=note.end
            )
            new_instrument.notes.append(new_note)
            
        new_midi.instruments.append(new_instrument)
    
    new_midi.write(output_filename)

def generate_versions(input_midi):
    consonant_intervals = [3, 4, 7, 12]  
    dissonant_intervals = [1, 6, 11]    

    original_midi = pretty_midi.PrettyMIDI(input_midi)
    original_midi.write("Original.mid")

    # Consonant
    add_intervals_to_midi(input_midi, "Consonant.mid", consonant_intervals)

    # Dissonant
    add_intervals_to_midi(input_midi, "Dissonant.mid", dissonant_intervals)
    
    print("Generated: Original.mid / Consonant.mid / Dissonant.mid")
