# mwl2bin
## a converter for turning lunar magic mwl files into bin files
**warning: this may or may not work on linux, i have not tried yet.**
### what is the point of this?
while lunar magic is good for level editing, the tool comes with some flaws.

lunar magic cannot edit every level in the game (examples: all of the sub sections in chocolate island 2).

the tool also auto patches your rom with custom assembly code, making technically every rom hack made with the level editor not vanilla.

with this, you can make any level you want and convert it to be used with SMWDisX: https://github.com/IsoFrieze/SMWDisX
### how to use
save your level inside lunar magic as a file by going to "file -> save level to file"

make sure to name the file the same as the bin file you are going to replace in the disassembly. (for example: 105 would be "105_YI1main.mwl")

after that, just drag the mwl file onto the python script and a new folder should appear called "lvl", this folder should have the two bin files.

just copy the "lvl" folder into the main directoy of the dissasembly and compile the rom.
### my game is crashing after importing the level, what does that mean?
this most likely means you have placed down a "direct map16 access" tile, make sure to get rid of that.

these tiles are not in the vanilla game, lunar magic automatically patches your rom with special code when saving for the first time to make those tiles work and because of that, they will not work inside the disassembly.