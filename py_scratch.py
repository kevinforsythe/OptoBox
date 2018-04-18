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
    new_song_name = input('\nPlease choose a name for your new song:\n>')
    path_new_song_dir = "~/Documents/Optobox_Files/Optobox_Songs/"+(new_song_name)
    while os.path.isdir(path_new_song_dir) == True:
        print("Sorry, a song folder with this name already exists.")
        new_song_name = input('Please choose a unique name for your new song:\n>')
        path_new_song_dir = "~/Documents/Optobox_Files/Optobox_Songs"+(new_song_name)
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

    num_blinks_per_active_phase = int(LED_active_time/blink_period)


    # recall, path_new_song_dir = "~/Documents/Optobox_Files/Optobox_Songs/"+(new_song_name)
    # this makes a hidden txt file which holds the song parameters
    path_temp_song_parameters = path_new_song_dir+"/."+(new_song_name)+".txt"
    handle_song_parameters_txt = open(path_temp_song_parameters, 'w')


#  4 different sections here for a 2x2 matrix of options: +/-PWM and +/- blinking
    if PWM_option == 0:
        if blink_frequency == 0:
            # Set the number of 'LED Active/Resting' cycle repeats
            handle_song_parameters_txt.write('for (int i = 0; i < '+ num_LED_pattern_repeats + '; i++) {/\n')
            handle_song_parameters_txt.write('        digitalWrite(LEDBlue, HIGH);\n')
            handle_song_parameters_txt.write('        delay(' + LED_active_time + ');\n')
            handle_song_parameters_txt.write('        digitalWrite(LEDBlue, LOW);\n')
            handle_song_parameters_txt.write('        delay(' + LED_rest_time+ ');\n')
            handle_song_parameters_txt.write('}')

        if blink frequency != 0:
            handle_song_parameters_txt.write('for (int i = 0; i < '+ num_LED_pattern_repeats + '; i++) {/\n')
            handle_song_parameters_txt.write('    for (j = 0; j < '+ num_blinks_per_active_phase + '; j++) {\n')
            handle_song_parameters_txt.write('    }')
            handle_song_parameters_txt.write('}')


        else:
            print("error!")
            quit
    if PWM_option == 1:
        if blink_frequency == 0:
            asdf
        if blink frequency != 0:
            asdf
        else:
            print("error!")
            quit







    handle_song_parameters_txt.write('    for (j = 0; j < '+ num_blinks_per_active_phase + '; j++) {\n')
    handle_song_parameters_txt.write('        digitalWrite(LEDBlue, HIGH);\n')
    handle_song_parameters_txt.write('        delay(' + blink_on_msec + ');\n')
    handle_song_parameters_txt.write('        digitalWrite(LEDBlue, LOW);\n')
    handle_song_parameters_txt.write('        delay(' + blink_off_msec + ');\n')

    # close the for loop for LED Active phase blinking
    handle_song_parameters_txt.write('    }')

    #LEDs Resting

    # close the for loop for Active/Resting cycle repeats
    handle_song_parameters_txt.write('}')

#
#
#
#         handle_song_parameters_txt.write('digitalWrite(LEDBlue, LOW);\n')
#         handle_song_parameters_txt.write('delay(' + beat_value + ');\n')
#
#
#
#         elif song_csv_data[i] == '1\n':
#             handle_song_parameters_txt.write('digitalWrite(LEDBlue, HIGH);\n')
#             handle_song_parameters_txt.write('delay(' + beat_value + ');\n')
#         else:
#             print("ERROR:  You're CSV data is dirty (i.e. contains data other than '1' or '0')")
#             quit()
#     handle_song_parameters_txt.close()
#
#     # now take hidden intermediate txt file and add template text to make ino file
#     song_beginning = open('./.template_files/template_song_intro.txt', 'r')
#     handle_song_parameters_txt = open(path_temp_song_parameters, 'r')
#     song_end = open('./.template_files/template_song_coda.txt', 'r')
#     song_complete = open(path_new_song_dir+"/"+(new_song_name)+".ino", 'w')
#     a = song_beginning.read()
#     b = handle_song_parameters_txt.read()
#     c = song_end.read()
#     song_complete.write(a + b + c)
#     # now close all the files
#     song_beginning.close()
#     handle_song_parameters_txt.close()
#     song_end.close()
#     song_complete.close()




compose_song()
