from fastapi import APIRouter

router = APIRouter(
    tags=["Animals"],
    responses={404: {"description": "Not found"}},
)


@router.get("/animals")
def get_all_animals():
    return [
        {
            "id": 1,
            "name": "cat",
            "species": "cat",
            "age": 2,
            "weight": 5,
            "is_adopted": False,
        },
        {
            "id": 2,
            "name": "dog",
            "species": "dog",
            "age": 3,
            "weight": 10,
            "is_adopted": True,
        },
        {
            "id": 3,
            "name": "bird",
            "species": "bird",
            "age": 1,
            "weight": 2,
            "is_adopted": False,
        },
    ]
