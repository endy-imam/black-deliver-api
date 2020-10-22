from deliver.models import world

def test_world():
    assert "Warudo" in world()
