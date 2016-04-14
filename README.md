# 3DModeViewer

基于Three.JS (WebGL)实现3d模型展示

## 使用

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

## 效果
![image](https://github.com/kuangch/3DModelView/blob/master/assets/facemodel.gif)
