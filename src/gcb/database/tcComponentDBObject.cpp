#include "tcComponentDBObject.h"

tcComponentDBObject::tcComponentDBObject() {}


void tcComponentDBObject::SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const
{
    obj.SetObject();
}
