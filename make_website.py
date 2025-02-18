def read_and_store_file(file):
    '''takes a text file as an argument and stores each line in the file in memory.
    Returns a list of each line in the file.'''
    #opens the file for reading and stores it in the variable f.
    f = open(file, "r")
    #creates a list of lines variable for the file. Each line in the file is a item in the list.
    lst_of_lines = [line.strip() for line in f.readlines()]
    #close the file.
    f.close()
    return(lst_of_lines)

def detect_and_return_name(line_list):
    '''finds the name in the list of lines returned from the read_and_store_file function.
    Returns the name as a string.'''
    #It is a given for the test resumes that the first line of the resume is always the name.
    name = line_list[0]
    #checks if the first letter of the name is uppercase or not.
    if name[0].isupper() == True:
        #Returns the name is the first letter is uppercase.
        return(name)
    else:
        #otherwsie returns the string 'Invalid Name'.
        return('Invalid Name')

def detect_and_return_email(line_list):
    '''finds the email in the list of lines returned from the read_and_store_file function.
    Returns the email as a string.'''
    #loops through each item in the list of lines from the file.
    for each in line_list:
        #for each item in the line list, loops through each character and checks conditions to find the email address.
        for i in range(0, len(each)):
            #if the the email has an '@' symbol in it, and the last four characters are '.edu' or '.com', and there are no digits in the email, and the first character after the '@' symbol is lowercase.
            #then the email is returned.
            if each[i] == '@' and (each[-4:] == '.edu' or each[-4:] == '.com') and any(char.isdigit() for char in each) == False and each[i+1].islower() == True:
                  return(each)
    #otherwise, an empty string is returned.
    return('')

def detect_and_return_courses(line_list):
    '''finds the course list in the list of lines returned from the read_and_store_file function.
    Returns the courselist as a list.'''
    line_with_courses = ''
    courses_start_index = ''
    
    #loops through the list of file lines and gets the line that contains the courses list.
    for i in range(0,len(line_list)):
        if 'Courses' in line_list[i]:
            #stores the line containing the courses list as a variable
            line_with_courses = line_list[i]
            break

    #loops through the line with the course list that was previously identifed, starting at the end of the word courses.
    #finds the index for the first character that is in the alphabet. Then returns that index.
    for i in range(len('Courses'),len(line_with_courses)):
        if line_with_courses[i].isalpha() == True:
            courses_start_index = i
            break

    #splits the line with the course list starting at the index where the random punctuation ends and the courses start.
    #Adds each course to course list.
    #strips any starting or ending whitespace from the course list.
    courselist = [each.strip() for each in line_with_courses[courses_start_index:].split(',')]

    return(courselist)

def detect_and_return_projects(line_list):
    '''finds the project list in the list of lines returned from the read_and_store_file function.
    Returns the project list as a list.'''
    #sets the index where the projects list starts.
    projects_start_index = line_list.index('Projects')
    #Finds the index of the line that contains at least 10 minus signs.
    for each in line_list:
      if '----------' in each:
        projects_end_index = line_list.index(each)
 
    #adds the list of projects to the project list based on the previously found start and end index.
    project_list = [each for each in line_list[projects_start_index:projects_end_index]]
   
    #goes through the project list and makes sure that there are no empty strings in the list.
    for each in project_list:
        if each == '':
            #removes empty strings if they are found.
            project_list.pop(project_list.index(each))
    return(project_list)


def surround_block(tag, text):
    """Surrounds the given text with the given html tag.
    Returns the proper html formatting for the given tag and text as a string."""
    return(f'<{tag}>{text}</{tag}>')


def write_html_div_to_file(html_file_to_write,interior_block_1_type, interior_block_2_type, interior_block_1_text, interior_block_2_text):
    '''Uses the surround_block function to write an html dv block of two levels to an html file.
    Takes the html file yu want to write to, the type of the first interior html block, the type of the second interior html block, 
    the text to be enclosed in the first interior html block, and the text to be enclosed in the second interior html block.'''
    html_file_to_write.write(surround_block('div', '\n' + surround_block(interior_block_1_type, interior_block_1_text) + '\n' + surround_block(interior_block_2_type,interior_block_2_text) + '\n')+ '\n')
    

def create_email_link(email_address):
    """Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything."""
    #checks if the '@' symbol is in the email address.
    if '@' in email_address:
        #if '@' is in the email, the index of the '@' symbol in the email string is found, and replaced with the string '[aT]'.
        at_index = email_address.index('@')
        #the email is returned in an html format.
        return(f'<a href="mailto:{email_address}">{email_address[:at_index]}[aT]{email_address[at_index+1:]}</a>')
    else:
        #if an '@' is not found, then the email is returned as it is in the correct format.
        return(f'<a href="mailto:{email_address}">{email_address}</a>')


def read_html_file_to_list(html_file):
    '''takes an html file and writes it to a list'''
    #opens the old html file to read
    old_html_file = open(html_file, "r")

    #reads each line from the old html file and adds them to a new list.
    html_list = [line for line in old_html_file.readlines()]

    old_html_file.close()

    return(html_list)

    
def generate_html(txt_input_file, html_output_file):
    """Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file"""

    #converts the txt file into a list of lines of that text.
    txt_list = read_and_store_file(txt_input_file)
    #extracts the name from the txt list.
    name = detect_and_return_name(txt_list)
    #extracts the email from the txt list.
    email = detect_and_return_email(txt_list)
    #extracts the projects list from the txt list.
    projects = detect_and_return_projects(txt_list)
    #extracts the courses list from the txt list.
    courses = detect_and_return_courses(txt_list)
    #generates the formated email link
    email_link = create_email_link(email)

    new_html_list = read_html_file_to_list('resume_template.html')

    #creates a new html file to write to
    new_html_file = open(html_output_file, "w+")

    #writes the lines from the html list until the first body tag to the new html file.
    for i in range(0,new_html_list.index('<body>\n')+1):
        new_html_file.write(new_html_list[i])

    #writes the first div line to the new html file.
    new_html_file.write('<div id="page-wrap">\n')
    #writes the email line to the new html file.
    write_html_div_to_file(new_html_file,'h1', 'p', name, 'Email: ' + email_link)
    #stores the projects list item html block as a string
    projects_list_html = '\n' + surround_block('li',projects[1]) +  '\n' + surround_block('li',projects[2]) + '\n'
    #writes the projects line to the new html file.
    write_html_div_to_file(new_html_file,'h2', 'ul', projects[0], projects_list_html)
    #writes the courses line to the new html file.
    write_html_div_to_file(new_html_file,'h3', 'span', 'Courses', courses[0]+', '+courses[1]+', '+courses[2])
    #writes the closing lines to the new html file.
    new_html_file.write('\n</div>\n' + '</body>\n' + '</html>\n')
    #wcloses the new html file.
    new_html_file.close()

def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    generate_html('Test_Resume/resume_bad_name_lowercase/resume.txt', 'Test_Resume/resume_bad_name_lowercase/resume.html')
    generate_html('Test_Resume/resume_courses_w_whitespace/resume.txt', 'Test_Resume/resume_courses_w_whitespace/resume.html')
    generate_html('Test_Resume/resume_courses_weird_punc/resume.txt', 'Test_Resume/resume_courses_weird_punc/resume.html')
    generate_html('Test_Resume/resume_projects_w_whitespace/resume.txt', 'Test_Resume/resume_projects_w_whitespace/resume.html')
    generate_html('Test_Resume/resume_projects_with_blanks/resume.txt', 'Test_Resume/resume_projects_with_blanks/resume.html')
    generate_html('Test_Resume/resume_template_email_w_whitespace/resume.txt', 'Test_Resume/resume_template_email_w_whitespace/resume.html')
    generate_html('Test_Resume/resume_wrong_email/resume.txt', 'Test_Resume/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()

