// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from communication_msgs:msg/TaskAllocation.idl
// generated code does not contain a copyright notice

#ifndef COMMUNICATION_MSGS__MSG__DETAIL__TASK_ALLOCATION__TRAITS_HPP_
#define COMMUNICATION_MSGS__MSG__DETAIL__TASK_ALLOCATION__TRAITS_HPP_

#include "communication_msgs/msg/detail/task_allocation__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<communication_msgs::msg::TaskAllocation>()
{
  return "communication_msgs::msg::TaskAllocation";
}

template<>
inline const char * name<communication_msgs::msg::TaskAllocation>()
{
  return "communication_msgs/msg/TaskAllocation";
}

template<>
struct has_fixed_size<communication_msgs::msg::TaskAllocation>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<communication_msgs::msg::TaskAllocation>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<communication_msgs::msg::TaskAllocation>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // COMMUNICATION_MSGS__MSG__DETAIL__TASK_ALLOCATION__TRAITS_HPP_
