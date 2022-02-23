# SCREEN EXITS:
# 07 00 00 CB
# 07 = screen number
# 00 = would be set to 02 when its an secondary exit (?)
# 00 = empty (?)
# CB = level destination

import os, sys

# create directories and stuff
if not os.path.isdir("lvl"):
    os.mkdir("lvl")

if not os.path.isdir("lvl/obj"):
    os.mkdir("lvl/obj")

if not os.path.isdir("lvl/spr"):
    os.mkdir("lvl/spr")

# read mwl data
with open(sys.argv[1], "rb") as mwl:
    data = mwl.read()

removepath = os.path.basename(sys.argv[1])
filename = os.path.splitext(removepath)[0]

# ----------------
# level data - obj
# ----------------

data_headerless = data[200:]
obj_datasplit = data_headerless.split(b"\xff\x04", 1)
obj_data = obj_datasplit[0]

print("converted obj: "+filename)

print("doing experimental stuff now... things might go wrong!")

warpamount = input("enter the amount of warps in the level: ")

print("fixing "+warpamount+" warp(s)...")

warpdata = obj_data[-4*int(warpamount):]
nowarpdata = obj_data[:-4*int(warpamount)]

warpdatapossiblefix = warpdata.replace(b"\x05\x00", b"\x00\x00") # replace 05 00 -> 00 00 to fix warp???

reconstructedwarps = nowarpdata+warpdatapossiblefix

print(str(warpdata)+" -> "+str(warpdatapossiblefix))

print("(hopefully) fixed screen exits: "+filename)

# export finished bin
with open("lvl/obj/"+filename+".bin", "wb") as binobj:
    binobj.write(reconstructedwarps)
    binobj.write(b"\xff")

# ----------------
# level data - spr
# ----------------

data_objremove = data.split(b"\xff\x04", 1)
data_objless = data_objremove[1]

data_sprstart = data_objless[2063:]

spr_datasplit = data_sprstart.split(b"\xff", 1)
spr_data = spr_datasplit[0]

print("converted spr: "+filename)

# export finished bin
with open("lvl/spr/"+filename+".bin", "wb") as binspr:
    binspr.write(spr_data)
    binspr.write(b"\xff")

input("press enter to exit!")