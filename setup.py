from setuptools import setup, find_packages

setup(
    name             = 'nlpk',
    version          = '0.0.6',
    description      = 'Natural Language Processing for Korean',
    author           = 'GyuHyeon Nam',
    author_email     = 'ngh3053@gmail.com',

    packages         = find_packages() ,
    
    package_data     =  {
        'nlpk' : [
            'lib/*',
    ]},
    
    zip_safe=False,
    python_requires  = '>=3',

    keywords         = ['nlp', 'korean'],
    classifiers      = [
        'Programming Language :: Python :: 3'
    ],
)