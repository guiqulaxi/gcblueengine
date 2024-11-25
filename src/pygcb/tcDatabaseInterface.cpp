#include "tcDatabaseInterface.h"
#include "tcDatabase.h"
using namespace scriptinterface ;
tcDatabaseInterface::tcDatabaseInterface() {}

tcDatabaseInterface::~tcDatabaseInterface()
{

}

object tcDatabaseInterface::GetInterface()
{
    py::module pybind11_module = py::module::import("pygcb");
    // 获取Python类的引用
    py::object  interfaceType = pybind11_module.attr("tcDatabaseInterface");
    return interfaceType;
}

void tcDatabaseInterface::Clear()
{
    tcDatabase::Get()->Clear();
}


/**
* When using useDynamicLoad, this clears platform data before loading new scenario
*/
void tcDatabaseInterface::ClearForNewScenario()
{
    tcDatabase::Get()->ClearForNewScenario();
}



int tcDatabaseInterface::DeleteObject(long anKey)
{
    return tcDatabase::Get()->DeleteObject(anKey);
}


/**
* sets the three integer version fields using mnVersion
* (works with old database binary file system)
*/
void tcDatabaseInterface::GetVersion(int& v1, int& v2, int& v3) {
    return tcDatabase::Get()->GetVersion(v1,v2,v3);
}
const tcWeaponDamage* tcDatabaseInterface::GetWeaponDamageData(const std::string& s) const
{
    return tcDatabase::Get()->GetWeaponDamageData(s);
}

const tcAcousticModel* tcDatabaseInterface::GetAcousticModel(const std::string& modelName) const
{
    return tcDatabase::Get()->GetAcousticModel(modelName);
}


void tcDatabaseInterface::GetCountryList(std::vector<std::string>& countryList) const
{
          tcDatabase::Get()->GetCountryList(countryList);
}


const tcDamageEffect* tcDatabaseInterface::GetDamageEffectData(const std::string& s) const
{
return tcDatabase::Get()->GetDamageEffectData(s);
}

/**
* @return the display name for this platform based on useNatoASCC option
*/
const std::string& tcDatabaseInterface::GetDisplayName(const std::string& className) const
{
    return tcDatabase::Get()->GetDisplayName(className);
}

long tcDatabaseInterface::GetSize()
{
    return tcDatabase::Get()->GetSize();
}


tcDatabaseObject* tcDatabaseInterface::GetRandomOfType(UINT model_type)
{
         return tcDatabase::Get()->GetRandomOfType(model_type);
}

/**
* @return random tcPlatformDBObject, tcMissileDBObject,
* or tcJetDBObject key.
*/
long tcDatabaseInterface::GetRandomKey() {
      return tcDatabase::Get()->GetRandomKey();
}

const tcSignatureModel* tcDatabaseInterface::GetSignatureModel(const std::string& modelName) const
{
    return tcDatabase::Get()->GetSignatureModel(modelName);
}


long tcDatabaseInterface::AddOrUpdateObject(tcDatabaseObject *rpobj)
{
    return tcDatabase::Get()->AddOrUpdateObject(rpobj);
}

/**
* @return NULL if not found
*/
tcDatabaseObject* tcDatabaseInterface::GetObjectByKey(long anKey)
{
    return tcDatabase::Get()->GetObject(anKey);
}

/**
* Lookup and return object database class name by key
* @return empty string reference if not found
*/
const std::string& tcDatabaseInterface::GetObjectClassName(long key)
{
return tcDatabase::Get()->GetObjectClassName(key);
}

long tcDatabaseInterface::GetKey(const char* s)
{
return tcDatabase::Get()->GetKey(s);
}

/**
* Gets object by class name.
* @return NULL if not found
*/
tcDatabaseObject* tcDatabaseInterface::GetObjectByClassName(const std::string& className)
{

return tcDatabase::Get()->GetObject(className);

}
bool tcDatabaseInterface::ObjectExists(const std::string& className) const
{
return tcDatabase::Get()->ObjectExists(className);
}

/**
* find key of next object of same mnClassID as anKey
*/
long tcDatabaseInterface::GetNextObjectOfSameClass(long anKey)
{
    return tcDatabase::Get()->GetNextObjectOfSameClass(anKey);
}


std::vector<std::string> tcDatabaseInterface::GetPlatformNames(const std::string& className)
{
return tcDatabase::Get()->GetPlatformNames(className);
}



/**
* Find key of previous object of same mnClassID as anKey
*/
long tcDatabaseInterface::GetPrevObjectOfSameClass(long anKey)
{
   return tcDatabase::Get()->GetPrevObjectOfSameClass(anKey);
}


// lookup class string associated with key
int tcDatabaseInterface::GetObjectClass(long anKey, std::string& rzClass) {
return tcDatabase::Get()->GetObjectClass(anKey,rzClass);
}






/**
* @param filter leave empty to allow all database entries, "loadout" to return only weapons, CM, fuel tanks
* Future goal: Searches full database (not just what's dynamically loaded) and add time parameter
*/
std::vector<std::string> tcDatabaseInterface::WildcardSearch(const std::string& expression, const std::string& filter)
{
return tcDatabase::Get()->WildcardSearch(expression,filter);
}

/**
* @param filter leave empty to allow all database entries, "loadout" to return only weapons, CM, fuel tanks
* Searches only what is currently loaded in active database
*/
std::vector<std::string> tcDatabaseInterface::WildcardSearchLoaded(const std::string& expression, const std::string& filter)
{
    return tcDatabase::Get()->WildcardSearchLoaded(expression,filter);
}







