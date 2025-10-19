#ifndef TCCOMPONENT_H
#define TCCOMPONENT_H

#include <memory>
#include <rapidjson/document.h>
class tcComponent : public std::enable_shared_from_this<tcComponent>
{
public:
    tcComponent();
    virtual ~tcComponent() = default;
    virtual std::string GetType() const =0 ;
    virtual void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const =0 ;
};
#endif // TCCOMPONENT_H
