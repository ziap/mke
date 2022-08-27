import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

repo = 'https://github.com/ziap/mke'

setuptools.setup(
    name='mke_pypi_test',
    author='Bùi Huy Giáp',
    author_email='67962871+ziap@users.noreply.github.com',
    description='MKE PyPI (Python Package Index)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=repo,
    project_urls={
        'Documentation': repo + '#readme',
        'Bug Reports': repo + '/issues',
        'Source Code': repo
        },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        
        'Natural Language :: Vietnamese',
        
        'Operating System :: OS Independent',
        ],
    python_requires='>=3.6'
    )
