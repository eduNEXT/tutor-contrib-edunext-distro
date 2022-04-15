import pytest

from tests.distro.packages.domain.package_mock import GitPackageMock
from tests.distro.packages.infrastructure.git_in_memory_package_repository import GitInMemoryPackageRepository
from tutordistro.distro.packages.application.package_cloner import PackageCloner
from tutordistro.distro.packages.share.domain.clone_exception import CloneException


def test_should_clone_one_repository_in_a_path():
    # Given
    mocker = GitPackageMock()
    package = mocker.create()
    path = "test_dir"
    repository = GitInMemoryPackageRepository()

    # When
    cloner = PackageCloner(repository=repository)
    cloner(package=package, path=path)

    # Then
    assert package.name in repository.repos[path]


def test_should_fail_when_the_repos_has_already_been_cloned():
    # Given
    mocker = GitPackageMock()
    package = mocker.create()
    path = "test_dir"
    repository = GitInMemoryPackageRepository(repos={
        path: [package.name]
    })

    # When
    with pytest.raises(CloneException) as git_error:
        cloner = PackageCloner(repository=repository)
        cloner(package=package, path=path)

    # Then
    assert git_error.type is CloneException
