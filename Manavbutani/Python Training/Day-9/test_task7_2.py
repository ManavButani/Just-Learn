import re, pytest

def check(user_input):
    try:
        k = len(user_input)

        urls = re.findall(
            r"http[s]?://(?:[a-zA-Z]|[\d]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            user_input,
        )
        # print(urls)
        k1 = len(urls[0])
        if k == k1:
            return 1
        else:
            return 0
    except Exception:
        return 0


@pytest.mark.parametrize("user_input, output", [("https://bitbucket.org/crestdatasys/2023-charusat-college/branch/manav-butani-python-day-4", 1), (7, 0), (5, 0), ("https://www.manav.com",1)])
def test_task7_2(user_input, output):
    assert check(user_input) == output
