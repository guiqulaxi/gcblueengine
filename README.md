## 依赖
libgeotiff libtif libproj libsqlite3 libcurl python pybind11
## 高程数据
可以从 https://www.ncei.noaa.gov/products/etopo-global-relief-model下载需要的高程tif
## 战役级的作战仿真引擎  
从[gcblue
](https://github.com/WarfareCode/gcblue)剥离  
1. 去除前端的依赖,纯C/C++,如WxWidget,boost,TVM；  
2. 用pybind11封装接口取代boost；  
3. 用Eigen替换TVM游戏引擎的碰撞检测；  
4. 用http,json对外开放接口（去除会加速很多）;  
5. 修改了一些bug。  
## 运行
app.exe --scenario scenarios/Tutorial/SateliteOperations.py --times 100 --runmode normal --ip  0.0.0.0 --port 8081
