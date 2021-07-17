from setuptools import setup, find_packages


with open("README.md") as file:
    long_description = file.read()

setup(
    name="python-midi",
    description="A pure python library for creating multi-track MIDI files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mark Conway Wirt",
    author_email="MarkCWirt@gmail.com",
    license="MIT",
    url="https://github.com/MarkCWirt/MIDIUtil",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,
    platforms="Platform Independent",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
    ],
    keywords="Music MIDI",
)
