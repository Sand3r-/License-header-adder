import sys, os, datetime

license_text = '''{start_multi_line_comment}
 {bullet} {filename}
 {bullet} {description}
 {bullet}
   Copyright {year} {author}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
{end_multi_line_comment}'''

supported_extensions = ['.h', '.cpp', '.cs', '.py']

def add_c_data(dictionary):
    dictionary["start_multi_line_comment"] = "/*"
    dictionary["end_multi_line_comment"] = "*/"
    dictionary["bullet"] = "*"
    return dictionary

def add_py_data(dictionary):
    dictionary["start_multi_line_comment"] = "\'\'\'"
    dictionary["end_multi_line_comment"] = "\'\'\'"
    dictionary["bullet"] = "\'"
    return dictionary

def does_file_exist(path):
    return os.path.isfile(path)

def get_name_and_extension(path):
    name, extension = os.path.splitext(path)
    global supported_extensions
    valid = True
    for ext in supported_extensions:
        if ext == extension:
            break
    else:
        print("Unsupported file extension: " + extension)
        print("Please use one of the following extensions:")
        print(supported_extensions)
        valid = False

    return valid, name, extension

def print_help():
    print("Usage 1:\npython " + sys.argv[0] + " <file_name_1> <filename_2> ... <filename_n>\n")
    print("Usage 2 (not supported yet):\npython "  + sys.argv[0] + " <file_name> -m <description>\n")

    print("The first command adds license headers with filename,")
    print("author, year and an empty description to each valid file")
    print("provided in the argument list.")
    print("The second command is not implemented yet.\n")
    print("In order to set the author, please create file named")
    print("'lic_settings.ini' storing your name in the first line.\n")

    print("Supported types: ")
    global supported_extensions
    print(supported_extensions)

def get_file_list(): # A. k. a. parse the cmd line arguments
    arg_num = len(sys.argv)
    if arg_num < 2:
        print_help()
        exit(-1)

    file_list = []
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if arg == '-m':
            print("This operation is not supported yet.")
            exit(-3)
        path = arg
        if not does_file_exist(path):
            print("File " + path + " does not exist")
        else:
            valid, name, extension = get_name_and_extension(path)
            if valid:
                file_list.append(path)

    return file_list

def contains_header(path):
    return "Copyright" in open(path).read()

def get_license_data_data(path, extension, author, year, description):
    license_data = {}
    license_data["filename"] = path
    license_data["description"] = description
    license_data["year"] = year
    license_data["author"] = author

    if extension == ".cpp" or extension == ".h" or extension ==".cs":
        return add_c_data(license_data)
    elif extension == ".py":
        return add_py_data(license_data)
    else:
        print("Sorry, the extension " + extension + " is NYI")

def get_author():
    license_path = "lic_settings.ini"
    if not does_file_exist(license_path):
        print("Please specify the author name in lic_settings.ini")
        exit(-4)
    return(open(license_path).read())

def get_current_year():
    return datetime.datetime.now().year

def get_license_body(path, description=""):
    name, ext = os.path.splitext(path)
    license_body = license_text
    author = get_author()
    year = get_current_year()
    license_data = get_license_data_data(path, ext, author, year, description)
    return license_body.format(**license_data)

def add_header_to_file(path):
    license_body = get_license_body(path)
    with open(path, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(license_body + '\n' + content)

def add_headers(file_list):
    for path in file_list:
        if not contains_header(path):
            add_header_to_file(path)
        else:
            print("File " + path + " already has a header")


file_list = get_file_list()
add_headers(file_list)
