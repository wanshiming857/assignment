path = 'Register.txt'
def intro():
    print('--------------------------------------------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------------------------------------------')
    print('Welcome enter the register:')
    print('1.  Register New Student  ')
    print('2.  Update Student Record   ')
    print('3.  Manage Enrolment         ')
    print('4.  Issue Transcripts         ')
    print('5.  View Student Information  ')
    print('6.  EXIT')
    print('--------------------------------------------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------------------------------------------')
def menu_function():
    File_exists = False      #using the try except to judge the destination about the file
    try :
        with open (path,'r') as file:
            file.read()
            File_exists = True
            print('Open the file successfully')
    except FileNotFoundError:
        print('Has something wrong about the file path')
    except IOError:
        print('Do not read file')
    while File_exists: #if File_exists = True ,active the menu loop and choice = 6 can break
        input('Press Enter to continue...')
        intro()
        try:
            choice = int(input('please enter your function number:'))
            if choice == 1:
                register_function()
            elif choice == 2:
                update_function()
            elif  choice == 3:
                manage_function()
            elif  choice == 4:
                issue_function()
            elif  choice == 5:
                view_function()
            elif  choice == 6:
                print('Exit successful!!!!!!!!!!!!!!!!!')
                break
            else:
                print('Please check your input number')
        except ValueError:
            print('Invalid input. Please enter a number.')
def id_input():
    while True:
        try:
            student_ID = input('Enter your student_ID (TPxxxxxx):')
            if len(student_ID) == 8 and str(student_ID[0:2]) == 'TP':
               return student_ID
            else:
                raise ValueError
        except ValueError:
            print('Your number is too long or error format')
def born_input():
    while True:
        born_time = input('Enter your time of born (YYYY-mm-dd):')
        try:
            Year,month,day = map(int,born_time.split('-'))
            if 1 <= month <= 12 and 1 <= day <= 31:
                return born_time
            else:
                print('Date and day is wrong')
        except ValueError:
            print('Input format is wrong')
def register_function():
    with open(path,'a',encoding='utf-8') as file,open(path,'rt',encoding='utf-8')as file1:
        while True:
            print('If you want to exit ,please enter【Q】in name ')
            name = str(input('Enter  your name:'))
            if name.upper() == 'Q':
                print('Exit the register successfully')
                break
            program = str(input('Enter your program:'))
            student_ID = id_input()
            born = born_input()
            contact = str(input('Enter your contact number or email:'))
            print('Running!')  # it used to add the context
            student_information = ','.join(
                [name, student_ID, program, born, contact + '\n'])  # Put the written data into one line
            if any(student_ID in line for line in file1.readlines()):
                print(f'You already register {student_ID}')
                input('Press Enter to continue...')
            else:
                print(student_information)
                file.write(str(student_information))  # witten the line into the file
                file.flush()
                print('Data stored successful')
def update_function():
    with open(path, 'rt', encoding='utf-8') as file:
        read_lines = file.readlines()
        while True:
            print('Please enter your want to update student ID and input TP000000 are return')
            Update_list = []
            Update_status = False
            search_ID = id_input()
            if str(search_ID)== 'TP000000':
                break
            for line in read_lines:
                deal_line = line.strip().split(',')
                if len(deal_line) == 5:
                        if str(deal_line[1]) == str(search_ID):
                            print(deal_line)
                            print(f'We are find student {deal_line[1]} * {deal_line[0]}')
                            deal_line[0] = str(input('Enter your new name:'))
                            deal_line[2] = str(input('Enter your new program:'))
                            deal_line[3] = born_input()
                            deal_line[4] = str(input('Enter your new contact number or email:'))
                            print(f'This your new information {deal_line},Running !!!!!')
                            Update_status = True
                        new_line = ','.join(deal_line)
                        Update_list.append(new_line+'\n')
                else:
                    print(f'Line format error: {line.strip()}')

            if Update_status:
                    with open(path, 'wt', encoding='utf-8') as file1:
                        file1.writelines(Update_list)
                        file1.flush()
                        print(f'{search_ID} update running successfully!!!! ')
                        input('Press Enter to continue...')
                        break
            else:
                print(f'we dont find your information {search_ID}')
                input('Press Enter to continue...')
def manage_function():
    with open(path,'rt',encoding='utf-8') as file:
        read_lines = file.readlines()
        while True:
            manage_status = False
            print('please enter your want to manage student ID')
            print('If you want to return ,please enter the TP000000 in the input of student ID')
            manage_list = []
            student_ID = id_input()
            if str(student_ID) == 'TP000000':
                print('Exit the register successfully')
                break
            for line in read_lines:
                if str(student_ID) in line:
                    read_lines.remove(line)
                    manage_status = True
                else:
                    manage_list.append(line)
            if manage_status:
                with open(path, 'wt', encoding='utf-8') as file1:
                    file1.writelines(manage_list)
                    file1.flush()
                    print('Delete successful')
                    input('Press Enter to continue...')
            else:
                print('We dont find the student in data please check and do it again')
                input('Press Enter to continue...')
def issue_function():
    with open(path,'rt',encoding='utf-8') as file:
        read_lines = file.readlines()
        while True:
            print('Please enter your ID number')
            print('If you want to exit , please enter TP000000 in ID of input')
            student_id_search = id_input()
            search_status = False
            if str(student_id_search) == 'TP000000':
                print('Exit the register successfully')
                break
            for line in read_lines:
                new_line = line.strip().split(',')
                student_id_info = new_line[1]
                if str(student_id_search) == student_id_info:
                    print(f'Student information {line}')
                    generate_info = line
                    search_status = True
            if search_status:
                confirm = str(input('Please confirm it[Enter:YES/NO} , system will generate a txt for this student:'))
                if confirm.upper() == 'YES':
                    with open(f'{student_id_info}.txt','wt',encoding='utf-8') as file1:
                        file1.write(generate_info)
                        print('Generate successfully')
            else:
                print(f'We dont find about {student_id_search} in text, please check it again')
                input('Press Enter to continue...')
def view_function():
    with open(path,'rt',encoding='utf-8')as file:
        read_lines = file.readlines()
        while True:
            try:
                choice = int(input('1---View all student 2---View search student 3---Return \nEnter your function number:'))
                if choice == 1:
                    for line in read_lines:
                        print(line)
                elif choice == 2:
                    student_id_search = id_input()
                    for line in read_lines:
                        if str(student_id_search) in line:
                            print(f'This is about {student_id_search} information \n{line}')
                            break
                elif choice == 3:
                    break
                else:
                    print('Please check your input number')
            except ValueError:
                print('Invalid input. Please enter a number.')
                input('Press Enter to continue...')
menu_function()
