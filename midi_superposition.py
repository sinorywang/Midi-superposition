import pretty_midi
import random

def generate_versions(input_midi):
    midi_data = pretty_midi.PrettyMIDI(input_midi)
    #You can edit as you wish here
    consonant_intervals = [3, 4, 7, 12]  
    dissonant_intervals = [1, 6, 11]     

    #Original
    midi_data.write("Original.mid")

    #Consonant
    consonant_midi = pretty_midi.PrettyMIDI()
    for instrument in midi_data.instruments:
        new_instrument = pretty_midi.Instrument(program=instrument.program, is_drum=instrument.is_drum)
        interval = random.choice(consonant_intervals)  
        for note in instrument.notes:
            new_instrument.notes.append(note)
            new_note = pretty_midi.Note(
                velocity=note.velocity,
                pitch=min(note.pitch + interval, 127), 
                start=note.start,
                end=note.end
            )
            new_instrument.notes.append(new_note)
        consonant_midi.instruments.append(new_instrument)
    consonant_midi.write("Consonant.mid")

    # Dissonant
    dissonant_midi = pretty_midi.PrettyMIDI()
    for instrument in midi_data.instruments:
        new_instrument = pretty_midi.Instrument(program=instrument.program, is_drum=instrument.is_drum)
        interval = random.choice(dissonant_intervals) 
        for note in instrument.notes:
            new_instrument.notes.append(note)
            new_note = pretty_midi.Note(
                velocity=note.velocity,
                pitch=min(note.pitch + interval, 127),
                start=note.start,
                end=note.end
            )
            new_instrument.notes.append(new_note)
        dissonant_midi.instruments.append(new_instrument)
    dissonant_midi.write("Dissonant.mid")

    print("Generated Original.mid / Consonant.mid / Dissonant.mid")

generate_versions("input.mid")
