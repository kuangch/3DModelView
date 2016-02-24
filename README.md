# MeshViewer

Simple 3D objects file viewer in Three.JS (WebGL)

## Target

The objective is to create a simple object viewer that can well handle low-rez 3d meshes & textures for CollectiveAccess.

![Screen capture](https://raw.githubusercontent.com/ideesculture/meshviewer/master/capture1.png "Screen capture")


## Demo
[Click here](http://3d.idcultu.re/index.html) to see a live demo of the 3D mesh viewer with some OBJ examples.

Just select the example you want to show in the examples menu (on top left)

## Howto 

This viewer is easy to handle, give the path to the obj & mtl files, the ID where you want the viewer to be in, eventually a format if it can't be guessed

``` html 
<script type="text/javascript">
meshviewer({
  'objFile' : 'examples/cow/mesh.obj',
  'mtlFile' : 'examples/cow/mesh.mtl', 
  'container':'#viewer', 
  'format':'obj'});
</script>
<div id="viewer">
</div>
```

See index.html for more informations.

## Credits
Icons : [Gentleface](http://www.gentleface.com/free_icon_set.html) licence Creative Commons Attribution-NonCommercial
