from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [
        line for line in f.read().strip().split("\n")
        if line and not line.startswith("#")
    ]

setup(
    name="energy_erp",
    version="0.0.1",
    description="Full-stack energy ERP for India covering thermal and renewable power generation, grid distribution, plant asset management, fuel supply chain, BEE energy audits, CERC regulatory reporting, outage management, and real-time generation monitoring across multiple plant sites.",
    author="Your Company",
    author_email="dev@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
