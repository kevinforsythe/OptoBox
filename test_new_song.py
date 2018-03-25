import os       # for making directories
#import errno    # ?for dealing with filename collisions?



#def new_name_check():
# here the user gives us a name for the new song and we make a directory to hold
# the files needed to make the new song and flash the microcontroller.
# if a file already exists with the same name, the program will not overwrite it
new_song_name = input('Please choose a name for your new song\n>')
path_dir_new_song = "./output_songs/"+(new_song_name)
if os.path.isdir(path_dir_new_song) == True:
    print("this dir already exists")
    quit()
else:
    os.makedirs(path_dir_new_song)
    #print("new dir made")

#def time_signature():
# here we ask the user for how long each 'beat' is in the song (beat_value)
beat_value = input('how many milli-seconds per beat? (i.e. msec for each row in spreadsheet)\n>')
##  need to figure out how to restrict beat_value to valid values,
##  this way here doesn't work,
## "TypeError: '<' not supported between instances of 'str' and 'int'
#
# if (beat_value < 1):
#     print("\n\n\tThat's too fast for me right now.")
#     print("\tPlease pick a bigger number for your beet value")
#     time_signature()
# else:
#     print("your beat value is "+(beat_value))

#def transpose_csv_data():
# here we prompt user to tell us where the .csv file is, verify its existence & location,
# then transpose the csv data into a text file within the new song directory
path_csv_file = "./input_csv_song_files/"+(input('what is the filename of your *.csv file? (include the ".csv" suffix)\n>'))
if os.path.exists(path_csv_file) == False:
    print("OptoBoxComposer cannot find that file.  Please make sure the file is in the correct folder and re-type the filename carefully.")
    quit()
else:
    pass
path_file_new_song = "./output_songs/"+(new_song_name)"/"+(new_song_name)+".txt"
handle_csv_file = open(path_csv_file, 'r')
handle_csv-to-txt = open(path_file_new_song, 'w')
song_csv_notes = handle_csv_file.readlines()  # this makes a list
for i in range(len(notes)):
    if song_csv_notes[i] == '0\n':
        handle_csv-to-txt.write('digitalWrite(LEDBlue, LOW);\n')
        handle_csv-to-txt.write('delay(' + beat_value + ');\n')
    if song_csv_notes[i] == '1\n':
        handle_csv-to-txt.write('digitalWrite(LEDBlue, HIGH);\n')
        handle_csv-to-txt.write('delay(' + beat_value + ');\n')
handle_csv-to-txt.close()
handle_csv_file.close()

#def compile_song_ino_file():
# song_beginning = open('./.template_song_files/song_intro.txt', 'r')
# handle_csv-to-txt = open('song_temp.txt', 'r')
# song_end = open('song_coda.txt', 'r')
# song_complete = open('song_complete.ino', 'w')
# a = song_beginning.read()
# b = handle_csv-to-txt.read()
# c = song_end.read()
# song_complete.write(a + b + c)
#
#
# sheetmusic.close()
# song_beginning.close()
# handle_csv-to-txt.close()
# song_end.close()
# song_complete.close()



# new_name_check()
# time_signature()
# transpose_csv_data()
#compile_song_ino_file()
