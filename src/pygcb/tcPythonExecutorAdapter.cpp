#include "tcPythonExecutorAdapter.h"
#include "tcSimPythonInterface.h"
using namespace scriptinterface;
bool tcPythonExecutorAdapter::CallTaskScript(ScriptedTask *task, const char *command)
{
    return tcSimPythonInterface::Get()->CallTaskScript(task, command);
}

int tcPythonExecutorAdapter::CallScript(const char *commandtext, const char *errortext)
{
    return tcSimPythonInterface::Get()->CallPython(commandtext, errortext);
}
IScriptExecutor* tcPythonExecutorAdapter::Get()
{
    static tcPythonExecutorAdapter instance;
    return &instance;
}
