# Execution :
# $ /Applications/blender/blender.app/Contents/MacOS/blender -b -P ~/test_blender.py -- Scene_2012_01_11_15_10_03
# avec : Scene_2012_01_11_15_10_03 : le nom du fichier obj
#
# Réalise :

import bpy 
import math
import mathutils
import sys
import os 

class locationxyz(list):
    pass

# main variables
rayon = 80


#meshname = "Scene_2012_01_11_15_10_03"
meshname = str(sys.argv[5])   

dir = "render"


angle = math.radians(5)
etapes = int(math.radians(360) / angle)

# camera position variables
x = 0
y = 0
z = -100
targetLoc = locationxyz()
targetLoc.x = 0
targetLoc.y = 0
targetLoc.z = 10

# rendered image resolution
rnd = bpy.data.scenes[0].render  
rnd.resolution_x = 1280
rnd.resolution_y = 756
rnd.resolution_percentage = 50

def pointCameraToTarget(cam, targetLoc):
    # targetLoc is (x, y, z) of what we want to point at
    # camera angles appear to be set up so that
    #  cam.rotation_euler = Euler((0,0,0), 'XYZ') points downward,
    #  i.e., along the -z axis direction.
    # In the xy plane (i.e., rotate around z-axis):
    dx = targetLoc.x - cam.location.x
    dy = targetLoc.y - cam.location.y
    dz = targetLoc.z - cam.location.z
    print("dx, dy, dz:", dx, dy, dz)
    # Signs are chosen carefully due to geometry.  If we rotate
    #  by this much from the -z orientation around the x-axis, we
    #  will be pointing along the y-axis (for angle < pi rad)
    xRad = (3.14159/2.) + math.atan2(dz, math.sqrt(dy**2 + dx**2))
    print("xRad: %f, %f deg" % (xRad, xRad*180./math.pi))
    
    zRad = math.atan2(dy, dx) - (3.14159256 / 2.)
    print("zRad: %f, %f deg" % (zRad, zRad*180./math.pi))
    cam.rotation_euler = mathutils.Euler((xRad, 0, zRad), 'XYZ')
    
# Suppression du cube présent par défaut
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

currentdir = os.getcwd()

# Chargement d'un fichier OBJ
bpy.ops.import_scene.obj(filepath= meshname + '.obj',axis_forward='X', axis_up='Z')

if not os.path.exists(currentdir + "/" + dir):
    os.makedirs(currentdir + "/" + dir)
#os.chdir(dir)
#print(currentdir)
#sys.exit()

lamp = bpy.data.objects['Lamp'] # bpy.types.Camera
lamp.location = (0, -20, 10)
lamp.scale = (1, 1, 1)
bpy.data.lamps[0].energy = 100

# Cam rotation part
cam = bpy.data.objects['Camera'] # bpy.types.Camera

i = 1
cam.location = (x, y, z)
pointCameraToTarget(cam, targetLoc)
lamp.location = (x, y, z)	

print("Rendering image " + str(i + 1) + "...")
bpy.ops.render.render()

if i < 9 :
    filename = dir + "/image-0" + str(i + 1) + ".jpg"
else :
    filename = dir + "/image-" + str(i + 1) + ".jpg"

bpy.data.images[0].save_render(filename)
if i == 0 :
	bpy.data.images[0].save_render(dir + "/image-72.jpg")
x2 = x * math.cos(angle) + y * math.sin(angle)
y2 = y * math.cos(angle) - x * math.sin(angle)
x = x2
y = y2
	
#bpy.ops.wm.collada_export(filepath = meshname + '.dae')
