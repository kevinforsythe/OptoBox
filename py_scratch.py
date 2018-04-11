import os
import datetime

def compose_song():
    # this function creates a directory (ie file folder) for the new song in
    # "~/Documents/Optobox_Files/Optobox_Songs"
    # the directory's name is the same as the song's name, so song names need to be
    # unique.  the song folders contain files required for compiling the output song and
    # uploading it to the microcontroller.
    # the song parameters (LED 'on-off' instructions) are entered by the user
    # here and saved as an intermediate text file, then this program converts
    # these instructions into arduino source code (*.ino file), which ultimately
    # gets compiled into machine code and uploaded to the microcontroller

    os.system('clear')
    new_song_name = input('Please choose a name for your new song:\n>')
    path_new_song_dir = "~/Documents/Optobox_Files/Optobox_Songs/"+(new_song_name)
    while os.path.isdir(path_new_song_dir) == True:
        print("Sorry, a song folder with this name already exists.")
        new_song_name = input('Please choose a unique name for your new song:\n>')
        path_new_song_dir = "~/Documents/Optobox_Files/Optobox_Songs"+(new_song_name)
    os.makedirs(path_new_song_dir)

    print("What blinking frequency (in Hz) would you like to use when the LEDs are active?\n")
    print('NB: if you want the LEDs to be constantly on (ie, no blinking) when active, enter "0"\n')
    int blink_frequency= input("please enter a number:")

    if blink_frequency != 0:
        print("\nyour blinking frequency is: "+blink_frequency+"Hz\n")
        float blink_period = (1/blink_frequency)
        float blink_on_seconds = (blink_period/2)
        float blink_on_msec = (blink_on_seconds*1000)
        print("so your cycle period time is "+blink_period+" seconds.")
        print("For every cycle, the LEDs will be active for "+blink_on_msec+"msec, then off for "+blink_on_msec"msec\n")
    else:
        print("The LEDs will not blink when activated (ie, they will be constantly on)")
        int blink_period = 0
        flash_on_msec
    #
    # path_csv_file = "./input_csv_song_files/"+(input('What is the filename of your *.csv file? (include the ".csv" suffix)\n>'))
    # print("looking for:"+path_csv_file)
    # while os.path.exists(path_csv_file) == False:
    #     print("OptoBoxComposer cannot find that file.  Please make sure the file is in the 'input_csv_song_files' folder and re-type the filename carefully.")
    #     path_csv_file = "./input_csv_song_files/"+(input('What is the filename of your *.csv file? (include the ".csv" suffix)\n>'))
    #     print("looking for:"+path_csv_file)
    # print("\ttransposing csv data in output song format...\n")
    # # this makes a hidden txt file which holds the converted csv data
    # path_temp_song_data = path_new_song_dir+"/."+(new_song_name)+".txt"
    # handle_csv_file = open(path_csv_file, 'r')
    # handle_csv2txt = open(path_temp_song_data, 'w')
    # song_csv_data = handle_csv_file.readlines()  # this makes a list
    # for i in range(len(song_csv_data)):
    #     if song_csv_data[i] == '0\n':
    #         handle_csv2txt.write('digitalWrite(LEDBlue, LOW);\n')
    #         handle_csv2txt.write('delay(' + beat_value + ');\n')
    #     elif song_csv_data[i] == '1\n':
    #         handle_csv2txt.write('digitalWrite(LEDBlue, HIGH);\n')
    #         handle_csv2txt.write('delay(' + beat_value + ');\n')
    #     else:
    #         print("ERROR:  You're CSV data is dirty (i.e. contains data other than '1' or '0')")
    #         quit()
    # handle_csv2txt.close()
    # handle_csv_file.close()
    # # now take hidden intermediate txt file and add template text to make ino file
    # song_beginning = open('./.template_files/template_song_intro.txt', 'r')
    # handle_csv2txt = open(path_temp_song_data, 'r')
    # song_end = open('./.template_files/template_song_coda.txt', 'r')
    # song_complete = open(path_new_song_dir+"/"+(new_song_name)+".ino", 'w')
    # a = song_beginning.read()
    # b = handle_csv2txt.read()
    # c = song_end.read()
    # song_complete.write(a + b + c)
    # # now close all the files
    # song_beginning.close()
    # handle_csv2txt.close()
    # song_end.close()
    # song_complete.close()
