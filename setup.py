import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.md"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutordistro", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-edunext-distro",
    version=ABOUT["__version__"],
    url="https://github.com/eduNEXT/tutor-contrib-edunext-distro",
    project_urls={
        "Code": "https://github.com/eduNEXT/tutor-contrib-edunext-distro",
        "Issue tracker": "https://github.com/eduNEXT/tutor-contrib-edunext-distro/issues",
    },
    license="AGPLv3",
    author="eduNEXT",
    description="edunext-distro plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["tutor<=14.0.0"],
    extras_require={
            "test": ["behave", "pytest", "pylint"]
        },
    entry_points={
        "tutor.plugin.v0": [
            "distro = tutordistro.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
