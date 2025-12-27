#pragma once
 namespace ai {
class ScriptedTask;
}
using namespace ai ;
class IScriptExecutor {
public:
    virtual ~IScriptExecutor() = default;
    virtual int CallScript(const char *commandtext, const char *errortext) = 0;
    virtual bool CallTaskScript(ScriptedTask* task, const char* azCommand) = 0;
};
