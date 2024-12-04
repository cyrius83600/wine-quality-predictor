import setuptools

setuptools.setup(
    name='wqp',
    version='1.0.0',
    author='my_email@email.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "joblib-1.4.2",
        "numpy-2.1.3",
        "pandas-2.2.3",
        "python-dateutil-2.9.0.post0",
         "pytz-2024.2",
         "scikit-learn-1.5.2",
         "scipy-1.14.1",
         "six-1.16.0",
         "threadpoolctl-3.5.0",
         "tzdata-2024.2"
    ]
)