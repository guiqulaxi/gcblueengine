#ifndef EVENTHANDLER_H
#define EVENTHANDLER_H

#include <functional>
#include <queue>
#include <mutex>

// 简单的事件处理器类，用于替代wxWidgets的wxEvtHandler
class EventHandler 
{
public:
    // 事件回调函数类型
    using EventCallback = std::function<void()>;
    
    // 添加待处理事件
    void AddPendingEvent(const EventCallback& callback) {
        std::lock_guard<std::mutex> lock(eventMutex);
        eventQueue.push(callback);
    }
    
    // 处理队列中的事件
    void ProcessEvents() {
        std::lock_guard<std::mutex> lock(eventMutex);
        while (!eventQueue.empty()) {
            auto callback = eventQueue.front();
            eventQueue.pop();
            callback();
        }
    }
    
    // 检查是否有待处理事件
    bool HasPendingEvents() const {
        std::lock_guard<std::mutex> lock(eventMutex);
        return !eventQueue.empty();
    }

private:
    std::queue<EventCallback> eventQueue;
    mutable std::mutex eventMutex;
};

#endif // EVENTHANDLER_H