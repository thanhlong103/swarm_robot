// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from communication_msgs:msg/Task.idl
// generated code does not contain a copyright notice
#include "communication_msgs/msg/detail/task__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "communication_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "communication_msgs/msg/detail/task__struct.h"
#include "communication_msgs/msg/detail/task__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Task__ros_msg_type = communication_msgs__msg__Task;

static bool _Task__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Task__ros_msg_type * ros_message = static_cast<const _Task__ros_msg_type *>(untyped_ros_message);
  // Field name: task_id
  {
    cdr << ros_message->task_id;
  }

  // Field name: pickup_x
  {
    cdr << ros_message->pickup_x;
  }

  // Field name: pickup_y
  {
    cdr << ros_message->pickup_y;
  }

  // Field name: dropoff_x
  {
    cdr << ros_message->dropoff_x;
  }

  // Field name: dropoff_y
  {
    cdr << ros_message->dropoff_y;
  }

  // Field name: available
  {
    cdr << (ros_message->available ? true : false);
  }

  return true;
}

static bool _Task__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Task__ros_msg_type * ros_message = static_cast<_Task__ros_msg_type *>(untyped_ros_message);
  // Field name: task_id
  {
    cdr >> ros_message->task_id;
  }

  // Field name: pickup_x
  {
    cdr >> ros_message->pickup_x;
  }

  // Field name: pickup_y
  {
    cdr >> ros_message->pickup_y;
  }

  // Field name: dropoff_x
  {
    cdr >> ros_message->dropoff_x;
  }

  // Field name: dropoff_y
  {
    cdr >> ros_message->dropoff_y;
  }

  // Field name: available
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->available = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_communication_msgs
size_t get_serialized_size_communication_msgs__msg__Task(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Task__ros_msg_type * ros_message = static_cast<const _Task__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name task_id
  {
    size_t item_size = sizeof(ros_message->task_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pickup_x
  {
    size_t item_size = sizeof(ros_message->pickup_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pickup_y
  {
    size_t item_size = sizeof(ros_message->pickup_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dropoff_x
  {
    size_t item_size = sizeof(ros_message->dropoff_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dropoff_y
  {
    size_t item_size = sizeof(ros_message->dropoff_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name available
  {
    size_t item_size = sizeof(ros_message->available);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Task__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_communication_msgs__msg__Task(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_communication_msgs
size_t max_serialized_size_communication_msgs__msg__Task(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: task_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pickup_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pickup_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: dropoff_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: dropoff_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: available
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _Task__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_communication_msgs__msg__Task(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Task = {
  "communication_msgs::msg",
  "Task",
  _Task__cdr_serialize,
  _Task__cdr_deserialize,
  _Task__get_serialized_size,
  _Task__max_serialized_size
};

static rosidl_message_type_support_t _Task__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Task,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, communication_msgs, msg, Task)() {
  return &_Task__type_support;
}

#if defined(__cplusplus)
}
#endif
