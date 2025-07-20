#ifndef TCCOMMPLATFORM_H
#define TCCOMMPLATFORM_H
#include "tcComponent.h"
#include "tcCommDevice.h"
#include "tcFile.h"
#include "tcScenarioLogger.h"
#include "tcObjStream.h"
#include <vector>
class tcStream;
class tcCommandStream;
class tcCreateStream;
class tcUpdateStream;
class tcGameStream;
class tcGameObject;
struct Damage;
namespace database
{
class tcCommPlatformDBObject;
}
namespace scriptinterface
{
class tcScenarioLogger;
}
class tcGameObject;
using database::tcCommPlatformDBObject;

class tcCommPlatform:public tcComponent
{
public:
    enum
    {
        MAXCOMMS = 16   ///< number of comm device entries supported in database
    };

    std::vector<std::string> commClass;
    std::vector<std::shared_ptr<tcCommDevice>> commDevice;



    unsigned int GetCommCount() const;
    bool HasActivatedComm();
    std::shared_ptr<const tcCommDevice> GetComm(unsigned idx) const;
    std::string GetCommDescription();
    std::shared_ptr<tcCommDevice> GetCommMutable(unsigned idx) const;
    std::shared_ptr<tcCommDevice> GetCommMutable(const std::string& commClass) const;
    std::shared_ptr<tcCommDevice> GetCommMutable(const std::string& commClass, unsigned int& idx) const;
    std::shared_ptr<const tcCommDevice> GetCommByDatabaseID(long id) const;
    void Init(std::shared_ptr<tcCommPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent);
    void Init(const char* databaseClass, std::shared_ptr<tcGameObject> parent);
    void SetActivityFlag(unsigned int flag);
    void SetCommState(unsigned idx, bool state);

    void Update(double t);

    void PrintToFile(tcFile&) ;
    void SaveToFile(tcFile& file) ;
    void LoadFromFile(tcFile& file);
    void Serialize(tcFile& file, bool mbLoad);
    void SaveToPython(scriptinterface::tcScenarioLogger& logger);

    bool ApplyAdvancedDamage(const Damage& damage, std::shared_ptr<tcGameObject> damager, float damageLevel);

    tcCommandStream& operator<<(tcCommandStream& stream);
    tcCreateStream& operator<<(tcCreateStream& stream);
    tcUpdateStream& operator<<(tcUpdateStream& stream);
    tcGameStream& operator<<(tcGameStream& stream);

    tcCommandStream& operator>>(tcCommandStream& stream);
    tcCreateStream& operator>>(tcCreateStream& stream);
    tcUpdateStream& operator>>(tcUpdateStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);

    void ClearNewCommand();
    bool HasNewCommand() const;

    tcCommPlatform();
    tcCommPlatform(const tcCommPlatform&);
    tcCommPlatform(std::shared_ptr<tcCommPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent);
    tcCommPlatform(const char* databaseClass, std::shared_ptr<tcGameObject> parent);


    virtual ~tcCommPlatform();

protected:
    unsigned int commActivityFlags; ///< flags for faster check of activity state of diff sensor types

    void ClearActivityFlags();

};

#endif // TCCOMMPLATFORM_H
