import os
import datetime

def upload_song():
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
    while os.path.isdir(path_song_Makefile) == False:
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

    os.system('clear')
    print('--your song has been uploaded to OptoBox.')

upload_song()
