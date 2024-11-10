#ifndef TCGAMEINTERFACE_H
#define TCGAMEINTERFACE_H
#include <pybind11-global/pybind11/pybind11.h>
#include <pybind11-global/pybind11/eval.h>
#include <pybind11-global/pybind11/embed.h>
#include<string>
using namespace std ;
#include "tcSimState.h"
namespace py = pybind11;
using namespace py;
namespace scriptinterface
{
    class tcGameInterface
    {
    public:
        tcGameInterface();
        void SetEditMode(bool state);
        void SetTimeAccel(long accel);
        void ClearScenario();
        void LoadScenario(const std::string &filePath);

        static object GetInterface();
        static void AttachSimState(tcSimState *apSS) {mpSimState = apSS;}

    private:
        static tcSimState *mpSimState;
    };
};

#endif // TCGAMEINTERFACE_H
