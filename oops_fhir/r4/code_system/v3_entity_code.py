from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3EntityCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityCode:
    """
    v3 Code System EntityCode

      OpenIssue:  Missing description.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-EntityCode
    """

    underscore_material_entity_class_type = CodeSystemConcept(
        {
            "code": "_MaterialEntityClassType",
            "concept": [
                {
                    "code": "_ContainerEntityType",
                    "concept": [
                        {
                            "code": "PKG",
                            "concept": [
                                {
                                    "code": "_NonRigidContainerEntityType",
                                    "concept": [
                                        {
                                            "code": "BAG",
                                            "definition": "A pouched or pendulous container.",
                                            "display": "Bag",
                                        },
                                        {
                                            "code": "PACKT",
                                            "definition": "A paper",
                                            "display": "Packet",
                                        },
                                        {
                                            "code": "PCH",
                                            "definition": "A small bag or container made of a soft material.",
                                            "display": "Pouch",
                                        },
                                        {
                                            "code": "SACH",
                                            "definition": "A small bag or packet containing a small portion of a substance.",
                                            "display": "Sachet",
                                        },
                                    ],
                                    "definition": "A container having dimensions that adjust somewhat based on the amount and shape of the material placed within it.",
                                    "display": "NonRigidContainerEntityType",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_RigidContainerEntityType",
                                    "concept": [
                                        {
                                            "code": "_IndividualPackageEntityType",
                                            "concept": [
                                                {
                                                    "code": "AMP",
                                                    "definition": "A small sealed glass container that holds a measured amount of a medicinal substance.",
                                                    "display": "Ampule",
                                                },
                                                {
                                                    "code": "MINIM",
                                                    "definition": "Individually dosed ophthalmic solution.  One time eye dropper dispenser.",
                                                    "display": "Minim",
                                                },
                                                {
                                                    "code": "NEBAMP",
                                                    "definition": "Individually dosed inhalation solution.",
                                                    "display": "Nebuamp",
                                                },
                                                {
                                                    "code": "OVUL",
                                                    "definition": "A container either glass or plastic and a narrow neck, for storing liquid.",
                                                    "display": "Ovule",
                                                },
                                            ],
                                            "definition": "Container intended to contain sufficient material for only one use.",
                                            "display": "IndividualPackageEntityType",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "_MultiUseContainerEntityType",
                                            "concept": [
                                                {
                                                    "code": "BOT",
                                                    "concept": [
                                                        {
                                                            "code": "BOTA",
                                                            "definition": "A bottle of yellow to brown color.  Used to store light-sensitive materials",
                                                            "display": "Amber Bottle",
                                                        },
                                                        {
                                                            "code": "BOTD",
                                                            "definition": "A bottle with a cap designed to release the contained liquid in droplets of a specific size.",
                                                            "display": "Dropper Bottle",
                                                        },
                                                        {
                                                            "code": "BOTG",
                                                            "definition": "A bottle made of glass",
                                                            "display": "Glass Bottle",
                                                        },
                                                        {
                                                            "code": "BOTP",
                                                            "concept": [
                                                                {
                                                                    "code": "BOTPLY",
                                                                    "definition": "A bottle made of polyethylene",
                                                                    "display": "Polyethylene Bottle",
                                                                }
                                                            ],
                                                            "definition": "A bottle made of plastic",
                                                            "display": "Plastic Bottle",
                                                        },
                                                    ],
                                                    "definition": "A container, typically rounded, either glass or plastic with a narrow neck and capable of storing liquid.",
                                                    "display": "Bottle",
                                                },
                                                {
                                                    "code": "BOX",
                                                    "definition": "A 6-sided container commonly made from paper or cardboard used for solid forms.",
                                                    "display": "Box",
                                                },
                                                {
                                                    "code": "CAN",
                                                    "definition": "A metal container in which a material is hermetically sealed to enable storage over long periods.",
                                                    "display": "Can",
                                                },
                                                {
                                                    "code": "CART",
                                                    "definition": "A sealed container of liquid or powder intended to be loaded into a device.",
                                                    "display": "Cartridge",
                                                },
                                                {
                                                    "code": "CNSTR",
                                                    "definition": "A pressurized metal container holding a substance released as a spray or aerosol.",
                                                    "display": "Canister",
                                                },
                                                {
                                                    "code": "JAR",
                                                    "definition": "A container of glass, earthenware, plastic, etc.  Top of the container has a diameter of similar size to the diameter of the container as a whole",
                                                    "display": "Jar",
                                                },
                                                {
                                                    "code": "JUG",
                                                    "definition": "A deep vessel  for holding liquids, with a handle and often with a spout or lip shape for pouring.",
                                                    "display": "Jug",
                                                },
                                                {
                                                    "code": "TIN",
                                                    "definition": "A lidded container made of thin sheet metal.",
                                                    "display": "Tin",
                                                },
                                                {
                                                    "code": "TUB",
                                                    "definition": "An open flat bottomed round container.",
                                                    "display": "Tub",
                                                },
                                                {
                                                    "code": "TUBE",
                                                    "definition": "A long hollow rigid or flexible cylinder.  Material is extruded by squeezing the container.",
                                                    "display": "Tube",
                                                },
                                                {
                                                    "code": "VIAL",
                                                    "definition": "A small cylindrical glass for holding liquid medicines.",
                                                    "display": "Vial",
                                                },
                                            ],
                                            "definition": "A container intended to contain sufficient material for more than one use.  (I.e. Material is intended to be removed from the container at more than one discrete time period.)",
                                            "display": "MultiUseContainerEntityType",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "BLSTRPK",
                                            "concept": [
                                                {
                                                    "code": "CARD",
                                                    "definition": "A bubble pack card.  Multiple individual/separated doses.",
                                                    "display": "Card",
                                                }
                                            ],
                                            "definition": "A bubblepack.  Medications sealed individually, separated into doses.",
                                            "display": "Blister Pack",
                                        },
                                    ],
                                    "definition": "A container having a fixed and inflexible dimensions and volume",
                                    "display": "RigidContainerEntityType",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "COMPPKG",
                                    "concept": [
                                        {
                                            "code": "DIALPK",
                                            "definition": "Rotatable dispenser.  Eg. Birth control package.",
                                            "display": "Dial Pack",
                                        },
                                        {
                                            "code": "DISK",
                                            "definition": "Object that is thin, flat, and circular.  Doses of medication often contained in bubbles on the disk.",
                                            "display": "Disk",
                                        },
                                        {
                                            "code": "DOSET",
                                            "definition": "Special packaging that will help patients take their medications on a regular basis.",
                                            "display": "Dosette",
                                        },
                                        {
                                            "code": "STRIP",
                                            "definition": "A continuous strip of plastic sectioned into individual pouches, each one containing the quantity of 1 or more medications intended to be administered at a specific time",
                                            "display": "Strip",
                                        },
                                    ],
                                    "definition": "A container intended to contain sufficient material for more than one use, but grouped or organized to provide individual access to sufficient material for a single use.  Often used to ensure that the proper type and amount of material is consumed/expended for each use.",
                                    "display": "Compliance Package",
                                    "property": [
                                        {"code": "child", "valueCode": "BLSTRPK"}
                                    ],
                                },
                                {
                                    "code": "KIT",
                                    "concept": [
                                        {
                                            "code": "SYSTM",
                                            "definition": "A kit in which the components are interconnected.",
                                            "display": "System",
                                        }
                                    ],
                                    "definition": "A container for a diverse collection of products intended to be used together for some purpose (e.g. Medicinal kits often contain a syringe, a needle and the injectable medication).",
                                    "display": "Kit",
                                },
                            ],
                            "definition": "A material intended to hold other materials for purposes of storage or transportation",
                            "display": "Package",
                        }
                    ],
                    "definition": "Material intended to hold another material for purpose of storage or transport.",
                    "display": "ContainerEntityType",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_MedicalDevice",
                    "concept": [
                        {
                            "code": "_AccessMedicalDevice",
                            "concept": [
                                {
                                    "code": "LINE",
                                    "concept": [
                                        {
                                            "code": "IALINE",
                                            "definition": "A line used to administer a substance into an artery",
                                            "display": "Intra-arterial Line",
                                        },
                                        {
                                            "code": "IVLINE",
                                            "definition": "A line used to administer a substance into a vein",
                                            "display": "Intraveneous Line",
                                        },
                                    ],
                                    "definition": "A hollow tube used to administer a substance into a vein, artery or body cavity",
                                    "display": "Line",
                                }
                            ],
                            "definition": "A device used to allow access to a part of a body",
                            "display": "AccessMedicalDevice",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_AdministrationMedicalDevice",
                            "concept": [
                                {
                                    "code": "_InjectionMedicalDevice",
                                    "concept": [
                                        {
                                            "code": "AINJ",
                                            "definition": "Automatically injects medication.",
                                            "display": "AutoInjector",
                                        },
                                        {
                                            "code": "PEN",
                                            "definition": "A device which can contain a cartridge for injection purposes.  Eg. Insulin pen.",
                                            "display": "Pen",
                                        },
                                        {
                                            "code": "SYR",
                                            "definition": "A barrel with a plunger.",
                                            "display": "Syringe",
                                        },
                                    ],
                                    "definition": "A device intended to administer liquid into a subject via a",
                                    "display": "InjectionMedicalDevice",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "APLCTR",
                                    "definition": "A device used to apply a liquid or powder to a surface.",
                                    "display": "Applicator",
                                },
                                {
                                    "code": "INH",
                                    "concept": [
                                        {
                                            "code": "DSKS",
                                            "definition": "The device used to inhale the doses of medication contained in the disk form.",
                                            "display": "Diskus",
                                        },
                                        {
                                            "code": "DSKUNH",
                                            "definition": "The device used to inhale the doses of medication contained in the disk form.",
                                            "display": "Diskhaler",
                                        },
                                        {
                                            "code": "TRBINH",
                                            "definition": "Asthma medication delivery device.",
                                            "display": "Turbuhaler",
                                        },
                                    ],
                                    "definition": "A small device used for inhaling medicine in the form of a vapour or gas in order to ease a respiratory condition such as asthma or to relieve nasal congestion.",
                                    "display": "Inhaler",
                                },
                                {
                                    "code": "PMP",
                                    "definition": "A device that is used to raise, compress, or transfer liquids or gases and is operated by a piston or similar mechanism.",
                                    "display": "Pump",
                                },
                            ],
                            "definition": "A device intended to administer a substance to a subject",
                            "display": "AdministrationMedicalDevice",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": 'A device with direct or indirect therapeutic purpose.  Values for EntityCode when EntityClass = "DEV"',
                    "display": "MedicalDevice",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_SpecimenAdditiveEntity",
                    "concept": [
                        {
                            "code": "ACDA",
                            "definition": "ACD Solution A of trisodium citrate, 22.0g/L; citric acid, 8.0 g/L; and dextrose 24.5 g/L. Used in Blood banking and histocompatibilty testing",
                            "display": "ACD Solution A",
                        },
                        {
                            "code": "ACDB",
                            "definition": "ACD Solution B of trisodium citrate, 13.2g/L; citric acid, 4.8 g/L; and dextrose 14.7 g/L. Used in Blood banking and histocompatibilty testing.",
                            "display": "ACD Solution B",
                        },
                        {
                            "code": "ACET",
                            "definition": "50% V/V acetic acid in water.  Used as  a urine preservative",
                            "display": "Acetic Acid",
                        },
                        {
                            "code": "AMIES",
                            "definition": "Sodium Chloride 3.0g, Potassium Chloride 0.2g, Calcium Chloride 0.1g, Magnesium Chloride 0.1g, Monopotassium Phosphate 0.2g, Disodium Phosphate 1.15g, Sodium Thiogly collate 1.0g, Distilled Water 1 liter",
                            "display": "Amies transport medium",
                        },
                        {
                            "code": "BACTM",
                            "definition": "Any medium used to maintain bacterial viability (e.g. Stuart's, Cary-Blair, Amies)",
                            "display": "Bacterial Transport medium",
                        },
                        {
                            "code": "BF10",
                            "definition": "Formaldehyde 4% w/v; methyl alcohol 1% w/v; phosphate buffering salts. Tissue preservative",
                            "display": "Buffered 10% formalin",
                        },
                        {
                            "code": "BOR",
                            "definition": "Powdered boric acid (usually 10 g) added to 24-hour urine collections as a preservative.",
                            "display": "Boric Acid",
                        },
                        {
                            "code": "BOUIN",
                            "definition": "Picric acid, saturated aqueous solution (750.0 ml), 37-40% formalin (250.0 ml), glacial acetic acid (50.0 ml). Tissue preservative.",
                            "display": "Bouin's solution",
                        },
                        {
                            "code": "BSKM",
                            "definition": "50% skim milk in 0.01 M phosphate-buffered saline.  Maintain virus viability",
                            "display": "Buffered skim milk",
                        },
                        {
                            "code": "C32",
                            "definition": "A 3.2% solution of Sodium Citrate in water.  Used as a blood preservative",
                            "display": "3.2% Citrate",
                        },
                        {
                            "code": "C38",
                            "definition": "A 3.8% solution of Sodium Citrate in water. Used as a blood preservative",
                            "display": "3.8% Citrate",
                        },
                        {
                            "code": "CARS",
                            "definition": "A modification of buffered 10% formalin used as a general tissue preservative.",
                            "display": "Carson's Modified 10% formalin",
                        },
                        {
                            "code": "CARY",
                            "definition": "Sodium Thioglycollate 1.5 g, Disodium Hydrogen Phosphate 1.1 g, Sodium Chloride 5.0 g, Calcium Chloride 0.09 g, Agar 5.0 g, per Liter of Water",
                            "display": "Cary Blair Medium",
                        },
                        {
                            "code": "CHLTM",
                            "definition": "Any of a number of non-nutritive buffered media used to maintain Chlamydia viability during transportation to the laboratory",
                            "display": "Chlamydia transport medium",
                        },
                        {
                            "code": "CTAD",
                            "definition": "Buffered tri-sodium citrate solution with theophylline, adenosine and dipyridamole",
                            "display": "CTAD",
                        },
                        {
                            "code": "EDTK15",
                            "definition": "Potassium EDTA 15% solution in water",
                            "display": "Potassium/K EDTA 15%",
                        },
                        {
                            "code": "EDTK75",
                            "definition": "Potassium EDTA 7.5% solution in water",
                            "display": "Potassium/K EDTA 7.5%",
                        },
                        {
                            "code": "EDTN",
                            "definition": "Sodium fluoride and Disodium EDTA",
                            "display": "Sodium/Na EDTA",
                        },
                        {
                            "code": "ENT",
                            "definition": "Any of a number of non-nutritive buffered media used to maintain enteric bacterial viability during transportation to the laboratory",
                            "display": "Enteric bacteria transport medium",
                        },
                        {
                            "code": "F10",
                            "definition": "A 10% v/v solution in water of formalin( a 37% solution of formaldehyde and water).  Used for tissue preservation.",
                            "display": "10% Formalin",
                        },
                        {
                            "code": "FDP",
                            "definition": "Thrombin plus soybean trypsin inhibitor.  For use in identifying fibrn degredation products.",
                            "display": "Thrombin NIH; soybean trypsin inhibitor",
                        },
                        {
                            "code": "FL10",
                            "definition": "Sodium fluoride, 10mg added as a urine preservative.",
                            "display": "Sodium Fluoride, 10mg",
                        },
                        {
                            "code": "FL100",
                            "definition": "Sodium fluoride, 100mg added as a urine preservative.",
                            "display": "Sodium Fluoride, 100mg",
                        },
                        {
                            "code": "HCL6",
                            "definition": "A solution of HCl containing 6moles of hydrogen ion/L. Used as a Urine Preservative.",
                            "display": "6N HCL",
                        },
                        {
                            "code": "HEPA",
                            "definition": "Ammonium heparin",
                            "display": "Ammonium heparin",
                        },
                        {
                            "code": "HEPL",
                            "definition": "Lithium heparin salt",
                            "display": "Lithium/Li Heparin",
                        },
                        {
                            "code": "HEPN",
                            "definition": "Sodium heparin salt",
                            "display": "Sodium/Na Heparin",
                        },
                        {
                            "code": "HNO3",
                            "definition": "6N Nitric acid used to preserve urine for heavy metal analysis.",
                            "display": "Nitric Acid",
                        },
                        {
                            "code": "JKM",
                            "definition": "A transport medium formulated to maintain Bordetella pertussis viability.",
                            "display": "Jones Kendrick Medium",
                        },
                        {
                            "code": "KARN",
                            "definition": "5% Glutaraldehyde, 4% Formaldehyde in 0.08M buffer. Tissue preservation",
                            "display": "Karnovsky's fixative",
                        },
                        {
                            "code": "KOX",
                            "definition": "Potassium oxalate and sodium fluoride in a 1.25:1 ratio",
                            "display": "Potassium Oxalate",
                        },
                        {
                            "code": "LIA",
                            "definition": "Iodoacetate lithium salt",
                            "display": "Lithium iodoacetate",
                        },
                        {
                            "code": "M4",
                            "definition": "Modified Hank's balanced salt solution supplemented with bovine serum albumin, gelatin, sucrose and glutamic acid. It is buffered to pH 7.3+ or - 0.2 with HEPES buffer. Phenol red is used to indicate pH. Vancomycin, Amphotericin B and Colistin are used to",
                            "display": "M4",
                        },
                        {
                            "code": "M4RT",
                            "definition": "Modified Hank's balanced salt solution supplemented with bovine serum albumin, gelatin, sucrose and glutamic acid. It is buffered to pH 7.3+ or - 0.2 with Hepes buffer. Phenol red is used to indicate pH. Gentamicin and amphotericin B are used to inhibit c",
                            "display": "M4-RT",
                        },
                        {
                            "code": "M5",
                            "definition": "Modified Hank's balanced salt solution supplemented with protein stabilizers, sucrose and glutamic acid. It is buffered to pH 7.3+ or - 0.2 with Hepes buffer. Phenol red is used to indicate pH. Vancomycin, Amphotericin B and Colistin are used to inhibit c",
                            "display": "M5",
                        },
                        {
                            "code": "MICHTM",
                            "definition": "1M potassium citrate, pH 7.0 2.5 ml, 0.1M magnesium sulfate 5.0 ml, 0.1M N-ethyl malemide  5.0 ml, dH2O 87.5 ml, ammonium sulfate 55gm. Preserve antigens for Immunofluorescence procedures",
                            "display": "Michel's transport medium",
                        },
                        {
                            "code": "MMDTM",
                            "definition": "A buffered medium with ammonium sulfate added to preserve antigens for Immunofluorescence procedures",
                            "display": "MMD transport medium",
                        },
                        {
                            "code": "NAF",
                            "definition": "Sodium fluoride",
                            "display": "Sodium Fluoride",
                        },
                        {
                            "code": "NONE",
                            "definition": "No additive. Specifically identifes the specimen as having no additives.",
                            "display": "None",
                        },
                        {
                            "code": "PAGE",
                            "definition": "0.12 g NaCl, 0.004 g MgSO, 0.004 g, CaCl, 0.142 g Na2HPO4 and 0.136 g KH2PO4 per liter of distilled water. Maintain Acanthaoemba viability.",
                            "display": "Page's Saline",
                        },
                        {
                            "code": "PHENOL",
                            "definition": "Phenol. Urine preservative",
                            "display": "Phenol",
                        },
                        {
                            "code": "PVA",
                            "definition": "Polyvinyl alcohol",
                            "display": "Polyvinylalcohol",
                        },
                        {
                            "code": "RLM",
                            "definition": "A transport medium formulated to maintain Bordetella pertussis viability.",
                            "display": "Reagan Lowe Medium",
                        },
                        {
                            "code": "SILICA",
                            "definition": "Diatomaceous earth. For glucose determination blood samples",
                            "display": "Siliceous earth",
                        },
                        {
                            "code": "SPS",
                            "definition": "Sodium polyanethol sulfonate in saline. Anticomplementary and antiphagocytic properties. Used in blood culture collection.",
                            "display": "Sodium polyanethol sulfonate 0.35% in 0.85% sodium chloride",
                        },
                        {
                            "code": "SST",
                            "definition": "Polymer separator gel with clot activator",
                            "display": "Serum Separator Tube",
                        },
                        {
                            "code": "STUTM",
                            "definition": "Sodium Glycerophosphate 10.0g, Calcium Chloride 0.1g, Mercaptoacetic Acid 1.0ml, Distilled Water 1 liter",
                            "display": "Stuart transport medium",
                        },
                        {
                            "code": "THROM",
                            "definition": "Thrombin. Accelerates clotting.",
                            "display": "Thrombin",
                        },
                        {
                            "code": "THYMOL",
                            "definition": "2-Isopropyl-5-methyl phenol. A preservative for 24 Hr Urine samples",
                            "display": "Thymol",
                        },
                        {
                            "code": "THYO",
                            "definition": "A nutritive medium with a reducing agent  (sodium thioglycolate) which, due to a chemical reaction, removes oxygen from the broth.",
                            "display": "Thyoglycolate broth",
                        },
                        {
                            "code": "TOLU",
                            "definition": "Also known as Methylbenzene; Toluol; Phenylmethane. A preservative for 24 Hr Urine samples",
                            "display": "Toluene",
                        },
                        {
                            "code": "URETM",
                            "definition": "A buffered salt solution with antifungal agents added for the collection and transport of Ureaplasma specimens.",
                            "display": "Ureaplasma transport medium",
                        },
                        {
                            "code": "VIRTM",
                            "definition": "Sucrose 74.6g, Potassium hydrogenphosphate 0.52g, L-glutamic acid 0.72g, Bovine serum albumin 5.0g, Gentamicin 50mg, Potassium dihydrogenphosphate 1.25g, L-15 medium 9.9L, Water to 10L. Maintain Virus viability.",
                            "display": "Viral Transport medium",
                        },
                        {
                            "code": "WEST",
                            "definition": "3.8% Citrate buffered to a pH of 5.5 for Westergren Sedimentation Rate",
                            "display": "Buffered Citrate",
                        },
                    ],
                    "definition": "Set of codes related to specimen additives",
                    "display": "SpecimenAdditiveEntity",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "BLDPRD",
                    "definition": "A manufactured product that is produced from the raw blood oi a donor with the intention of using it in a recipient transfusion.",
                    "display": "Blood Product",
                },
                {
                    "code": "VCCNE",
                    "definition": "A Type of medicine that creates an immune protection without the recipient experiencing the disease.",
                    "display": "Vaccine",
                },
                {
                    "code": "_DrugEntity",
                    "concept": [
                        {
                            "code": "_ClinicalDrug",
                            "definition": "Any substance or mixture of substances manufactured, sold or represented for use in: (a) the diagnosis, treatment, mitigation or prevention of a disease, disorder, abnormal physical state, or its symptoms, in human beings or animals; (b) restoring, correcting or modifying organic functions in human beings or animals.",
                            "display": "ClinicalDrug",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True},
                                {"code": "status", "valueCode": "retired"},
                            ],
                        }
                    ],
                    "definition": "A substance whose therapeutic effect is produced by chemical action within the body.",
                    "display": "DrugEntity",
                    "property": [
                        {"code": "notSelectable", "valueBoolean": True},
                        {"code": "status", "valueCode": "retired"},
                    ],
                },
            ],
            "definition": 'Types of Material for EntityClass "MAT"',
            "display": "MaterialEntityClassType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    MaterialEntityClassType

    Types of Material for EntityClass "MAT"
    """

    underscore_non_drug_agent_entity = CodeSystemConcept(
        {
            "code": "_NonDrugAgentEntity",
            "concept": [
                {"code": "NDA01", "definition": "egg", "display": "egg"},
                {"code": "NDA02", "definition": "fish", "display": "fish"},
                {"code": "NDA03", "definition": "lactose", "display": "lactose"},
                {"code": "NDA04", "definition": "peanut", "display": "peanut"},
                {"code": "NDA05", "definition": "soy", "display": "soy"},
                {"code": "NDA06", "definition": "sulfites", "display": "sulfites"},
                {
                    "code": "NDA07",
                    "definition": "wheat or gluten",
                    "display": "wheat or gluten",
                },
                {
                    "code": "NDA08",
                    "definition": "isocyanates",
                    "display": "isocyanates",
                },
                {"code": "NDA09", "definition": "solvents", "display": "solvents"},
                {"code": "NDA10", "definition": "oils", "display": "oils"},
                {"code": "NDA11", "definition": "venoms", "display": "venoms"},
                {"code": "NDA12", "definition": "latex", "display": "latex"},
                {"code": "NDA13", "definition": "shellfish", "display": "shellfish"},
                {
                    "code": "NDA14",
                    "definition": "strawberries",
                    "display": "strawberries",
                },
                {"code": "NDA15", "definition": "tomatoes", "display": "tomatoes"},
                {"code": "NDA16", "definition": "dust", "display": "dust"},
                {"code": "NDA17", "definition": "dust mites", "display": "dust mites"},
            ],
            "definition": "Indicates types of allergy and intolerance agents which are non-drugs.  (E.g. foods, latex, etc.)",
            "display": "NonDrugAgentEntity",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    NonDrugAgentEntity

    Indicates types of allergy and intolerance agents which are non-drugs.  (E.g. foods, latex, etc.)
    """

    underscore_organization_entity_type = CodeSystemConcept(
        {
            "code": "_OrganizationEntityType",
            "concept": [
                {
                    "code": "HHOLD",
                    "definition": "The group of persons who occupy a single housing unit.",
                    "display": "household",
                },
                {
                    "code": "NAT",
                    "definition": "Codes identifying nation states.  Allows for finer grained specification of Entity with classcode <= NAT\r\n\n                        \n                           Example:ISO3166 country codes.",
                    "display": "NationEntityType",
                },
                {
                    "code": "RELIG",
                    "definition": "An organization that provides religious rites of worship.",
                    "display": "religious institution",
                },
            ],
            "definition": "Further classifies entities of classCode ORG.",
            "display": "OrganizationEntityType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    OrganizationEntityType

    Further classifies entities of classCode ORG.
    """

    underscore_place_entity_type = CodeSystemConcept(
        {
            "code": "_PlaceEntityType",
            "concept": [
                {
                    "code": "BED",
                    "definition": "The location of a bed",
                    "display": "Bed Location",
                },
                {
                    "code": "BLDG",
                    "definition": "The location of a building",
                    "display": "Building Location",
                },
                {
                    "code": "FLOOR",
                    "definition": "The location of a floor of a building",
                    "display": "Floor Location",
                },
                {
                    "code": "ROOM",
                    "definition": "The location of a room",
                    "display": "Room Location",
                },
                {
                    "code": "WING",
                    "definition": "The location of a wing of a building (e.g. East Wing).  The same room number for the same floor number can be distinguished by wing number in some situations",
                    "display": "Wing Location",
                },
            ],
            "definition": 'Types of places for EntityClass "PLC"',
            "display": "PlaceEntityType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    PlaceEntityType

    Types of places for EntityClass "PLC"
    """

    underscore_resource_group_entity_type = CodeSystemConcept(
        {
            "code": "_ResourceGroupEntityType",
            "concept": [
                {
                    "code": "PRAC",
                    "definition": "PractitionerGroup",
                    "display": "PractitionerGroup",
                }
            ],
            "definition": "Codes to characterize a Resource Group using categories that typify its membership and/or function\r\n\n                        .\r\n\n                        \n                           Example: PractitionerGroup",
            "display": "ResourceGroupEntityType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    ResourceGroupEntityType

    Codes to characterize a Resource Group using categories that typify its membership and/or function

                        .

                        
                           Example: PractitionerGroup
    """

    class Meta:
        resource = _resource
