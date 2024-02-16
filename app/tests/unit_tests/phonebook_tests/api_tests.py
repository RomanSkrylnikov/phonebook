import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("lastname, name, middlename, org_name, work_phone, cell_phone, status_code", [
    ('petrov', 'petr', 'petrovich', 'zavod', '77788', '8905789254', 200),
    ('nikitin', 'nikita', 'nikitovich', 'zavod', '77789', '8920741852', 200)
])
async def test_create_user(lastname, name, middlename, org_name, work_phone, cell_phone, status_code, ac: AsyncClient):
    response = await ac.post('/phone_book/create_user', json={
        'lastname': lastname,
        'name': name,
        'middlename': middlename,
        'org_name': org_name,
        'work_phone': work_phone,
        'cell_phone': cell_phone
    })
    assert response.status_code == status_code
