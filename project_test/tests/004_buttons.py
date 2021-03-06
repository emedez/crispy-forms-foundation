import pytest

from crispy_forms_foundation.layout import (Layout, ButtonGroup,
                                            Submit, Button)

from forms import BasicInputForm
from utils import read_output, write_output


def test_buttongroup(output_test_path, rendered_template, helper, client):
    form = BasicInputForm()
    pack = helper.template_pack

    helper.layout = Layout(
        'simple',
        ButtonGroup(
            Submit('Save', 'Save'),
            Button('Cancel', 'Cancel'),
        )
    )

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, pack, "test_buttongroup.html")
    #write_output(output_test_path, pack, "test_buttongroup.html", rendered)

    assert rendered == attempted
