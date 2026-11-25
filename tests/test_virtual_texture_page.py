import pytest
import graphics.virtual_texture_page as mod

CASES = [
    ("request_coalesce_sort", (1,)),
    ("page_generation_check", (1,)),
    ("pin_sampled_page", (1,)),
    ("feedback_deferred", (1,)),
    ("mip_coverage_area", (1,)),
    ("placeholder_on_miss", (1,)),
    ("request", (1,)),
    ("reside", (1,)),
    ("sample", (1,)),
    ("present", (1,)),
    ("validate_vt", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
