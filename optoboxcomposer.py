#!/usr/bin/env python3


input_csv_filename = input('what is the filename of your *.csv file? (include the ".csv" suffix)\n>')
beat_value = input('how many milli-seconds per beat? (i.e. msec for each row in spreadsheet)\n>')

# here we take the .csv input, re-format it into 'song_middle' text (~transpose)
sheetmusic = open(input_csv_filename, 'r')
song_middle = open('song_temp.txt', 'w')


notes = sheetmusic.readlines()

for i in range(len(notes)):
    if notes[i] == '0\n':
        song_middle.write('digitalWrite(LEDBlue, LOW);\n')
        song_middle.write('delay(' + beat_value + ');\n')
    if notes[i] == '1\n':
        song_middle.write('digitalWrite(LEDBlue, HIGH);\n')
        song_middle.write('delay(' + beat_value + ');\n')



          #digitalWrite(LEDBlue, HIGH);
          #delay(250);
          #digitalWrite(LEDBlue, LOW);
          #delay(250);
song_middle.close()



song_beginning = open('song_intro.txt', 'r')
song_middle = open('song_temp.txt', 'r')
song_end = open('song_coda.txt', 'r')
song_complete = open('song_complete.ino', 'w')
a = song_beginning.read()
b = song_middle.read()
c = song_end.read()
song_complete.write(a + b + c)


sheetmusic.close()
song_beginning.close()
song_middle.close()
song_end.close()
song_complete.close()
