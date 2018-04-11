#! /usr/bin/env python3

import os
import datetime

def main_menu():
  print("\n\t\t\tMAIN MENU OPTIONS:")
  print('\n\t0. Open Spreadsheet Program to Create *.csv Data File')
  print("\t(Remember to 'Save As' .csv Format)")
  print("\n\t1. See a List of Saved CSV Files")
  print("\t    (NOTE: After viewing, press 'q' to return to the main menu)")
  print("\n\t2. Create a New Song from a *.csv File and Upload to OptoBox")
  print("\t   (currently only works for single column/channel LED control)")
  print("\n\t3. See a List of Previously Transposed Songs")
  print("\n\t4. Upload a Previously Transposed Song to OptoBox")
  print("\t    (NOTE: After viewing, press 'q' to return to the main menu)")
  print("\n\t5. See a Log of Songs Previously Uploaded to OptoBox")
  print("\t    (NOTE: After viewing, press 'q' to return to the main menu)")
  print("\n\t6. Quit")
  main_menu_choice = input("\n\nWhat would you like to do?\n>")
  if main_menu_choice == '0':
      main_menu_0()
  elif main_menu_choice == '1':
      main_menu_1()
  elif main_menu_choice == '2':
      main_menu_2()
  elif main_menu_choice == '3':
      main_menu_3()
  elif main_menu_choice == '4':
      main_menu_4()
  elif main_menu_choice == '5':
      main_menu_5()
  elif main_menu_choice == '6':
      quit()
  else:
      os.system('clear')
      print("\nPlease Choose a Valid Option:\n")


def main_menu_0():
    to_open_libre_calc= "libreoffice --calc"
    os.system(to_open_libre_calc)
    os.system('clear')
    print('--remember to save your data in CSV format!')


def main_menu_1():
    os.system("ls ./input_csv_song_files | grep '.csv' | less")
    os.system('clear')


def main_menu_2():
    os.system('clear')
    transpose_and_upload()


def main_menu_3():
    os.system("ls -lu --time-style=long-iso ./output_songs | awk '{print $6, $7, $8, $9}' | less")
    os.system('clear')


def main_menu_4():
    os.system('clear')
    upload()


def main_menu_5():
    os.system("cat ./output_songs/.upload_log.txt | less")
    os.system('clear')


def transpose_and_upload():
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
    print("\ttransposing csv data in output song format...\n")
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

    # now copy the Makefile into the new song dir from template Makefile
    path_song_Makefile = path_new_song_dir+"/Makefile"
    handle_template_Makefile = open('./.template_files/template_Makefile', 'r')
    handle_song_Makefile = open(path_song_Makefile, 'w')
    transcribed_makefile = handle_template_Makefile.readlines()
    for i in range(len(transcribed_makefile)):
        handle_song_Makefile.write(transcribed_makefile[i])
    handle_template_Makefile.close()
    handle_song_Makefile.close()

    print("\n\t"+new_song_name+".ino is ready to be compiled & uploaded.")
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

    # next issue the make & upload commands
    make_command= "cd "+path_new_song_dir+"; make upload"
    os.system(make_command)

    # now add upload to the Log
    datetime_stamp = datetime.datetime.now().strftime("%Y-%b-%d\t%H:%M:%S\t(%a)")
    path_upload_log = "./output_songs/.upload_log.txt"
    while os.path.exists(path_upload_log) == False:
        handle_upload_log = open(path_upload_log, 'w+')
        handle_upload_log.write("\tBegin Log")
        handle_upload_log.close()
        print("couldn't find the upload log file so created a new one...")
    handle_upload_log = open(path_upload_log, 'r')
    data_upload_log = handle_upload_log.readlines() # copy all previous log entries
    handle_upload_log.close()
    handle_upload_log = open(path_upload_log, 'w')
    handle_upload_log.write(datetime_stamp+"\t "+new_song_name+"\n")
    handle_upload_log.close()
    handle_upload_log = open(path_upload_log, 'a')
    for i in range(len(data_upload_log)):
        handle_upload_log.write(data_upload_log[i])
    handle_upload_log.close()

    os.system('clear')
    print('--your song has been uploaded to OptoBox.')


def upload():
    os.system('clear')
    old_song_name = input('Please enter the name of the old song:\n>')
    path_old_song_dir = "./output_songs/"+(old_song_name)
    while os.path.isdir(path_old_song_dir) == False:
        print("Sorry, that song name doesn't exist")
        old_song_name = input('Please enter the name of a song saved in the "output_songs" folder:\n>')
        path_old_song_dir = "./output_songs/"+(old_song_name)
    print("\n\t...found it!\n")

    print("\n\nPlease make sure the Optobox is connected to the laptop via USB cable,")
    print(" then press the 'enter' key to continue.")
    foo = input('>')

    # check for a Makefile and create one if not present
    path_song_Makefile = path_old_song_dir+"/Makefile"
    while os.path.isfile(path_song_Makefile) == False:
        handle_template_Makefile = open('./.template_files/template_Makefile', 'r')
        handle_song_Makefile = open(path_song_Makefile, 'w')
        transcribed_makefile = handle_template_Makefile.readlines()
        for i in range(len(transcribed_makefile)):
            handle_song_Makefile.write(transcribed_makefile[i]+'\n')
        handle_template_Makefile.close()
        handle_song_Makefile.close()
        print("couldn't find a Makefile in the song directory so made a new one")

    #issue the make & upload commands
    make_command= "cd "+path_old_song_dir+"; make upload"
    os.system(make_command)

    # now add upload to the Log
    datetime_stamp = datetime.datetime.now().strftime("%Y-%b-%d\t%H:%M:%S\t(%a)")
    path_upload_log = "./output_songs/.upload_log.txt"
    while os.path.exists(path_upload_log) == False:
        handle_upload_log = open(path_upload_log, 'w+')
        handle_upload_log.write(datetime_stamp+"\t Begin Log")
        handle_upload_log.close()
        print("couldn't find the upload log file so created a new one...")
    handle_upload_log = open(path_upload_log, 'r')
    data_upload_log = handle_upload_log.readlines() # copy all previous log entries
    handle_upload_log.close()
    handle_upload_log = open(path_upload_log, 'w')
    handle_upload_log.write(datetime_stamp+"\t "+old_song_name+"\n")
    handle_upload_log.close()
    handle_upload_log = open(path_upload_log, 'a')
    for i in range(len(data_upload_log)):
        handle_upload_log.write(data_upload_log[i])
    handle_upload_log.close()

    os.system('clear')
    print('--your song has been uploaded to OptoBox.')


# this is the main start
while True:
    os.system('clear')
    print("\nWelcome to OptoBoxComposer (version alpha, for single 35mm dish only)")
    main_menu()
