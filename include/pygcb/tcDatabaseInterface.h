#ifndef TCDATABASEINTERFACE_H
#define TCDATABASEINTERFACE_H
#include <pybind11-global/pybind11/pybind11.h>
#include <pybind11-global/pybind11/eval.h>
#include <pybind11-global/pybind11/embed.h>

#include <tcAcousticModel.h>
#include <tcDamageEffect.h>
#include <tcDatabaseObject.h>
#include <tcSignatureModel.h>
#include <tcWeaponDamage.h>
namespace py = pybind11;
using namespace py;
using namespace database ;
namespace scriptinterface
{

class tcDatabaseInterface
{
public:
    tcDatabaseInterface();
    ~tcDatabaseInterface();
    static object GetInterface();
    void Clear();
    void ClearForNewScenario();
    int CreateObjectCopy(int anKey);
    int DeleteObject(int anKey);
    int GetRandomKey();
    std::shared_ptr<tcDatabaseObject> GetRandomOfType(UINT model_type);
    std::vector<std::string> GetPlatformNames(const std::string& className);
    std::vector<std::string> GetPlatformNamesByDate(const std::string& className, float dateYear);
    std::vector<std::string> GetPlatformHulls(const std::string& className);
    const std::string& GetDisplayName(const std::string& className) const;

    bool CheckForErrors(const std::string& logFile);
    bool CheckTableReferences(const char* table, const char* field, const std::vector<std::string>& refTables, const char* refField,
                              std::ofstream &log, unsigned int& errorCount);
    int GetSize();
    int AddOrUpdateObject( std::shared_ptr<tcDatabaseObject> rpobj);
    void AddOrUpdateSignatureModelData(const tcSignatureModel&data);
    void AddOrUpdateAcousticModelData(const tcAcousticModel& data);
    void AddOrUpdateWeaponDamageData(const tcWeaponDamage& data);
    void AddOrUpdateDamageEffectData(const tcDamageEffect& data);

    std::shared_ptr<tcDatabaseObject> GetObjectByKey(int anKey);
    std::shared_ptr<tcDatabaseObject> GetObjectByClassName(const std::string& className); ///< gets object by class name
    const std::string& GetObjectClassName(int key);
    std::vector<std::string> WildcardSearch(const std::string& expression, const std::string& filter);
    std::vector<std::string> WildcardSearchLoaded(const std::string& expression, const std::string& filter);
    int GetObjectClass(int anKey, std::string& rzClass);
    int GetNextObjectOfSameClass(int anKey);
    int GetPrevObjectOfSameClass(int anKey);
    int GetKey(const char* s);
    void GetVersion(int& v1, int& v2, int& v3);


    void GetCountryList(std::vector<std::string>& countryList) const;
    const tcSignatureModel* GetSignatureModel(const std::string& modelName) const;
    const tcAcousticModel * GetAcousticModel(const std::string& modelName) const;
    const tcWeaponDamage * GetWeaponDamageData(const std::string& s) const;
    const tcDamageEffect* GetDamageEffectData(const std::string& s) const;
    bool ObjectExists(const std::string& className) const; ///< check if obj matching className already in db
    bool FindPlatformSetups(const std::string& databaseClass, float searchYear, std::vector<std::string>& setupNames);


};
}
#endif // TCDATABASEINTERFACE_H
