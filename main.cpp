//#include <QCoreApplication>

#include "Game.h"
#include <thread>
#include <chrono>
int main(int argc, char *argv[])
{
    tcGame  *game = new tcGame();
    game->Init();
    game->InitSim();
    game->LoadScenario(argv[1],"",false);
    game->SetTimeAccel(std::stol(argv[2]));
    while (!game->UpdateFrame()) {
    }
    return  0;

}

