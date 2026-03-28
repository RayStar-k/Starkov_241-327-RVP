import subprocess
import pytest

# Для Windows
INTERPRETER = 'python'
# Для MAC
# INTERPRETER = 'python3' 

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ]
}

def test_hello():
    assert run_script('hello.py') == 'Hello, World!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

def test_division_1():
    assert run_script('division.py', ['10', '3']).split('\n') == ['3', '3.3333333333333335']

def test_division_2():
    assert run_script('division.py', ['7', '2']).split('\n') == ['3', '3.5']

def test_division_3():
    assert run_script('division.py', ['100', '10']).split('\n') == ['10', '10.0']

def test_loops_1():
    assert run_script('loops.py', ['3']).split('\n') == ['0', '1', '4']

def test_loops_2():
    assert run_script('loops.py', ['5']).split('\n') == ['0', '1', '4', '9', '16']

def test_loops_3():
    assert run_script('loops.py', ['1']).split('\n') == ['0']

def test_print_function_1():
    assert run_script('print_function.py', ['5']) == '12345'

def test_print_function_2():
    assert run_script('print_function.py', ['10']) == '12345678910'

def test_print_function_3():
    assert run_script('print_function.py', ['1']) == '1'

def test_second_score_1():
    assert run_script('second_score.py', ['5', '2 3 6 6 5']) == '5'

def test_second_score_2():
    assert run_script('second_score.py', ['3', '1 2 3']) == '2'

def test_second_score_3():
    assert run_script('second_score.py', ['4', '10 5 8 10']) == '8'

def test_nested_list_1():
    assert run_script('nested_list.py', ['5', 'Harry', '37.21', 'Berry', '37.21', 'Tina', '37.2', 'Akriti', '41', 'Harsh', '39']).split('\n') == ['Berry', 'Harry']

def test_nested_list_2():
    assert run_script('nested_list.py', ['3', 'Alpha', '20', 'Beta', '50', 'Gamma', '50']).split('\n') == ['Beta', 'Gamma']

def test_nested_list_3():
    assert run_script('nested_list.py', ['4', 'A', '10', 'B', '20', 'C', '15', 'D', '15']).split('\n') == ['C', 'D']

def test_lists_1():
    assert run_script('lists.py', ['4', 'append 1', 'append 2', 'insert 1 3', 'print']).split('\n') == ['[1, 3, 2]']

def test_lists_2():
    assert run_script('lists.py', ['12', 'insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']).split('\n') == ['[6, 5, 10]', '[1, 5, 9, 10]', '[9, 5, 1]']

def test_lists_3():
    assert run_script('lists.py', ['3', 'append 5', 'append 10', 'print']).split('\n') == ['[5, 10]']

def test_swap_case_1():
    assert run_script('swap_case.py', ['Www.MosPolytech.ru']) == 'wWW.mOSpOLYTECH.RU'

def test_swap_case_2():
    assert run_script('swap_case.py', ['Pythonist 2']) == 'pYTHONIST 2'

def test_swap_case_3():
    assert run_script('swap_case.py', ['Hello World']) == 'hELLO wORLD'

def test_split_and_join_1():
    assert run_script('split_and_join.py', ['this is a string']) == 'this-is-a-string'

def test_split_and_join_2():
    assert run_script('split_and_join.py', ['hello world']) == 'hello-world'

def test_split_and_join_3():
    assert run_script('split_and_join.py', ['a b c']) == 'a-b-c'

def test_max_word():
    result = run_script('max_word.py').split('\n')
    assert len(result) > 0

def test_price_sum():
    result = run_script('price_sum.py')
    parts = result.split()
    assert len(parts) == 3
    assert all(len(p.split('.')[1]) == 2 for p in parts)

def test_anagram_1():
    assert run_script('anagram.py', ['listen', 'silent']) == 'YES'

def test_anagram_2():
    assert run_script('anagram.py', ['hello', 'world']) == 'NO'

def test_anagram_3():
    assert run_script('anagram.py', ['abc', 'bca']) == 'YES'

def test_metro_1():
    assert run_script('metro.py', ['3', '1 5', '2 6', '4 7', '5']) == '3'

def test_metro_2():
    assert run_script('metro.py', ['2', '1 3', '2 4', '3']) == '2'

def test_metro_3():
    assert run_script('metro.py', ['1', '5 10', '7']) == '1'

def test_minion_game_1():
    assert run_script('minion_game.py', ['BANANA']) == 'Стюарт 12'

def test_minion_game_2():
    result = run_script('minion_game.py', ['BAANANAS'])
    assert 'Стюарт' in result or 'Кевин' in result

def test_minion_game_3():
    result = run_script('minion_game.py', ['ABC'])
    assert 'Стюарт' in result or 'Кевин' in result or 'Ничья' in result

def test_is_leap_1():
    assert run_script('is_leap.py', ['2000']) == 'True'

def test_is_leap_2():
    assert run_script('is_leap.py', ['1900']) == 'False'

def test_is_leap_3():
    assert run_script('is_leap.py', ['2024']) == 'True'

def test_is_leap_4():
    assert run_script('is_leap.py', ['2001']) == 'False'

def test_happiness_1():
    assert run_script('happiness.py', ['3 2', '1 5 3', '3 1', '5 7']) == '1'

def test_happiness_2():
    assert run_script('happiness.py', ['5 3', '1 2 3 4 5', '1 2 3', '4 5 6']) == '1'

def test_happiness_3():
    assert run_script('happiness.py', ['2 1', '5 5', '5', '6']) == '2'

def test_pirate_ship_1():
    result = run_script('pirate_ship.py', ['10 3', 'gold 5 100', 'silver 8 80', 'bronze 3 30'])
    lines = result.split('\n')
    assert len(lines) > 0

def test_pirate_ship_2():
    result = run_script('pirate_ship.py', ['5 2', 'item1 3 60', 'item2 4 40'])
    lines = result.split('\n')
    assert len(lines) > 0

def test_pirate_ship_3():
    result = run_script('pirate_ship.py', ['20 3', 'a 10 100', 'b 5 50', 'c 15 75'])
    lines = result.split('\n')
    assert len(lines) > 0

def test_matrix_mult_1():
    result = run_script('matrix_mult.py', ['2', '1 2', '3 4', '5 6', '7 8'])
    expected = ['19 22', '43 50']
    assert result.split('\n') == expected

def test_matrix_mult_2():
    result = run_script('matrix_mult.py', ['3', '1 0 0', '0 1 0', '0 0 1', '2 3 4', '5 6 7', '8 9 10'])
    lines = result.split('\n')
    assert len(lines) == 3

def test_matrix_mult_3():
    result = run_script('matrix_mult.py', ['2', '1 1', '1 1', '2 2', '2 2'])
    expected = ['4 4', '4 4']
    assert result.split('\n') == expected

def test_python_if_else_edge_1():
    assert run_script('python_if_else.py', ['2']) == 'Not Weird'

def test_python_if_else_edge_2():
    assert run_script('python_if_else.py', ['5']) == 'Weird'

def test_python_if_else_edge_3():
    assert run_script('python_if_else.py', ['20']) == 'Weird'

def test_python_if_else_edge_4():
    assert run_script('python_if_else.py', ['21']) == 'Weird'

def test_arithmetic_operators_large():
    assert run_script('arithmetic_operators.py', ['1000', '999']).split('\n') == ['1999', '1', '999000']

def test_division_large():
    assert run_script('division.py', ['1000', '3']).split('\n')[0] == '333'

def test_loops_large():
    result = run_script('loops.py', ['10'])
    lines = result.split('\n')
    assert len(lines) == 10
    assert lines[9] == '81'

def test_second_score_duplicates():
    assert run_script('second_score.py', ['6', '5 5 5 3 3 3']) == '3'

def test_swap_case_numbers():
    assert run_script('swap_case.py', ['ABC123def']) == 'abc123DEF'

def test_anagram_case():
    assert run_script('anagram.py', ['ABC', 'CBA']) == 'YES'

def test_is_leap_div_by_4():
    assert run_script('is_leap.py', ['2016']) == 'True'

def test_is_leap_century():
    assert run_script('is_leap.py', ['2100']) == 'False'


def test_arithmetic_operators_limit():
    result = run_script('arithmetic_operators.py', ['10000000001', '1'])
    assert 'Limit error' in result

def test_loops_limit():
    result = run_script('loops.py', ['25'])
    assert 'Limit error' in result

def test_print_function_limit():
    result = run_script('print_function.py', ['0'])
    assert 'Limit error' in result

def test_nested_list_limit():
    result = run_script('nested_list.py', ['1', 'John', '10'])
    assert 'Limit error' in result

def test_swap_case_limit():
    long_string = 'a' * 1001
    result = run_script('swap_case.py', [long_string])
    assert 'Limit error' in result

def test_minion_game_limit():
    # Проверка ограничения на пустую строку через прямой вызов subprocess
    import subprocess
    proc = subprocess.run(
        [INTERPRETER, 'minion_game.py'],
        input='\n',  # Пустая строка с символом новой строки
        capture_output=True,
        text=True,
        check=False
    )
    assert 'Limit error' in proc.stdout

def test_is_leap_limit():
    result = run_script('is_leap.py', ['1899'])
    assert 'Limit error' in result

def test_happiness_limit():
    result = run_script('happiness.py', ['100001 1', '1', '1', '2'])
    assert 'Limit error' in result

def test_matrix_mult_limit():
    result = run_script('matrix_mult.py', ['1', '1'])
    assert 'Limit error' in result
