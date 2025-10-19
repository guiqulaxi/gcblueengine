#ifndef TCCOMPONENTDBOBJECT_H
#define TCCOMPONENTDBOBJECT_H
#include <memory>
#include"rapidjson/document.h"
class tcComponentDBObject : public std::enable_shared_from_this<tcComponentDBObject>
{
public:
    tcComponentDBObject();
    virtual ~tcComponentDBObject() = default;
    virtual void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const;

};

#endif // TCCOMPONENTDBOBJECT_H
