import re, pytest


def main(s):
    try:
        x = re.findall("\d{4}-\d{2}-\d{2}", s)
        x = x[0]
        # print(x)
        if len(x) != 10:
            print("Invalid Input")
            return 0

        m = re.findall("-\d{2}-", s)
        y = re.findall("\d{4}-", s)
        d = re.findall("-\d{2}$", s)

        x = d[0] + m[0] + y[0]
        x = re.findall("\d{2}-\d{2}-\d{4}", x)
        print("dd-mm-yyyy = ", x[0])
        return x[0]
    except Exception:
        return 0


@pytest.mark.parametrize(
    "input,output", [("10-11-2001", 0), ("2001-10-11", "11-10-2001"), ("25-25-25", 0)]
)
def test_task7_3(input, output):
    assert main(input) == output


# def test_task7_3():
#     assert main("10-11-2001") == 0
