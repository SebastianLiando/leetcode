import main

def python_list_to_list_node(python_list):
    res_head = main.ListNode(python_list[0])
    res = res_head

    for i in range(1, len(python_list)):
        res.next = main.ListNode(python_list[i])
        res = res.next

    return res_head

def list_node_to_python_list(list_node):
    res = []
    tmp = list_node

    while not tmp == None:
        res.append(tmp.val)
        tmp = tmp.next
        
    return res

def get_result_from_solution(list, n):
    list_node = python_list_to_list_node(list)
    return list_node_to_python_list(main.Solution().removeNthFromEnd(list_node, n))

def test_case_1():
    assert get_result_from_solution([1, 2, 3, 4, 5], 2) == [1, 2, 3, 5]

def test_case_2():
    assert get_result_from_solution([1], 1) == []

def test_case_remove_first():
    assert get_result_from_solution([1, 2, 3, 4, 5], 5) == [2, 3, 4, 5]

def test_case_remove_last():
    assert get_result_from_solution([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4]