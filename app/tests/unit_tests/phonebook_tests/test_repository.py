import pytest

from app.phone_book.repo import BookRepo


@pytest.mark.parametrize('user_id, is_exist', [
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (5, True),
    (6, False)
])
async def test_find_by_id(user_id, is_exist):
    user = await BookRepo.find_by_id(user_id)
    if is_exist:
        assert user
        assert user.id == user_id
    else:
        assert not user
