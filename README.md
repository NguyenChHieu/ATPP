# ATPP
ATPP (Automatic Test Preparation Program) is the first "big" Python program I've ever created.

**Derived from first assignment of INFO1110 mid year entry 2023**

This program allowing students like yourself to complete an online exam. The exam can contain multiple-choice questions (single or multiple answers) and short answer questions (numerical or text). 
The user interface of the program is text-based. In short, students have to type in commands into the terminal instead of 'point and click'. 

The program expects the administrator to provide the details of the exam to the program, in the order of appearance, as command line arguments:

+ An absolute path to the directory containing two files - an exam contents and a student list file. The files in this directory must be correctly labeled. See below for File Formats.
+ A number indicating the duration of the exam in minutes (as an integer).
+ [optional] A flag -r to indicate that the answers are to be shuffled. If this is not provided, the answers are displayed as-is. 

The program support the entire examination process which covers these stages:
1) Set up the exam.
2) Assign the exam to candidates.
3) Administer the exam and auto-marking.
