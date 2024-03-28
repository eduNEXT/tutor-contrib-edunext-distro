"""
Package mocker for tests.
"""


class PackageMockMother:
    """
    Defines a simple package using a name, a domain, a verison and extra commands.
    """

    def __init__(self) -> None:
        self._name = "eox-tests"
        self._domain = "github.com"
        self._version = "v1.0.0"
        self._extra = {"repo": "eox-tests", "protocol": "ssh", "path": "eduNEXT"}

    def create(
        self,
        name: str = None,
        domain: str = None,
        version: str = None,
        extra: dict = None
    ):
        """
        Setter method for package mocker
        """
        package = {
            "name": name if name else self._name,
            "domain": domain if domain else self._domain,
            "version": version if version else self._version,
            "extra": extra if extra else self._extra
        }
        return package["name"], package["domain"], package["version"], package["extra"]
