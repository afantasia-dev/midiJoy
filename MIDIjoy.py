import XInput

import mido
from mido import Message

import time

import rtmidi
midiin = rtmidi.MidiIn() # For input
midiout = rtmidi.MidiOut() # For output
#midiin.open_virtual_port("MIDIjoy")

port = mido.open_output('LoopBe Internal MIDI 1')




noteon1=mido.Message('note_on', note=36, velocity=100, time=0)
noteoff1=mido.Message('note_off', note=36, velocity=0, time=0)

noteon2=mido.Message('note_on', note=37, velocity=100, time=0)
noteoff2=mido.Message('note_off', note=37, velocity=0, time=0)

noteon3=mido.Message('note_on', note=38, velocity=100, time=0)
noteoff3=mido.Message('note_off', note=38, velocity=0, time=0)

noteon4=mido.Message('note_on', note=39, velocity=100, time=0)
noteoff4=mido.Message('note_off', note=39, velocity=0, time=0)

noteon5=mido.Message('note_on', note=40, velocity=100, time=0)
noteoff5=mido.Message('note_off', note=40, velocity=0, time=0)

noteon6=mido.Message('note_on', note=41, velocity=100, time=0)
noteoff6=mido.Message('note_off', note=41, velocity=0, time=0)

noteon7=mido.Message('note_on', note=42, velocity=100, time=0)
noteoff7=mido.Message('note_off', note=42, velocity=0, time=0)

noteon8=mido.Message('note_on', note=43, velocity=100, time=0)
noteoff8=mido.Message('note_off', note=43, velocity=0, time=0)

noteon9=mido.Message('note_on', note=44, velocity=100, time=0)
noteoff9=mido.Message('note_off', note=44, velocity=0, time=0)

noteon0=mido.Message('note_on', note=45, velocity=100, time=0)
noteoff0=mido.Message('note_off', note=45, velocity=0, time=0)




def midi_update(button,bButton,noteon,noteoff):
    match button:
        case True:
            if button==bButton:
                return None
            else:
                print("note_on")
                return port.send(noteon)

        case False:
            if button==bButton:
                return None
            else:
                print("note_off")
                return port.send(noteoff)
            

x=1

controller_count = len(XInput.get_connected())
print(f"Number of connected controllers: {controller_count}")

dib=dict()

time.sleep(2.5)

bA=''
bB=''
bX=''
bY=''
bRS=''
bLS=''
bUP=''
bDN=''
bLF=''
bRI=''

while x :
    state = XInput.get_state(0)
    dib=XInput.get_button_values(state)
    #print(dib)
    midi_update(dib['A'],bA,noteon1,noteoff1)
    midi_update(dib['B'],bB,noteon2,noteoff2)
    midi_update(dib['X'],bX,noteon3,noteoff3)
    midi_update(dib['Y'],bY,noteon4,noteoff4)
    midi_update(dib['RIGHT_SHOULDER'],bRS,noteon5,noteoff5)
    midi_update(dib['LEFT_SHOULDER'],bLS,noteon6,noteoff6)
    midi_update(dib['DPAD_DOWN'],bDN,noteon7,noteoff7)
    midi_update(dib['DPAD_LEFT'],bLF,noteon8,noteoff8)
    midi_update(dib['DPAD_RIGHT'],bRI,noteon9,noteoff9)
    midi_update(dib['DPAD_UP'],bUP,noteon0,noteoff0)
    bA=dib['A']
    bB=dib['B']
    bX=dib['X']
    bY=dib['Y']
    bRS=dib['RIGHT_SHOULDER']
    bLS=dib['LEFT_SHOULDER']
    bUP=dib['DPAD_UP']
    bDN=dib['DPAD_DOWN']
    bLF=dib['DPAD_LEFT']
    bRI=dib['DPAD_RIGHT']

# port.send(mido.Message('note_on', note=60, velocity=100, time=1.2))
# time.sleep(2.5)
# port.send(note_off)