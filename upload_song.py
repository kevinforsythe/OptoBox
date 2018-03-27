import os

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

    # ## we can use the old Makefile here, no need to rewrite it
    # # now copy the Makefile into the new song dir
    # path_song_Makefile = path_old_song_dir+"/Makefile"
    # handle_template_Makefile = open('./.template_files/template_Makefile', 'r')
    # handle_song_Makefile = open(path_song_Makefile, 'w')
    # transcribed_makefile = handle_template_Makefile.readlines()
    # for i in range(len(transcribed_makefile)):
    #     handle_song_Makefile.write(transcribed_makefile[i]+'\n')
    # handle_template_Makefile.close()
    # handle_song_Makefile.close()

    # issue the make & upload commands
    make_command= "cd "+path_old_song_dir+"; make upload"
    os.system(make_command)
    os.system('clear')
    print('--your song has been uploaded to OptoBox.')

upload_song()
