# 3DModeViewer

基于Three.JS (WebGL)实现3d模型展示

## Howto 

This viewer is easy to handle, give the path to the obj & mtl files, the ID where you want the viewer to be in, eventually a format if it can't be guessed

``` html 
<script type="text/javascript">
meshviewer({
  'objFile' : 'examples/cow/mesh.obj',
  'mtlFile' : 'examples/cow/mesh.mtl', 
  'showWireFrame': true,
  'container':'#viewer', 
  'format':'obj'});
</script>
<div id="viewer">
</div>
```
