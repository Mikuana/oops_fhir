from importlib import resources

from oops_fhir.terminologies import r4
from oops_fhir.terminologies.us import core as us_core

implementations = [r4, us_core]

if __name__ == '__main__':
    for i in implementations:
        contents = resources.contents(i)

        if 'code_system' in contents:
            print(resources)
        if 'value_set' in contents:
            pass

    # for i in implementations:
    #     prefix = "/home/chris/PycharmProjects/oops_fhir/oops_fhir/terminologies"
    #     CodeSystem(f"{prefix}/r4/code_system/administrative_gender.json")
    #     ValueSet(f"{prefix}/r4/value_set/administrative_gender.json")
    #     reg_p.write_text(
    #         json.dumps({k: registry[k] for k in sorted(registry.keys())}, indent=2)
    #     )
