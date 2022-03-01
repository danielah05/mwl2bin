<p align="center"><img src="mwl2bin-logo.png" alt="mwl2bin" width="500"/></p>
<h2 align="center">a converter for turning lunar magic mwl files into bin files</h2>

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
3. various level modes
4. possibly other stuff i do not know about

everything else like swapping gfx, music, palettes etc is supported.
### what game versions are supported?
1. Japanese
2. North American
3. Super System
4. PAL 1.0
5. PAL 1.1

note for super system, pal 1.0/1.1:  
lunar magic is unable to open the roms for any of these version, you will have to make the levels either inside the north american version or the japanese version and then import them into the game instead.
### my game is crashing after importing the level, what does that mean?
here are a few things to check for:  
1. make sure the level is not using any "direct access map16" tiles.
2. make sure the level is not using any sprites that are not using the right GFX files.

none of the things listed above actually work in smw and get automatically patched into the game by lunar magic.  
because of that, the game will either crash or not compile at all, please fix those problems and try again!
### example footages of the python script in action
https://www.youtube.com/watch?v=qbKnbBTWI5U - converting lunar magic mwl to smw level bin example (feb 21, 2022)  
https://www.youtube.com/watch?v=M_rCSGLC-m4 - mwl2bin successfully importing custom level into smw pal 1.1 rom (feb 28, 2022)
