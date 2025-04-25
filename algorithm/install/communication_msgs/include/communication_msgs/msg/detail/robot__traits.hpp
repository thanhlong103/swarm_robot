// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from communication_msgs:msg/Robot.idl
// generated code does not contain a copyright notice

#ifndef COMMUNICATION_MSGS__MSG__DETAIL__ROBOT__TRAITS_HPP_
#define COMMUNICATION_MSGS__MSG__DETAIL__ROBOT__TRAITS_HPP_

#include "communication_msgs/msg/detail/robot__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<communication_msgs::msg::Robot>()
{
  return "communication_msgs::msg::Robot";
}

template<>
inline const char * name<communication_msgs::msg::Robot>()
{
  return "communication_msgs/msg/Robot";
}

template<>
struct has_fixed_size<communication_msgs::msg::Robot>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<communication_msgs::msg::Robot>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<communication_msgs::msg::Robot>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // COMMUNICATION_MSGS__MSG__DETAIL__ROBOT__TRAITS_HPP_
