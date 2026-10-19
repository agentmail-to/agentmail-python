from importlib.metadata import metadata, requires, version

from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.version import Version


def test_distribution_requires_patched_python_runtime() -> None:
    supported = SpecifierSet(metadata("agentmail")["Requires-Python"])
    assert Version("3.9.99") not in supported
    assert Version("3.10.0") in supported


def test_consumers_cannot_resolve_vulnerable_anyio() -> None:
    dependencies = [Requirement(value) for value in requires("agentmail") or []]
    anyio = next(dependency for dependency in dependencies if dependency.name == "anyio")
    assert anyio.marker is None
    assert Version("4.14.1") not in anyio.specifier
    assert Version("4.14.2") in anyio.specifier


def test_test_environment_uses_patched_anyio() -> None:
    assert Version(version("anyio")) >= Version("4.14.2")
