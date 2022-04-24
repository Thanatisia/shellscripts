"""
Generic System/Server Monitoring Control Utility
"""

# Import Internal Libraries
import os
import sys
import json

# Import Dependencies
import setup
import lib.gui.gui_interface as gui_interface

### Get Command Line Arguments ###
argv = sys.argv
script_name = argv[0]
argv = argv[1:] # Take all arguments past the 1st (Script)
argc = len(argv)

# Variables #
options = {
    "Clean" : {
        "description" : "Format Standard Output for Terminal/CLI scripting use",
        "arguments" : ["-c", "--clean"],
    },
    "CLI-Mode" : {
        "description" : "Start in Terminal Mode",
        "arguments" : ["--cli"],
    },
    "GUI-Mode" : {
        "description" : "Start in GUI Mode",
        "arguments" : ["--gui"],
    },
    "Help" : {
        "description" : "Displays this Help menu",
        "arguments" : ["-h", "--help"],
    },
    "Version" : {
        "description" : "Prints the version and author",
        "arguments" : ["-v", "--version"]
    }
}

to_run = {} # List of things to run
variables = {} # Variables for use

# Functions #

def run_cli():
    """
    Start in CLI Mode
    """
    if not ("Clean" in variables):
        print("Starting in CLI...")
    print("Hello World") # Print test here to simulate standard output manipulation for CLI/Terminal Scripting uses

def run_gui():
    """
    Start in GUI Mode
    """
    if not ("Clean" in variables):
        print("Starting in GUI...")
    App = gui_interface.App() 
    root = App.app
    print("Hello World") # Print test here to simulate standard output manipulation for CLI/Terminal Scripting uses
    App.start_app(root)

def help_menu():
    """
    Help Menu
    """
    for k,v in options.items():
        curr_opt_fullname = k
        curr_opt_description = v["description"]
        curr_opts = v["arguments"]

        print("{} : {}".format(curr_opt_fullname, curr_opt_description))
        print("\tOptions:")
        for i in range(len(curr_opts)):
            curr_opt = curr_opts[i]
            print("\t\t{}".format(curr_opt))

def version():
    """
    Display Version
    """
    print("Version : {}".format(PROG_SETUP.get_prog_vers()))
    print("Made by : {}".format(PROG_SETUP.get_prog_author()))

def init():
    """
    PROG_NAME = "Server Controller Utility"
    PROG_VERS = "v0.1.0" # major.minor.patch-state
    PROG_CONFIG_PATH = "~/.config/serverctrl/config.json"
    """
    global PROG_SETUP
    PROG_SETUP = setup.Settings("Server Controller Utility", "v0.1.0", "~/.config/serverctrl/config.json", "Asura (https://github.com/Thanatisia]")

def main():
    # to_run = [] # List of things to run

    # Get Functions & Variables
    if argc > 0:
        # Arguments Provided
        for i in range(argc):
            # print("{} : {}".format(i, argv[i]))
            curr_arg = argv[i]
            if curr_arg == "--help" or curr_arg == "-h":
                if not ("Help" in to_run):
                    to_run["Help"] = help_menu
            elif curr_arg == "--version" or curr_arg == "-v":
                if not ("Version" in to_run):
                    to_run["Version"] = version
            elif curr_arg == "--clean" or curr_arg == "-c":
                if not ("Clean"  in to_run):
                    variables["Clean"] = True
            elif curr_arg == "--cli":
                if not ("CLI-Mode" in to_run):
                    to_run["CLI-Mode"] = run_cli
            elif curr_arg == "--gui":
                if not ("GUI-Mode" in to_run):
                    to_run["GUI-Mode"] = run_gui
            else:
                print("Invalid Argument [{}]" .format(curr_arg))
                to_run["Invalid"] = help_menu
                break

    else:
        # No Arguments Provided
        # Display Help Menu
        help_menu()

    # Validation Check - Only run if valid
    if not ("Invalid" in to_run):
        # print("To Run : ")
        for label, val in to_run.items():
            # print("\t{} : {}".format(k, v))
            if not ("Clean" in variables.keys()):
                print("====")
                print("{}".format(label))
                print("====")
            val()
            
            if len(to_run) > 1:
                print("")

if __name__ == "__main__":
    init()
    main()

