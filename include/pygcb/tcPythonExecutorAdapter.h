#include "tcSimPythonInterface.h"
#include "tcScriptExecutor.h"

// 适配器实现（在 pygcb 模块中）
class tcPythonExecutorAdapter : public IScriptExecutor {
public:
    virtual int CallScript(const char *commandtext, const char *errortext) override;
    virtual bool CallTaskScript(ScriptedTask* task, const char* azCommand) override;
// 全局可访问的工厂函数
   static std::shared_ptr<IScriptExecutor> Get() ;
};
