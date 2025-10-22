import pytest
from request import get_status_code, get_json_placeholder_post

def test_status_code_is_200():
    # We'll call a real site (ok for learning; later we’ll mock)
    result = get_status_code("https://jsonplaceholder.typicode.com/posts/1")
    assert result == 200


def test_json_placeholder_post_has_expected_keys():
    post = get_json_placeholder_post(1)
    assert isinstance(post, dict)
    # This API always has these keys
    for key in ["userId", "id", "title", "body"]:
        assert key in post
