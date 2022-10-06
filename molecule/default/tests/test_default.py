"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("directory", [{"path": "/etc/sysctl.d", "mode": "0o755"}])
def test_directories(host, directory):
    """Test that the appropriate directories were created."""
    assert host.file(directory["path"]).exists
    assert host.file(directory["path"]).is_directory
    if "mode" in directory:
        assert oct(host.file(directory["path"]).mode) == directory["mode"]


@pytest.mark.parametrize(
    "file",
    [
        {
            "contents": "^vm.zone_reclaim_mode=0$",
            "mode": "0o644",
            "path": "/etc/sysctl.d/99-disable-numa.conf",
        }
    ],
)
def test_files(host, file):
    """Test that config files were modified as expected."""
    assert host.file(file["path"]).exists
    assert host.file(file["path"]).is_file
    assert oct(host.file(file["path"]).mode) == file["mode"]
    assert host.file(file["path"]).contains(file["contents"])
