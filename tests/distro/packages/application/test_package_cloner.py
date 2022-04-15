import pytest

from tests.distro.packages.application.package_mock_mother import PackageMockMother
from tests.distro.packages.infrastructure.git_in_memory_package_repository import GitInMemoryPackageRepository
from tutordistro.distro.packages.application.package_cloner import PackageCloner
from tutordistro.distro.packages.share.domain.clone_exception import CloneException


def test_should_clone_one_repository_in_a_path():
    # Given
    mocker = PackageMockMother()
    name, domain, version, extra = mocker.create()
    path = "test_dir"
    repository = GitInMemoryPackageRepository()

    # When
    cloner = PackageCloner(repository=repository)
    cloner(name=name, domain=domain, version=version, extra=extra, path=path)

    # Then
    assert name in repository.paths[path]


def test_should_fail_when_the_repos_has_already_been_cloned():
    # Given
    mocker = PackageMockMother()
    name, domain, version, extra = mocker.create()
    path = "test_dir"
    repository = GitInMemoryPackageRepository(paths={
        f"{path}": [name]
    })

    # When
    with pytest.raises(CloneException) as git_error:
        cloner = PackageCloner(repository=repository)
        cloner(name=name, domain=domain, version=version, extra=extra, path=path)

    # Then
    assert git_error.type is CloneException
