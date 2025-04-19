#ifndef TCCOMPONENTDBOBJECT_H
#define TCCOMPONENTDBOBJECT_H
#include <memory>
class tcComponentDBObject : public std::enable_shared_from_this<tcComponentDBObject>
{
public:
    tcComponentDBObject();
    virtual ~tcComponentDBObject() = default;
};

#endif // TCCOMPONENTDBOBJECT_H
