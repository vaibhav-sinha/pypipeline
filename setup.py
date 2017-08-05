from setuptools import setup

setup(
    name = "pypipeline-esb",
    packages = ["pypipeline"],
    version = "1.0.0",
    description = "ESB for Python",
    author = "Vaibhav Sinha",
    author_email = "vaibhavsinh@gmail.com",
    url = "https://github.com/vaibhav-sinha/pypipeline",
    keywords = ["esb", "eip", "pipeline"],
    python_requires='>=3',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
PyPipeline is meant to be a lightweight ESB, configurable via an intutive DSL. PyPipeline implements many of the Enterprise Integration Patterns.
""",
)
