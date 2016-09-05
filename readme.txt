具体使用步骤：
1.打开项目/example/test/文件夹注意里面三个文件的名称和后缀名
2.把你要演示的模型文件（mtl，obj，jpg）复制到/example/test/目录下
3.用文本编辑器打开index.html找到第123行 找到以下两行：
'meshFile': 'examples/test/neutral.obj'
'mtlFile': 'examples/test/neutral.mtl',
把“neutral.obj”和“neutral.mtl”替换为你copy到/example/test/目录下的对应文件的文件名
4.找到谷歌浏览器图标，右键图标-》属性》快捷方式-》目标-》在目标后面的文本编辑框中的原有内容后面加上“ --allow-file-access-from-files”
5.注意--allow前面有个空格
6.重启浏览器
7.点击项目根目录下的index.html
