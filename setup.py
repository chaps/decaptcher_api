from distutils.core import setup

setup(
    name="decaptcher_api",
    version="0.0.1",
    author="Chaps",
    author_email="drumchaps@gmail.com",
    maintainer="Chaps",
    maintainer_email="drumchaps@gmail.com",
    url="https://bitbucket.org/drumchaps/decaptcherapi",
    packages  = [
        "decaptcher_api",
        #'md5',
        #'xml',
        #'traceback',
    ],
    package_dir={'decaptcher_api': 'src/decaptcher_api'},
    install_requires = ["requests",]
)


