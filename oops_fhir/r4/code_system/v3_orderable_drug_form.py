from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3orderableDrugForm"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3orderableDrugForm:
    """
    v3 Code System orderableDrugForm

      OpenIssue:  Missing description.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm
    """

    underscore_administrable_drug_form = CodeSystemConcept(
        {
            "code": "_AdministrableDrugForm",
            "concept": [
                {
                    "code": "APPFUL",
                    "definition": "Applicatorful",
                    "display": "Applicatorful",
                },
                {
                    "code": "DROP",
                    "concept": [
                        {
                            "code": "NDROP",
                            "definition": "Nasal Drops",
                            "display": "Nasal Drops",
                        },
                        {
                            "code": "OPDROP",
                            "definition": "Ophthalmic Drops",
                            "display": "Ophthalmic Drops",
                        },
                        {
                            "code": "ORDROP",
                            "definition": "Oral Drops",
                            "display": "Oral Drops",
                        },
                        {
                            "code": "OTDROP",
                            "definition": "Otic Drops",
                            "display": "Otic Drops",
                        },
                    ],
                    "definition": "Drops",
                    "display": "Drops",
                },
                {"code": "PUFF", "definition": "Puff", "display": "Puff"},
                {"code": "SCOOP", "definition": "Scoops", "display": "Scoops"},
                {"code": "SPRY", "definition": "Sprays", "display": "Sprays"},
            ],
            "definition": "AdministrableDrugForm",
            "display": "AdministrableDrugForm",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    AdministrableDrugForm

    AdministrableDrugForm
    """

    underscore_dispensable_drug_form = CodeSystemConcept(
        {
            "code": "_DispensableDrugForm",
            "concept": [
                {
                    "code": "_GasDrugForm",
                    "concept": [
                        {
                            "code": "GASINHL",
                            "definition": "Gas for Inhalation",
                            "display": "Gas for Inhalation",
                        }
                    ],
                    "definition": "Any elastic aeriform fluid in which the molecules are separated from one another and have free paths.",
                    "display": "GasDrugForm",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_GasLiquidMixture",
                    "concept": [
                        {
                            "code": "AER",
                            "concept": [
                                {
                                    "code": "BAINHL",
                                    "definition": "Breath Activated Inhaler",
                                    "display": "Breath Activated Inhaler",
                                },
                                {
                                    "code": "INHLSOL",
                                    "definition": "Inhalant Solution",
                                    "display": "Inhalant Solution",
                                },
                                {
                                    "code": "MDINHL",
                                    "definition": "Metered Dose Inhaler",
                                    "display": "Metered Dose Inhaler",
                                },
                                {
                                    "code": "NASSPRY",
                                    "definition": "Nasal Spray",
                                    "display": "Nasal Spray",
                                },
                            ],
                            "definition": "Aerosol",
                            "display": "Aerosol",
                        },
                        {
                            "code": "DERMSPRY",
                            "definition": "Dermal Spray",
                            "display": "Dermal Spray",
                        },
                        {
                            "code": "FOAM",
                            "concept": [
                                {
                                    "code": "FOAMAPL",
                                    "definition": "Foam with Applicator",
                                    "display": "Foam with Applicator",
                                },
                                {
                                    "code": "RECFORM",
                                    "definition": "Rectal foam",
                                    "display": "Rectal foam",
                                },
                                {
                                    "code": "VAGFOAM",
                                    "concept": [
                                        {
                                            "code": "VAGFOAMAPL",
                                            "definition": "Vaginal foam with applicator",
                                            "display": "Vaginal foam with applicator",
                                        }
                                    ],
                                    "definition": "Vaginal foam",
                                    "display": "Vaginal foam",
                                },
                            ],
                            "definition": "Foam",
                            "display": "Foam",
                        },
                        {
                            "code": "RECSPRY",
                            "definition": "Rectal Spray",
                            "display": "Rectal Spray",
                        },
                        {
                            "code": "VAGSPRY",
                            "definition": "Vaginal Spray",
                            "display": "Vaginal Spray",
                        },
                    ],
                    "definition": "GasLiquidMixture",
                    "display": "GasLiquidMixture",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_GasSolidSpray",
                    "concept": [
                        {
                            "code": "INHL",
                            "concept": [
                                {
                                    "code": "BAINHLPWD",
                                    "definition": "Breath Activated Powder Inhaler",
                                    "display": "Breath Activated Powder Inhaler",
                                },
                                {
                                    "code": "INHLPWD",
                                    "definition": "Inhalant Powder",
                                    "display": "Inhalant Powder",
                                },
                                {
                                    "code": "MDINHLPWD",
                                    "definition": "Metered Dose Powder Inhaler",
                                    "display": "Metered Dose Powder Inhaler",
                                },
                                {
                                    "code": "NASINHL",
                                    "definition": "Nasal Inhalant",
                                    "display": "Nasal Inhalant",
                                },
                                {
                                    "code": "ORINHL",
                                    "definition": "Oral Inhalant",
                                    "display": "Oral Inhalant",
                                },
                            ],
                            "definition": "Inhalant",
                            "display": "Inhalant",
                        },
                        {
                            "code": "PWDSPRY",
                            "definition": "Powder Spray",
                            "display": "Powder Spray",
                        },
                        {
                            "code": "SPRYADAPT",
                            "definition": "Spray with Adaptor",
                            "display": "Spray with Adaptor",
                        },
                    ],
                    "definition": "GasSolidSpray",
                    "display": "GasSolidSpray",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Liquid",
                    "concept": [
                        {
                            "code": "LIQCLN",
                            "concept": [
                                {
                                    "code": "LIQSOAP",
                                    "definition": "Medicated Liquid Soap",
                                    "display": "Medicated Liquid Soap",
                                },
                                {
                                    "code": "SHMP",
                                    "definition": "A liquid soap or detergent used to clean the hair and scalp and is often used as a vehicle for dermatologic agents.",
                                    "display": "Shampoo",
                                },
                            ],
                            "definition": "Liquid Cleanser",
                            "display": "Liquid Cleanser",
                        },
                        {
                            "code": "OIL",
                            "concept": [
                                {
                                    "code": "TOPOIL",
                                    "definition": "Topical Oil",
                                    "display": "Topical Oil",
                                }
                            ],
                            "definition": "An unctuous, combustible substance which is liquid, or easily liquefiable, on warming, and is soluble in ether but insoluble in water. Such substances, depending on their origin, are classified as animal, mineral, or vegetable oils.",
                            "display": "Oil",
                        },
                        {
                            "code": "SOL",
                            "concept": [
                                {
                                    "code": "IPSOL",
                                    "definition": "Intraperitoneal Solution",
                                    "display": "Intraperitoneal Solution",
                                },
                                {
                                    "code": "IRSOL",
                                    "concept": [
                                        {
                                            "code": "DOUCHE",
                                            "definition": "A liquid preparation, intended for the irrigative cleansing of the vagina, that is prepared from powders, liquid solutions, or liquid concentrates and contains one or more chemical substances dissolved in a suitable solvent or mutually miscible solvents.",
                                            "display": "Douche",
                                        },
                                        {
                                            "code": "ENEMA",
                                            "definition": "A rectal preparation for therapeutic, diagnostic, or nutritive purposes.",
                                            "display": "Enema",
                                        },
                                        {
                                            "code": "OPIRSOL",
                                            "definition": "Ophthalmic Irrigation Solution",
                                            "display": "Ophthalmic Irrigation Solution",
                                        },
                                    ],
                                    "definition": "A sterile solution intended to bathe or flush open wounds or body cavities; they're used topically, never parenterally.",
                                    "display": "Irrigation Solution",
                                },
                                {
                                    "code": "IVSOL",
                                    "definition": "Intravenous Solution",
                                    "display": "Intravenous Solution",
                                },
                                {
                                    "code": "ORALSOL",
                                    "concept": [
                                        {
                                            "code": "ELIXIR",
                                            "definition": "A clear, pleasantly flavored, sweetened hydroalcoholic liquid containing dissolved medicinal agents; it is intended for oral use.",
                                            "display": "Elixir",
                                        },
                                        {
                                            "code": "RINSE",
                                            "definition": "An aqueous solution which is most often used for its deodorant, refreshing, or antiseptic effect.",
                                            "display": "Mouthwash/Rinse",
                                        },
                                        {
                                            "code": "SYRUP",
                                            "definition": "An oral solution containing high concentrations of sucrose or other sugars; the term has also been used to include any other liquid dosage form prepared in a sweet and viscid vehicle, including oral suspensions.",
                                            "display": "Syrup",
                                        },
                                    ],
                                    "definition": "Oral Solution",
                                    "display": "Oral Solution",
                                    "property": [
                                        {"code": "child", "valueCode": "ORDROP"}
                                    ],
                                },
                                {
                                    "code": "RECSOL",
                                    "definition": "Rectal Solution",
                                    "display": "Rectal Solution",
                                },
                                {
                                    "code": "TOPSOL",
                                    "concept": [
                                        {
                                            "code": "LIN",
                                            "definition": "A solution or mixture of various substances in oil, alcoholic solutions of soap, or emulsions intended for external application.",
                                            "display": "Liniment",
                                        },
                                        {
                                            "code": "MUCTOPSOL",
                                            "definition": "Mucous Membrane Topical Solution",
                                            "display": "Mucous Membrane Topical Solution",
                                        },
                                        {
                                            "code": "TINC",
                                            "definition": "Tincture",
                                            "display": "Tincture",
                                        },
                                    ],
                                    "definition": "Topical Solution",
                                    "display": "Topical Solution",
                                },
                            ],
                            "definition": "A liquid preparation that contains one or more chemical substances dissolved, i.e., molecularly dispersed, in a suitable solvent or mixture of mutually miscible solvents.",
                            "display": "Solution",
                            "property": [{"code": "child", "valueCode": "DROP"}],
                        },
                    ],
                    "definition": "A state of substance that is an intermediate one entered into as matter goes from solid to gas; liquids are also intermediate in that they have neither the orderliness of a crystal nor the randomness of a gas. (Note: This term should not be used to describe solutions, only pure chemicals in their liquid state.)",
                    "display": "Liquid",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_LiquidLiquidEmulsion",
                    "concept": [
                        {
                            "code": "CRM",
                            "concept": [
                                {
                                    "code": "NASCRM",
                                    "definition": "Nasal Cream",
                                    "display": "Nasal Cream",
                                },
                                {
                                    "code": "OPCRM",
                                    "definition": "Ophthalmic Cream",
                                    "display": "Ophthalmic Cream",
                                },
                                {
                                    "code": "ORCRM",
                                    "definition": "Oral Cream",
                                    "display": "Oral Cream",
                                },
                                {
                                    "code": "OTCRM",
                                    "definition": "Otic Cream",
                                    "display": "Otic Cream",
                                },
                                {
                                    "code": "RECCRM",
                                    "definition": "Rectal Cream",
                                    "display": "Rectal Cream",
                                },
                                {
                                    "code": "TOPCRM",
                                    "definition": "Topical Cream",
                                    "display": "Topical Cream",
                                },
                                {
                                    "code": "VAGCRM",
                                    "concept": [
                                        {
                                            "code": "VAGCRMAPL",
                                            "definition": "Vaginal Cream with Applicator",
                                            "display": "Vaginal Cream with Applicator",
                                        }
                                    ],
                                    "definition": "Vaginal Cream",
                                    "display": "Vaginal Cream",
                                },
                            ],
                            "definition": "A semisolid dosage form containing one or more drug substances dissolved or dispersed in a suitable base; more recently, the term has been restricted to products consisting of oil-in-water emulsions or aqueous microcrystalline dispersions of long chain fatty acids or alcohols that are water washable and more cosmetically and aesthetically acceptable.",
                            "display": "Cream",
                        },
                        {
                            "code": "LTN",
                            "concept": [
                                {
                                    "code": "TOPLTN",
                                    "definition": "Topical Lotion",
                                    "display": "Topical Lotion",
                                }
                            ],
                            "definition": 'The term "lotion" has been used to categorize many topical suspensions, solutions and emulsions intended for application to the skin.',
                            "display": "Lotion",
                        },
                        {
                            "code": "OINT",
                            "concept": [
                                {
                                    "code": "NASOINT",
                                    "definition": "Nasal Ointment",
                                    "display": "Nasal Ointment",
                                },
                                {
                                    "code": "OINTAPL",
                                    "definition": "Ointment with Applicator",
                                    "display": "Ointment with Applicator",
                                },
                                {
                                    "code": "OPOINT",
                                    "definition": "Ophthalmic Ointment",
                                    "display": "Ophthalmic Ointment",
                                },
                                {
                                    "code": "OTOINT",
                                    "definition": "Otic Ointment",
                                    "display": "Otic Ointment",
                                },
                                {
                                    "code": "RECOINT",
                                    "definition": "Rectal Ointment",
                                    "display": "Rectal Ointment",
                                },
                                {
                                    "code": "TOPOINT",
                                    "definition": "Topical Ointment",
                                    "display": "Topical Ointment",
                                },
                                {
                                    "code": "VAGOINT",
                                    "concept": [
                                        {
                                            "code": "VAGOINTAPL",
                                            "definition": "Vaginal Ointment with Applicator",
                                            "display": "Vaginal Ointment with Applicator",
                                        }
                                    ],
                                    "definition": "Vaginal Ointment",
                                    "display": "Vaginal Ointment",
                                },
                            ],
                            "definition": "A semisolid preparation intended for external application to the skin or mucous membranes.",
                            "display": "Ointment",
                        },
                    ],
                    "definition": "A two-phase system in which one liquid is dispersed throughout another liquid in the form of small droplets.",
                    "display": "LiquidLiquidEmulsion",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_LiquidSolidSuspension",
                    "concept": [
                        {
                            "code": "GEL",
                            "concept": [
                                {
                                    "code": "GELAPL",
                                    "definition": "Gel with Applicator",
                                    "display": "Gel with Applicator",
                                },
                                {
                                    "code": "NASGEL",
                                    "definition": "Nasal Gel",
                                    "display": "Nasal Gel",
                                },
                                {
                                    "code": "OPGEL",
                                    "definition": "Ophthalmic Gel",
                                    "display": "Ophthalmic Gel",
                                },
                                {
                                    "code": "OTGEL",
                                    "definition": "Otic Gel",
                                    "display": "Otic Gel",
                                },
                                {
                                    "code": "TOPGEL",
                                    "definition": "Topical Gel",
                                    "display": "Topical Gel",
                                },
                                {
                                    "code": "URETHGEL",
                                    "definition": "Urethral Gel",
                                    "display": "Urethral Gel",
                                },
                                {
                                    "code": "VAGGEL",
                                    "concept": [
                                        {
                                            "code": "VGELAPL",
                                            "definition": "Vaginal Gel with Applicator",
                                            "display": "Vaginal Gel with Applicator",
                                        }
                                    ],
                                    "definition": "Vaginal Gel",
                                    "display": "Vaginal Gel",
                                },
                            ],
                            "definition": "A semisolid system consisting of either suspensions made up of small inorganic particles or large organic molecules interpenetrated by a liquid.",
                            "display": "Gel",
                        },
                        {
                            "code": "PASTE",
                            "concept": [
                                {
                                    "code": "PUD",
                                    "definition": "Pudding",
                                    "display": "Pudding",
                                },
                                {
                                    "code": "TPASTE",
                                    "definition": "A paste formulation intended to clean and/or polish the teeth, and which may contain certain additional agents.",
                                    "display": "Toothpaste",
                                },
                            ],
                            "definition": "A semisolid dosage form that contains one or more drug substances intended for topical application.",
                            "display": "Paste",
                        },
                        {
                            "code": "SUSP",
                            "concept": [
                                {
                                    "code": "ITSUSP",
                                    "definition": "Intrathecal Suspension",
                                    "display": "Intrathecal Suspension",
                                },
                                {
                                    "code": "OPSUSP",
                                    "definition": "Ophthalmic Suspension",
                                    "display": "Ophthalmic Suspension",
                                },
                                {
                                    "code": "ORSUSP",
                                    "concept": [
                                        {
                                            "code": "ERSUSP",
                                            "concept": [
                                                {
                                                    "code": "ERSUSP12",
                                                    "definition": "12 Hour Extended-Release Suspension",
                                                    "display": "12 Hour Extended-Release Suspension",
                                                },
                                                {
                                                    "code": "ERSUSP24",
                                                    "definition": "24 Hour Extended Release Suspension",
                                                    "display": "24 Hour Extended Release Suspension",
                                                },
                                            ],
                                            "definition": "Extended-Release Suspension",
                                            "display": "Extended-Release Suspension",
                                        }
                                    ],
                                    "definition": "Oral Suspension",
                                    "display": "Oral Suspension",
                                },
                                {
                                    "code": "OTSUSP",
                                    "definition": "Otic Suspension",
                                    "display": "Otic Suspension",
                                },
                                {
                                    "code": "RECSUSP",
                                    "definition": "Rectal Suspension",
                                    "display": "Rectal Suspension",
                                },
                            ],
                            "definition": "Suspension",
                            "display": "Suspension",
                        },
                    ],
                    "definition": "A liquid preparation which consists of solid particles dispersed throughout a liquid phase in which the particles are not soluble.",
                    "display": "LiquidSolidSuspension",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_SolidDrugForm",
                    "concept": [
                        {
                            "code": "BAR",
                            "concept": [
                                {
                                    "code": "BARSOAP",
                                    "concept": [
                                        {
                                            "code": "MEDBAR",
                                            "definition": "Medicated Bar Soap",
                                            "display": "Medicated Bar Soap",
                                        }
                                    ],
                                    "definition": "Bar Soap",
                                    "display": "Bar Soap",
                                },
                                {
                                    "code": "CHEWBAR",
                                    "definition": "A solid dosage form usually in the form of a rectangle that is meant to be chewed.",
                                    "display": "Chewable Bar",
                                },
                            ],
                            "definition": "Bar",
                            "display": "Bar",
                        },
                        {
                            "code": "BEAD",
                            "definition": "A solid dosage form in the shape of a small ball.",
                            "display": "Beads",
                        },
                        {"code": "CAKE", "definition": "Cake", "display": "Cake"},
                        {
                            "code": "CEMENT",
                            "definition": "A substance that serves to produce solid union between two surfaces.",
                            "display": "Cement",
                        },
                        {
                            "code": "CRYS",
                            "definition": "A naturally produced angular solid of definite form in which the ultimate units from which it is built up are systematically arranged; they are usually evenly spaced on a regular space lattice.",
                            "display": "Crystals",
                        },
                        {
                            "code": "DISK",
                            "definition": "A circular plate-like organ or structure.",
                            "display": "Disk",
                        },
                        {"code": "FLAKE", "definition": "Flakes", "display": "Flakes"},
                        {
                            "code": "GRAN",
                            "definition": "A small particle or grain.",
                            "display": "Granules",
                        },
                        {
                            "code": "GUM",
                            "definition": "A sweetened and flavored insoluble plastic material of various shapes which when chewed, releases a drug substance into the oral cavity.",
                            "display": "ChewingGum",
                        },
                        {
                            "code": "PAD",
                            "concept": [
                                {
                                    "code": "MEDPAD",
                                    "definition": "Medicated Pad",
                                    "display": "Medicated Pad",
                                }
                            ],
                            "definition": "Pad",
                            "display": "Pad",
                        },
                        {
                            "code": "PATCH",
                            "concept": [
                                {
                                    "code": "TPATCH",
                                    "concept": [
                                        {
                                            "code": "TPATH16",
                                            "definition": "16 Hour Transdermal Patch",
                                            "display": "16 Hour Transdermal Patch",
                                        },
                                        {
                                            "code": "TPATH24",
                                            "definition": "24 Hour Transdermal Patch",
                                            "display": "24 Hour Transdermal Patch",
                                        },
                                        {
                                            "code": "TPATH2WK",
                                            "definition": "Biweekly Transdermal Patch",
                                            "display": "Biweekly Transdermal Patch",
                                        },
                                        {
                                            "code": "TPATH72",
                                            "definition": "72 Hour Transdermal Patch",
                                            "display": "72 Hour Transdermal Patch",
                                        },
                                        {
                                            "code": "TPATHWK",
                                            "definition": "Weekly Transdermal Patch",
                                            "display": "Weekly Transdermal Patch",
                                        },
                                    ],
                                    "definition": "Transdermal Patch",
                                    "display": "Transdermal Patch",
                                }
                            ],
                            "definition": "A drug delivery system that contains an adhesived backing and that permits its ingredients to diffuse from some portion of it (e.g., the backing itself, a reservoir, the adhesive, or some other component) into the body from the external site where it is applied.",
                            "display": "Patch",
                        },
                        {
                            "code": "PELLET",
                            "definition": "A small sterile solid mass consisting of a highly purified drug (with or without excipients) made by the formation of granules, or by compression and molding.",
                            "display": "Pellet",
                        },
                        {
                            "code": "PILL",
                            "concept": [
                                {
                                    "code": "CAP",
                                    "concept": [
                                        {
                                            "code": "ORCAP",
                                            "concept": [
                                                {
                                                    "code": "ENTCAP",
                                                    "concept": [
                                                        {
                                                            "code": "ERENTCAP",
                                                            "definition": "Extended Release Enteric Coated Capsule",
                                                            "display": "Extended Release Enteric Coated Capsule",
                                                        }
                                                    ],
                                                    "definition": "Enteric Coated Capsule",
                                                    "display": "Enteric Coated Capsule",
                                                },
                                                {
                                                    "code": "ERCAP",
                                                    "concept": [
                                                        {
                                                            "code": "ERCAP12",
                                                            "definition": "12 Hour Extended Release Capsule",
                                                            "display": "12 Hour Extended Release Capsule",
                                                        },
                                                        {
                                                            "code": "ERCAP24",
                                                            "definition": "24 Hour Extended Release Capsule",
                                                            "display": "24 Hour Extended Release Capsule",
                                                        },
                                                        {
                                                            "code": "ERECCAP",
                                                            "definition": "Rationale: Duplicate of code ERENTCAP. Use code ERENTCAP instead.",
                                                            "display": "Extended Release Enteric Coated Capsule",
                                                            "property": [
                                                                {
                                                                    "code": "status",
                                                                    "valueCode": "retired",
                                                                }
                                                            ],
                                                        },
                                                    ],
                                                    "definition": "A solid dosage form in which the drug is enclosed within either a hard or soft soluble container made from a suitable form of gelatin, and which releases a drug (or drugs) in such a manner to allow a reduction in dosing frequency as compared to that drug (or drugs) presented as a conventional dosage form.",
                                                    "display": "Extended Release Capsule",
                                                    "property": [
                                                        {
                                                            "code": "child",
                                                            "valueCode": "ERENTCAP",
                                                        }
                                                    ],
                                                },
                                            ],
                                            "definition": "Oral Capsule",
                                            "display": "Oral Capsule",
                                        }
                                    ],
                                    "definition": 'A solid dosage form in which the drug is enclosed within either a hard or soft soluble container or "shell" made from a suitable form of gelatin.',
                                    "display": "Capsule",
                                },
                                {
                                    "code": "TAB",
                                    "concept": [
                                        {
                                            "code": "ORTAB",
                                            "concept": [
                                                {
                                                    "code": "BUCTAB",
                                                    "concept": [
                                                        {
                                                            "code": "SRBUCTAB",
                                                            "definition": "Sustained Release Buccal Tablet",
                                                            "display": "Sustained Release Buccal Tablet",
                                                        }
                                                    ],
                                                    "definition": "Buccal Tablet",
                                                    "display": "Buccal Tablet",
                                                },
                                                {
                                                    "code": "CAPLET",
                                                    "definition": "Caplet",
                                                    "display": "Caplet",
                                                },
                                                {
                                                    "code": "CHEWTAB",
                                                    "definition": "A solid dosage form containing medicinal substances with or without suitable diluents that is intended to be chewed, producing a pleasant tasting residue in the oral cavity that is easily swallowed and does not leave a bitter or unpleasant after-taste.",
                                                    "display": "Chewable Tablet",
                                                },
                                                {
                                                    "code": "CPTAB",
                                                    "definition": "Coated Particles Tablet",
                                                    "display": "Coated Particles Tablet",
                                                },
                                                {
                                                    "code": "DISINTAB",
                                                    "definition": "A solid dosage form containing medicinal substances which disintegrates rapidly, usually within a matter of seconds, when placed upon the tongue.",
                                                    "display": "Disintegrating Tablet",
                                                },
                                                {
                                                    "code": "DRTAB",
                                                    "definition": "Delayed Release Tablet",
                                                    "display": "Delayed Release Tablet",
                                                },
                                                {
                                                    "code": "ECTAB",
                                                    "concept": [
                                                        {
                                                            "code": "ERECTAB",
                                                            "definition": "Extended Release Enteric Coated Tablet",
                                                            "display": "Extended Release Enteric Coated Tablet",
                                                        }
                                                    ],
                                                    "definition": "Enteric Coated Tablet",
                                                    "display": "Enteric Coated Tablet",
                                                },
                                                {
                                                    "code": "ERTAB",
                                                    "concept": [
                                                        {
                                                            "code": "ERTAB12",
                                                            "definition": "12 Hour Extended Release Tablet",
                                                            "display": "12 Hour Extended Release Tablet",
                                                        },
                                                        {
                                                            "code": "ERTAB24",
                                                            "definition": "24 Hour Extended Release Tablet",
                                                            "display": "24 Hour Extended Release Tablet",
                                                        },
                                                    ],
                                                    "definition": "A solid dosage form containing a drug which allows at least a reduction in dosing frequency as compared to that drug presented in conventional dosage form.",
                                                    "display": "Extended Release Tablet",
                                                    "property": [
                                                        {
                                                            "code": "child",
                                                            "valueCode": "ERECTAB",
                                                        }
                                                    ],
                                                },
                                                {
                                                    "code": "ORTROCHE",
                                                    "definition": "A solid preparation containing one or more medicaments, usually in a flavored, sweetened base which is intended to dissolve or disintegrate slowly in the mouth.",
                                                    "display": "Lozenge/Oral Troche",
                                                },
                                                {
                                                    "code": "SLTAB",
                                                    "definition": "Sublingual Tablet",
                                                    "display": "Sublingual Tablet",
                                                },
                                            ],
                                            "definition": "Oral Tablet",
                                            "display": "Oral Tablet",
                                        },
                                        {
                                            "code": "VAGTAB",
                                            "definition": "Vaginal Tablet",
                                            "display": "Vaginal Tablet",
                                        },
                                    ],
                                    "definition": "A solid dosage form containing medicinal substances with or without suitable diluents.",
                                    "display": "Tablet",
                                },
                            ],
                            "definition": "A small, round solid dosage form containing a medicinal agent intended for oral administration.",
                            "display": "Pill",
                        },
                        {
                            "code": "POWD",
                            "concept": [
                                {
                                    "code": "TOPPWD",
                                    "concept": [
                                        {
                                            "code": "RECPWD",
                                            "definition": "Rectal Powder",
                                            "display": "Rectal Powder",
                                        },
                                        {
                                            "code": "VAGPWD",
                                            "definition": "Vaginal Powder",
                                            "display": "Vaginal Powder",
                                        },
                                    ],
                                    "definition": "Topical Powder",
                                    "display": "Topical Powder",
                                }
                            ],
                            "definition": "An intimate mixture of dry, finely divided drugs and/or chemicals that may be intended for internal or external use.",
                            "display": "Powder",
                        },
                        {
                            "code": "SUPP",
                            "concept": [
                                {
                                    "code": "RECSUPP",
                                    "definition": "Rectal Suppository",
                                    "display": "Rectal Suppository",
                                },
                                {
                                    "code": "URETHSUPP",
                                    "definition": "Urethral suppository",
                                    "display": "Urethral suppository",
                                },
                                {
                                    "code": "VAGSUPP",
                                    "definition": "Vaginal Suppository",
                                    "display": "Vaginal Suppository",
                                },
                            ],
                            "definition": "A solid body of various weights and shapes, adapted for introduction into the rectal, vaginal, or urethral orifice of the human body; they usually melt, soften, or dissolve at body temperature.",
                            "display": "Suppository",
                        },
                        {
                            "code": "SWAB",
                            "concept": [
                                {
                                    "code": "MEDSWAB",
                                    "definition": "Medicated swab",
                                    "display": "Medicated swab",
                                }
                            ],
                            "definition": "A wad of absorbent material usually wound around one end of a small stick and used for applying medication or for removing material from an area.",
                            "display": "Swab",
                        },
                        {
                            "code": "WAFER",
                            "definition": "A thin slice of material containing a medicinal agent.",
                            "display": "Wafer",
                        },
                    ],
                    "definition": "SolidDrugForm",
                    "display": "SolidDrugForm",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "DispensableDrugForm",
            "display": "DispensableDrugForm",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    DispensableDrugForm

    DispensableDrugForm
    """

    class Meta:
        resource = _resource
