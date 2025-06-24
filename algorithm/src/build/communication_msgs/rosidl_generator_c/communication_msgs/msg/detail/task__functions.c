// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from communication_msgs:msg/Task.idl
// generated code does not contain a copyright notice
#include "communication_msgs/msg/detail/task__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
communication_msgs__msg__Task__init(communication_msgs__msg__Task * msg)
{
  if (!msg) {
    return false;
  }
  // task_id
  // pickup_x
  // pickup_y
  // dropoff_x
  // dropoff_y
  // available
  return true;
}

void
communication_msgs__msg__Task__fini(communication_msgs__msg__Task * msg)
{
  if (!msg) {
    return;
  }
  // task_id
  // pickup_x
  // pickup_y
  // dropoff_x
  // dropoff_y
  // available
}

bool
communication_msgs__msg__Task__are_equal(const communication_msgs__msg__Task * lhs, const communication_msgs__msg__Task * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // task_id
  if (lhs->task_id != rhs->task_id) {
    return false;
  }
  // pickup_x
  if (lhs->pickup_x != rhs->pickup_x) {
    return false;
  }
  // pickup_y
  if (lhs->pickup_y != rhs->pickup_y) {
    return false;
  }
  // dropoff_x
  if (lhs->dropoff_x != rhs->dropoff_x) {
    return false;
  }
  // dropoff_y
  if (lhs->dropoff_y != rhs->dropoff_y) {
    return false;
  }
  // available
  if (lhs->available != rhs->available) {
    return false;
  }
  return true;
}

bool
communication_msgs__msg__Task__copy(
  const communication_msgs__msg__Task * input,
  communication_msgs__msg__Task * output)
{
  if (!input || !output) {
    return false;
  }
  // task_id
  output->task_id = input->task_id;
  // pickup_x
  output->pickup_x = input->pickup_x;
  // pickup_y
  output->pickup_y = input->pickup_y;
  // dropoff_x
  output->dropoff_x = input->dropoff_x;
  // dropoff_y
  output->dropoff_y = input->dropoff_y;
  // available
  output->available = input->available;
  return true;
}

communication_msgs__msg__Task *
communication_msgs__msg__Task__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  communication_msgs__msg__Task * msg = (communication_msgs__msg__Task *)allocator.allocate(sizeof(communication_msgs__msg__Task), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(communication_msgs__msg__Task));
  bool success = communication_msgs__msg__Task__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
communication_msgs__msg__Task__destroy(communication_msgs__msg__Task * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    communication_msgs__msg__Task__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
communication_msgs__msg__Task__Sequence__init(communication_msgs__msg__Task__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  communication_msgs__msg__Task * data = NULL;

  if (size) {
    data = (communication_msgs__msg__Task *)allocator.zero_allocate(size, sizeof(communication_msgs__msg__Task), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = communication_msgs__msg__Task__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        communication_msgs__msg__Task__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
communication_msgs__msg__Task__Sequence__fini(communication_msgs__msg__Task__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      communication_msgs__msg__Task__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

communication_msgs__msg__Task__Sequence *
communication_msgs__msg__Task__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  communication_msgs__msg__Task__Sequence * array = (communication_msgs__msg__Task__Sequence *)allocator.allocate(sizeof(communication_msgs__msg__Task__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = communication_msgs__msg__Task__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
communication_msgs__msg__Task__Sequence__destroy(communication_msgs__msg__Task__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    communication_msgs__msg__Task__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
communication_msgs__msg__Task__Sequence__are_equal(const communication_msgs__msg__Task__Sequence * lhs, const communication_msgs__msg__Task__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!communication_msgs__msg__Task__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
communication_msgs__msg__Task__Sequence__copy(
  const communication_msgs__msg__Task__Sequence * input,
  communication_msgs__msg__Task__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(communication_msgs__msg__Task);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    communication_msgs__msg__Task * data =
      (communication_msgs__msg__Task *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!communication_msgs__msg__Task__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          communication_msgs__msg__Task__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!communication_msgs__msg__Task__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
