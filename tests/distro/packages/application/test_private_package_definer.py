import pytest

from tests.distro.packages.application.package_mock_mother import PackageMockMother
from tests.distro.packages.infrastructure.git_in_memory_package_repository import GitInMemoryPackageRepository
from tutordistro.distro.packages.application.private_package_definer import PrivatePackageDefiner
from tutordistro.distro.packages.domain.package_does_not_exist import PackageDoesNotExist


def test_should_define_a_private_package_if_it_has_already_been_cloned():
    # Given
    mocker = PackageMockMother()
    name, *_ = mocker.create()
    repository = GitInMemoryPackageRepository(paths={
        "requirements": [name]
    })

    # When
    definer = PrivatePackageDefiner(repository=repository)
    definer(name=name)

    # Then
    assert name in repository.private_file


def test_should_fail_if_package_has_not_been_cloned_yet():
    # Given
    mocker = PackageMockMother()
    name, *_ = mocker.create()
    repository = GitInMemoryPackageRepository()

    # When
    with pytest.raises(PackageDoesNotExist) as package_error:
        definer = PrivatePackageDefiner(repository=repository)
        definer(name=name)

    # Then
    assert package_error.type is PackageDoesNotExist
