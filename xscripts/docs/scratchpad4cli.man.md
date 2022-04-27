# GenScratch

A generic non-graphical environment reliant universal Scratchpad powered by xdotools

## Table of Contents
- [Information](#information)
- [Setup](#setup)
- [Documentation](#documentation)
- [Resources](#resources)
- [References](#references)
- [Remarks](#remarks)

# Information

genscratch is a Generic, Non-Graphical Environment reliant, Universal Scratchpad thats using xdotools' "window-in", "window-out" functionality layered on top of UI to create a modifiable, portable scratchpad.

genscratch utilises the Environment Variables, thus this will make the program scriptable as well alongside launcher like dmenu or rofi (Optional).

The only dependency that you need is the scratchpad and any other programs you wish to script this with.

------------------

This is the CLI Scratchpad variant, use this to launch terminal/cli-based applications such as vim, rangerFM or the shell itself

## Setup

### Pre-Requisites

- Ensure that you have the following 
    + git

### Dependencies

+ xdotools

### Obtaining

- clone whole repository
    ```console
    git clone https://github.com/Thanatisia/shellscripts
    ```
- curl the script 
    ```console
    curl -L-O https://raw.githubusercontent.com/Thanatisia/shellscripts/main/xscripts/scratchpads
    ```

### Installing/Compiling/Building

- Map the script and the commands to your Keybind script (e.g. sxhkdrc)
    ```console
    # Assuming is sxhkd
    super + F12
        scratchpads alacritty YOUR_TITLE -e [command]
    ```

## Documentation

### Synopsis/Syntax

scratchpad4cli {options} [terminal-to-use (Default: $TERM)] [window_name] [command-arguments...]

### Parameters

+ No Options as of now

### Usage

+ Opening vim using alacritty
   ```console
   scratchpad4cli alacritty EDITOR -e vim
   ```
   
+ Opening your terminal emulator
    ```console
    scratchpad4cli alacritty 
    ```
    
### Customization/Configuration

## References

## Remarks

## Resources
