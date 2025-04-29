
## 战役级的作战仿真引擎  
从[gcblue
](https://github.com/WarfareCode/gcblue)剥离  
1. 去除前端的依赖,纯C/C++,如WxWidget,boost,TVM；  
2. 用pybind11封装接口取代boost；  
3. 用Eigen替换TVM游戏引擎的碰撞检测；  
4. 用http,json对外开放接口（去除会加速很多）;  
5. 修改了一些bug；
6. 去除从sqlite中读取模型参数，改用从python文件中读取（好像更慢了）。  
## 模型
 模型类型包括："stores","ballistic", "ballistic_missile","cm", "air","ecm","esm","flightport","fueltank","ground","item","missile","optical","radar","ship","simpleair", "sonar","sonobuoy","space","sub","torpedo","launcher"，总共大约5900个
## 依赖
libgeotiff libtif libproj libsqlite3 libcurl python pybind11
## 高程数据
可以从 https://www.ncei.noaa.gov/products/etopo-global-relief-model下载需要的高程tif
## 运行
app.exe --scenario scenarios/Tutorial/SateliteOperations.py --times 100 --runmode normal --ip  0.0.0.0 --port 8081
