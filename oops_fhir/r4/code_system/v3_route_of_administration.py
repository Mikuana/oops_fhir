from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3RouteOfAdministration"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3RouteOfAdministration:
    """
    v3 Code System RouteOfAdministration

     The path the administered medication takes to get into the body or into
contact with the body.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration
    """

    underscore_route_by_method = CodeSystemConcept(
        {
            "code": "_RouteByMethod",
            "concept": [
                {
                    "code": "SOAK",
                    "definition": "Immersion (soak)",
                    "display": "Immersion (soak)",
                },
                {"code": "SHAMPOO", "definition": "Shampoo", "display": "Shampoo"},
                {
                    "code": "TRNSLING",
                    "definition": "Translingual",
                    "display": "Translingual",
                },
                {
                    "code": "PO",
                    "definition": "Swallow, oral",
                    "display": "Swallow, oral",
                },
                {"code": "GARGLE", "definition": "Gargle", "display": "Gargle"},
                {
                    "code": "SUCK",
                    "definition": "Suck, oromucosal",
                    "display": "Suck, oromucosal",
                },
                {
                    "code": "_Chew",
                    "concept": [
                        {
                            "code": "CHEW",
                            "definition": "Chew, oral",
                            "display": "Chew, oral",
                        }
                    ],
                    "definition": "Chew",
                    "display": "Chew",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Diffusion",
                    "concept": [
                        {
                            "code": "EXTCORPDIF",
                            "definition": "Diffusion, extracorporeal",
                            "display": "Diffusion, extracorporeal",
                        },
                        {
                            "code": "HEMODIFF",
                            "definition": "Diffusion, hemodialysis",
                            "display": "Diffusion, hemodialysis",
                        },
                        {
                            "code": "TRNSDERMD",
                            "definition": "Diffusion, transdermal",
                            "display": "Diffusion, transdermal",
                        },
                    ],
                    "definition": "Diffusion",
                    "display": "Diffusion",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Dissolve",
                    "concept": [
                        {
                            "code": "DISSOLVE",
                            "definition": "Dissolve, oral",
                            "display": "Dissolve, oral",
                        },
                        {
                            "code": "SL",
                            "definition": "Dissolve, sublingual",
                            "display": "Dissolve, sublingual",
                        },
                    ],
                    "definition": "Dissolve",
                    "display": "Dissolve",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Douche",
                    "concept": [
                        {
                            "code": "DOUCHE",
                            "definition": "Douche, vaginal",
                            "display": "Douche, vaginal",
                        }
                    ],
                    "definition": "Douche",
                    "display": "Douche",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_ElectroOsmosisRoute",
                    "concept": [
                        {
                            "code": "ELECTOSMOS",
                            "definition": "Electro-osmosis",
                            "display": "Electro-osmosis",
                        }
                    ],
                    "definition": "Electro-osmosis",
                    "display": "ElectroOsmosisRoute",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Enema",
                    "concept": [
                        {
                            "code": "ENEMA",
                            "definition": "Enema, rectal",
                            "display": "Enema, rectal",
                        },
                        {
                            "code": "RETENEMA",
                            "definition": "Enema, rectal retention",
                            "display": "Enema, rectal retention",
                        },
                    ],
                    "definition": "Enema",
                    "display": "Enema",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Flush",
                    "concept": [
                        {
                            "code": "IVFLUSH",
                            "definition": "Flush, intravenous catheter",
                            "display": "Flush, intravenous catheter",
                        }
                    ],
                    "definition": "Flush",
                    "display": "Flush",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Implantation",
                    "concept": [
                        {
                            "code": "IDIMPLNT",
                            "definition": "Implantation, intradermal",
                            "display": "Implantation, intradermal",
                        },
                        {
                            "code": "IVITIMPLNT",
                            "definition": "Implantation, intravitreal",
                            "display": "Implantation, intravitreal",
                        },
                        {
                            "code": "SQIMPLNT",
                            "definition": "Implantation, subcutaneous",
                            "display": "Implantation, subcutaneous",
                        },
                    ],
                    "definition": "Implantation",
                    "display": "Implantation",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Infusion",
                    "concept": [
                        {
                            "code": "EPI",
                            "definition": "Infusion, epidural",
                            "display": "Infusion, epidural",
                        },
                        {
                            "code": "IA",
                            "definition": "Infusion, intraarterial catheter",
                            "display": "Infusion, intraarterial catheter",
                        },
                        {
                            "code": "IC",
                            "definition": "Infusion, intracardiac",
                            "display": "Infusion, intracardiac",
                        },
                        {
                            "code": "ICOR",
                            "definition": "Infusion, intracoronary",
                            "display": "Infusion, intracoronary",
                        },
                        {
                            "code": "IOSSC",
                            "definition": "Infusion, intraosseous, continuous",
                            "display": "Infusion, intraosseous, continuous",
                        },
                        {
                            "code": "IT",
                            "definition": "Infusion, intrathecal",
                            "display": "Infusion, intrathecal",
                        },
                        {
                            "code": "IV",
                            "concept": [
                                {
                                    "code": "IVC",
                                    "definition": "Infusion, intravenous catheter",
                                    "display": "Infusion, intravenous catheter",
                                },
                                {
                                    "code": "IVCC",
                                    "definition": "Infusion, intravenous catheter, continuous",
                                    "display": "Infusion, intravenous catheter, continuous",
                                },
                                {
                                    "code": "IVCI",
                                    "definition": "Infusion, intravenous catheter, intermittent",
                                    "display": "Infusion, intravenous catheter, intermittent",
                                },
                                {
                                    "code": "PCA",
                                    "definition": "Infusion, intravenous catheter, pca pump",
                                    "display": "Infusion, intravenous catheter, pca pump",
                                },
                            ],
                            "definition": "Infusion, intravenous",
                            "display": "Infusion, intravenous",
                        },
                        {
                            "code": "IVASCINFUS",
                            "definition": "Infusion, intravascular",
                            "display": "Infusion, intravascular",
                        },
                        {
                            "code": "SQINFUS",
                            "definition": "Infusion, subcutaneous",
                            "display": "Infusion, subcutaneous",
                        },
                    ],
                    "definition": "Infusion",
                    "display": "Infusion",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Inhalation",
                    "concept": [
                        {
                            "code": "IPINHL",
                            "concept": [
                                {
                                    "code": "ORIFINHL",
                                    "definition": "Inhalation, oral intermittent flow",
                                    "display": "Inhalation, oral intermittent flow",
                                },
                                {
                                    "code": "REBREATH",
                                    "definition": "Inhalation, oral rebreather mask",
                                    "display": "Inhalation, oral rebreather mask",
                                },
                            ],
                            "definition": "Inhalation, oral",
                            "display": "Inhalation, respiratory",
                        },
                        {
                            "code": "IPPB",
                            "definition": "Inhalation, intermittent positive pressure breathing (ippb)",
                            "display": "Inhalation, intermittent positive pressure breathing (ippb)",
                        },
                        {
                            "code": "NASINHL",
                            "concept": [
                                {
                                    "code": "NASINHLC",
                                    "definition": "Inhalation, nasal, prongs",
                                    "display": "Inhalation, nasal cannula",
                                }
                            ],
                            "definition": "Inhalation, nasal",
                            "display": "Inhalation, nasal",
                        },
                        {
                            "code": "NEB",
                            "concept": [
                                {
                                    "code": "NASNEB",
                                    "definition": "Inhalation, nebulization, nasal",
                                    "display": "Inhalation, nebulization, nasal",
                                },
                                {
                                    "code": "ORNEB",
                                    "definition": "Inhalation, nebulization, oral",
                                    "display": "Inhalation, nebulization, oral",
                                },
                            ],
                            "definition": "Inhalation, nebulization",
                            "display": "Inhalation, nebulization",
                        },
                        {
                            "code": "TRACH",
                            "definition": "Inhalation, tracheostomy",
                            "display": "Inhalation, tracheostomy",
                        },
                        {
                            "code": "VENT",
                            "definition": "Inhalation, ventilator",
                            "display": "Inhalation, ventilator",
                        },
                        {
                            "code": "VENTMASK",
                            "definition": "Inhalation, ventimask",
                            "display": "Inhalation, ventimask",
                        },
                    ],
                    "definition": "Inhalation",
                    "display": "Inhalation",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Injection",
                    "concept": [
                        {
                            "code": "AMNINJ",
                            "definition": "Injection, amniotic fluid",
                            "display": "Injection, amniotic fluid",
                        },
                        {
                            "code": "BILINJ",
                            "definition": "Injection, biliary tract",
                            "display": "Injection, biliary tract",
                        },
                        {
                            "code": "CHOLINJ",
                            "definition": "Injection, for cholangiography",
                            "display": "Injection, for cholangiography",
                        },
                        {
                            "code": "CERVINJ",
                            "definition": "Injection, cervical",
                            "display": "Injection, cervical",
                        },
                        {
                            "code": "EPIDURINJ",
                            "definition": "Injection, epidural",
                            "display": "Injection, epidural",
                        },
                        {
                            "code": "EPIINJ",
                            "definition": "Injection, epidural, push",
                            "display": "Injection, epidural, push",
                        },
                        {
                            "code": "EPINJSP",
                            "definition": "Injection, epidural, slow push",
                            "display": "Injection, epidural, slow push",
                        },
                        {
                            "code": "EXTRAMNINJ",
                            "definition": "Injection, extra-amniotic",
                            "display": "Injection, extra-amniotic",
                        },
                        {
                            "code": "EXTCORPINJ",
                            "definition": "Injection, extracorporeal",
                            "display": "Injection, extracorporeal",
                        },
                        {
                            "code": "GBINJ",
                            "definition": "Injection, gastric button",
                            "display": "Injection, gastric button",
                        },
                        {
                            "code": "GINGINJ",
                            "definition": "Injection, gingival",
                            "display": "Injection, gingival",
                        },
                        {
                            "code": "BLADINJ",
                            "definition": "Injection, urinary bladder",
                            "display": "Injection, urinary bladder",
                        },
                        {
                            "code": "ENDOSININJ",
                            "definition": "Injection, endosinusial",
                            "display": "Injection, endosinusial",
                        },
                        {
                            "code": "HEMOPORT",
                            "definition": "Injection, hemodialysis port",
                            "display": "Injection, hemodialysis port",
                        },
                        {
                            "code": "IABDINJ",
                            "definition": "Injection, intra-abdominal",
                            "display": "Injection, intra-abdominal",
                        },
                        {
                            "code": "IAINJ",
                            "concept": [
                                {
                                    "code": "IAINJP",
                                    "definition": "Injection, intraarterial, push",
                                    "display": "Injection, intraarterial, push",
                                },
                                {
                                    "code": "IAINJSP",
                                    "definition": "Injection, intraarterial, slow push",
                                    "display": "Injection, intraarterial, slow push",
                                },
                            ],
                            "definition": "Injection, intraarterial",
                            "display": "Injection, intraarterial",
                        },
                        {
                            "code": "IARTINJ",
                            "definition": "Injection, intraarticular",
                            "display": "Injection, intraarticular",
                        },
                        {
                            "code": "IBURSINJ",
                            "definition": "Injection, intrabursal",
                            "display": "Injection, intrabursal",
                        },
                        {
                            "code": "ICARDINJ",
                            "concept": [
                                {
                                    "code": "ICARDINJRP",
                                    "definition": "Injection, intracardiac, rapid push",
                                    "display": "Injection, intracardiac, rapid push",
                                },
                                {
                                    "code": "ICARDINJSP",
                                    "definition": "Injection, intracardiac, slow push",
                                    "display": "Injection, intracardiac, slow push",
                                },
                                {
                                    "code": "ICARINJP",
                                    "definition": "Injection, intracardiac, push",
                                    "display": "Injection, intracardiac, push",
                                },
                            ],
                            "definition": "Injection, intracardiac",
                            "display": "Injection, intracardiac",
                        },
                        {
                            "code": "ICARTINJ",
                            "definition": "Injection, intracartilaginous",
                            "display": "Injection, intracartilaginous",
                        },
                        {
                            "code": "ICAUDINJ",
                            "definition": "Injection, intracaudal",
                            "display": "Injection, intracaudal",
                        },
                        {
                            "code": "ICAVINJ",
                            "definition": "Injection, intracavernous",
                            "display": "Injection, intracavernous",
                        },
                        {
                            "code": "ICAVITINJ",
                            "definition": "Injection, intracavitary",
                            "display": "Injection, intracavitary",
                        },
                        {
                            "code": "ICEREBINJ",
                            "definition": "Injection, intracerebral",
                            "display": "Injection, intracerebral",
                        },
                        {
                            "code": "ICISTERNINJ",
                            "definition": "Injection, intracisternal",
                            "display": "Injection, intracisternal",
                        },
                        {
                            "code": "ICORONINJ",
                            "concept": [
                                {
                                    "code": "ICORONINJP",
                                    "definition": "Injection, intracoronary, push",
                                    "display": "Injection, intracoronary, push",
                                }
                            ],
                            "definition": "Injection, intracoronary",
                            "display": "Injection, intracoronary",
                        },
                        {
                            "code": "ICORPCAVINJ",
                            "definition": "Injection, intracorpus cavernosum",
                            "display": "Injection, intracorpus cavernosum",
                        },
                        {
                            "code": "IDINJ",
                            "definition": "Injection, intradermal",
                            "display": "Injection, intradermal",
                        },
                        {
                            "code": "IDISCINJ",
                            "definition": "Injection, intradiscal",
                            "display": "Injection, intradiscal",
                        },
                        {
                            "code": "IDUCTINJ",
                            "definition": "Injection, intraductal",
                            "display": "Injection, intraductal",
                        },
                        {
                            "code": "IDURINJ",
                            "definition": "Injection, intradural",
                            "display": "Injection, intradural",
                        },
                        {
                            "code": "IEPIDINJ",
                            "definition": "Injection, intraepidermal",
                            "display": "Injection, intraepidermal",
                        },
                        {
                            "code": "IEPITHINJ",
                            "definition": "Injection, intraepithelial",
                            "display": "Injection, intraepithelial",
                        },
                        {
                            "code": "ILESINJ",
                            "definition": "Injection, intralesional",
                            "display": "Injection, intralesional",
                        },
                        {
                            "code": "ILUMINJ",
                            "definition": "Injection, intraluminal",
                            "display": "Injection, intraluminal",
                        },
                        {
                            "code": "ILYMPJINJ",
                            "definition": "Injection, intralymphatic",
                            "display": "Injection, intralymphatic",
                        },
                        {
                            "code": "IM",
                            "concept": [
                                {
                                    "code": "IMD",
                                    "definition": "Injection, intramuscular, deep",
                                    "display": "Injection, intramuscular, deep",
                                },
                                {
                                    "code": "IMZ",
                                    "definition": "Injection, intramuscular, z track",
                                    "display": "Injection, intramuscular, z track",
                                },
                            ],
                            "definition": "Injection, intramuscular",
                            "display": "Injection, intramuscular",
                        },
                        {
                            "code": "IMEDULINJ",
                            "definition": "Injection, intramedullary",
                            "display": "Injection, intramedullary",
                        },
                        {
                            "code": "INTERMENINJ",
                            "definition": "Injection, interameningeal",
                            "display": "Injection, interameningeal",
                        },
                        {
                            "code": "INTERSTITINJ",
                            "definition": "Injection, interstitial",
                            "display": "Injection, interstitial",
                        },
                        {
                            "code": "IOINJ",
                            "definition": "Injection, intraocular",
                            "display": "Injection, intraocular",
                        },
                        {
                            "code": "IOSSINJ",
                            "definition": "Injection, intraosseous",
                            "display": "Injection, intraosseous",
                        },
                        {
                            "code": "IOVARINJ",
                            "definition": "Injection, intraovarian",
                            "display": "Injection, intraovarian",
                        },
                        {
                            "code": "IPCARDINJ",
                            "definition": "Injection, intrapericardial",
                            "display": "Injection, intrapericardial",
                        },
                        {
                            "code": "IPERINJ",
                            "definition": "Injection, intraperitoneal",
                            "display": "Injection, intraperitoneal",
                        },
                        {
                            "code": "IPINJ",
                            "definition": "Injection, intrapulmonary",
                            "display": "Injection, intrapulmonary",
                        },
                        {
                            "code": "IPLRINJ",
                            "definition": "Injection, intrapleural",
                            "display": "Injection, intrapleural",
                        },
                        {
                            "code": "IPROSTINJ",
                            "definition": "Injection, intraprostatic",
                            "display": "Injection, intraprostatic",
                        },
                        {
                            "code": "IPUMPINJ",
                            "definition": "Injection, insulin pump",
                            "display": "Injection, insulin pump",
                        },
                        {
                            "code": "ISINJ",
                            "definition": "Injection, intraspinal",
                            "display": "Injection, intraspinal",
                        },
                        {
                            "code": "ISTERINJ",
                            "definition": "Injection, intrasternal",
                            "display": "Injection, intrasternal",
                        },
                        {
                            "code": "ISYNINJ",
                            "definition": "Injection, intrasynovial",
                            "display": "Injection, intrasynovial",
                        },
                        {
                            "code": "ITENDINJ",
                            "definition": "Injection, intratendinous",
                            "display": "Injection, intratendinous",
                        },
                        {
                            "code": "ITESTINJ",
                            "definition": "Injection, intratesticular",
                            "display": "Injection, intratesticular",
                        },
                        {
                            "code": "ITHORINJ",
                            "definition": "Injection, intrathoracic",
                            "display": "Injection, intrathoracic",
                        },
                        {
                            "code": "ITINJ",
                            "definition": "Injection, intrathecal",
                            "display": "Injection, intrathecal",
                        },
                        {
                            "code": "ITUBINJ",
                            "definition": "Injection, intratubular",
                            "display": "Injection, intratubular",
                        },
                        {
                            "code": "ITUMINJ",
                            "definition": "Injection, intratumor",
                            "display": "Injection, intratumor",
                        },
                        {
                            "code": "ITYMPINJ",
                            "definition": "Injection, intratympanic",
                            "display": "Injection, intratympanic",
                        },
                        {
                            "code": "IUINJ",
                            "definition": "Injection, intracervical (uterus)",
                            "display": "Injection, intrauterine",
                        },
                        {
                            "code": "IUINJC",
                            "definition": "Injection, intracervical (uterus)",
                            "display": "Injection, intracervical (uterus)",
                        },
                        {
                            "code": "IURETINJ",
                            "definition": "Injection, intraureteral, retrograde",
                            "display": "Injection, intraureteral, retrograde",
                        },
                        {
                            "code": "IVASCINJ",
                            "definition": "Injection, intravascular",
                            "display": "Injection, intravascular",
                        },
                        {
                            "code": "IVENTINJ",
                            "definition": "Injection, intraventricular (heart)",
                            "display": "Injection, intraventricular (heart)",
                        },
                        {
                            "code": "IVESINJ",
                            "definition": "Injection, intravesicle",
                            "display": "Injection, intravesicle",
                        },
                        {
                            "code": "IVINJ",
                            "concept": [
                                {
                                    "code": "IVINJBOL",
                                    "definition": "Injection, intravenous, bolus",
                                    "display": "Injection, intravenous, bolus",
                                },
                                {
                                    "code": "IVPUSH",
                                    "definition": "Injection, intravenous, push",
                                    "display": "Injection, intravenous, push",
                                },
                                {
                                    "code": "IVRPUSH",
                                    "definition": "Injection, intravenous, rapid push",
                                    "display": "Injection, intravenous, rapid push",
                                },
                                {
                                    "code": "IVSPUSH",
                                    "definition": "Injection, intravenous, slow push",
                                    "display": "Injection, intravenous, slow push",
                                },
                            ],
                            "definition": "Injection, intravenous",
                            "display": "Injection, intravenous",
                        },
                        {
                            "code": "IVITINJ",
                            "definition": "Injection, intravitreal",
                            "display": "Injection, intravitreal",
                        },
                        {
                            "code": "PAINJ",
                            "definition": "Injection, periarticular",
                            "display": "Injection, periarticular",
                        },
                        {
                            "code": "PARENTINJ",
                            "definition": "Injection, parenteral",
                            "display": "Injection, parenteral",
                        },
                        {
                            "code": "PDONTINJ",
                            "definition": "Injection, periodontal",
                            "display": "Injection, periodontal",
                        },
                        {
                            "code": "PDPINJ",
                            "definition": "Injection, peritoneal dialysis port",
                            "display": "Injection, peritoneal dialysis port",
                        },
                        {
                            "code": "PDURINJ",
                            "definition": "Injection, peridural",
                            "display": "Injection, peridural",
                        },
                        {
                            "code": "PNINJ",
                            "definition": "Injection, perineural",
                            "display": "Injection, perineural",
                        },
                        {
                            "code": "PNSINJ",
                            "definition": "Injection, paranasal sinuses",
                            "display": "Injection, paranasal sinuses",
                        },
                        {
                            "code": "RBINJ",
                            "definition": "Injection, retrobulbar",
                            "display": "Injection, retrobulbar",
                        },
                        {
                            "code": "SCINJ",
                            "definition": "Injection, subconjunctival",
                            "display": "Injection, subconjunctival",
                        },
                        {
                            "code": "SLESINJ",
                            "definition": "Injection, sublesional",
                            "display": "Injection, sublesional",
                        },
                        {
                            "code": "SOFTISINJ",
                            "definition": "Injection, soft tissue",
                            "display": "Injection, soft tissue",
                        },
                        {
                            "code": "SQ",
                            "definition": "Injection, subcutaneous",
                            "display": "Injection, subcutaneous",
                        },
                        {
                            "code": "SUBARACHINJ",
                            "definition": "Injection, subarachnoid",
                            "display": "Injection, subarachnoid",
                        },
                        {
                            "code": "SUBMUCINJ",
                            "definition": "Injection, submucosal",
                            "display": "Injection, submucosal",
                        },
                        {
                            "code": "TRPLACINJ",
                            "definition": "Injection, transplacental",
                            "display": "Injection, transplacental",
                        },
                        {
                            "code": "TRTRACHINJ",
                            "definition": "Injection, transtracheal",
                            "display": "Injection, transtracheal",
                        },
                        {
                            "code": "URETHINJ",
                            "definition": "Injection, urethral",
                            "display": "Injection, urethral",
                        },
                        {
                            "code": "URETINJ",
                            "definition": "Injection, ureteral",
                            "display": "Injection, ureteral",
                        },
                    ],
                    "definition": "Injection",
                    "display": "Injection",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Insertion",
                    "concept": [
                        {
                            "code": "CERVINS",
                            "definition": "Insertion, cervical (uterine)",
                            "display": "Insertion, cervical (uterine)",
                        },
                        {
                            "code": "IOSURGINS",
                            "definition": "Insertion, intraocular, surgical",
                            "display": "Insertion, intraocular, surgical",
                        },
                        {
                            "code": "IU",
                            "definition": "Insertion, intrauterine",
                            "display": "Insertion, intrauterine",
                        },
                        {
                            "code": "LPINS",
                            "definition": "Insertion, lacrimal puncta",
                            "display": "Insertion, lacrimal puncta",
                        },
                        {
                            "code": "PR",
                            "definition": "Insertion, rectal",
                            "display": "Insertion, rectal",
                        },
                        {
                            "code": "SQSURGINS",
                            "definition": "Insertion, subcutaneous, surgical",
                            "display": "Insertion, subcutaneous, surgical",
                        },
                        {
                            "code": "URETHINS",
                            "definition": "Insertion, urethral",
                            "display": "Insertion, urethral",
                        },
                        {
                            "code": "VAGINSI",
                            "definition": "Insertion, vaginal",
                            "display": "Insertion, vaginal",
                        },
                    ],
                    "definition": "Insertion",
                    "display": "Insertion",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Instillation",
                    "concept": [
                        {
                            "code": "CECINSTL",
                            "definition": "Instillation, cecostomy",
                            "display": "Instillation, cecostomy",
                        },
                        {
                            "code": "EFT",
                            "definition": "Instillation, enteral feeding tube",
                            "display": "Instillation, enteral feeding tube",
                        },
                        {
                            "code": "ENTINSTL",
                            "definition": "Instillation, enteral",
                            "display": "Instillation, enteral",
                        },
                        {
                            "code": "GT",
                            "definition": "Instillation, gastrostomy tube",
                            "display": "Instillation, gastrostomy tube",
                        },
                        {
                            "code": "NGT",
                            "definition": "Instillation, nasogastric tube",
                            "display": "Instillation, nasogastric tube",
                        },
                        {
                            "code": "OGT",
                            "definition": "Instillation, orogastric tube",
                            "display": "Instillation, orogastric tube",
                        },
                        {
                            "code": "BLADINSTL",
                            "definition": "Instillation, urinary catheter",
                            "display": "Instillation, urinary catheter",
                        },
                        {
                            "code": "CAPDINSTL",
                            "definition": "Instillation, continuous ambulatory peritoneal dialysis port",
                            "display": "Instillation, continuous ambulatory peritoneal dialysis port",
                        },
                        {
                            "code": "CTINSTL",
                            "definition": "Instillation, chest tube",
                            "display": "Instillation, chest tube",
                        },
                        {
                            "code": "ETINSTL",
                            "definition": "Instillation, endotracheal tube",
                            "display": "Instillation, endotracheal tube",
                        },
                        {
                            "code": "GJT",
                            "definition": "Instillation, gastro-jejunostomy tube",
                            "display": "Instillation, gastro-jejunostomy tube",
                        },
                        {
                            "code": "IBRONCHINSTIL",
                            "definition": "Instillation, intrabronchial",
                            "display": "Instillation, intrabronchial",
                        },
                        {
                            "code": "IDUODINSTIL",
                            "definition": "Instillation, intraduodenal",
                            "display": "Instillation, intraduodenal",
                        },
                        {
                            "code": "IESOPHINSTIL",
                            "definition": "Instillation, intraesophageal",
                            "display": "Instillation, intraesophageal",
                        },
                        {
                            "code": "IGASTINSTIL",
                            "definition": "Instillation, intragastric",
                            "display": "Instillation, intragastric",
                        },
                        {
                            "code": "IILEALINJ",
                            "definition": "Instillation, intraileal",
                            "display": "Instillation, intraileal",
                        },
                        {
                            "code": "IOINSTL",
                            "definition": "Instillation, intraocular",
                            "display": "Instillation, intraocular",
                        },
                        {
                            "code": "ISININSTIL",
                            "definition": "Instillation, intrasinal",
                            "display": "Instillation, intrasinal",
                        },
                        {
                            "code": "ITRACHINSTIL",
                            "definition": "Instillation, intratracheal",
                            "display": "Instillation, intratracheal",
                        },
                        {
                            "code": "IUINSTL",
                            "definition": "Instillation, intrauterine",
                            "display": "Instillation, intrauterine",
                        },
                        {
                            "code": "JJTINSTL",
                            "definition": "Instillation, jejunostomy tube",
                            "display": "Instillation, jejunostomy tube",
                        },
                        {
                            "code": "LARYNGINSTIL",
                            "definition": "Instillation, laryngeal",
                            "display": "Instillation, laryngeal",
                        },
                        {
                            "code": "NASALINSTIL",
                            "definition": "Instillation, nasal",
                            "display": "Instillation, nasal",
                        },
                        {
                            "code": "NASOGASINSTIL",
                            "definition": "Instillation, nasogastric",
                            "display": "Instillation, nasogastric",
                        },
                        {
                            "code": "NTT",
                            "definition": "Instillation, nasotracheal tube",
                            "display": "Instillation, nasotracheal tube",
                        },
                        {
                            "code": "OJJ",
                            "definition": "Instillation, orojejunum tube",
                            "display": "Instillation, orojejunum tube",
                        },
                        {
                            "code": "OT",
                            "definition": "Instillation, otic",
                            "display": "Instillation, otic",
                        },
                        {
                            "code": "PDPINSTL",
                            "definition": "Instillation, peritoneal dialysis port",
                            "display": "Instillation, peritoneal dialysis port",
                        },
                        {
                            "code": "PNSINSTL",
                            "definition": "Instillation, paranasal sinuses",
                            "display": "Instillation, paranasal sinuses",
                        },
                        {
                            "code": "RECINSTL",
                            "concept": [
                                {
                                    "code": "RECTINSTL",
                                    "definition": "Instillation, rectal tube",
                                    "display": "Instillation, rectal tube",
                                }
                            ],
                            "definition": "Instillation, rectal",
                            "display": "Instillation, rectal",
                        },
                        {
                            "code": "SININSTIL",
                            "definition": "Instillation, sinus, unspecified",
                            "display": "Instillation, sinus, unspecified",
                        },
                        {
                            "code": "SOFTISINSTIL",
                            "definition": "Instillation, soft tissue",
                            "display": "Instillation, soft tissue",
                        },
                        {
                            "code": "TRACHINSTL",
                            "definition": "Instillation, tracheostomy",
                            "display": "Instillation, tracheostomy",
                        },
                        {
                            "code": "TRTYMPINSTIL",
                            "definition": "Instillation, transtympanic",
                            "display": "Instillation, transtympanic",
                        },
                        {
                            "code": "URETHINSTL",
                            "definition": "Instillation, urethral",
                            "display": "instillation, urethral",
                        },
                    ],
                    "definition": "Instillation",
                    "display": "Instillation",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_IontophoresisRoute",
                    "concept": [
                        {
                            "code": "IONTO",
                            "definition": "Topical application, iontophoresis",
                            "display": "Topical application, iontophoresis",
                        }
                    ],
                    "definition": "Iontophoresis",
                    "display": "IontophoresisRoute",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Irrigation",
                    "concept": [
                        {
                            "code": "GUIRR",
                            "definition": "Irrigation, genitourinary",
                            "display": "Irrigation, genitourinary",
                        },
                        {
                            "code": "IGASTIRR",
                            "definition": "Irrigation, intragastric",
                            "display": "Irrigation, intragastric",
                        },
                        {
                            "code": "ILESIRR",
                            "definition": "Irrigation, intralesional",
                            "display": "Irrigation, intralesional",
                        },
                        {
                            "code": "IOIRR",
                            "definition": "Irrigation, intraocular",
                            "display": "Irrigation, intraocular",
                        },
                        {
                            "code": "BLADIRR",
                            "concept": [
                                {
                                    "code": "BLADIRRC",
                                    "definition": "Irrigation, urinary bladder, continuous",
                                    "display": "Irrigation, urinary bladder, continuous",
                                },
                                {
                                    "code": "BLADIRRT",
                                    "definition": "Irrigation, urinary bladder, tidal",
                                    "display": "Irrigation, urinary bladder, tidal",
                                },
                            ],
                            "definition": "Irrigation, urinary bladder",
                            "display": "Irrigation, urinary bladder",
                        },
                        {
                            "code": "RECIRR",
                            "definition": "Irrigation, rectal",
                            "display": "Irrigation, rectal",
                        },
                    ],
                    "definition": "Irrigation",
                    "display": "Irrigation",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_LavageRoute",
                    "concept": [
                        {
                            "code": "IGASTLAV",
                            "definition": "Lavage, intragastric",
                            "display": "Lavage, intragastric",
                        }
                    ],
                    "definition": "Lavage",
                    "display": "LavageRoute",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_MucosalAbsorptionRoute",
                    "concept": [
                        {
                            "code": "IDOUDMAB",
                            "definition": "Mucosal absorption, intraduodenal",
                            "display": "Mucosal absorption, intraduodenal",
                        },
                        {
                            "code": "ITRACHMAB",
                            "definition": "Mucosal absorption, intratracheal",
                            "display": "Mucosal absorption, intratracheal",
                        },
                        {
                            "code": "SMUCMAB",
                            "definition": "Mucosal absorption, submucosal",
                            "display": "Mucosal absorption, submucosal",
                        },
                    ],
                    "definition": "Mucosal absorption",
                    "display": "MucosalAbsorptionRoute",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Nebulization",
                    "concept": [
                        {
                            "code": "ETNEB",
                            "definition": "Nebulization, endotracheal tube",
                            "display": "Nebulization, endotracheal tube",
                        }
                    ],
                    "definition": "Nebulization",
                    "display": "Nebulization",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Rinse",
                    "concept": [
                        {
                            "code": "DENRINSE",
                            "definition": "Rinse, dental",
                            "display": "Rinse, dental",
                        },
                        {
                            "code": "ORRINSE",
                            "definition": "Rinse, oral",
                            "display": "Rinse, oral",
                        },
                    ],
                    "definition": "Rinse",
                    "display": "Rinse",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_SuppositoryRoute",
                    "concept": [
                        {
                            "code": "URETHSUP",
                            "definition": "Suppository, urethral",
                            "display": "Suppository, urethral",
                        }
                    ],
                    "definition": "Suppository",
                    "display": "SuppositoryRoute",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Swish",
                    "concept": [
                        {
                            "code": "SWISHSPIT",
                            "definition": "Swish and spit out, oromucosal",
                            "display": "Swish and spit out, oromucosal",
                        },
                        {
                            "code": "SWISHSWAL",
                            "definition": "Swish and swallow, oromucosal",
                            "display": "Swish and swallow, oromucosal",
                        },
                    ],
                    "definition": "Swish",
                    "display": "Swish",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_TopicalAbsorptionRoute",
                    "concept": [
                        {
                            "code": "TTYMPTABSORP",
                            "definition": "Topical absorption, transtympanic",
                            "display": "Topical absorption, transtympanic",
                        }
                    ],
                    "definition": "Topical absorption",
                    "display": "TopicalAbsorptionRoute",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_TopicalApplication",
                    "concept": [
                        {
                            "code": "DRESS",
                            "definition": "Topical application, soaked dressing",
                            "display": "Topical application, soaked dressing",
                        },
                        {
                            "code": "SWAB",
                            "definition": "Topical application, swab",
                            "display": "Topical application, swab",
                        },
                        {
                            "code": "TOPICAL",
                            "definition": "Topical",
                            "display": "Topical",
                        },
                        {
                            "code": "BUC",
                            "definition": "Topical application, buccal",
                            "display": "Topical application, buccal",
                        },
                        {
                            "code": "CERV",
                            "definition": "Topical application, cervical",
                            "display": "Topical application, cervical",
                        },
                        {
                            "code": "DEN",
                            "definition": "Topical application, dental",
                            "display": "Topical application, dental",
                        },
                        {
                            "code": "GIN",
                            "definition": "Topical application, gingival",
                            "display": "Topical application, gingival",
                        },
                        {
                            "code": "HAIR",
                            "definition": "Topical application, hair",
                            "display": "Topical application, hair",
                        },
                        {
                            "code": "ICORNTA",
                            "definition": "Topical application, intracorneal",
                            "display": "Topical application, intracorneal",
                        },
                        {
                            "code": "ICORONTA",
                            "definition": "Topical application, intracoronal (dental)",
                            "display": "Topical application, intracoronal (dental)",
                        },
                        {
                            "code": "IESOPHTA",
                            "definition": "Topical application, intraesophageal",
                            "display": "Topical application, intraesophageal",
                        },
                        {
                            "code": "IILEALTA",
                            "definition": "Topical application, intraileal",
                            "display": "Topical application, intraileal",
                        },
                        {
                            "code": "ILTOP",
                            "definition": "Topical application, intralesional",
                            "display": "Topical application, intralesional",
                        },
                        {
                            "code": "ILUMTA",
                            "definition": "Topical application, intraluminal",
                            "display": "Topical application, intraluminal",
                        },
                        {
                            "code": "IOTOP",
                            "definition": "Topical application, intraocular",
                            "display": "Topical application, intraocular",
                        },
                        {
                            "code": "LARYNGTA",
                            "definition": "Topical application, laryngeal",
                            "display": "Topical application, laryngeal",
                        },
                        {
                            "code": "MUC",
                            "definition": "Topical application, mucous membrane",
                            "display": "Topical application, mucous membrane",
                        },
                        {
                            "code": "NAIL",
                            "definition": "Topical application, nail",
                            "display": "Topical application, nail",
                        },
                        {
                            "code": "NASAL",
                            "definition": "Topical application, nasal",
                            "display": "Topical application, nasal",
                        },
                        {
                            "code": "OPTHALTA",
                            "definition": "Topical application, ophthalmic",
                            "display": "Topical application, ophthalmic",
                        },
                        {
                            "code": "ORALTA",
                            "definition": "Topical application, oral",
                            "display": "Topical application, oral",
                        },
                        {
                            "code": "ORMUC",
                            "definition": "Topical application, oromucosal",
                            "display": "Topical application, oromucosal",
                        },
                        {
                            "code": "OROPHARTA",
                            "definition": "Topical application, oropharyngeal",
                            "display": "Topical application, oropharyngeal",
                        },
                        {
                            "code": "PERIANAL",
                            "definition": "Topical application, perianal",
                            "display": "Topical application, perianal",
                        },
                        {
                            "code": "PERINEAL",
                            "definition": "Topical application, perineal",
                            "display": "Topical application, perineal",
                        },
                        {
                            "code": "PDONTTA",
                            "definition": "Topical application, periodontal",
                            "display": "Topical application, periodontal",
                        },
                        {
                            "code": "RECTAL",
                            "definition": "Topical application, rectal",
                            "display": "Topical application, rectal",
                        },
                        {
                            "code": "SCALP",
                            "definition": "Topical application, scalp",
                            "display": "Topical application, scalp",
                        },
                        {
                            "code": "OCDRESTA",
                            "definition": "Occlusive dressing technique",
                            "display": "Occlusive dressing technique",
                        },
                        {
                            "code": "SKIN",
                            "definition": "Topical application, skin",
                            "display": "Topical application, skin",
                        },
                        {
                            "code": "SUBCONJTA",
                            "definition": "Subconjunctival",
                            "display": "Subconjunctival",
                        },
                        {
                            "code": "TMUCTA",
                            "definition": "Topical application, transmucosal",
                            "display": "Topical application, transmucosal",
                        },
                        {
                            "code": "VAGINS",
                            "definition": "Insertion, vaginal",
                            "display": "Topical application, vaginal",
                        },
                    ],
                    "definition": "Topical application",
                    "display": "TopicalApplication",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IONTO"},
                    ],
                },
                {
                    "code": "INSUF",
                    "definition": "Insufflation",
                    "display": "Insufflation",
                },
                {
                    "code": "TRNSDERM",
                    "definition": "Transdermal",
                    "display": "Transdermal",
                    "property": [{"code": "child", "valueCode": "TRNSDERMD"}],
                },
            ],
            "definition": "Route of substance administration classified by administration method.",
            "display": "RouteByMethod",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    RouteByMethod

    Route of substance administration classified by administration method.
    """

    underscore_route_by_site = CodeSystemConcept(
        {
            "code": "_RouteBySite",
            "concept": [
                {
                    "code": "_AmnioticFluidSacRoute",
                    "definition": "Amniotic fluid sac",
                    "display": "AmnioticFluidSacRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "AMNINJ"},
                    ],
                },
                {
                    "code": "_BiliaryRoute",
                    "definition": "Biliary tract",
                    "display": "BiliaryRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "BILINJ"},
                        {"code": "child", "valueCode": "CHOLINJ"},
                    ],
                },
                {
                    "code": "_BodySurfaceRoute",
                    "definition": "Body surface",
                    "display": "BodySurfaceRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "DRESS"},
                        {"code": "child", "valueCode": "ELECTOSMOS"},
                        {"code": "child", "valueCode": "IONTO"},
                        {"code": "child", "valueCode": "SOAK"},
                        {"code": "child", "valueCode": "SWAB"},
                        {"code": "child", "valueCode": "TOPICAL"},
                    ],
                },
                {
                    "code": "_BuccalMucosaRoute",
                    "definition": "Buccal mucosa",
                    "display": "BuccalMucosaRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "BUC"},
                    ],
                },
                {
                    "code": "_CecostomyRoute",
                    "definition": "Cecostomy",
                    "display": "CecostomyRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "CECINSTL"},
                    ],
                },
                {
                    "code": "_CervicalRoute",
                    "definition": "Cervix of the uterus",
                    "display": "CervicalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "CERV"},
                        {"code": "child", "valueCode": "CERVINJ"},
                        {"code": "child", "valueCode": "CERVINS"},
                        {"code": "child", "valueCode": "DEN"},
                        {"code": "child", "valueCode": "DENRINSE"},
                    ],
                },
                {
                    "code": "_EndocervicalRoute",
                    "definition": "Endocervical",
                    "display": "EndocervicalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "AMNINJ"},
                        {"code": "child", "valueCode": "BILINJ"},
                    ],
                },
                {
                    "code": "_EnteralRoute",
                    "definition": "Enteral",
                    "display": "EnteralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "EFT"},
                        {"code": "child", "valueCode": "ENTINSTL"},
                    ],
                },
                {
                    "code": "_EpiduralRoute",
                    "definition": "Epidural",
                    "display": "EpiduralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "EPI"},
                        {"code": "child", "valueCode": "EPIDURINJ"},
                        {"code": "child", "valueCode": "EPIINJ"},
                        {"code": "child", "valueCode": "EPINJSP"},
                    ],
                },
                {
                    "code": "_ExtraAmnioticRoute",
                    "definition": "Extra-amniotic",
                    "display": "ExtraAmnioticRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "EXTRAMNINJ"},
                    ],
                },
                {
                    "code": "_ExtracorporealCirculationRoute",
                    "definition": "Extracorporeal circulation",
                    "display": "ExtracorporealCirculationRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "EXTCORPDIF"},
                        {"code": "child", "valueCode": "EXTCORPINJ"},
                    ],
                },
                {
                    "code": "_GastricRoute",
                    "definition": "Gastric",
                    "display": "GastricRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "GBINJ"},
                        {"code": "child", "valueCode": "GT"},
                        {"code": "child", "valueCode": "NGT"},
                        {"code": "child", "valueCode": "OGT"},
                    ],
                },
                {
                    "code": "_GenitourinaryRoute",
                    "definition": "Genitourinary",
                    "display": "GenitourinaryRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "GUIRR"},
                    ],
                },
                {
                    "code": "_GingivalRoute",
                    "definition": "Gingival",
                    "display": "GingivalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "GIN"},
                        {"code": "child", "valueCode": "GINGINJ"},
                    ],
                },
                {
                    "code": "_HairRoute",
                    "definition": "Hair",
                    "display": "HairRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "HAIR"},
                        {"code": "child", "valueCode": "SHAMPOO"},
                    ],
                },
                {
                    "code": "_InterameningealRoute",
                    "definition": "Interameningeal",
                    "display": "InterameningealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "INTERMENINJ"},
                    ],
                },
                {
                    "code": "_InterstitialRoute",
                    "definition": "Interstitial",
                    "display": "InterstitialRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "INTERSTITINJ"},
                    ],
                },
                {
                    "code": "_IntraabdominalRoute",
                    "definition": "Intra-abdominal",
                    "display": "IntraabdominalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IABDINJ"},
                    ],
                },
                {
                    "code": "_IntraarterialRoute",
                    "definition": "Intra-arterial",
                    "display": "IntraarterialRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IA"},
                        {"code": "child", "valueCode": "IAINJ"},
                    ],
                },
                {
                    "code": "_IntraarticularRoute",
                    "definition": "Intraarticular",
                    "display": "IntraarticularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IARTINJ"},
                    ],
                },
                {
                    "code": "_IntrabronchialRoute",
                    "definition": "Intrabronchial",
                    "display": "IntrabronchialRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IBRONCHINSTIL"},
                    ],
                },
                {
                    "code": "_IntrabursalRoute",
                    "definition": "Intrabursal",
                    "display": "IntrabursalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IBURSINJ"},
                    ],
                },
                {
                    "code": "_IntracardiacRoute",
                    "definition": "Intracardiac",
                    "display": "IntracardiacRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IC"},
                        {"code": "child", "valueCode": "ICARDINJ"},
                    ],
                },
                {
                    "code": "_IntracartilaginousRoute",
                    "definition": "Intracartilaginous",
                    "display": "IntracartilaginousRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICARTINJ"},
                    ],
                },
                {
                    "code": "_IntracaudalRoute",
                    "definition": "Intracaudal",
                    "display": "IntracaudalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICAUDINJ"},
                    ],
                },
                {
                    "code": "_IntracavernosalRoute",
                    "definition": "Intracavernosal",
                    "display": "IntracavernosalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICAVINJ"},
                    ],
                },
                {
                    "code": "_IntracavitaryRoute",
                    "definition": "Intracavitary",
                    "display": "IntracavitaryRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICAVITINJ"},
                    ],
                },
                {
                    "code": "_IntracerebralRoute",
                    "definition": "Intracerebral",
                    "display": "IntracerebralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICEREBINJ"},
                    ],
                },
                {
                    "code": "_IntracervicalRoute",
                    "definition": "Intracervical",
                    "display": "IntracervicalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IUINJC"},
                    ],
                },
                {
                    "code": "_IntracisternalRoute",
                    "definition": "Intracisternal",
                    "display": "IntracisternalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICISTERNINJ"},
                    ],
                },
                {
                    "code": "_IntracornealRoute",
                    "definition": "Intracorneal",
                    "display": "IntracornealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICORNTA"},
                    ],
                },
                {
                    "code": "_IntracoronalRoute",
                    "definition": "Intracoronal (dental)",
                    "display": "IntracoronalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICORONTA"},
                    ],
                },
                {
                    "code": "_IntracoronaryRoute",
                    "definition": "Intracoronary",
                    "display": "IntracoronaryRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICOR"},
                        {"code": "child", "valueCode": "ICORONINJ"},
                    ],
                },
                {
                    "code": "_IntracorpusCavernosumRoute",
                    "definition": "Intracorpus cavernosum",
                    "display": "IntracorpusCavernosumRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ICORPCAVINJ"},
                    ],
                },
                {
                    "code": "_IntradermalRoute",
                    "definition": "Intradermal",
                    "display": "IntradermalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IDIMPLNT"},
                        {"code": "child", "valueCode": "IDINJ"},
                    ],
                },
                {
                    "code": "_IntradiscalRoute",
                    "definition": "Intradiscal",
                    "display": "IntradiscalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IDISCINJ"},
                    ],
                },
                {
                    "code": "_IntraductalRoute",
                    "definition": "Intraductal",
                    "display": "IntraductalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IDUCTINJ"},
                    ],
                },
                {
                    "code": "_IntraduodenalRoute",
                    "definition": "Intraduodenal",
                    "display": "IntraduodenalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IDUODINSTIL"},
                        {"code": "child", "valueCode": "IDOUDMAB"},
                    ],
                },
                {
                    "code": "_IntraduralRoute",
                    "definition": "Intradural",
                    "display": "IntraduralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IDURINJ"},
                    ],
                },
                {
                    "code": "_IntraepidermalRoute",
                    "definition": "Intraepidermal",
                    "display": "IntraepidermalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IEPIDINJ"},
                    ],
                },
                {
                    "code": "_IntraepithelialRoute",
                    "definition": "Intraepithelial",
                    "display": "IntraepithelialRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IEPITHINJ"},
                    ],
                },
                {
                    "code": "_IntraesophagealRoute",
                    "definition": "Intraesophageal",
                    "display": "IntraesophagealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IESOPHINSTIL"},
                        {"code": "child", "valueCode": "IESOPHTA"},
                    ],
                },
                {
                    "code": "_IntragastricRoute",
                    "definition": "Intragastric",
                    "display": "IntragastricRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IGASTINSTIL"},
                        {"code": "child", "valueCode": "IGASTIRR"},
                        {"code": "child", "valueCode": "IGASTLAV"},
                    ],
                },
                {
                    "code": "_IntrailealRoute",
                    "definition": "Intraileal",
                    "display": "IntrailealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IILEALINJ"},
                        {"code": "child", "valueCode": "IILEALTA"},
                    ],
                },
                {
                    "code": "_IntralesionalRoute",
                    "definition": "Intralesional",
                    "display": "IntralesionalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ILESINJ"},
                        {"code": "child", "valueCode": "ILESIRR"},
                        {"code": "child", "valueCode": "ILTOP"},
                    ],
                },
                {
                    "code": "_IntraluminalRoute",
                    "definition": "Intraluminal",
                    "display": "IntraluminalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ILUMINJ"},
                        {"code": "child", "valueCode": "ILUMTA"},
                    ],
                },
                {
                    "code": "_IntralymphaticRoute",
                    "definition": "Intralymphatic",
                    "display": "IntralymphaticRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ILYMPJINJ"},
                    ],
                },
                {
                    "code": "_IntramedullaryRoute",
                    "definition": "Intramedullary",
                    "display": "IntramedullaryRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IMEDULINJ"},
                    ],
                },
                {
                    "code": "_IntramuscularRoute",
                    "definition": "Intramuscular",
                    "display": "IntramuscularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IM"},
                    ],
                },
                {
                    "code": "_IntraocularRoute",
                    "definition": "Intraocular",
                    "display": "IntraocularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IOINJ"},
                        {"code": "child", "valueCode": "IOSURGINS"},
                        {"code": "child", "valueCode": "IOINSTL"},
                        {"code": "child", "valueCode": "IOIRR"},
                        {"code": "child", "valueCode": "IOTOP"},
                    ],
                },
                {
                    "code": "_IntraosseousRoute",
                    "definition": "Intraosseous",
                    "display": "IntraosseousRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IOSSC"},
                        {"code": "child", "valueCode": "IOSSINJ"},
                    ],
                },
                {
                    "code": "_IntraovarianRoute",
                    "definition": "Intraovarian",
                    "display": "IntraovarianRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IOVARINJ"},
                    ],
                },
                {
                    "code": "_IntrapericardialRoute",
                    "definition": "Intrapericardial",
                    "display": "IntrapericardialRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IPCARDINJ"},
                    ],
                },
                {
                    "code": "_IntraperitonealRoute",
                    "definition": "Intraperitoneal",
                    "display": "IntraperitonealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IPERINJ"},
                        {"code": "child", "valueCode": "PDPINJ"},
                        {"code": "child", "valueCode": "CAPDINSTL"},
                        {"code": "child", "valueCode": "PDPINSTL"},
                    ],
                },
                {
                    "code": "_IntrapleuralRoute",
                    "definition": "Intrapleural",
                    "display": "IntrapleuralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IPLRINJ"},
                        {"code": "child", "valueCode": "CTINSTL"},
                    ],
                },
                {
                    "code": "_IntraprostaticRoute",
                    "definition": "Intraprostatic",
                    "display": "IntraprostaticRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IPROSTINJ"},
                    ],
                },
                {
                    "code": "_IntrapulmonaryRoute",
                    "definition": "Intrapulmonary",
                    "display": "IntrapulmonaryRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "EXTCORPINJ"},
                        {"code": "child", "valueCode": "IPINJ"},
                    ],
                },
                {
                    "code": "_IntrasinalRoute",
                    "definition": "Intrasinal",
                    "display": "IntrasinalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ISININSTIL"},
                    ],
                },
                {
                    "code": "_IntraspinalRoute",
                    "definition": "Intraspinal",
                    "display": "IntraspinalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ISINJ"},
                    ],
                },
                {
                    "code": "_IntrasternalRoute",
                    "definition": "Intrasternal",
                    "display": "IntrasternalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ISTERINJ"},
                    ],
                },
                {
                    "code": "_IntrasynovialRoute",
                    "definition": "Intrasynovial",
                    "display": "IntrasynovialRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ISYNINJ"},
                    ],
                },
                {
                    "code": "_IntratendinousRoute",
                    "definition": "Intratendinous",
                    "display": "IntratendinousRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ITENDINJ"},
                    ],
                },
                {
                    "code": "_IntratesticularRoute",
                    "definition": "Intratesticular",
                    "display": "IntratesticularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ITESTINJ"},
                    ],
                },
                {
                    "code": "_IntrathecalRoute",
                    "definition": "Intrathecal",
                    "display": "IntrathecalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IT"},
                        {"code": "child", "valueCode": "ITINJ"},
                    ],
                },
                {
                    "code": "_IntrathoracicRoute",
                    "definition": "Intrathoracic",
                    "display": "IntrathoracicRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ITHORINJ"},
                    ],
                },
                {
                    "code": "_IntratrachealRoute",
                    "definition": "Intratracheal",
                    "display": "IntratrachealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ITRACHINSTIL"},
                        {"code": "child", "valueCode": "ITRACHMAB"},
                    ],
                },
                {
                    "code": "_IntratubularRoute",
                    "definition": "Intratubular",
                    "display": "IntratubularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ITUBINJ"},
                    ],
                },
                {
                    "code": "_IntratumorRoute",
                    "definition": "Intratumor",
                    "display": "IntratumorRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ITUMINJ"},
                    ],
                },
                {
                    "code": "_IntratympanicRoute",
                    "definition": "Intratympanic",
                    "display": "IntratympanicRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ITYMPINJ"},
                    ],
                },
                {
                    "code": "_IntrauterineRoute",
                    "definition": "Intrauterine",
                    "display": "IntrauterineRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IUINJ"},
                        {"code": "child", "valueCode": "IURETINJ"},
                        {"code": "child", "valueCode": "IU"},
                        {"code": "child", "valueCode": "IUINSTL"},
                    ],
                },
                {
                    "code": "_IntravascularRoute",
                    "definition": "Intravascular",
                    "display": "IntravascularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "HEMODIFF"},
                        {"code": "child", "valueCode": "IVASCINFUS"},
                        {"code": "child", "valueCode": "HEMOPORT"},
                        {"code": "child", "valueCode": "IVASCINJ"},
                    ],
                },
                {
                    "code": "_IntravenousRoute",
                    "definition": "Intravenous",
                    "display": "IntravenousRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IVFLUSH"},
                        {"code": "child", "valueCode": "IVINJ"},
                    ],
                },
                {
                    "code": "_IntraventricularRoute",
                    "definition": "Intraventricular",
                    "display": "IntraventricularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IVENTINJ"},
                    ],
                },
                {
                    "code": "_IntravesicleRoute",
                    "definition": "Intravesicle",
                    "display": "IntravesicleRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IVESINJ"},
                    ],
                },
                {
                    "code": "_IntravitrealRoute",
                    "definition": "Intravitreal",
                    "display": "IntravitrealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IVITINJ"},
                    ],
                },
                {
                    "code": "_JejunumRoute",
                    "definition": "Jejunum",
                    "display": "JejunumRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "GJT"},
                        {"code": "child", "valueCode": "JJTINSTL"},
                        {"code": "child", "valueCode": "OJJ"},
                    ],
                },
                {
                    "code": "_LacrimalPunctaRoute",
                    "definition": "Lacrimal puncta",
                    "display": "LacrimalPunctaRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "LPINS"},
                    ],
                },
                {
                    "code": "_LaryngealRoute",
                    "definition": "Laryngeal",
                    "display": "LaryngealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "LARYNGINSTIL"},
                        {"code": "child", "valueCode": "LARYNGTA"},
                    ],
                },
                {
                    "code": "_LingualRoute",
                    "definition": "Lingual",
                    "display": "LingualRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "TRNSLING"},
                    ],
                },
                {
                    "code": "_MucousMembraneRoute",
                    "definition": "Mucous membrane",
                    "display": "MucousMembraneRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "MUC"},
                    ],
                },
                {
                    "code": "_NailRoute",
                    "definition": "Nail",
                    "display": "NailRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "NAIL"},
                    ],
                },
                {
                    "code": "_NasalRoute",
                    "definition": "Nasal",
                    "display": "NasalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "NASINHL"},
                        {"code": "child", "valueCode": "NASALINSTIL"},
                        {"code": "child", "valueCode": "NASOGASINSTIL"},
                        {"code": "child", "valueCode": "NASAL"},
                    ],
                },
                {
                    "code": "_OphthalmicRoute",
                    "definition": "Ophthalmic",
                    "display": "OphthalmicRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "OPTHALTA"},
                    ],
                },
                {
                    "code": "_OralRoute",
                    "definition": "Oral",
                    "display": "OralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "CHEW"},
                        {"code": "child", "valueCode": "DISSOLVE"},
                        {"code": "child", "valueCode": "IPINHL"},
                        {"code": "child", "valueCode": "ORALTA"},
                        {"code": "child", "valueCode": "ORRINSE"},
                        {"code": "child", "valueCode": "PO"},
                    ],
                },
                {
                    "code": "_OromucosalRoute",
                    "definition": "Oromucosal",
                    "display": "OromucosalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "GARGLE"},
                        {"code": "child", "valueCode": "ORMUC"},
                        {"code": "child", "valueCode": "SUCK"},
                        {"code": "child", "valueCode": "SWISHSPIT"},
                        {"code": "child", "valueCode": "SWISHSWAL"},
                    ],
                },
                {
                    "code": "_OropharyngealRoute",
                    "definition": "Oropharyngeal",
                    "display": "OropharyngealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "OROPHARTA"},
                    ],
                },
                {
                    "code": "_OticRoute",
                    "definition": "Otic",
                    "display": "OticRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "OT"},
                    ],
                },
                {
                    "code": "_ParanasalSinusesRoute",
                    "definition": "Paranasal sinuses",
                    "display": "ParanasalSinusesRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PNSINJ"},
                        {"code": "child", "valueCode": "PNSINSTL"},
                    ],
                },
                {
                    "code": "_ParenteralRoute",
                    "definition": "Parenteral",
                    "display": "ParenteralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PARENTINJ"},
                    ],
                },
                {
                    "code": "_PerianalRoute",
                    "definition": "Perianal",
                    "display": "PerianalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PERIANAL"},
                    ],
                },
                {
                    "code": "_PeriarticularRoute",
                    "definition": "Periarticular",
                    "display": "PeriarticularRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PAINJ"},
                    ],
                },
                {
                    "code": "_PeriduralRoute",
                    "definition": "Peridural",
                    "display": "PeriduralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PDURINJ"},
                    ],
                },
                {
                    "code": "_PerinealRoute",
                    "definition": "Perineal",
                    "display": "PerinealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PERINEAL"},
                    ],
                },
                {
                    "code": "_PerineuralRoute",
                    "definition": "Perineural",
                    "display": "PerineuralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PNINJ"},
                    ],
                },
                {
                    "code": "_PeriodontalRoute",
                    "definition": "Periodontal",
                    "display": "PeriodontalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "PDONTINJ"},
                        {"code": "child", "valueCode": "PDONTTA"},
                    ],
                },
                {
                    "code": "_PulmonaryRoute",
                    "definition": "Pulmonary",
                    "display": "PulmonaryRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IPPB"},
                        {"code": "child", "valueCode": "VENT"},
                        {"code": "child", "valueCode": "VENTMASK"},
                        {"code": "child", "valueCode": "ETINSTL"},
                        {"code": "child", "valueCode": "NTT"},
                        {"code": "child", "valueCode": "ETNEB"},
                    ],
                },
                {
                    "code": "_RectalRoute",
                    "definition": "Rectal",
                    "display": "RectalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ENEMA"},
                        {"code": "child", "valueCode": "RETENEMA"},
                        {"code": "child", "valueCode": "PR"},
                        {"code": "child", "valueCode": "RECINSTL"},
                        {"code": "child", "valueCode": "RECIRR"},
                        {"code": "child", "valueCode": "RECTAL"},
                    ],
                },
                {
                    "code": "_RespiratoryTractRoute",
                    "definition": "Respiratory tract",
                    "display": "RespiratoryTractRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IPINHL"},
                    ],
                },
                {
                    "code": "_RetrobulbarRoute",
                    "definition": "Retrobulbar",
                    "display": "RetrobulbarRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "RBINJ"},
                    ],
                },
                {
                    "code": "_ScalpRoute",
                    "definition": "Scalp",
                    "display": "ScalpRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SCALP"},
                    ],
                },
                {
                    "code": "_SinusUnspecifiedRoute",
                    "definition": "Sinus, unspecified",
                    "display": "SinusUnspecifiedRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "ENDOSININJ"},
                        {"code": "child", "valueCode": "SININSTIL"},
                    ],
                },
                {
                    "code": "_SkinRoute",
                    "definition": "Skin",
                    "display": "SkinRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "OCDRESTA"},
                        {"code": "child", "valueCode": "SKIN"},
                    ],
                },
                {
                    "code": "_SoftTissueRoute",
                    "definition": "Soft tissue",
                    "display": "SoftTissueRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SOFTISINJ"},
                        {"code": "child", "valueCode": "SOFTISINSTIL"},
                    ],
                },
                {
                    "code": "_SubarachnoidRoute",
                    "definition": "Subarachnoid",
                    "display": "SubarachnoidRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SUBARACHINJ"},
                    ],
                },
                {
                    "code": "_SubconjunctivalRoute",
                    "definition": "Subconjunctival",
                    "display": "SubconjunctivalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SCINJ"},
                        {"code": "child", "valueCode": "SUBCONJTA"},
                    ],
                },
                {
                    "code": "_SubcutaneousRoute",
                    "definition": "Subcutaneous",
                    "display": "SubcutaneousRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SQIMPLNT"},
                        {"code": "child", "valueCode": "SQINFUS"},
                        {"code": "child", "valueCode": "IPUMPINJ"},
                        {"code": "child", "valueCode": "SQ"},
                        {"code": "child", "valueCode": "SQSURGINS"},
                    ],
                },
                {
                    "code": "_SublesionalRoute",
                    "definition": "Sublesional",
                    "display": "SublesionalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SLESINJ"},
                    ],
                },
                {
                    "code": "_SublingualRoute",
                    "definition": "Sublingual",
                    "display": "SublingualRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SL"},
                    ],
                },
                {
                    "code": "_SubmucosalRoute",
                    "definition": "Submucosal",
                    "display": "SubmucosalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "SUBMUCINJ"},
                        {"code": "child", "valueCode": "SMUCMAB"},
                    ],
                },
                {
                    "code": "_TracheostomyRoute",
                    "definition": "Tracheostomy",
                    "display": "TracheostomyRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "TRACH"},
                        {"code": "child", "valueCode": "TRACHINSTL"},
                    ],
                },
                {
                    "code": "_TransmucosalRoute",
                    "definition": "Transmucosal",
                    "display": "TransmucosalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "TMUCTA"},
                    ],
                },
                {
                    "code": "_TransplacentalRoute",
                    "definition": "Transplacental",
                    "display": "TransplacentalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "TRPLACINJ"},
                    ],
                },
                {
                    "code": "_TranstrachealRoute",
                    "definition": "Transtracheal",
                    "display": "TranstrachealRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "TRTRACHINJ"},
                    ],
                },
                {
                    "code": "_TranstympanicRoute",
                    "definition": "Transtympanic",
                    "display": "TranstympanicRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "TRTYMPINSTIL"},
                        {"code": "child", "valueCode": "TTYMPTABSORP"},
                    ],
                },
                {
                    "code": "_UreteralRoute",
                    "definition": "Ureteral",
                    "display": "UreteralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "URETINJ"},
                    ],
                },
                {
                    "code": "_UrethralRoute",
                    "definition": "Urethral",
                    "display": "UrethralRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "URETHINJ"},
                        {"code": "child", "valueCode": "URETHINS"},
                        {"code": "child", "valueCode": "URETHINSTL"},
                        {"code": "child", "valueCode": "URETHSUP"},
                    ],
                },
                {
                    "code": "_UrinaryBladderRoute",
                    "definition": "Urinary bladder",
                    "display": "UrinaryBladderRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "BLADINJ"},
                        {"code": "child", "valueCode": "BLADIRR"},
                    ],
                },
                {
                    "code": "_UrinaryTractRoute",
                    "definition": "Urinary tract",
                    "display": "UrinaryTractRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "BLADINSTL"},
                    ],
                },
                {
                    "code": "_VaginalRoute",
                    "definition": "Vaginal",
                    "display": "VaginalRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "DOUCHE"},
                        {"code": "child", "valueCode": "VAGINSI"},
                        {"code": "child", "valueCode": "VAGINS"},
                    ],
                },
                {
                    "code": "_VitreousHumourRoute",
                    "definition": "Vitreous humour",
                    "display": "VitreousHumourRoute",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "child", "valueCode": "IVITIMPLNT"},
                    ],
                },
            ],
            "definition": "Route of substance administration classified by site.",
            "display": "RouteBySite",
            "property": [
                {"code": "notSelectable", "valueBoolean": True},
                {"code": "child", "valueCode": "TRNSDERM"},
            ],
        }
    )
    """
    RouteBySite

    Route of substance administration classified by site.
    """

    class Meta:
        resource = _resource
