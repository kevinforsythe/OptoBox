import os       # for making directories
#import errno    # ?for dealing with filename collisions?


# here the user gives us a name for the new song and we make a directory to hold
# the files needed to make the new song and flash the microcontroller.
# if a file already exists with the same name, the program will not overwrite it
new_song_name = input('Please choose a name for your new song\n>')


# here we prompt user to tell us where the .csv file is and how long each 'beat' is
filename_csv_data = "./input_csv_song_files/"+(input('what is the filename of your *.csv file? (include the ".csv" suffix)\n>'))
beat_value = input('how many milli-seconds per beat? (i.e. msec for each row in spreadsheet)\n>')

# here we take the data from the .csv input file and re-format it into the text file ''
handle_csv_file = open(filename_csv_data, 'r')
handle_csv-to-txt = open('song_temp.txt', 'w')

notes = handle_csv_file.readlines()

for i in range(len(notes)):
    if notes[i] == '0\n':
        handle_csv-to-txt.write('digitalWrite(LEDBlue, LOW);\n')
        handle_csv-to-txt.write('delay(' + beat_value + ');\n')
    if notes[i] == '1\n':
        handle_csv-to-txt.write('digitalWrite(LEDBlue, HIGH);\n')
        handle_csv-to-txt.write('delay(' + beat_value + ');\n')



          #digitalWrite(LEDBlue, HIGH);
          #delay(250);
          #digitalWrite(LEDBlue, LOW);
          #delay(250);
handle_csv-to-txt.close()



song_beginning = open('./.template_song_files/song_intro.txt', 'r')
handle_csv-to-txt = open('song_temp.txt', 'r')
song_end = open('song_coda.txt', 'r')
song_complete = open('song_complete.ino', 'w')
a = song_beginning.read()
b = handle_csv-to-txt.read()
c = song_end.read()
song_complete.write(a + b + c)


sheetmusic.close()
song_beginning.close()
handle_csv-to-txt.close()
song_end.close()
song_complete.close()
