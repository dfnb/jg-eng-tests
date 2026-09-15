#!/usr/bin/env python3
from generate_dotnet_exercises import CASES as cases_01_06, dotnet_case
from generate_dotnet_exercises_12_18 import CASES as cases_12_18
from generate_dotnet_exercises_19_27 import CASES as cases_19_27
from generate_frontend_exercises import CASES as frontend_cases, make as frontend_case
from generate_special_exercises import make28, make29, make30
from extend_catalog_100 import main as extend_catalog
from generate_extended_backend import main as generate_extended_backend
from generate_extended_frontend import main as generate_extended_frontend
from extend_catalog_130 import main as extend_catalog_130
from generate_production_scale_exercises import main as generate_production_scale

for case in [*cases_01_06, *cases_12_18, *cases_19_27]:
    dotnet_case(case)
for case in frontend_cases:
    frontend_case(case)
make28()
make29()
make30()
extend_catalog()
generate_extended_backend()
generate_extended_frontend()
extend_catalog_130()
generate_production_scale()
print("Generated all 130 exercises")
