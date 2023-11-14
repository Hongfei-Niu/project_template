from setuptools import setup, find_packages

setup(
    name='xxx',
    version=__version__,
    packages=[''],
    package_dir = {
        'xxxx.audio': 'xxxx/audio',
        'xxxx.encrypt': 'xxxx/encrypt'
        },
    # packages=find_packages(), #where="dailytools"),
    # package_dir={"": "dailytools"},
    install_requires=[
    ],

    author='K2.ANNN',
    author_email='xxxxx@gmail.com',
    description='Project Template',
    keywords='',
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',

        'Programming Language :: Python :: 3.11',
    ],
    include_package_data=True,
    exclude_package_data={'':['.gitignore', "__pycache__/", ".DS_Store"]}
)
