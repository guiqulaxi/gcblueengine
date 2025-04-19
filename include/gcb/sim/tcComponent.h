#ifndef TCCOMPONENT_H
#define TCCOMPONENT_H

#include <memory>
class tcComponent : public std::enable_shared_from_this<tcComponent>
{
public:
    tcComponent();
    virtual ~tcComponent() = default;
};
#endif // TCCOMPONENT_H
