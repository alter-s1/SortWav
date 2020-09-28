#main function
import os
import shutil
import py7zr as sz


def print_red(text):
    print("\033[31m {}".format(text))
def print_white(text):
    print("\033[37m {}".format(text))


def searching(file):
    seacrh_file = os.path.exists(file)
    if seacrh_file:
        return True;
    else:
        return False;


def sort():
    parent_directory = os.getcwd()
    positive_answer = 'y'
    negative_answer = 'n'
    copied_records = []
    lost_records = []
    clone_file = ''
    list_clone_file = []
    append_i = 0
    lost_i = 0
    j = 0
    e = 0


    print(' \nCurrent directory: ' + parent_directory + '\n')
    name_directory = str(input(' A directory will be created. Enter the title:\n '))          

    while True:
        
        search = searching(name_directory)

        if search:
            name_directory = str(input(' The directory already exists. Please choose another name:\n '))

        else:
            os.mkdir(name_directory)
            break


    while True:

        user_answer = str.lower(input(' Are you sure you want to continue? [Y/n]\n '))

        if user_answer == positive_answer:
            search_csv = searching('master/csv/main.csv')
            lost = open('lost.txt', 'w')
            complite = open('complite.txt', 'w')
            сlone = open('clone.txt', 'w')

            if search_csv:

                with open('master/csv/main.csv') as file:

                    for line in file:
                        line = line.strip('\n')
                        copied_records.append(line)

                    for elements in copied_records:
                        audio = copied_records[append_i]
                        path_to_file = parent_directory + '/' + name_directory + '/' + audio
                        source = parent_directory + '/master/wav/' + audio
                        search_file = searching(parent_directory + '/master/wav/' + audio)

                        if search_file == True:
                            clone_file = searching(parent_directory + '/' + name_directory + '/' + audio)

                            if clone_file == False:
                                copy = shutil.copyfile(source, path_to_file)
                                print_white(audio + ' - copied to directory ' + parent_directory + '/' + name_directory + '/')
                                append_i = append_i + 1
                                complite.write(audio + '\n')
                                e = e + 1

                            elif clone_file == True:
                                list_clone_file.append(audio)
                                append_i = append_i + 1
                                clone.write(audio + '\n')

                        elif search_file == False:
                                lost_records.append(audio)
                                append_i = append_i + 1

                    for elements in lost_records:
                        lost_audio = lost_records[lost_i]
                        print_red('\nError: ' + lost_audio + ' - file not found.')
                        lost_i = lost_i + 1
                        lost.write(lost_audio + '\n')

                    for elements in list_clone_file:
                        clone_audio = list_clone_file[j]
                        print(' \nClone: ' + clone_audio)
                        j = j + 1

                    print_white('Copied: ' + str(e) + '.')
                    print(' Clone: ' + str(j) + '.')
                    print(' Not found: ' + str(lost_i) + '.\n')

                    lost.close()
                    complite.close()
                    сlone.close()

                    while True:

                        if e == 0:
                            exit()

                        else:
                            user_answer = input(' Want to archive a directory? [Y/n] \n ')

                            if user_answer == positive_answer:
                                arch = parent_directory + '/' + name_directory
                                print(' Creating archive: ' + name_directory + '.7z')
                                sz.pack_7zarchive(name_directory, arch)
                                break

                            elif user_answer == negative_answer:
                                exit()

                            else:
                                print(' Please enter valid data.')

                    break

            else:
                print_red('File main.csv - not found.')
                exit()

        elif user_answer == negative_answer:
            print(' Exit...')
            exit()

        else:
            print(' Please enter valid data.')