作战仿真游戏后台引擎
从[gcblue
](https://github.com/WarfareCode/gcblue)中剥离的后台  
1.去除依赖,如WxWidget,boost,TVM游戏引擎；  
2.用pybind11封装接口；  
3.用Eigen替换TVM游戏引擎的碰撞检测；  
4.用http对外开放接口（去除会加速很多）; 
5.修改了一些bug。  
运行
gcblue scenarios/SinglePlayer/Modern/Odyssey_Dawn.py 100 0.0.0.0 8081
