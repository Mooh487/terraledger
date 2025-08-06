from setuptools import setup, find_packages

setup(
    name="terraledger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.21.1",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "pytest>=7.3.1",
        "requests>=2.28.2",
        "sentinelhub>=3.8.0",
        "tensorflow>=2.12.0",
        "numpy>=1.24.3",
        "hedera-sdk-py>=2.18.0",
        "python-multipart>=0.0.6",
        "groq>=0.4.1",
    ],
    python_requires=">=3.9",
    author="TerraLedger Team",
    author_email="info@terraledger.com",
    description="A hyper-transparent, AI-verified carbon credit marketplace using Hedera's immutable ledger",
    keywords="carbon, credits, blockchain, hedera, nft",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
