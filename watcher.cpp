#include <CoreServices/CoreServices.h>
#include <iostream>
#include <vector>

// This function runs every time a file changes
void callback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[]) 
{
    char **paths = (char **)eventPaths;
    for (size_t i = 0; i < numEvents; i++) {
        std::cout << "📂 File change detected: " << paths[i] << std::endl;
        // Tell Python to re-index
        system("curl -X POST http://127.0.0.1:8000/index-folder");
    }
}

int main() {
    std::cout << "🛡️ Watchman is standing guard over 'my_docs'..." << std::endl;
    
    CFStringRef mypath = CFSTR("./my_docs");
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&mypath, 1, NULL);
    
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL, &callback, NULL, pathsToWatch,
        kFSEventStreamEventIdSinceNow, 1.0, kFSEventStreamCreateFlagNone
    );

    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);
    FSEventStreamStart(stream);
    CFRunLoopRun();
    return 0;
}
