from Stack_Basics.Examples.ex_3_custom_implementation_using_linked_lists import MyStack


def are_parenthesis_balanced(input: str) -> bool:
    stack = MyStack()
    open_to_close_map = {"(": ")", "{": "}", "[": "]"}

    for bracket in input:
        if bracket in open_to_close_map:
            stack.push(open_to_close_map[bracket])
        else:
            if stack.is_empty() or (stack.peek() != bracket):
                return False
            stack.pop()

    return stack.is_empty()


if __name__ == '__main__':
    tcs = ["[[{(())}]]", "([])", "([](", "((())", "{}{}([()])", "]()"]
    for tc in tcs:
        print(are_parenthesis_balanced(tc))
