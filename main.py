# Todos: (conversion bugs), merge same notes or save with correct note time, optimize code, english gui / code comments

# midi datei in json konvertieren
import json
from music21 import *
from fractions import Fraction

class FractionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Fraction):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

# Pfad zur MIDI-Datei
midi_file = "River_flows_in_you_oZjQfDa.mid" ##########################################################################################################################################

# Lade die MIDI-Datei
midi = converter.parse(midi_file)

# Extrahiere Informationen
metadata = {}
metadata['title'] = midi_file[:-4]
metadata['key'] = midi.analyze('key').name  # speichere den Namen der Tonart als Zeichenkette

# Überprüfe, ob die Taktart vorhanden ist, bevor du darauf zugreifst
if midi.timeSignature is not None:
    metadata['time_signature'] = midi.timeSignature.ratioString
else:
    metadata['time_signature'] = None

# Extrahiere das Tempo aus der MIDI-Datei, falls vorhanden
tempo = midi.flat.getElementsByClass('MetronomeMark')
if tempo:
    metadata['tempo'] = int(tempo[0].number)
else:
    metadata['tempo'] = None

# Erstelle eine Liste von Noten-Objekten aus allen Stimmen in der MIDI-Datei
notes = []
durations = [1, 1.3333333333333333, 2, 2.6666666666666665, 4, 5.333333333333333, 8, 10.666666666666666, 16]
for part in midi.parts:
    for element in part.flat.notesAndRests:  # Änderung hier: notAndRests statt notes
        if isinstance(element, note.Note):
            if 4/element.duration.quarterLength <= (durations[0]+durations[1])/2: #krumme notenlängen zu normalen notenlängen umändern
                duration = durations[0]
            elif 4/element.duration.quarterLength > (durations[0]+durations[1])/2 and 4/element.duration.quarterLength <= (durations[1]+durations[2])/2:
                duration = durations[1]
            elif 4/element.duration.quarterLength > (durations[1]+durations[2])/2 and 4/element.duration.quarterLength <= (durations[2]+durations[3])/2:
                duration = durations[2]
            elif 4/element.duration.quarterLength > (durations[2]+durations[3])/2 and 4/element.duration.quarterLength <= (durations[3]+durations[4])/2:
                duration = durations[3]
            elif 4/element.duration.quarterLength > (durations[3]+durations[4])/2 and 4/element.duration.quarterLength <= (durations[4]+durations[5])/2:
                duration = durations[4]
            elif 4/element.duration.quarterLength > (durations[4]+durations[5])/2 and 4/element.duration.quarterLength <= (durations[5]+durations[6])/2:
                duration = durations[5]
            elif 4/element.duration.quarterLength > (durations[5]+durations[6])/2 and 4/element.duration.quarterLength <= (durations[6]+durations[7])/2:
                duration = durations[6]
            elif 4/element.duration.quarterLength > (durations[6]+durations[7])/2 and 4/element.duration.quarterLength <= (durations[7]+durations[8])/2:
                duration = durations[7]
            elif 4/element.duration.quarterLength > (durations[7]+durations[8])/2:
                duration = durations[8]
            notes.append({
                'pitch': str(element.pitch),
                'offset': float(element.offset),
                'duration': duration
            })
        elif isinstance(element, chord.Chord):
            chords = []
            for pitch in element.pitches:
                if 4/element.duration.quarterLength <= (durations[0]+durations[1])/2:
                    duration = durations[0]
                elif 4/element.duration.quarterLength > (durations[0]+durations[1])/2 and 4/element.duration.quarterLength <= (durations[1]+durations[2])/2:
                    duration = durations[1]
                elif 4/element.duration.quarterLength > (durations[1]+durations[2])/2 and 4/element.duration.quarterLength <= (durations[2]+durations[3])/2:
                    duration = durations[2]
                elif 4/element.duration.quarterLength > (durations[2]+durations[3])/2 and 4/element.duration.quarterLength <= (durations[3]+durations[4])/2:
                    duration = durations[3]
                elif 4/element.duration.quarterLength > (durations[3]+durations[4])/2 and 4/element.duration.quarterLength <= (durations[4]+durations[5])/2:
                    duration = durations[4]
                elif 4/element.duration.quarterLength > (durations[4]+durations[5])/2 and 4/element.duration.quarterLength <= (durations[5]+durations[6])/2:
                    duration = durations[5]
                elif 4/element.duration.quarterLength > (durations[5]+durations[6])/2 and 4/element.duration.quarterLength <= (durations[6]+durations[7])/2:
                    duration = durations[6]
                elif 4/element.duration.quarterLength > (durations[6]+durations[7])/2 and 4/element.duration.quarterLength <= (durations[7]+durations[8])/2:
                    duration = durations[7]
                elif 4/element.duration.quarterLength > (durations[7]+durations[8])/2:
                    duration = durations[8]
                notes.append({
                    'pitch': str(pitch),
                    'offset': float(element.offset),
                    'duration': duration
                })
        elif isinstance(element, note.Rest):  # Neue Bedingung hier: note.Rest
            if 4/element.duration.quarterLength <= (durations[0]+durations[1])/2:
                duration = durations[0]
            elif 4/element.duration.quarterLength > (durations[0]+durations[1])/2 and 4/element.duration.quarterLength <= (durations[1]+durations[2])/2:
                duration = durations[1]
            elif 4/element.duration.quarterLength > (durations[1]+durations[2])/2 and 4/element.duration.quarterLength <= (durations[2]+durations[3])/2:
                duration = durations[2]
            elif 4/element.duration.quarterLength > (durations[2]+durations[3])/2 and 4/element.duration.quarterLength <= (durations[3]+durations[4])/2:
                duration = durations[3]
            elif 4/element.duration.quarterLength > (durations[3]+durations[4])/2 and 4/element.duration.quarterLength <= (durations[4]+durations[5])/2:
                duration = durations[4]
            elif 4/element.duration.quarterLength > (durations[4]+durations[5])/2 and 4/element.duration.quarterLength <= (durations[5]+durations[6])/2:
                duration = durations[5]
            elif 4/element.duration.quarterLength > (durations[5]+durations[6])/2 and 4/element.duration.quarterLength <= (durations[6]+durations[7])/2:
                duration = durations[6]
            elif 4/element.duration.quarterLength > (durations[6]+durations[7])/2 and 4/element.duration.quarterLength <= (durations[7]+durations[8])/2:
                duration = durations[7]
            elif 4/element.duration.quarterLength > (durations[7]+durations[8])/2:
                duration = durations[8]
            notes.append({
                'pitch': "rest",
                'offset': float(element.offset),
                'duration': duration
            })

# Speichere alles in einer JSON-Datei
data = {'metadata': metadata, 'notes': notes}
data['notes'].reverse()
with open('in.json', 'w') as outfile:
    json.dump(data, outfile, indent=2, cls=FractionEncoder)


    
################################################################################################################



# Fasse alle gelichzeitig gespielte Noten zusmmen und ändert die namen der Notenparameter
import json

# Lade die Eingabedatei
with open('in.json', 'r') as f:
    data = json.load(f)

# Erstelle eine leere Liste, um die gruppierten Noten zu speichern
grouped_notes = []

# Gruppiere die Noten
current_group = []
current_offset = None
for note in data['notes']:
    if note['offset'] != current_offset:
        # Neue Gruppe beginnen
        if current_group:
            grouped_notes.append(current_group)
        current_group = [{'note': note['pitch'], 'time': note['duration'], 'tripletMode': False}]
        current_offset = note['offset']
    else:
        # Bestehende Gruppe fortsetzen
        current_group.append({'note': note['pitch'], 'time': note['duration'], 'tripletMode': False})

# Letzte Gruppe hinzufügen
if current_group:
    grouped_notes.append(current_group)

# Erstelle die Ausgabe als Python-Dictionary
output_data = {
    'metadata': data['metadata'],
    'notes': grouped_notes
}


# Speichere die Ausgabe als JSON-Datei
with open('in2.json', 'w') as f:
    json.dump(output_data, f, indent = 2)



############################################################################################################################


    
# Inportiert die richtige Tonart
import json

def get_scale_notes(scale_key):
    with open('scales.json', 'r') as f:
        scales = json.load(f)
    for scale in scales:
        if scale['key'] == scale_key:
            return scale['tineNotes']
    return None


    
################################################################################################################



#entferne die metadaten und füge den richtigen kal datei kopf hinzu
import json

def create_output_dict(input_dict):
    global scale_notes
    #scale_notes = get_scale_notes(input_dict["metadata"]["key"]) ##################################################################################################
    scale_notes = get_scale_notes("C major")
    # Erstelle das gewünschte Output-Dictionary
    output_dict = {
        "songTitle": input_dict["metadata"]["title"],
        "tempo": input_dict["metadata"]["tempo"],
        "tineNotes": scale_notes,
        "song": []
    }
    
    # Konvertiere die Noten in das gewünschte Format und füge sie dem Output-Dictionary hinzu
    output_dict["song"] = input_dict["notes"]
    return output_dict
    
# Öffne die Eingabedatei und lade den Inhalt als JSON
with open("in2.json", "r") as infile:
    input_json = json.load(infile)
    
# Erstelle das Output-Dictionary
output_dict = create_output_dict(input_json)

# Öffne die Ausgabedatei und schreibe das Output-Dictionary als JSON
with open("out.json", "w") as outfile:
    json.dump(output_dict, outfile, indent=2)   



#######################################################################################################################################################################
    
    

#noten im array sortieren und leere noten hinzufügen
import json

# Einlesen der JSON-Datei
with open('out.json', 'r') as f:
    song_data = json.load(f)

# Song-Titel und Tine Notes
song_title = song_data['songTitle']
tine_notes = song_data['tineNotes']

# Song-Array durchlaufen und fehlende Noten hinzufügen
for bar in song_data['song']:
    # Zählen der bereits vorhandenen Noten
    notes_count = sum([1 for note in bar if note['note'] != 'rest'])
    # Wenn weniger als 17 Noten vorhanden sind, wird das Array aufgefüllt
    if notes_count < 17:
        # Ermitteln der fehlenden Anzahl an Noten
        missing_notes = 17 - notes_count
        # Hinzufügen von leeren Noten-Objekten ans Ende des Arrays
        for i in range(missing_notes):
            bar.append({'note': '', 'time': 0, 'tripletMode': False})

# Sortieren der Noten nach der Reihenfolge der tine_notes
for bar in song_data['song']:
    sorted_notes = []
    for note in tine_notes:
        for bar_note in bar:
            if bar_note['note'] == note:
                sorted_notes.append(bar_note)
                break
            elif bar_note['note'] == 'rest':
                sorted_notes.append(bar_note)
                break
        else:
            sorted_notes.append({'note': '', 'time': 0, 'tripletMode': False})
    bar[:] = sorted_notes

# Erstellen der Ausgabe-JSON-Datei
output_data = {'songTitle': song_title, 'tempo': song_data['tempo'], 'tineNotes': tine_notes, 'song': song_data['song']}

# Schreiben der Ausgabe-JSON-Datei
with open('out2.json', 'w') as f:
    json.dump(output_data, f, indent = 2)



####################################################################################################################################



# überflüssige rest noten durch leere noten erstzen
import json

# Eingabedatei einlesen
with open('out2.json') as f:
    data = json.load(f)

# Konvertierung durchführen
for part in data['song']:
    rest_count_start = 0
    rest_count_end = 0
    for i in range(len(part)):
        note = part[i]
        if note['note'] == 'rest':
            for j in range (17):
                if j == 8:
                    part[j] = {'note': note['note'], 'time': note['time'], 'tripletMode': note['tripletMode']}
                else:
                    part[j] = {'note': '', 'time': 0, 'tripletMode': False}

# Ausgabedatei schreiben
with open(midi_file[:-4]+".kal", 'w') as f:
    json.dump(data, f, indent=2)


import os
files_to_remove = ['in.json', 'in2.json', 'out.json', 'out2.json']
for file in files_to_remove:
    os.remove(file)
    #pass