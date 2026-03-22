from Lesson7.hw7.employee import EmployeeApi


base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)

def test_create_employee():
    employee_json = {
        "first_name": "Alex",
        "last_name": "string",
        "middle_name": "string",
        "company_id": 2,
        "email": "user@example.com",
        "phone": "string",
        "birthdate": "2026-03-18",
        "is_active": True
    }

    new_empl = api.create_employ(data_json=employee_json)
    assert new_empl["first_name"] == "Alex"


def test_get_employee():
    employee_info = api.get_employee_by_id(1)
    assert employee_info["first_name"] == "Иван"


def test_edit_employee():
    mod_employ = api.edit_employee(1, "sidorov", "harrypotter", "expelliarmus")
    assert mod_employ["last_name"] == "sidorov"
