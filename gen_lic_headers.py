import sys
import os

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


def does_file_exist(path):
    return os.path.isfile(path)

def get_name_and_extension(path):
    name, extension = os.path.splitext(path)
    supported_extensions = ['.h', '.cpp', '.cs', '.py']
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
    print("Usage 1 (not supported yet):\npython "  + sys.argv[0] + " <file_name> -m <description>")
    print("Usage 2:\npython " + sys.argv[0] + " <file_name_1> <filename_2> ... <filename_n>")

    # print("The first command will add ") # TODO

def process_path():
    arg_num = len(sys.argv)
    if arg_num < 2:
        print_help()
        exit(-1)
    # TODO: handle the case when we have either the filename and desc or list of files

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
                file_list.append((name, extension))
    
    print(file_list)

    return file_list


process_path()


# arg_num = len(sys.argv)




# path = sys.argv[1]
# print(path)