import pytest
import math
from fact import fact_rec, fact_it
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_gen
from my_sum import my_sum
from email_validation import fun, filter_mail
from fibonacci import fibonacci
from average_scores import compute_average_scores
from plane_angle import plane_angle, Point
from complex_numbers import Complex
from circle_square_mk import circle_square_mk
from log_decorator import function_logger
from people_sort import name_format
import os


class TestFactorial:
    def test_fact_rec_base_0(self):
        assert fact_rec(0) == 1

    def test_fact_rec_base_1(self):
        assert fact_rec(1) == 1

    def test_fact_rec_small(self):
        assert fact_rec(5) == 120

    def test_fact_rec_medium(self):
        assert fact_rec(10) == 3628800

    def test_fact_it_base_0(self):
        assert fact_it(0) == 1

    def test_fact_it_base_1(self):
        assert fact_it(1) == 1

    def test_fact_it_small(self):
        assert fact_it(5) == 120

    def test_fact_it_medium(self):
        assert fact_it(10) == 3628800

    def test_fact_rec_limit_min(self):
        assert fact_rec(1) == 1

    def test_fact_it_limit_min(self):
        assert fact_it(1) == 1

    def test_fact_rec_limit_large(self):
        assert fact_rec(100) > 0

    def test_fact_it_limit_large(self):
        assert fact_it(100) > 0


class TestShowEmployee:
    def test_with_default_salary(self):
        assert show_employee("Иванов Иван Иванович") == "Иванов Иван Иванович: 100000 ₽"

    def test_with_custom_salary(self):
        assert show_employee("Петров Петр Петрович", 50000) == "Петров Петр Петрович: 50000 ₽"

    def test_with_zero_salary(self):
        assert show_employee("Сидоров Сидор Сидорович", 0) == "Сидоров Сидор Сидорович: 0 ₽"

    def test_with_large_salary(self):
        assert show_employee("Test Name", 999999) == "Test Name: 999999 ₽"


class TestSumAndSub:
    def test_positive_numbers(self):
        assert sum_and_sub(5, 3) == (8, 2)

    def test_negative_numbers(self):
        assert sum_and_sub(-5, -3) == (-8, -2)

    def test_mixed_numbers(self):
        assert sum_and_sub(5, -3) == (2, 8)

    def test_floats(self):
        result = sum_and_sub(5.5, 2.3)
        assert abs(result[0] - 7.8) < 0.01
        assert abs(result[1] - 3.2) < 0.01

    def test_zeros(self):
        assert sum_and_sub(0, 0) == (0, 0)


class TestProcessList:
    def test_process_list_even(self):
        assert process_list([2, 4, 6]) == [4, 16, 36]

    def test_process_list_odd(self):
        assert process_list([1, 3, 5]) == [1, 27, 125]

    def test_process_list_mixed(self):
        assert process_list([1, 2, 3, 4]) == [1, 4, 27, 16]

    def test_process_list_gen_even(self):
        assert list(process_list_gen([2, 4, 6])) == [4, 16, 36]

    def test_process_list_gen_odd(self):
        assert list(process_list_gen([1, 3, 5])) == [1, 27, 125]

    def test_process_list_gen_mixed(self):
        assert list(process_list_gen([1, 2, 3, 4])) == [1, 4, 27, 16]

    def test_process_list_limit_min(self):
        assert process_list([1]) == [1]

    def test_process_list_gen_limit_min(self):
        assert list(process_list_gen([1])) == [1]

    def test_process_list_limit_max(self):
        arr = list(range(1, 1001))
        result = process_list(arr)
        assert len(result) == 1000

    def test_process_list_gen_limit_max(self):
        arr = list(range(1, 1001))
        result = list(process_list_gen(arr))
        assert len(result) == 1000


class TestMySum:
    def test_no_args(self):
        assert my_sum() == 0

    def test_single_arg(self):
        assert my_sum(5) == 5

    def test_multiple_args(self):
        assert my_sum(1, 2, 3, 4, 5) == 15

    def test_negative_numbers(self):
        assert my_sum(-1, -2, -3) == -6

    def test_floats(self):
        assert abs(my_sum(1.5, 2.5, 3.0) - 7.0) < 0.01


class TestEmailValidation:
    def test_valid_email_simple(self):
        assert fun("test@example.com") == True

    def test_valid_email_with_dash(self):
        assert fun("test-user@example.com") == True

    def test_valid_email_with_underscore(self):
        assert fun("test_user@example.com") == True

    def test_valid_email_with_numbers(self):
        assert fun("user123@domain456.org") == True

    def test_invalid_email_no_at(self):
        assert fun("testexample.com") == False

    def test_invalid_email_no_extension(self):
        assert fun("test@example") == False

    def test_invalid_email_long_extension(self):
        assert fun("test@example.comm") == False

    def test_filter_mail(self):
        emails = ["valid@test.com", "invalid", "another@valid.org"]
        assert filter_mail(emails) == ["valid@test.com", "another@valid.org"]


class TestFibonacci:
    def test_fibonacci_0(self):
        assert fibonacci(0) == []

    def test_fibonacci_1(self):
        assert fibonacci(1) == [0]

    def test_fibonacci_5(self):
        assert fibonacci(5) == [0, 1, 1, 2, 3]

    def test_fibonacci_10(self):
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_limit_min(self):
        assert fibonacci(1) == [0]

    def test_fibonacci_limit_max(self):
        result = fibonacci(15)
        assert len(result) == 15
        assert result[0] == 0
        assert result[1] == 1

    def test_fibonacci_limit_mid(self):
        result = fibonacci(7)
        assert result == [0, 1, 1, 2, 3, 5, 8]


class TestAverageScores:
    def test_single_student(self):
        scores = [(90,), (85,), (88,)]
        result = compute_average_scores(scores)
        assert abs(result[0] - 87.67) < 0.1

    def test_multiple_students(self):
        scores = [(89, 90), (90, 91)]
        result = compute_average_scores(scores)
        assert abs(result[0] - 89.5) < 0.1
        assert abs(result[1] - 90.5) < 0.1

    def test_three_subjects(self):
        scores = [(89, 90, 78), (90, 91, 85), (91, 92, 83)]
        result = compute_average_scores(scores)
        assert abs(result[0] - 90.0) < 0.1
        assert abs(result[1] - 91.0) < 0.1
        assert abs(result[2] - 82.0) < 0.1

    def test_limit_n_min(self):
        scores = [(85.0,)]
        result = compute_average_scores(scores)
        assert abs(result[0] - 85.0) < 0.1

    def test_limit_n_max(self):
        scores = [tuple([80.0] * 100)]
        result = compute_average_scores(scores)
        assert len(result) == 100
        assert abs(result[0] - 80.0) < 0.1

    def test_limit_x_max(self):
        scores = [tuple([i]) for i in range(100)]
        result = compute_average_scores(scores)
        assert abs(result[0] - 49.5) < 0.1

    def test_limit_both_max(self):
        scores = [tuple([90.0] * 100) for _ in range(100)]
        result = compute_average_scores(scores)
        assert len(result) == 100
        assert abs(result[0] - 90.0) < 0.1


class TestPlaneAngle:
    def test_point_subtraction(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        p3 = p2 - p1
        assert p3.x == 3 and p3.y == 3 and p3.z == 3

    def test_point_dot_product(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        assert p1.dot(p2) == 32

    def test_point_cross_product(self):
        p1 = Point(1, 0, 0)
        p2 = Point(0, 1, 0)
        p3 = p1.cross(p2)
        assert p3.x == 0 and p3.y == 0 and p3.z == 1

    def test_point_absolute(self):
        p = Point(3, 4, 0)
        assert p.absolute() == 5


class TestComplexNumbers:
    def test_complex_init(self):
        c = Complex(2, 3)
        assert c.real == 2 and c.imaginary == 3

    def test_complex_add(self):
        c1 = Complex(2, 3)
        c2 = Complex(1, 4)
        c3 = c1 + c2
        assert c3.real == 3 and c3.imaginary == 7

    def test_complex_sub(self):
        c1 = Complex(5, 6)
        c2 = Complex(2, 3)
        c3 = c1 - c2
        assert c3.real == 3 and c3.imaginary == 3

    def test_complex_mul(self):
        c1 = Complex(2, 1)
        c2 = Complex(5, 6)
        c3 = c1 * c2
        assert c3.real == 4 and c3.imaginary == 17

    def test_complex_div(self):
        c1 = Complex(2, 1)
        c2 = Complex(5, 6)
        c3 = c1 / c2
        assert abs(c3.real - 0.26) < 0.01
        assert abs(c3.imaginary - (-0.11)) < 0.01

    def test_complex_mod(self):
        c = Complex(3, 4)
        m = c.mod()
        assert abs(m.real - 5.0) < 0.01
        assert m.imaginary == 0

    def test_complex_str_positive_imag(self):
        c = Complex(2, 3)
        assert str(c) == "2.00+3.00i"

    def test_complex_str_negative_imag(self):
        c = Complex(2, -3)
        assert str(c) == "2.00-3.00i"


class TestCircleSquareMonteCarlo:
    def test_small_n(self):
        result = circle_square_mk(1, 100)
        assert result > 0

    def test_accuracy_increases_with_n(self):
        r = 5
        real_area = math.pi * r ** 2
        result_small = circle_square_mk(r, 100)
        result_large = circle_square_mk(r, 10000)
        error_small = abs(result_small - real_area) / real_area
        error_large = abs(result_large - real_area) / real_area
        assert error_large < error_small or error_large < 0.1


class TestLogDecorator:
    def test_decorator_creates_file(self):
        log_file = "test_files/test_log1.txt"
        if os.path.exists(log_file):
            os.remove(log_file)

        @function_logger(log_file)
        def test_func(x):
            return x * 2

        test_func(5)
        assert os.path.exists(log_file)
        os.remove(log_file)

    def test_decorator_logs_function_name(self):
        log_file = "test_files/test_log2.txt"
        if os.path.exists(log_file):
            os.remove(log_file)

        @function_logger(log_file)
        def my_function(x):
            return x + 1

        my_function(10)
        with open(log_file, 'r') as f:
            content = f.read()
            assert "my_function" in content
        os.remove(log_file)

    def test_decorator_logs_args(self):
        log_file = "test_files/test_log3.txt"
        if os.path.exists(log_file):
            os.remove(log_file)

        @function_logger(log_file)
        def add(a, b):
            return a + b

        add(3, 4)
        with open(log_file, 'r') as f:
            content = f.read()
            assert "(3, 4)" in content
        os.remove(log_file)

    def test_decorator_logs_return_value(self):
        log_file = "test_files/test_log4.txt"
        if os.path.exists(log_file):
            os.remove(log_file)

        @function_logger(log_file)
        def multiply(x, y):
            return x * y

        multiply(2, 3)
        with open(log_file, 'r') as f:
            content = f.read()
            assert "6" in content
        os.remove(log_file)

    def test_decorator_logs_duration(self):
        log_file = "test_files/test_log5.txt"
        if os.path.exists(log_file):
            os.remove(log_file)

        @function_logger(log_file)
        def slow_func():
            import time
            time.sleep(0.1)
            return "done"

        slow_func()
        with open(log_file, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "slow_func" in content
            assert "done" in content
        os.remove(log_file)


class TestPeopleSort:
    def test_single_person(self):
        people = [["Mike", "Thomson", "20", "M"]]
        result = name_format(people)
        assert result == ["Mr. Mike Thomson"]

    def test_multiple_people_sorted(self):
        people = [["Mike", "Thomson", "20", "M"], ["Robert", "Bustle", "32", "M"], ["Andria", "Bustle", "30", "F"]]
        result = name_format(people)
        assert result == ["Mr. Mike Thomson", "Ms. Andria Bustle", "Mr. Robert Bustle"]

    def test_limit_min(self):
        people = [["John", "Doe", "25", "M"]]
        result = name_format(people)
        assert len(result) == 1
        assert result[0] == "Mr. John Doe"

    def test_limit_max(self):
        people = [[f"Name{i}", f"Surname{i}", str(20 + i), "M"] for i in range(10)]
        result = name_format(people)
        assert len(result) == 10

    def test_female_format(self):
        people = [["Mary", "George", "25", "F"]]
        result = name_format(people)
        assert result == ["Ms. Mary George"]

    def test_same_age_order(self):
        people = [["Alice", "Smith", "25", "F"], ["Bob", "Jones", "25", "M"]]
        result = name_format(people)
        assert result[0] == "Ms. Alice Smith"
        assert result[1] == "Mr. Bob Jones"


class TestPhoneNumber:
    def test_wrapper_11_digits(self):
        from phone_number import sort_phone
        phones = ["88005553535"]
        result = sort_phone(phones)
        assert result == ["+7 (800) 555-35-35"]

    def test_wrapper_10_digits(self):
        from phone_number import sort_phone
        phones = ["9161234567"]
        result = sort_phone(phones)
        assert result == ["+7 (916) 123-45-67"]

    def test_wrapper_with_formatting(self):
        from phone_number import sort_phone
        phones = ["+7 (916) 123-45-67"]
        result = sort_phone(phones)
        assert result == ["+7 (916) 123-45-67"]

    def test_wrapper_multiple_phones(self):
        from phone_number import sort_phone
        phones = ["89161234567", "79161234568"]
        result = sort_phone(phones)
        assert len(result) == 2
        assert result[0] == "+7 (916) 123-45-67"
        assert result[1] == "+7 (916) 123-45-68"


class TestFileSearch:
    def test_search_file_exists(self):
        from file_search import search_file
        result = search_file("test1.txt", "test_files")
        assert result == True

    def test_search_file_not_exists(self):
        from file_search import search_file
        result = search_file("nonexistent.txt", "test_files")
        assert result == False

    def test_search_file_in_subdirectory(self):
        from file_search import search_file
        result = search_file("nested.txt", "test_files")
        assert result == True

    def test_search_file_deep(self):
        from file_search import search_file
        result = search_file("deep.log", "test_files")
        assert result == True


class TestMySum:
    def test_command_line_sum(self):
        import subprocess
        result = subprocess.run(
            ["python", "my_sum_argv.py", "1", "2", "3"],
            capture_output=True,
            text=True
        )
        assert result.stdout.strip() == "6.0"

    def test_command_line_floats(self):
        import subprocess
        result = subprocess.run(
            ["python", "my_sum_argv.py", "1.5", "2.5"],
            capture_output=True,
            text=True
        )
        assert result.stdout.strip() == "4.0"


class TestFilesSort:
    def test_sort_by_extension(self):
        import subprocess
        result = subprocess.run(
            ["python", "files_sort.py", "test_files"],
            capture_output=True,
            text=True
        )
        lines = result.stdout.strip().split('\n')
        assert len(lines) >= 4

    def test_sort_order(self):
        import subprocess
        result = subprocess.run(
            ["python", "files_sort.py", "test_files"],
            capture_output=True,
            text=True
        )
        lines = result.stdout.strip().split('\n')
        json_files = [line for line in lines if line.endswith('.json')]
        md_files = [line for line in lines if line.endswith('.md')]
        py_files = [line for line in lines if line.endswith('.py')]
        txt_files = [line for line in lines if line.endswith('.txt')]
        assert len(json_files) >= 2
        assert len(md_files) >= 2
        assert len(py_files) >= 2
        assert len(txt_files) >= 2
