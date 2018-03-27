import os

def transpose_song():
    # this function creates a directory (ie file folder) in the 'output_songs'
    # directory for each new song based on the song's name.  these directories
    # will each contain files required for compiling the output song and
    # uploading it to the microcontroller.  the song parameters are based on
    # *.csv files which should be placed in the "input_csv_song_files" folder
    # the user needs to provide a song name which is new and unique
    os.system('clear')
    new_song_name = input('Please choose a name for your new song:\n>')
    path_new_song_dir = "./output_songs/"+(new_song_name)
    while os.path.isdir(path_new_song_dir) == True:
        print("Sorry, a song with this name already exists.")
        new_song_name = input('Please choose a unique name for your new song:\n>')
        path_new_song_dir = "./output_songs/"+(new_song_name)
    os.makedirs(path_new_song_dir)

    beat_value = input('how many milli-seconds per beat? (i.e. msec for each row in spreadsheet)\n>')
    print("beat value is: "+beat_value+"msec")

    path_csv_file = "./input_csv_song_files/"+(input('What is the filename of your *.csv file? (include the ".csv" suffix)\n>'))
    print("looking for:"+path_csv_file)
    while os.path.exists(path_csv_file) == False:
        print("OptoBoxComposer cannot find that file.  Please make sure the file is in the 'input_csv_song_files' folder and re-type the filename carefully.")
        path_csv_file = "./input_csv_song_files/"+(input('What is the filename of your *.csv file? (include the ".csv" suffix)\n>'))
        print("looking for:"+path_csv_file)
    print("\n\ttransposing csv data in output song format...\n")
    # this makes a hidden txt file which holds the converted csv data
    path_temp_song_data = path_new_song_dir+"/."+(new_song_name)+".txt"
    handle_csv_file = open(path_csv_file, 'r')
    handle_csv2txt = open(path_temp_song_data, 'w')
    song_csv_data = handle_csv_file.readlines()  # this makes a list
    for i in range(len(song_csv_data)):
        if song_csv_data[i] == '0\n':
            handle_csv2txt.write('digitalWrite(LEDBlue, LOW);\n')
            handle_csv2txt.write('delay(' + beat_value + ');\n')
        elif song_csv_data[i] == '1\n':
            handle_csv2txt.write('digitalWrite(LEDBlue, HIGH);\n')
            handle_csv2txt.write('delay(' + beat_value + ');\n')
        else:
            print("ERROR:  You're CSV data is dirty (i.e. contains data other than '1' or '0')")
            quit()
    handle_csv2txt.close()
    handle_csv_file.close()
    # now take hidden intermediate txt file and add template text to make ino file
    song_beginning = open('./.template_files/template_song_intro.txt', 'r')
    handle_csv2txt = open(path_temp_song_data, 'r')
    song_end = open('./.template_files/template_song_coda.txt', 'r')
    song_complete = open(path_new_song_dir+"/"+(new_song_name)+".ino", 'w')
    a = song_beginning.read()
    b = handle_csv2txt.read()
    c = song_end.read()
    song_complete.write(a + b + c)
    # now close all the files
    song_beginning.close()
    handle_csv2txt.close()
    song_end.close()
    song_complete.close()
    print("\n\t"+path_new_song_dir+"/"+(new_song_name)+".ino is ready to be compiled & uploaded.")

    # give user option to go back to main menu or proceed with upload
    proceed2upload = None
    while (proceed2upload != "y"):
        print('\n--Would you like to upload this song to OptoBox now? (y/n)')
        print("(enter 'y' to start uploading, or 'n' to go back to main menu)\n")
        proceed2upload = input('>')
        if proceed2upload == "n":
            main_menu()
    else:
        # remind user to have micrrocontroller plugged into laptop
        print("\n\nPlease make sure the Optobox is connected to the laptop via USB cable,")
        print(" then press the 'enter' key to continue.")
        foo = input('>')

    # now copy the Makefile into the new song dir from template Makefile
    path_song_Makefile = path_new_song_dir+"/Makefile"
    handle_template_Makefile = open('./.template_files/template_Makefile', 'r')
    handle_song_Makefile = open(path_song_Makefile, 'w')
    transcribed_makefile = handle_template_Makefile.readlines()
    for i in range(len(transcribed_makefile)):
        handle_song_Makefile.write(transcribed_makefile[i])
    handle_template_Makefile.close()
    handle_song_Makefile.close()
    # next issue the make & upload commands
    make_command= "cd "+path_new_song_dir+"; make upload"
    os.system(make_command)
    os.system('clear')

transpose_song()
