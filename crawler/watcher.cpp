#include <CoreServices/CoreServices.h>
#include <iostream>

// This is the function that runs when a file changes
void myCallback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[]) 
{
    char **paths = (char **)eventPaths;
    for (size_t i = 0; i < numEvents; i++) {
        std::cout << "🔔 Watchman saw a change in: " << paths[i] << std::endl;
    }
}

int main() {
    // Watch the 'my_docs' folder which is one level up from the 'crawler' folder
    CFStringRef myPath = CFStringCreateWithCString(NULL, "../my_docs", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    FSEventStreamRef stream;
    stream = FSEventStreamCreate(NULL,
        &myCallback,
        NULL,
        pathsToWatch,
        kFSEventStreamEventIdSinceNow,
        1.0, 
        kFSEventStreamCreateFlagFileEvents
    );

    std::cout << "👀 Watchman is on duty. Watching '../my_docs'..." << std::endl;
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);
    FSEventStreamStart(stream);
    CFRunLoopRun(); 

    return 0;
}
