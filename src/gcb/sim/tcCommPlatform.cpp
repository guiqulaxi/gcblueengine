#include "tcCommPlatform.h"
#include "math_constants.h"
#include "strutil.h"

#include "tcCommDeviceDBObject.h"
#include "tcCommPlatformDBObject.h"
#include "tcDatabase.h"

#include <assert.h>
unsigned int tcCommPlatform::GetCommCount() const
{
    return (unsigned)commDevice.size();

}

bool tcCommPlatform::HasActivatedComm()
{
    int nComms = (int)commDevice.size();
    for (int k=0;k<nComms;k++)
    {
        std::shared_ptr<tcCommDevice>pComm = commDevice[k];
        if (pComm->IsActive()) {return true;}
    }
    return false;
}

std::shared_ptr<const tcCommDevice> tcCommPlatform::GetComm(unsigned int idx) const
{
    if (idx >= commDevice.size()) return 0;
    else return commDevice[idx];
}

std::string tcCommPlatform::GetCommDescription()
{
    static std::string errorString = "Error";
    std::string description;

    unsigned nComms = GetCommCount();
    for (unsigned n=0; n < nComms; n++)
    {

        std::shared_ptr<const tcCommDevice> comm = GetComm(n);

        const char* text = (comm != 0) && (comm->mpDBObj != 0) ?
                               comm->mpDBObj->mzClass.c_str() : errorString.c_str();
        description += strutil::format("%s\n", text);
    }

    if (nComms == 0)
    {
        description = "No Comms\n";
    }

    return description;
}

std::shared_ptr<tcCommDevice> tcCommPlatform::GetCommMutable(unsigned int idx) const
{
    if (idx >= commDevice.size()) return 0;
    else return commDevice[idx];
}

std::shared_ptr<tcCommDevice> tcCommPlatform::GetCommMutable(const std::string &commClass) const
{
    for(size_t n=0; n<commDevice.size(); n++)
    {
        if (commClass == commDevice[n]->mpDBObj->mzClass.c_str())
        {
            return commDevice[n];
        }
    }

    return 0;
}

std::shared_ptr<tcCommDevice> tcCommPlatform::GetCommMutable(const std::string &commClass, unsigned int &idx) const
{
    for (size_t n=0; n<commDevice.size(); n++)
    {
        if (commClass == commDevice[n]->mpDBObj->mzClass.c_str())
        {
            idx = n;
            return commDevice[n];
        }
    }

    idx = 0;
    return 0;
}

std::shared_ptr<const tcCommDevice> tcCommPlatform::GetCommByDatabaseID(long id) const
{
    unsigned nComms = GetCommCount();
    for (unsigned n=0; n < nComms; n++)
    {
        std::shared_ptr<const tcCommDevice> comm = GetComm(n);
        if (comm->mnDBKey == id) return comm;
    }

    return 0;
}

void tcCommPlatform::Init(std::shared_ptr<tcCommPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent)
{
    using namespace database;

    // add comms
    if (obj->commClass.size() > tcCommPlatformDBObject::MAXCOMMS)
    {
        fprintf(stderr, "tcCommPlatform::Init - Warning - "
                        "DB comm count exceeded recommended limit (%s)\n", parent->mzClass.c_str());
    }
    commDevice.clear();

    tcDatabase* database = tcDatabase::Get();

    for(size_t i=0; i<obj->commClass.size(); i++)
    {
        std::shared_ptr<tcDatabaseObject>pDBObj = database->GetObject(obj->commClass[i]);

        if (std::shared_ptr<tcCommDeviceDBObject>pCommDBObj =  std::dynamic_pointer_cast<tcCommDeviceDBObject>(pDBObj))
        {
            std::shared_ptr<tcCommDevice> comm = pCommDBObj->CreateComm(parent); // factory method
            assert(comm);
            float lookAz_rad = C_PIOVER180 * obj->commAz[i];
            comm->SetMountAz(lookAz_rad);
            commDevice.push_back(comm);
        }
        else
        {
            std::string msg=strutil::format("Error - tcCommPlatform::Init - Comm (%s) not found when initializing platform (%s)\n", obj->commClass[i].c_str(), parent->mzClass.c_str());
            //            msg.Printf("Error - tcCommPlatform::Init - Comm (%s) not found when initializing platform (%s)\n", obj->commClass[i].c_str(), parent->mzClass.c_str());
            //wxMessageBox(msg);
            fprintf(stderr, msg.c_str());
        }

    }
}

void tcCommPlatform::Init(const char *databaseClass, std::shared_ptr<tcGameObject> parent)
{
    if (strlen(databaseClass) == 0)
    {
        return; // platform has no comm
    }

    std::shared_ptr<tcCommDeviceDBObject> commData =  std::dynamic_pointer_cast<tcCommDeviceDBObject>(
        tcDatabase::Get()->GetObject(databaseClass));

    if (commData == 0)
    {
        fprintf(stderr, "Error - tcCommPlatform(const char* databaseClass, std::shared_ptr<tcGameObject> parent)"
                        " - Comm not found in database (%s)\n", databaseClass);
        assert(false);
        return;
    }

    std::shared_ptr<tcCommDevice> comm = commData->CreateComm(parent); // factory method
    assert(comm);

    comm->mfCommHeight_m = 0.8f * parent->GetZmax(); //< guess comm height is 80% of zmax
    comm->SetMountAz(0);
    commDevice.push_back(comm);
}

void tcCommPlatform::SetActivityFlag(unsigned int flag)
{
    commActivityFlags |= flag;

}

void tcCommPlatform::SetCommState(unsigned int idx, bool state)
{
    if (idx >= commDevice.size()) return; // error

    std::shared_ptr<tcCommDevice> comm = commDevice[idx];
    if (comm->IsActive() == state) return; // no change, return

    commDevice[idx]->SetActive(state);
}


void tcCommPlatform::Update(double t)
{
    ClearActivityFlags(); // flags are updated in Update() methods of child comms

    size_t nComms = commDevice.size();
    for(size_t n=0; n<nComms; n++)
    {
        std::shared_ptr<tcCommDevice>comm = commDevice[n];
        assert(comm);
        comm->Update(t);
    }
}


void tcCommPlatform::PrintToFile(tcFile& file)
{
    tcString s;

    int nComms = (int)commDevice.size();
    for(int i=0;i<nComms;i++)
    {
        std::shared_ptr<tcCommDevice>& pSS = commDevice[i];
        if (pSS != NULL)
        {
            s.Format("   COMM%d: %s\n", i, pSS->mpDBObj->mzClass.c_str());
        }
        else
        {
            s = "   BAD SENSOR\n";
        }
        file.WriteString(s.GetBuffer());
    }
}
void tcCommPlatform::SaveToFile(tcFile& file)
{
    size_t nComms = commDevice.size();
    for(size_t i=0;i<nComms;i++)
    {
        std::shared_ptr<tcCommDevice>& pss = commDevice[i];
        // pss->Serialize(file, false);
    }
}
void tcCommPlatform::LoadFromFile(tcFile& file)
{
    // assumes that comms already created by higher level serialize method
    size_t nComms = commDevice.size();
    for(size_t i=0;i<nComms;i++)
    {
        std::shared_ptr<tcCommDevice>& pss = commDevice[i];
        //pss->Serialize(file,true);
    }
}

void tcCommPlatform::Serialize(tcFile& file, bool mbLoad)
{
    if (mbLoad)
    {
        LoadFromFile(file);
    }
    else
    {
        SaveToFile(file);
    }
}
void tcCommPlatform::SaveToPython(scriptinterface::tcScenarioLogger& logger)
{
    std::string s;

    size_t nComms = commDevice.size();
    for(size_t n=0; n<nComms; n++)
    {
        std::shared_ptr<tcCommDevice>comm = commDevice[n];
        assert(comm);

        bool setState = false; // true to write command in py file to set state of comm (i.e. isnt in default state)
        setState = comm->mbActive != 0;


        if (setState)
        {
            s=strutil::format("UI.SetCommState(%d, %d)", n, comm->mbActive);
            logger.AddScenarioText(s);
        }
    }
}

bool tcCommPlatform::ApplyAdvancedDamage(const Damage& damage, std::shared_ptr<tcGameObject> damager, float damageLevel)
{
    bool result = false;


    unsigned int nComms = GetCommCount();

    // next go through every comm and apply damage

    for (unsigned int n=0; n<nComms; n++)
    {
        std::shared_ptr<tcCommDevice> comm = GetCommMutable(n);
        assert(comm);

        result = result || comm->ApplyAdvancedDamage(damage);
    }

    // last apply general damage
    if (damageLevel <= 0) return result;

    float scaledDamage = damageLevel; //(damageLevel < 0.5f) ? (0.4f * damageLevel) : damageLevel;

    for (unsigned int n=0; n<nComms; n++)
    {
        std::shared_ptr<tcCommDevice> comm = GetCommMutable(n);

        if (!comm->IsDamaged() && (randf() <= scaledDamage))
        {
            comm->SetDamaged(true);
            result = true;
        }
    }

    return result;
}

tcCommandStream& tcCommPlatform::operator<<(tcCommandStream& stream)
{
    size_t nComms = commDevice.size();
    for(size_t n=0; n < nComms; n++)
    {
        stream >> commDevice[n]->mbActive;
    }

    return stream;
}
tcCreateStream& tcCommPlatform::operator<<(tcCreateStream& stream)
{

return stream;
}
tcUpdateStream& tcCommPlatform::operator<<(tcUpdateStream& stream)

{
    unsigned short commDamage;
    stream >> commDamage;


    unsigned short damageFlag = 0x0001;

    size_t nComms = commDevice.size();
    assert(nComms <= 8*sizeof(commDamage));

    for(size_t n=0; n < nComms; n++)
    {
        bool damageState = (commDamage & damageFlag) != 0;
        commDevice[n]->SetDamaged(damageState);

        damageFlag = damageFlag << 1;
    }

    return stream;
}
tcGameStream& tcCommPlatform::operator<<(tcGameStream& stream)
{
    unsigned int nComms;
    stream >> nComms;
    assert((size_t)nComms == commDevice.size());

    stream >> commActivityFlags;
    // commCommandObj << stream;

    for (size_t k=0; k<commDevice.size(); k++)
    {
        commDevice[k]->operator<<(stream);
    }

    stream.ReadCheckValue(678);

    return stream;
}

tcCommandStream& tcCommPlatform::operator>>(tcCommandStream& stream)
{
    size_t nComms = commDevice.size();
    for(size_t n=0; n < nComms; n++)
    {
        stream << commDevice[n]->mbActive;
    }

    return stream;
}
tcCreateStream& tcCommPlatform::operator>>(tcCreateStream& stream)
{
    return stream;

}
tcUpdateStream& tcCommPlatform::operator>>(tcUpdateStream& stream)
{
    unsigned short commDamage = 0;

    unsigned short damageFlag = 0x0001;

    size_t nComms = commDevice.size();
    assert(nComms <= 8*sizeof(commDamage));

    for(size_t n=0; n < nComms; n++)
    {
        if (commDevice[n]->IsDamaged())
        {
            commDamage |= damageFlag;
        }
        damageFlag = damageFlag << 1;
    }

    stream << commDamage;

    return stream;
}
tcGameStream& tcCommPlatform::operator>>(tcGameStream& stream)
{
    unsigned int nComms = (unsigned int)commDevice.size();
    stream << nComms;

    stream << commActivityFlags;

    for (size_t k=0; k<commDevice.size(); k++)
    {
        commDevice[k]->operator>>(stream);
    }

    stream.WriteCheckValue(678);

    return stream;
}

void tcCommPlatform::ClearNewCommand()
{

}
bool tcCommPlatform::HasNewCommand() const
{
    // return commCommandObj.HasNewCommand();
    return false;
}

tcCommPlatform::tcCommPlatform()
{

}
tcCommPlatform::tcCommPlatform(const tcCommPlatform& o)
{
    commDevice.clear();
    size_t nComms = o.commDevice.size();
    for (size_t n=0;n<nComms;n++)
    {
        std::shared_ptr< tcCommDevice> pCommDevice = o.commDevice[n];
        std::shared_ptr<tcCommDevice> pNewCommState = pCommDevice->Clone();
        commDevice.push_back(pNewCommState);
    }
}
tcCommPlatform::tcCommPlatform(std::shared_ptr<tcCommPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent)
{
    Init(obj, parent); // This way avoids using this pointer in base class initializer

}
tcCommPlatform::tcCommPlatform(const char* databaseClass, std::shared_ptr<tcGameObject> parent)
{
Init(databaseClass, parent);
}

tcCommPlatform::~tcCommPlatform()
{
    size_t nComms = commDevice.size();
    for (size_t n=0; n<nComms; n++)
    {
        //delete commDevice[n];
    }
}

void tcCommPlatform::ClearActivityFlags()
{
    commActivityFlags=0; ///< flags for faster check of activity state of diff sensor types
}
