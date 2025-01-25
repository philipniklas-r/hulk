from absl.testing import absltest

def get_linenumber(): ...

class SpecsTest(absltest.TestCase):
    def test_basic(self) -> None: ...
    def test_kwarg(self) -> None: ...
    def test_load_xml(self) -> None: ...
    def test_compile_errors_with_line_info(self) -> None: ...
    def test_recompile(self) -> None: ...
    def test_uncompiled_spec_cannot_be_written(self) -> None: ...
    def test_modelname_default_class(self) -> None: ...
    def test_element_list(self) -> None: ...
    def test_body_list(self) -> None: ...
    def test_iterators(self) -> None: ...
    def test_assets(self) -> None: ...
    def test_include(self) -> None: ...
    def test_delete(self) -> None: ...
    def test_plugin(self) -> None: ...
    def test_recompile_error(self) -> None: ...
    def test_delete_unused_plugin(self) -> None: ...
    def test_access_option_stat_visual(self) -> None: ...
    def test_assign_list_element(self) -> None: ...
    def test_assign_texture(self) -> None: ...
    def test_attach_units(self) -> None: ...
    def test_attach_body_to_site(self) -> None: ...
    def test_body_to_frame(self) -> None: ...
    def test_attach_spec_to_frame(self) -> None: ...
