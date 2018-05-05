from setuptools import setup, find_packages


setup(
    name='viech',
    version='0.1.0.dev0',
    author='Nicolas Drebenstedt',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='Apache-2.0',
    namespace_packages=['viech'],
    setup_requires=['setuptools_git'],
    install_requires=[
        'keras',
        'matplotlib',
        'graphviz',
        'numpy',
        'opencv-contrib-python',
        'pandas',
        'pillow',
        'scikit-learn',
        'scipy',
        'setuptools',
        'sklearn',
        'tensorflow'
    ],
    entry_points={
        'console_scripts': [
            'viech=viech.app:main'
        ]
    }
)
