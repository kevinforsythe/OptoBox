#! /usr/bin/env python3

import os
import datetime

def main_menu():
  print("\n\t\t\tMAIN MENU OPTIONS:")
  print("\n\t1. Compose a Song File (with option to Upload)")
  print("\n\t2. See the List of Song Files")
  print("\t    (NOTE: After viewing, press 'q' to return to the main menu)")
  print("\n\t3. Upload a Song to OptoBox")
  print("\n\t4. See a Log of Uploaded Songs")
  print("\t    (NOTE: After viewing, press 'q' to return to the main menu)")
  print("\n\t5. Quit")
  main_menu_choice = input("\n\nWhat would you like to do?\n>")
  if main_menu_choice == '1':
      main_menu_1()
  elif main_menu_choice == '2':
      main_menu_2()
  elif main_menu_choice == '3':
      main_menu_3()
  elif main_menu_choice == '4':
      main_menu_4()
  elif main_menu_choice == '5':
      quit()
  else:
      os.system('clear')
      print("\nPlease Choose a Valid Option:\n")


def main_menu_1():
    os.system('clear')
    compose_song()


def main_menu_2():
    os.system("ls -lu --time-style=long-iso ../Documents/Optobox_Files/Optobox_Songs | awk '{print $6, $7, $8, $9}' | less")
    os.system('clear')


def main_menu_3():
    os.system('clear')
    upload()


def main_menu_4():
    os.system("cat ../Documents/Optobox_Files/Optobox_Files/.upload_log.txt | less")
    os.system('clear')



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
    new_song_name = input('\nPlease choose a name for your new song:\n>')
    path_new_song_dir = "../Documents/Optobox_Files/Optobox_Songs/"+(new_song_name)
    while os.path.isdir(path_new_song_dir) == True:
        print("Sorry, a song folder with this name already exists.")
        new_song_name = input('Please choose a unique name for your new song:\n>')
        path_new_song_dir = "../Documents/Optobox_Files/Optobox_Songs"+(new_song_name)
    os.makedirs(path_new_song_dir)

        # input PWM settings for when LED is on
    print("\nWhen your LEDs are active, do you want to modulate their power with Pulse Width Modification (PWM)?")
    print("ie, do you want to attenuate LED output by decreasing LED duty cycle when it's on?")
    print("(by entering 'n', the LEDs will illuminate with full strength (100%) when on)")
    PWM_option = input("y/n)\n>")
    if PWM_option == 'y':
        PWM_option = 1
    elif PWM_option == 'n':
        PWM_option = 0
    else:
        PWM_option = 999
    while (PWM_option != 1 & PWM_option != 0):
        print("Do you want to decrease LED power using PWM? \n(please just type 'y' for yes, or 'n' for no, then hit 'enter')")
        PWM_option = input("y/n)\n>")
        if PWM_option == 'y':
            PWM_option = 1
        elif PWM_option == 'n':
            PWM_option = 0
        else:
            PWM_option = 999
    if PWM_option == 1:
        LED_duty_cycle = int(input("\n\tplease enter the desired percent duty cycle (1-100, omit the %%' sign):"))
    # ToDo: restrict input to valid response...
    # is_LED_duty_cycle_int = isinstance(LED_duty_cycle, int)
        while (LED_duty_cycle > 101) | (LED_duty_cycle < 0):
            LED_duty_cycle = int(input("\n\tplease enter the desired percent duty cycle (1-100):"))
        print("OK, LED duty cycle will be %d%%" % (LED_duty_cycle))
    elif PWM_option == 0:
        LED_duty_cycle = 100
        print("OK, LED duty cycle will be %d%%" % (LED_duty_cycle))
    else:
        print("error!")
        quit

        # input on-off blinking rate
    print("\nWhen your LEDs are active, what pulse-rate (ie blinking frequency) would you like to use? (in Hz)")
    print('NB: if you want the LEDs to be constantly on when active (ie, no blinking), enter "0"\n')
    blink_frequency = int(input("please enter a number:"))
    if blink_frequency != 0:
        print("\nyour pulse-rate is: %dHz\n" % (blink_frequency))
        blink_period = float(1/blink_frequency)
        blink_on_seconds = float(blink_period/2)
        blink_on_msec = int(blink_on_seconds*1000)
        blink_off_msec = blink_on_msec
        print("so your blinking period time is %5.3f seconds." % (blink_period))
        print("For every blink-cycle, the LEDs will be on for %dmsec, then off for %dmsec" % (blink_on_msec, blink_off_msec))
        print("The LEDs will continuously blink at this rate throughout the 'LED Active' period of the 'LED Active/Resting cycle'.")
    else:
        print("The LEDs will not blink when activated (ie, they will be constantly on throughout your 'LED-Active' period)\n")
        blink_period = 0

        #input LED Active/Resting times and total number of cycle repeats
    print("\nPlease provide parameters for the 'LED Active/Resting cycle':")
    print("\tfor each 'LED Active/Resting cycle', how many seconds should the LEDs be 'Active'?")
    LED_active_time = float(input("\t>"))
    print("\tbetween each 'Active' period, how many seconds should the LEDs be 'Resting'?")
    LED_rest_time = float(input("\t>"))
    print("OK, for every 'LED Active/Resting cycle', the LEDs will be active for %d seconds, then rest for %d seconds," % (LED_active_time, LED_rest_time))
    sum_LED_active_and_rest_time = LED_active_time + LED_rest_time
    print("so each 'LED Active/Resting cycle' will last   %d seconds." % (sum_LED_active_and_rest_time))
    print("\nHow many times would you like to repeat the 'LED Active/Resting cycle'?")
    num_LED_pattern_repeats = int(input("please enter a number:"))
    print("OK, your LEDs will repeat the 'Active/Resting' cycle %d times," % (num_LED_pattern_repeats))
    print("so your song's total time length will be   %d seconds." % (num_LED_pattern_repeats*sum_LED_active_and_rest_time))

    if blink_period != 0:
        num_blinks_per_active_phase = int(LED_active_time/blink_period)


    # recall, path_new_song_dir = "~/Documents/Optobox_Files/Optobox_Songs/"+(new_song_name)
    # this makes a hidden txt file which holds the song parameters
    path_temp_song_parameters = path_new_song_dir+"/."+(new_song_name)+".txt"
    handle_song_parameters_txt = open(path_temp_song_parameters, 'w')


#  4 different sections here for a 2x2 matrix of options: +/-PWM and +/- blinking
    if PWM_option == 0:
        if blink_frequency == 0:
            # Set the number of 'LED Active/Resting' cycle repeats
            handle_song_parameters_txt.write('for (int i = 0; i < '+ str(num_LED_pattern_repeats) + '; i++) {\n')
            handle_song_parameters_txt.write('        digitalWrite(LEDBlue, HIGH);\n')
            handle_song_parameters_txt.write('        delay(' + str(LED_active_time) + ');\n')
            handle_song_parameters_txt.write('        digitalWrite(LEDBlue, LOW);\n')
            handle_song_parameters_txt.write('        delay(' + str(LED_rest_time) + ');\n')
            handle_song_parameters_txt.write('}')

        if blink_frequency != 0:
            handle_song_parameters_txt.write('for (int i = 0; i < '+ str(num_LED_pattern_repeats) + '; i++) {\n')
            handle_song_parameters_txt.write('    for (int j = 0; j < '+ str(num_blinks_per_active_phase) + '; j++) {\n')
            handle_song_parameters_txt.write('        digitalWrite(LEDBlue, HIGH);\n')
            handle_song_parameters_txt.write('        delay(' + str(blink_on_msec) + ');\n')
            handle_song_parameters_txt.write('        digitalWrite(LEDBlue, LOW);\n')
            handle_song_parameters_txt.write('        delay(' + str(blink_off_msec) + ');\n')
            handle_song_parameters_txt.write('    }')
            handle_song_parameters_txt.write('    delay(' + str(LED_rest_time) + ');\n')
            handle_song_parameters_txt.write('}')

    if PWM_option == 1:
        if blink_frequency == 0:
            pass
        if blink_frequency != 0:
            pass



    handle_song_parameters_txt.close()

    # now take hidden intermediate txt file and add template text to make ino file
    song_beginning = open('./.template_files/template_song_intro.txt', 'r')
    handle_song_parameters_txt = open(path_temp_song_parameters, 'r')
    song_end = open('./.template_files/template_song_coda.txt', 'r')
    song_complete = open(path_new_song_dir+"/"+(new_song_name)+".ino", 'w')
    a = song_beginning.read()
    b = handle_song_parameters_txt.read()
    c = song_end.read()
    song_complete.write(a + b + c)
    # now close all the files
    song_beginning.close()
    handle_song_parameters_txt.close()
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

    # remind user to have micrrocontroller plugged into laptop
    print("\n\nPlease make sure the Optobox is connected to the laptop via USB cable,")
    print(" then press the 'enter' key to continue.")
    foo = input('>')

    # next issue the make & upload commands
    make_command= "cd "+path_new_song_dir+"; make upload"
    os.system(make_command)

    # now add upload to the Log
    datetime_stamp = datetime.datetime.now().strftime("%Y-%b-%d\t%H:%M:%S\t(%a)")
    path_upload_log = "../Documents/Optobox_Files/Optobox_Logs/.upload_log.txt"
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
