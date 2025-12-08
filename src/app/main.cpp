//#include <QCoreApplication>

#include "Game.h"
#include <thread>
#include <string>

// #include <chrono>
// #include "tinyxml2.h"
// #include <windows.h>

#include "cmdline.h"
#include "httplib.h"
void serverFunc( const std::string &ip, int port ,tcGame  *game) {
    httplib::Server svr;
    svr.Get("/simdata", [=](const httplib::Request & req, httplib::Response &res) {
        res.set_header("Access-Control-Allow-Origin", "*");  // 若有端口需写全（协议+域名+端口）
        res.set_header("Access-Control-Allow-Credentials", "true");
        res.set_header("Access-Control-Expose-Headers", "content-type");
        res.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
        res.set_header("Access-Control-Allow-Headers", "Content-Type,Access-Control-Allow-Headers,Authorization,X-Requested-With");
        if(! req.method.compare("OPTIONS"))
        {
            return;
        }
        res.set_content(game->GetOutSimData(), "application/json");
    });
    svr.Get("/dbdata", [=](const httplib::Request & req, httplib::Response &res) {
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Access-Control-Allow-Credentials", "true");
        res.set_header("Access-Control-Expose-Headers", "content-type");
        res.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
        res.set_header("Access-Control-Allow-Headers", "Content-Type,Access-Control-Allow-Headers,Authorization,X-Requested-With");
        if(! req.method.compare("OPTIONS"))
        {
            return;
        }
        auto id_it = req.params.find("id");
        auto name_it = req.params.find("name");
        if (id_it != req.params.end()) {
            int id = std::stoi(id_it->second);
            std::string dbData = game->GetOutDBData(id);
            res.set_content(dbData, "application/json");
        } else if (name_it != req.params.end()) {
            std::string name = name_it->second;
            std::string dbData = game->GetOutDBData(name);
            res.set_content(dbData, "application/json");
        }
         else {
            res.status = 400;
            res.set_content("{\"error\": \"Missing id parameter\"}", "application/json");
        }
    });
    svr.Post("/cmd", [=](const httplib::Request &req, httplib::Response &res) {
        game->AddCommand(req.body);
        res.set_header("Access-Control-Allow-Origin", "*");  // 若有端口需写全（协议+域名+端口）
        res.set_header("Access-Control-Allow-Credentials", "true");
        res.set_header("Access-Control-Expose-Headers", "content-type");
        res.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
        res.set_header("Access-Control-Allow-Headers", "Content-Type,Access-Control-Allow-Headers,Authorization,X-Requested-With");
        if(! req.method.compare("OPTIONS"))
        {
            return;
        }
        res.set_content("ok", "text/plain");
    });

    if (svr.listen(ip, port)) {
        std::cout << "Server is running at http"<<ip <<":"<<port<< std::endl;
    } else {
        std::cerr << "Failed to start server." <<ip <<":"<<port<< std::endl;
    }
}



int main(int argc, char *argv[])
{

    // create a parser
    cmdline::parser a;
    a.add<std::string>("scenario", 's', "scenario path", true, "");
    a.add<int>("times", 't', "run times", false, 1, cmdline::range(1, 10000));
    a.add<std::string>("runmode", 'r', "runmode", false, "normal", cmdline::oneof<std::string>("edit", "normal","extreme"));
    a.add<std::string>("ip", 'l', "http ip", false, "127.0.0.1");
    a.add<int>("port", 'o', "http port", false, 80, cmdline::range(1, 65535));
    a.add<std::string>("networkmode", 'm', "networkmode", false, "single", cmdline::oneof<std::string>("single", "client","server"));
    a.add<std::string>("serverip",'i',"server ip", false, "127.0.0.1");
    a.add<std::string>("name",'a',"name", false, "client");
    a.add<std::string>("password",'p',"password", false, "client");

    a.parse_check(argc, argv);


    tcGame  *game = new tcGame();
    game->Init();
    //game->LoadDatabase("database/py/sub/Gotland.py");
    std::string runmode=a.get<std::string>("runmode");
    std::string networkmode=a.get<std::string>("networkmode");
    int times=a.get<int>("times");
    if(runmode=="normal")
    {
        game->SetNetworkMode(networkmode);
        //如果是client模式，连接服务器
        if(networkmode=="client")
        {
            game->ConnectToServer(a.get<std::string>("serverip"),a.get<std::string>("name"),a.get<std::string>("password"));
        }
        else if (networkmode=="server")
        {
            game->LoadScenario( a.get<std::string>("scenario"),"",false);
            //先暂停 等待客户端连接
            game->SetTimeAccel(0);
        }
        
        std::string ip=a.get<std::string>("ip");
        int port=a.get<int>("port");
        std::thread serverThread(serverFunc,ip,port,game);
        serverThread.detach();

    }else if(runmode=="edit")
    {
        //game->LoadScenario( a.get<std::string>("scenario"),"",false);
        game->SetScenarioEdit(true);
        std::string ip=a.get<std::string>("ip");
        int port=a.get<int>("port");
        std::thread serverThread(serverFunc,ip,port,game);
        serverThread.detach();
    }
    while (!game->UpdateFrame()) {
    }
    return  0;

}

