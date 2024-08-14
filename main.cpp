//#include <QCoreApplication>

#include "Game.h"
#include <thread>
#include <chrono>
// #include "tinyxml2.h"
#include <windows.h>
#include "httplib.h"
void serverFunc( const std::string &ip, int port ,tcGame  *game) {
    httplib::Server svr;
    svr.Get("/simdata", [=](const httplib::Request &, httplib::Response &res) {
        res.set_content(game->GetOutSimData(), "application/json");
    });
    svr.Post("/cmd", [=](const httplib::Request &req, httplib::Response &res) {
        game->AddCommand(req.body);
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

    tcGame  *game = new tcGame();
    game->Init();
    game->InitSim();
    game->LoadScenario(argv[1],"",false);
    game->SetTimeAccel(std::stol(argv[2]));
    std::string ip=std::string(argv[3]);
    int port=std::stoi(argv[4]);
    std::thread serverThread(serverFunc,ip,port,game);
    while (!game->UpdateFrame()) {
    }
    serverThread.join();
    return  0;

}

