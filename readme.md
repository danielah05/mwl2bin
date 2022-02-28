<img src="mwl2bin-logo.png" alt="mwl2bin" width="500"/>

## a converter for turning lunar magic mwl files into bin files
### what is the point of this?
while lunar magic is good for level editing, the tool comes with some flaws.  
lunar magic cannot edit every level in the game (examples: all of the sub sections in chocolate island 2).  
the tool also auto patches your rom with custom assembly code, making technically every rom hack made with the level editor not vanilla.  
with this, you can make any level you want and convert it to be used with SMWDisX: https://github.com/IsoFrieze/SMWDisX
### how to use
1. save your level inside lunar magic as a file by going to "file -> save level to file"
2. make sure to name the file the same as the bin file you are going to replace in the disassembly. (for example: 105 would be "105_YI1main.mwl")
3. after that, just drag the mwl file onto the python script and a new folder should appear called "lvl", this folder should have the two bin files.
4. just copy the "lvl" folder into the main directoy of the dissasembly and compile the rom.
### what is currently not supported?
1. changing the background tiles
2. main/midway/secondary entrances
3. possibly other stuff i do not know about

everything else like swapping gfx, music, palettes etc is supported.
### my game is crashing after importing the level, what does that mean?
here are a few things to check for:  
1. make sure the level is not using any "direct access map16" tiles.
2. make sure the level is not using any sprites that are not using the right GFX files.

none of the things listed above actually work in smw and get automatically patched into the game by lunar magic.  
because of that, the game will either crash or not compile at all, please fix those problems and try again!