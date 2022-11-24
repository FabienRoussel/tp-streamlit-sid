from setuptools import setup, find_packages

setup(
    name='tp-streamlit-sid',
    version='0.1.0',
    packages=find_packages(),
    url='',
    license='',
    author='Fabien',
    author_email=' ',
    description='Projet streamlit pour la visualisation de KPI sur la vente de voitures d occasion',
    install_requires=['pandas==1.3.3',
                      'python-dotenv==0.19.1',
                      'streamlit==1.2.0',
                      'plotly==5.4.0',
                      'numerize'],
    extras_require={'dev': ['flake8==4.0.1',
                            'pytest==6.2.5']},
    python_requires='>=3.9',
)
