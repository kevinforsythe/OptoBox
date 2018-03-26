import os

def upload_song():

    # first copy the Makefile into the new song dir
    # temporary dummy/test value here for path_new_song_dir
    path_new_song_dir = './output_songs/test44'
    path_song_Makefile = path_new_song_dir+"/Makefile"
    handle_template_Makefile = open('./.template_files/template_Makefile', 'r')
    handle_song_Makefile = open(path_song_Makefile, 'w')
    transcribed_makefile = handle_template_Makefile.readlines()
    for i in range(len(transcribed_makefile)):
        handle_song_Makefile.write(transcribed_makefile[i]+'\n')
    handle_template_Makefile.close()
    handle_song_Makefile.close()



    make_command= "cd "+path_new_song_dir+"; make upload"
    os.system(make_command)

upload_song()
