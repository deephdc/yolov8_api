"""Testing module for api train. This is a test file designed to use
pytest and prepared for some basic assertions and to add your own tests.

You can add new tests using the following structure:
```py
def test_{description for the test}(metadata):
    # Add your assertions inside the test function
    assert {statement_1 that returns true or false}
    assert {statement_2 that returns true or false}
```
The conftest.py module in the same directory includes the fixture to return
to your tests inside the argument variable `metadata` the value generated by
your function defined at `api.get_metadata`.

If your file grows in complexity, you can split it into multiple files in
the same folder. However, remember to add the prefix `test_` to the file.
"""

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument


import os
import shutil
import pytest


# check if the chkp is saved in the chkp directory.
@pytest.mark.skip(reason="takes too much resources")
def test_train_function(training):
    """test if the chkp is saved in the chkp directory"""
    checkpoint_file = os.path.join(training, "weights/last.pt")
    assert os.path.isfile(checkpoint_file), "No checkpoint was saved"
    # Remove the saved model directory and its contents
    shutil.rmtree(training)


# Example to test training return includes 'run_id'
# def test_run_id(training):
#     """Test training result includes run_id on the return."""
#     assert "run_id" in training
#     assert isinstance(training["run_id"], str)
