## 战役级的作战仿真引擎  
从[gcblue
](https://github.com/WarfareCode/gcblue)剥离  
1. 去除前端的依赖,纯C/C++,如WxWidget,boost,TVM；  
2. 用pybind11封装接口取代boost；  
3. 用Eigen替换TVM游戏引擎的碰撞检测；  
4. 用http,json对外开放接口（去除会加速很多）;  
5. 修改了一些bug。  
## 运行
gcblue --scenario scenarios/SinglePlayer/Modern/Odyssey_Dawn.py --times 100 --runmode debug --ip  0.0.0.0 --port 8080
