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
    a.add<std::string>("ip", 'h', "http ip", false, "127.0.0.1");
    a.add<int>("port", 'p', "http port", false, 80, cmdline::range(1, 65535));
    a.parse_check(argc, argv);


    tcGame  *game = new tcGame();
    game->Init();
    //game->LoadDatabase("database/py/sub/Gotland.py");
    std::string runmode=a.get<std::string>("runmode");
    if(runmode=="normal")
    {
        game->LoadScenario( a.get<std::string>("scenario"),"",false);
        game->SetTimeAccel(a.get<int>("times"));
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

