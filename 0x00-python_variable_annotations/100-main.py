#!/usr/bin/env python3

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)

# output
# {'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}