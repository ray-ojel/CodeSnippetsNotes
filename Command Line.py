COMMAND LINE PROMPT:
# Directories or Folders
A subdirectory is contained in a parent directory. If no parent directory, it's called a root

# *nix System root directory
(/) Single slash, root directory, unlike windows with multiple directories C, D, E, etc
EX: in /home/mojel, the (/) is the root directory, home is a subdirectory of the root, mojel is a sub of home

# Home Directory
/home/mojel$

# Elementary commands
utility parameter1 parameter2 ... parameterN # for N non-negative

# Utility:
Also 'Command' or 'Program'
First item in the instruction

# Parameter:
Either an option or an argument:

# Option:
String of symbols that modifies the behavior of the command
Always starts with a dash (-)
IF it starts with (--) it is a long option, otherwise it is a short option
Also  called 'flag' and 'switch'

# Argument:
An object upon which the command acts
Also 'operand'

# Example
$ diff -y west east
# Diff is the command name
# 3 Parameters:
# -y is an option
# west and east are arugments because diff acts on them

# Types of Commands
# Files: Programs, Tools, Commands, etc. run files. .exe
# Builtin: Commands that run in RAM for quick access
# Alias: Diff name for command, to abbrev something
# Function: Just like in python
# Keyword: Unique words for commands

# Order of running commands
# 1. Aliases
# 2. Special built-ins (a small list of built-ins that are considered special)
# 3. Functions
# 4. Regular built-ins
# 5. And then it will look for files in a select list of directories called PATH

# Commands with multiple options
$ command -option1 -option2 argument
# OR
$ command -option1option2 argument

# Absolute path
Any path that starts with a slash (/)
EX: /home/mojel

# Relative path
Any other path, relative to the cwd
EX: home/mojel
EX: mojel/
________________________________________________________________________________


GENERAL COMMANDS:
# Get command options
$ command --help
# OR
$ help command

# Run Python
$ Python3 -c "code" # Python3 is a file type

# Print command (like Python)
$ echo 'string'

# Defaults to adding new line, to no add new lines
$ echo -n 'string'

# Set Autocomplete ON
$ compgen # Press TAB key to autocomplete

# List all Keyword type commands
$ comgen -k

# Create an alias command
$ alias a=alias

# Remove an alias
$ unalias a

# Get command type
$ type

# Get command type readable
$ type -t command # -t is not POSIX compliant and not portable

# Get command PATH
$ type -P command # Not portable

# Find total functions available to use rn
$ declare -F # Known as BASHISM i.e. only available for Bash, non-POSIX

# Access command history
# Use up and down arrow to write previous commands and rerun with ENTER
# OR
$ history

# Refrence commands history by indexing (!)
$ !4 # Runs 4th command
$ !-1 OR !! # Runs last command
$ !-2 # Runs second-to-last command

# Search for files
$ find [location] -iname ['filename'] # use (/) for location of root, -iname ignoes cases

# Clear the terminal
$ clear

# Exit the terminal
$ exit
________________________________________________________________________________


THE FILSYSTEM:
# Show current directory
$ pwd # print working directory

# List content of a directory
$ ls [OPTION] [FILE] # Defaults to current directory

# List content of a directory and highlight subdirectories
$ ls -p [FILE] # Adds (/) to the end of their names

# List content and hidden files
$ ls -A [FILE] # Adds (.) to the beginnning of their names

# List long content of directory
$ ls -l [FILE] # Lists
# 1. File type and file or folder permissions (e.g.: drwxr-xr-x)
# 2. The number of paths the file or folder has (e.g.: 1)
# 3. Owner of the file or folder (e.g.: root)
# 4. Group owner of the file or folder (e.g.: root)
# 5. The size of the file or folder in bytes (e.g.: 4096)
# 6. The modification date and time of the file or folder (e.g.: Jan 24 16:03)
# 7. The file or folder's name (e.g.: bin)
# Startswith:
# (-) Regular File
# (d) Directory
# (l) Symbolic Link

# list long content, hidden files and highlight subs
$ ls -lAp # Alt, if 1. starts with (d), you don't need -p option

# List human readable long content
$ ls -lh # Changes some values to easier to understand values, ex size in KB\

# Change directory
$ cd [PATH] # in Ubuntu, use /mnt/c/ before any path

# Change to the parent directory
$ cd .. # .. is parent of the current directory

# Go back two parent directories
$ cd ../..

# Change to root directory
$ cd /

# Change to home directory
$ cd

# Change to home directory of the user
$ cd ~[USERNAME]
$ cd ~ # To change to just home directory

# Change to last directory
$ cd - # switch between current and last directory

# Create a directory
$ mkdir [PATH] # Make directory

# Create more than one dir at once
$ mkdir dir1 dir2 dir3

# Delete an empty dir
$ rmdir [PATH] # Works on multiple dirs at once

# Delete a file
$ rm -i [FILE] # Should use -i to double check

# Delete non-empty dir
$ rm -R [PATH]

# Copy a file to another directory
$ cp [FILE] [PATH] # works with mult files,

# Copy a file in the same directory
$ cp [FILE] [FILE]

# Copy a file to a hidden file in the same dir
$ cp [FILE] .[FILE] # the (.) before the name

# Check overwrite when copying a file
$ cp -i [FILE] [PATH] # interactive mode, asks to overwrite or not

# Copy a directory with its full contents
$ cp -R [PATH] [PATH]

# Create a copy of Dir1 inside Dir2
$ cp -R Dir1 Dir2

# Move a file to another directory
$ mv [SOURCE PATH] [DEST PATH] # Can move multiple files at once, original file deleted

# Rename a filie
$ mv [OLD NAME] [NEW NAME]

# Current directory
.

# Parent directory
..
________________________________________________________________________________


GLOB PATTERNS & WILDCARDS:
# Like regular expressions
# Used to match file names for commands such as cp
# Built from special characters called "Wildcards" and regular characters
# Used in conjuction with other characters to form complex patterns
# That is done by concatenating wildcards

# Use the literal meaning of a character
Escape Character (\) # Backslash before char
OR
Single Quotes ('') # Matches literal word
EX:
# Create new directory 'Ray?'
mkdir Ray\?
# Create new dir "Ray?"
mkdir 'Ray?'

# Match any character, any number of times, expect for leading dots (.)
The * Wildcard # Like RegEx (.*)
EX:
# List any filename
$ ls *
# List any filename ending with 'st'
$ ls *st
# List any filename starting with 'v'
$ ls v*

# Match any character exactly one time
The ? Wildcard # Like RegEx (.)
EX:
# List any 4 letter filename that ends with 'its'
$ ls ?its
# List dir 'Ray?'
$ ls Ray\?

# Match either of specific characters exactly one time
The [] Wildcard # Like RegEx ([])
EX:
# list any filename that starts with either 'a', 'i', or 'u'
$ ls [aiu]*
# List any filename that starts with vowel, is four chars long and last letter either 's', 't', or 'u'
$ ls [aAiIuUeEoO]??[stu]

# Match any character OTHER than char exaclty one time
The ! Wildcard # Like RegEx (^)
EX:
# List any filename that doesnt start with 'a' or 'u'
$ ls [!au]

# Match any characters in ranges exactly one time
The [-] Wildcard # like RegEx ([-])
EX:
# List any upper case character
$ ls [A-Z]

# Match any letter only
The [[:alpha:]] Wildcard # like RegEx (w)

# Match any number 0-9
The [[:digit:]] Wildcard # like RegEx (d)

# Match any lower case letters
The [[:lower:]] Wildcard

# Match any upper case letters
The [[:upper:]] Wildcard

# Global regular expression print
$ grep -n 'pattern' file # -n prints line number for match

# Grep select non-match
$ grep -v 'pattern' file

# Grep select but ignore case
$ grep -i 'pattern' file

# Exclude filenames from output
$ grep -h 'pattern' file
________________________________________________________________________________


PERMISSIONS:
# Print the current user
$ whoami

# Print the current user
$ id -un

# Print the current user info
$ id

# Understanding Output
>>> uid=1000(mojel) gid=1000(mojel) groups=1000(mojel),27(sudo)
# UID: User ID, unique, and USERNAME
# GID: Main Group ID, unique, and GROUPNAME
# Groups: ALL GroupNames and IDs, i.e. mojel and sudo groups here

# Print the current groups of a user
$ groups

# Display file status
$ stat file

# Run commands as other users
$ sudo -u user <command> # sudo (substitute user do)

# Run commands as root or superuser
$ sudo <command> # is enough

# IN UNIX: EVERYTHING IS A FILE!
# Three scopes:
# 1. There are permissions for the owner
# 2. There are for the group
# 3. There are for everyone else
# For each scope, permisions are defined by
# a sequence of three characters called
# File Access Modes: In-Order
# 1. Read mode
# 2. Write mode
# 3. Execute mode

# Looking for file permissions
$ ls -l # Liat with long option
# OR
$ stat # File status

# Understanding Output
Filename        User    Group       Others
config_file_1   r-x     r--         r--
config_file_2   rw-     rw-         rw-
Trash           rwx     r--         r--
Mistery_file    ---     ---         ---

# Read Mode
(-) # Files can't be read, directory content can't be listed
(r) # Allowed file to be opened, allows dir content to be listed

# Write Mode
(-) # Files can't be modified, dir content can't be modified
(w) # Allows files contents to be modified.
# Contents of a dir to be deleted, renamed and created,
# Only if execution permission is set. Otherwise no effect.

# Execute Mode
# Some files are programs, therefore having execute permissions allows to execute them
# The execution permissions are hereditary. If an ancestor doesn't have execution permissions,
# none of its descendants will either, regardless of whether the x bit is set or not.
(-) # File can't be executed, Directory can't be entered.
(x) # Allows file to be executed, dir can't be entered

# Number of Possibilites
---, --x, -w-, -wx, r--, r-x, rw-, rwx # Eight possibilites (2 x 2 x 2)

# Octal Notation
---: 0 (No permissions)
--x: 1 (execute only permission)
-w-:2 (write only permissions)
-wx:3 (write and execute permissions)
r--:4 (read only permissions)
r-x:5 (read and execute permissions)
rw-:6 (read and write permissions)
rwx:7 (read, write, and execute permissions)
# Easy to memorize: -:0, x:1, w:2, r:4

# Change the permissions of files
$ chmod [ugoa][+-=][rwx] files # change mode
# Scope: Owner/user (u), group (g), others (o) and all (a)
# Operator: add (+) to existing, remove (-) modes, set (=) new modes and delete unmentioned
# Mode: read (r), write (w), execute (x)

# Change permissions of files in multiple scopes at once
$ chmod u=rwx,g=rx,o=r files

# Set permissions of modes equal
$ chmod g=u files # Can also use wildcards

# Set permissions of modes using Octal Notation
$ chmod 777 files # Octal = 777 eq to a=rwx

# Change the owner of the file
$ sudo chown [new_owner][:new_group] files...
# [] mean not necessary to be there
# ... mean can use multiple files

# Change the group of the file
$ chgrp
________________________________________________________________________________


LESS: # A terminal pager, i.e used to view contents of a text file
# Acess the command manual
$ man command # Display in a program called LESS, on the man page

# Structure:
# NAME: The command's name and a brief description of what it does.
# SYNOPSIS: The allowed syntax.
# DESCRIPTION: A description of the command. It frequently includes information about its options.
# OPTIONS: When not included in the section above, the options are documented in this section.

# Simple manual
$ whatis command

# Immedaite manual help
$ help command #OR
$ command --help

# Less command
$ less file # to open the file in a less pager

# Breakdown of MAN and HELP page
# Bold Text: Type exactly as seen
# Italic: replace with appr arg
# []: Optional arg
# arg|arg: Can't be used together
# Arg... : Can Repeat args
# [arg]... : Can repeat entire optional arg

# LESS Features:
# Input                             Action
# Up/down arrows         Scroll up/down one line
# Left/right arrows      Move page to the left/right
# b                      Scroll up (or backwards) one page
# Space                  Scroll down one page
# g                      Move to the beginning of the file
# G                      Move to the end of the file
# /pattern               Search forward for the occurrence of the regex pattern
# ?pattern               Search backwards for the occurrence of the regex pattern
# n                      Find next occurrence of the previous search
# N                      Find previous occurrence of the previous search
# :p                     Move to previous file
# :n                     Move to next file
# h                      Display less's help screen (with less)
# q                      Quit the active instance of less
________________________________________________________________________________


FILE TEXT PROCESSING: # Like data exploration and cleaning in python
# Determine file kind
$ file filename
#OR
$ file * # for all directory

# Create an empty file
$ >empty_file
# OR
$ touch file1, file2 # only if file doesn't exist already

# Display the top of a file
$ head file

# Displa the bottom of a file
$ tail file

# Defaults to list 10 lines, to change
$ head -n k file # k is the number of lines we want ex 5

# Exclude some number of lines from the ends
$ head -n -k file # -k means will print all lines except last k lines

# Exclude for tail
$ tail -n +k file # +k means will print all lines starting from k line

# Count the number of lines, words and bits of a file
$ wc file # In the order above

# Count the number of lines
$ wc -l file # -l option for lines only

# Print, view and count file columns
$ column -s"," -t file # Use (-s',') to specify , delimit instead of space

# Dispplay random set of lines
$ shuf -n k file # k is number of lines, shuf == shuffle random lines

# Concatenate files
$ cat file1 file2 # Like df.concat, order specific

# Concat all files in a directory
$ cat *

# Concat files but reverse the order of the lins
$ tac file1 file2 # still order specific

# View sorted file
$ sort file # sorts lexicographically, pass -g to sort by nums

# Sort by reverse/descending order
$ sort -r file # WARNING: Favores smaller case over cap

# Keep only unique values while sorting
$ sort -u file # Gets rid of duplicates

# Running two files in sort
$ sort file1 file2 # will concat and sort both as one

# Sort df by a column
$ sort -t',' -k<start,stop>g file.csv
# -t tells delimiter
# -k (key)
# col index, repeated (seen as a range)
# -g sorts by numeric

# Sort df by multiple columns, numerically, in reverse
$ sort -t',' -k<col1,col1>gr -k<col2,col2>g file.csv

# Display select columns
$ cut -d',' -f<col1,col2> file.csv # -d delimiter, -f specific cols

# Display range of columns
$ cut -d',' -f<col1-col2> file.csv # Can also mix both ex: 2,3,7-9

________________________________________________________________________________


REDIRECTION & PIPELINES:
# Process: Every instance of running a command
# Every process interacts with its *nix envi using communication channels
# These are known as streams, three special kinds are called Standard Streams
# Kinda like items on grovery store belt, checked out one at a time
1. Stdin: (Standard input) used to RECEIVE input
2. Stout: (standard output) where the command OUTPUT goes
3. Sterr: (Standard error) Where ERROR messages go

# Parent process: Process that spawns another process.
Ex: Bash=parent, cmd=child. # 'Bash is a parent process of the process spawned by cmd'

# Std. Streams are refered to by File Descriptors, non-negative int, which *nix uses
1. Stdin = 0
2. Stout = 1
3. Stderr = 2

# List files of the directory /proc/$$/fd
$ ls -l /proc/$$/fd
# /proc/$$ : Directory of the current path -> Bash in this case
# fd is the File Descriptors directory, represented as Symbolic Links (l)
# File /dev/tty1 represents our shell

# Stdin
$ sort -u >sorted_stdin # This command is an example that needs a stdin after running
a # Input text1
i # Input text2
u # Input text3
CTRL-D # End of transmission

# Transliteration
$ tr 'Old_char' 'new_chars' # Used to replace characters with (possibly other) characters

# Stdin redirection
$ command 0<filename # < tells to use file as input

# Redirection operator
$ command >filename # > tells to save result to file

# Redirect stout to file
$ command 1>filename # 1 tells to save stdout

# Defaults to overwriting file content, to append
$ command 1>>filename

# Redirect to discard output data
$ command 1>/dev/null # Output is ignored by OS and disappears

# Redirect to sterr
$ command 2>file # Use 2>> to append

# Redirecting multiple commands
$ command1 command2 1>file1 2>file2 # Or any other pattern, each one mathces its order

# Using file descriptors duplication to redirect both stdout and stderr to a file
$ command >filename 2>&1
# Redirect 1 to a file (>filename)
# Create a copy of 1 in 2 (2>&1)
# Both Stdout and Stderr will be redirected to a file

# Piping
$ command1 | command2 # | is a pipe, direct output of command1 as input of cmd2

# Pinping multiple commands
$ command1 | command2 | command3 # they execute in order
