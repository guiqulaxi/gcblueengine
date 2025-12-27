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
std::shared_ptr<IScriptExecutor> tcPythonExecutorAdapter::Get()
{
    static auto adapter = std::make_shared<tcPythonExecutorAdapter>();
    return adapter;
}
