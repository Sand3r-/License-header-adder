# License-header-adder
Allows to add Apache License 2.0 to .cpp, .h, .py and .cs files through a python script.

The license has the following format, when executed for .h, .cpp or .cs files:
```
/*
 * <file.name>
 * <description>
 *
   Copyright <current_year> <name_from_settings_file>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
```
Python version uses just a different syntax for comments.

When executed for files which already contain the header (that is those, that contain word "Copyright" anywhere in its source code),
those files are skipped.

Files 

## Installation
In order to get the license generator to work, modify the lic_settings.ini, so that it contains your name on the first line.

To run the script you can either:
* Copy the script and settings file to the directory you want to use it in
* Add the repository to the path, and modify the batch file so that it refers to that specified path

## Running
If you happen to have copied the *.py file and settings to the repository containing files that are to have their license headers added, please execute
```
python gen_lic_headers.py <file_name_1> <filename_2> ... <filename_n>
```

The command will add license headers with appropriate file name, author, current year, and an empty description to all files provided in
arguments list.
