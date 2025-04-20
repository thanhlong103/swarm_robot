// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from communication_msgs:msg/TaskAllocation.idl
// generated code does not contain a copyright notice
#include "communication_msgs/msg/detail/task_allocation__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `task_ids`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
communication_msgs__msg__TaskAllocation__init(communication_msgs__msg__TaskAllocation * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // task_ids
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->task_ids, 0)) {
    communication_msgs__msg__TaskAllocation__fini(msg);
    return false;
  }
  // total_distance
  return true;
}

void
communication_msgs__msg__TaskAllocation__fini(communication_msgs__msg__TaskAllocation * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // task_ids
  rosidl_runtime_c__int32__Sequence__fini(&msg->task_ids);
  // total_distance
}

bool
communication_msgs__msg__TaskAllocation__are_equal(const communication_msgs__msg__TaskAllocation * lhs, const communication_msgs__msg__TaskAllocation * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // task_ids
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->task_ids), &(rhs->task_ids)))
  {
    return false;
  }
  // total_distance
  if (lhs->total_distance != rhs->total_distance) {
    return false;
  }
  return true;
}

bool
communication_msgs__msg__TaskAllocation__copy(
  const communication_msgs__msg__TaskAllocation * input,
  communication_msgs__msg__TaskAllocation * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // task_ids
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->task_ids), &(output->task_ids)))
  {
    return false;
  }
  // total_distance
  output->total_distance = input->total_distance;
  return true;
}

communication_msgs__msg__TaskAllocation *
communication_msgs__msg__TaskAllocation__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  communication_msgs__msg__TaskAllocation * msg = (communication_msgs__msg__TaskAllocation *)allocator.allocate(sizeof(communication_msgs__msg__TaskAllocation), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(communication_msgs__msg__TaskAllocation));
  bool success = communication_msgs__msg__TaskAllocation__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
communication_msgs__msg__TaskAllocation__destroy(communication_msgs__msg__TaskAllocation * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    communication_msgs__msg__TaskAllocation__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
communication_msgs__msg__TaskAllocation__Sequence__init(communication_msgs__msg__TaskAllocation__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  communication_msgs__msg__TaskAllocation * data = NULL;

  if (size) {
    data = (communication_msgs__msg__TaskAllocation *)allocator.zero_allocate(size, sizeof(communication_msgs__msg__TaskAllocation), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = communication_msgs__msg__TaskAllocation__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        communication_msgs__msg__TaskAllocation__fini(&data[i - 1]);
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
communication_msgs__msg__TaskAllocation__Sequence__fini(communication_msgs__msg__TaskAllocation__Sequence * array)
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
      communication_msgs__msg__TaskAllocation__fini(&array->data[i]);
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

communication_msgs__msg__TaskAllocation__Sequence *
communication_msgs__msg__TaskAllocation__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  communication_msgs__msg__TaskAllocation__Sequence * array = (communication_msgs__msg__TaskAllocation__Sequence *)allocator.allocate(sizeof(communication_msgs__msg__TaskAllocation__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = communication_msgs__msg__TaskAllocation__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
communication_msgs__msg__TaskAllocation__Sequence__destroy(communication_msgs__msg__TaskAllocation__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    communication_msgs__msg__TaskAllocation__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
communication_msgs__msg__TaskAllocation__Sequence__are_equal(const communication_msgs__msg__TaskAllocation__Sequence * lhs, const communication_msgs__msg__TaskAllocation__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!communication_msgs__msg__TaskAllocation__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
communication_msgs__msg__TaskAllocation__Sequence__copy(
  const communication_msgs__msg__TaskAllocation__Sequence * input,
  communication_msgs__msg__TaskAllocation__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(communication_msgs__msg__TaskAllocation);
    communication_msgs__msg__TaskAllocation * data =
      (communication_msgs__msg__TaskAllocation *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!communication_msgs__msg__TaskAllocation__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          communication_msgs__msg__TaskAllocation__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!communication_msgs__msg__TaskAllocation__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
