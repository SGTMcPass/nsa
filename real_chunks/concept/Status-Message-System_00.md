### Message Publisher > User accessible routines

| [Home](/trick) → [Documentation Home](../Documentation-Home) → [Simulation Capabilities](Simulation-Capabilities) → Status Message System |
|------------------------------------------------------------------|

The Message Publisher publishes executive and/or model messages. A Message Subscriber gets the messages published by the Publisher.

## Message Publisher

Trick creates one instance of the Message Publisher (in the `S_define` file). It is responsible for keeping track of all Message Subscribers,
and sending any message that is published to all of the Message Subscribers. A subscriber is made known to the Message Publisher by calling its
`::message_subscribe` routine (and conversely can be removed from the publisher by calling `::message_unsubscribe`).
Publishing a message that you want to be output by all subscribers is done by calling `::message_publish`.
If there are no subscribers, then publishing a message has no effect.

## Message Subscriber

There can be any number of Message Subscribers, whose job is to receive (and usually output) published messages. Trick automatically creates three Message Subscribers:
- `Trick::MessageCout` - outputs messages with level < 100 to the standard output stream
- `Trick::MessageHSFile` - outputs messages with level < 100 to a file named `send_hs` in the RUN directory
- `Trick::MessageTCDevice` - outputs messages with level < 100 to a socket at port 7200, used by the Simulation Control Panel for its Status Messages display

When you publish a message, it will be output by the three subscribers above.
A subscriber can be enabled / disabled at any time during simulation execution to output / ignore messages as desired.
The user may also add their own subscriber by creating a derived class from `Trick::MessageSubscriber`.

- `Trick::MessageThreadedCout` - outputs messages to the standard output stream asynchronously.

The `MessageThreadedCout` class is included with the simulation but not activated by default.  When activated messages will be written to the standard output stream like `MessageCout`, but internally we use a separate thread to do the writing.  This helps real-time performance.

To activate the `MessageThreadedCout` class, there are two ways:
- Add these 2 lines to the input file:

```python
trick_message.mtcout.init()
trick.message_subscribe(trick_message.mtcout)
```

- Or add this line to the input file:
```python
trick_message.separate_thread_set_enabled(True)
```

`trick_message.separate_thread_set_enabled(True)`  - turns on outputting messages to the standard output stream on a separate thread while turning off outputting messages to the standard output stream on the same thread and Sim Control Panel
`trick_message.separate_thread_set_enabled(False)` - turns off outputting messages to the standard output stream on a separate thread while turning on outputing messages to the standard output stream on the same thread and Sim Control Panel

## Publish a message

To publish a message:

```cpp
#include "trick/message_proto.h"
#include "trick/message_level.h"

int message_publish(int level, const char * format_msg, ...) ;
```

The level number can be any number greater than or equal to 0. Levels 0-99 are captured by Trick's default message subscribers. Trick has a few predefined levels (`Trick::MessagePublisher::MESSAGE_TYPE`) that it uses for publishing messages.
If the message subscriber's color is enabled (see below), then a particular colored message will be displayed for each of these levels:
- 0 - normal message, default color
- 1 - informational message, green
- 2 - warning message, yellow
- 3 - error message, red
- 10 - debug message, cyan

## Open a custom log file

To open a custom message file:

```cpp
#include "trick/Message_proto.hh"

int open_custom_message_file(std::string file_name, std::string subscriber_name, int level = -1);
```

This function opens a new file, adds it to the list of message subscribers, and returns the level that can be used to write to the file.

A user can specify a level >= 0. If `open_custom_message_file` is called without a level argument, the function will assign a unique level to the file that is >= 100. If a user wants the messages written to this file to also be captured by default Trick message subscribers, they should specify a level from 0-99.

Example:
```cpp
// Open the logfile
int my_level = open_custom_message_file("my_log_dir/logfile", "custom_log");

// Write to it by publishing a message with the given level
message_publish(my_level, "This message will be written to my custom logfile");
```

## User accessible routines
