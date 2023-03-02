import setuptools

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="prince-api",
    packages=setuptools.find_packages(),
    version="0.1.1",
    license="MIT",
    description="A Project Made To Centralize Various APIs 📖 No Authorization Needed :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MaybePrince",
    author_email="princebots3011@gmail.com",
    url="https://github.com/MaybePrince/Prince-Api",
    keywords=["Prince-Api", "python-pakage", "api", "Prince"],
    install_requires=["requests>=2.28.1"],
    project_urls={
        "Tracker": "https://github.com/MaybePrince/Prince-API/issues",
        "Community": "https://t.me/SDBOTs_inifinity",
        "Source": "https://github.com/MaybePrince/Prince-API",
        "Documentation": "https://docs.prince-api.tk",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
