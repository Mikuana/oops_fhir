from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AmericanIndianAlaskaNativeLanguages"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AmericanIndianAlaskaNativeLanguages:
    """
    v3 Code System AmericanIndianAlaskaNativeLanguages

     American Indian and Alaska Native languages currently being used in the
United States.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AmericanIndianAlaskaNativeLanguages
    """

    underscore_algic = CodeSystemConcept(
        {
            "code": "_Algic",
            "concept": [
                {
                    "code": "_Algonquian",
                    "concept": [
                        {
                            "code": "_Arapahoan",
                            "concept": [
                                {
                                    "code": "_ArapahoGrosVentre",
                                    "concept": [
                                        {
                                            "code": "x-ARP",
                                            "definition": "Arapaho",
                                            "display": "Arapaho",
                                        },
                                        {
                                            "code": "x-ATS",
                                            "definition": "Gros Ventre",
                                            "display": "Gros Ventre",
                                        },
                                    ],
                                    "definition": "ArapahoGrosVentre",
                                    "display": "ArapahoGrosVentre",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                }
                            ],
                            "definition": "Arapahoan",
                            "display": "Arapahoan",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_CreeMontagnais",
                            "concept": [
                                {
                                    "code": "_Cree",
                                    "concept": [
                                        {
                                            "code": "x-CRP",
                                            "definition": "Western Cree",
                                            "display": "Western Cree",
                                        }
                                    ],
                                    "definition": "Cree",
                                    "display": "Cree",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                }
                            ],
                            "definition": "CreeMontagnais",
                            "display": "CreeMontagnais",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_EasternAlgonquin",
                            "concept": [
                                {
                                    "code": "_Abenakian",
                                    "concept": [
                                        {
                                            "code": "x-AAQ",
                                            "definition": "Eastern Abenaki",
                                            "display": "Eastern Abenaki",
                                        },
                                        {
                                            "code": "x-ABE",
                                            "definition": "Western Abenaki",
                                            "display": "Western Abenaki",
                                        },
                                        {
                                            "code": "x-MAC",
                                            "definition": "Maliseet-Passamaquoddy",
                                            "display": "Maliseet-Passamaquoddy",
                                        },
                                    ],
                                    "definition": "Abenakian",
                                    "display": "Abenakian",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_Delawaran",
                                    "concept": [
                                        {
                                            "code": "x-DEL",
                                            "definition": "Unami Delaware",
                                            "display": "Unami Delaware",
                                        }
                                    ],
                                    "definition": "Delawaran",
                                    "display": "Delawaran",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "x-MIC",
                                    "definition": "Micmac",
                                    "display": "Micmac",
                                },
                            ],
                            "definition": "EasternAlgonquin",
                            "display": "EasternAlgonquin",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_Ojibwayan",
                            "concept": [
                                {
                                    "code": "x-OJB",
                                    "definition": "Southern Ojibwa",
                                    "display": "Southern Ojibwa",
                                },
                                {
                                    "code": "x-POT",
                                    "definition": "Potawatami",
                                    "display": "Potawatami",
                                },
                            ],
                            "definition": "Ojibwayan",
                            "display": "Ojibwayan",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_SaukFoxKickapoo",
                            "concept": [
                                {
                                    "code": "x-KIC",
                                    "definition": "Kickapoo",
                                    "display": "Kickapoo",
                                },
                                {
                                    "code": "x-SAC",
                                    "definition": "Mesquakie",
                                    "display": "Mesquakie",
                                },
                                {
                                    "code": "x-SJW",
                                    "definition": "Shawnee",
                                    "display": "Shawnee",
                                },
                            ],
                            "definition": "SaukFoxKickapoo",
                            "display": "SaukFoxKickapoo",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "x-BLC",
                            "definition": "Blackfoot",
                            "display": "Blackfoot",
                        },
                        {
                            "code": "x-CHY",
                            "definition": "Cheyenne",
                            "display": "Cheyenne",
                        },
                        {
                            "code": "x-MEZ",
                            "definition": "Menominee",
                            "display": "Menominee",
                        },
                    ],
                    "definition": "Algonquian",
                    "display": "Algonquian",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Ritwan",
                    "concept": [
                        {"code": "x-YUR", "definition": "Yurok", "display": "Yurok"}
                    ],
                    "definition": "Ritwan",
                    "display": "Ritwan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Algic",
            "display": "Algic",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Algic

    Algic
    """

    underscore_caddoan = CodeSystemConcept(
        {
            "code": "_Caddoan",
            "concept": [
                {
                    "code": "_NorthernCaddoan",
                    "concept": [
                        {
                            "code": "x-ARI",
                            "definition": "Arikara",
                            "display": "Arikara",
                        },
                        {"code": "x-PAW", "definition": "Pawnee", "display": "Pawnee"},
                        {
                            "code": "x-WIC",
                            "definition": "Wichita",
                            "display": "Wichita",
                        },
                    ],
                    "definition": "NorthernCaddoan",
                    "display": "NorthernCaddoan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_SouthernCaddoan",
                    "concept": [
                        {"code": "x-CAD", "definition": "Caddo", "display": "Caddo"}
                    ],
                    "definition": "SouthernCaddoan",
                    "display": "SouthernCaddoan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Caddoan",
            "display": "Caddoan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Caddoan

    Caddoan
    """

    underscore_chimakuan = CodeSystemConcept(
        {
            "code": "_Chimakuan",
            "concept": [
                {"code": "x-QUI", "definition": "Quileute", "display": "Quileute"}
            ],
            "definition": "Chimakuan",
            "display": "Chimakuan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Chimakuan

    Chimakuan
    """

    underscore_eskimo_aleut = CodeSystemConcept(
        {
            "code": "_EskimoAleut",
            "concept": [
                {
                    "code": "_Aleut",
                    "concept": [
                        {"code": "x-ALW", "definition": "Aleut", "display": "Aleut"}
                    ],
                    "definition": "Aleut",
                    "display": "Aleut",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Eskimoan",
                    "concept": [
                        {
                            "code": "_InuitInupiaq",
                            "concept": [
                                {
                                    "code": "x-ESI",
                                    "definition": "North Alaskan Inuktitut",
                                    "display": "North Alaskan Inuktitut",
                                },
                                {
                                    "code": "x-ESK",
                                    "definition": "Northwest Alaska Inuktitut",
                                    "display": "Northwest Alaska Inuktitut",
                                },
                            ],
                            "definition": "InuitInupiaq",
                            "display": "InuitInupiaq",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_SirenikskiYupik",
                            "concept": [
                                {
                                    "code": "x-EMS",
                                    "definition": "Pacific Yupik Gulf",
                                    "display": "Pacific Yupik Gulf",
                                },
                                {
                                    "code": "x-ESS",
                                    "definition": "Central Siberian Yupik",
                                    "display": "Central Siberian Yupik",
                                },
                                {
                                    "code": "x-ESU",
                                    "definition": "Central Alaskan Yupik",
                                    "display": "Central Alaskan Yupik",
                                },
                            ],
                            "definition": "SirenikskiYupik",
                            "display": "SirenikskiYupik",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Eskimoan",
                    "display": "Eskimoan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "EskimoAleut",
            "display": "EskimoAleut",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    EskimoAleut

    EskimoAleut
    """

    underscore_hokan = CodeSystemConcept(
        {
            "code": "_Hokan",
            "concept": [
                {
                    "code": "_CochimiYuman",
                    "concept": [
                        {
                            "code": "_Yuman",
                            "concept": [
                                {
                                    "code": "_DeltaCalifornia",
                                    "concept": [
                                        {
                                            "code": "_Diegueno",
                                            "concept": [
                                                {
                                                    "code": "x-DIH",
                                                    "definition": "Kumeyaay",
                                                    "display": "Kumeyaay",
                                                }
                                            ],
                                            "definition": "Diegueno",
                                            "display": "Diegueno",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "x-COC",
                                            "definition": "Cocopa",
                                            "display": "Cocopa",
                                        },
                                    ],
                                    "definition": "DeltaCalifornia",
                                    "display": "DeltaCalifornia",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_Pai",
                                    "concept": [
                                        {
                                            "code": "x-YUF",
                                            "definition": "Havasupai",
                                            "display": "Havasupai",
                                        }
                                    ],
                                    "definition": "Pai",
                                    "display": "Pai",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_River",
                                    "concept": [
                                        {
                                            "code": "x-MOV",
                                            "definition": "Mohave",
                                            "display": "Mohave",
                                        },
                                        {
                                            "code": "x-MRC",
                                            "definition": "Maricopa",
                                            "display": "Maricopa",
                                        },
                                        {
                                            "code": "x-YUM",
                                            "definition": "Quechan",
                                            "display": "Quechan",
                                        },
                                    ],
                                    "definition": "River",
                                    "display": "River",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                            ],
                            "definition": "Yuman",
                            "display": "Yuman",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "CochimiYuman",
                    "display": "CochimiYuman",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Palaihnihan",
                    "concept": [
                        {
                            "code": "x-ACH",
                            "definition": "Achumawi",
                            "display": "Achumawi",
                        },
                        {
                            "code": "x-ATW",
                            "definition": "Atsugewi",
                            "display": "Atsugewi",
                        },
                    ],
                    "definition": "Palaihnihan",
                    "display": "Palaihnihan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Pomoan",
                    "concept": [
                        {
                            "code": "x-KJU",
                            "definition": "Kashaya",
                            "display": "Kashaya",
                        },
                        {
                            "code": "x-PEF",
                            "definition": "Northeastern Pomo",
                            "display": "Northeastern Pomo",
                        },
                        {
                            "code": "x-PEO",
                            "definition": "Southeastern Pomo",
                            "display": "Southeastern Pomo",
                        },
                        {
                            "code": "x-PEQ",
                            "definition": "Southern Pomo",
                            "display": "Southern Pomo",
                        },
                        {
                            "code": "x-POO",
                            "definition": "Central Pomo",
                            "display": "Central Pomo",
                        },
                    ],
                    "definition": "Pomoan",
                    "display": "Pomoan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Shasta",
                    "concept": [
                        {"code": "x-SHT", "definition": "Shasta", "display": "Shasta"}
                    ],
                    "definition": "Shasta",
                    "display": "Shasta",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {"code": "x-KYH", "definition": "Karok", "display": "Karok"},
                {"code": "x-WAS", "definition": "Washoe", "display": "Washoe"},
            ],
            "definition": "Hokan",
            "display": "Hokan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Hokan

    Hokan
    """

    underscore_iroquoian = CodeSystemConcept(
        {
            "code": "_Iroquoian",
            "concept": [
                {
                    "code": "_NorthernIroquoian",
                    "concept": [
                        {"code": "x-CAY", "definition": "Cayuga", "display": "Cayuga"},
                        {"code": "x-MOH", "definition": "Mohawk", "display": "Mohawk"},
                        {"code": "x-ONE", "definition": "Oneida", "display": "Oneida"},
                        {
                            "code": "x-ONO",
                            "definition": "Onondaga",
                            "display": "Onondaga",
                        },
                        {"code": "x-SEE", "definition": "Seneca", "display": "Seneca"},
                        {
                            "code": "x-TUS",
                            "definition": "Tuscarora",
                            "display": "Tuscarora",
                        },
                    ],
                    "definition": "NorthernIroquoian",
                    "display": "NorthernIroquoian",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {"code": "x-CER", "definition": "Cherokee", "display": "Cherokee"},
            ],
            "definition": "Iroquoian",
            "display": "Iroquoian",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Iroquoian

    Iroquoian
    """

    underscore_keresan = CodeSystemConcept(
        {
            "code": "_Keresan",
            "concept": [
                {
                    "code": "x-KEE",
                    "definition": "Rio Grande Keresan",
                    "display": "Rio Grande Keresan",
                },
                {
                    "code": "x-KJQ",
                    "definition": "Acoma-Laguna",
                    "display": "Acoma-Laguna",
                },
            ],
            "definition": "Keresan",
            "display": "Keresan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Keresan

    Keresan
    """

    underscore_kiowa_tanoan = CodeSystemConcept(
        {
            "code": "_KiowaTanoan",
            "concept": [
                {
                    "code": "_Tiwa",
                    "concept": [
                        {
                            "code": "x-TAO",
                            "definition": "Northern Tiwa",
                            "display": "Northern Tiwa",
                        },
                        {
                            "code": "x-TIX",
                            "definition": "Southern Tiwa",
                            "display": "Southern Tiwa",
                        },
                    ],
                    "definition": "Tiwa",
                    "display": "Tiwa",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {"code": "x-KIO", "definition": "Kiowa", "display": "Kiowa"},
                {"code": "x-TEW", "definition": "Tewa", "display": "Tewa"},
                {"code": "x-TOW", "definition": "Jemez", "display": "Jemez"},
            ],
            "definition": "KiowaTanoan",
            "display": "KiowaTanoan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    KiowaTanoan

    KiowaTanoan
    """

    underscore_muskogean = CodeSystemConcept(
        {
            "code": "_Muskogean",
            "concept": [
                {
                    "code": "_CentralMuskogean",
                    "concept": [
                        {
                            "code": "x-AKZ",
                            "definition": "Alabama",
                            "display": "Alabama",
                        },
                        {
                            "code": "x-CKU",
                            "definition": "Koasati",
                            "display": "Koasati",
                        },
                        {
                            "code": "x-MIK",
                            "definition": "Mikasuki",
                            "display": "Mikasuki",
                        },
                    ],
                    "definition": "CentralMuskogean",
                    "display": "CentralMuskogean",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_WesternMuskogean",
                    "concept": [
                        {
                            "code": "x-CCT",
                            "definition": "Choctaw",
                            "display": "Choctaw",
                        },
                        {
                            "code": "x-CIC",
                            "definition": "Chickasaw",
                            "display": "Chickasaw",
                        },
                    ],
                    "definition": "WesternMuskogean",
                    "display": "WesternMuskogean",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {"code": "x-CRK", "definition": "Creek", "display": "Creek"},
            ],
            "definition": "Muskogean",
            "display": "Muskogean",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Muskogean

    Muskogean
    """

    underscore_nadene = CodeSystemConcept(
        {
            "code": "_Nadene",
            "concept": [
                {
                    "code": "_AthapaskanEyak",
                    "concept": [
                        {
                            "code": "_Athapaskan",
                            "concept": [
                                {
                                    "code": "_Apachean",
                                    "concept": [
                                        {
                                            "code": "_EasternApachean",
                                            "concept": [
                                                {
                                                    "code": "x-APJ",
                                                    "definition": "Jicarilla",
                                                    "display": "Jicarilla",
                                                },
                                                {
                                                    "code": "x-APL",
                                                    "definition": "Lipan",
                                                    "display": "Lipan",
                                                },
                                            ],
                                            "definition": "EasternApachean",
                                            "display": "EasternApachean",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "_WesternApachean",
                                            "concept": [
                                                {
                                                    "code": "x-APM",
                                                    "definition": "Mescalero-Chiricahua",
                                                    "display": "Mescalero-Chiricahua",
                                                },
                                                {
                                                    "code": "x-APW",
                                                    "definition": "Western Apache",
                                                    "display": "Western Apache",
                                                },
                                                {
                                                    "code": "x-NAV",
                                                    "definition": "Dine",
                                                    "display": "Dine",
                                                },
                                            ],
                                            "definition": "WesternApachean",
                                            "display": "WesternApachean",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "x-APK",
                                            "definition": "Kiowa Apache",
                                            "display": "Kiowa Apache",
                                        },
                                    ],
                                    "definition": "Apachean",
                                    "display": "Apachean",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_CentralAlaskaYukon",
                                    "concept": [
                                        {
                                            "code": "_KoyukonIngalik",
                                            "concept": [
                                                {
                                                    "code": "x-HOI",
                                                    "definition": "Holikachuk",
                                                    "display": "Holikachuk",
                                                },
                                                {
                                                    "code": "x-ING",
                                                    "definition": "Degexit'an",
                                                    "display": "Degexit'an",
                                                },
                                                {
                                                    "code": "x-KOY",
                                                    "definition": "Koyukon",
                                                    "display": "Koyukon",
                                                },
                                            ],
                                            "definition": "KoyukonIngalik",
                                            "display": "KoyukonIngalik",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "_KutchinHan",
                                            "concept": [
                                                {
                                                    "code": "x-HAA",
                                                    "definition": "Han",
                                                    "display": "Han",
                                                },
                                                {
                                                    "code": "x-KUC",
                                                    "definition": "Kutchin",
                                                    "display": "Kutchin",
                                                },
                                            ],
                                            "definition": "KutchinHan",
                                            "display": "KutchinHan",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "_TananaTutchone",
                                            "concept": [
                                                {
                                                    "code": "_Tanana",
                                                    "concept": [
                                                        {
                                                            "code": "x-TAA",
                                                            "definition": "Lower Tanana",
                                                            "display": "Lower Tanana",
                                                        },
                                                        {
                                                            "code": "x-TAU",
                                                            "definition": "Upper Tanana",
                                                            "display": "Upper Tanana",
                                                        },
                                                        {
                                                            "code": "x-TCB",
                                                            "definition": "Tanacross",
                                                            "display": "Tanacross",
                                                        },
                                                    ],
                                                    "definition": "Tanana",
                                                    "display": "Tanana",
                                                    "property": [
                                                        {
                                                            "code": "notSelectable",
                                                            "valueBoolean": True,
                                                        }
                                                    ],
                                                },
                                                {
                                                    "code": "x-KUU",
                                                    "definition": "Upper Kuskokwim",
                                                    "display": "Upper Kuskokwim",
                                                },
                                            ],
                                            "definition": "TananaTutchone",
                                            "display": "TananaTutchone",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                    ],
                                    "definition": "CentralAlaskaYukon",
                                    "display": "CentralAlaskaYukon",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_PacificCoastAthapaskan",
                                    "concept": [
                                        {
                                            "code": "_CaliforniaAthapaskan",
                                            "concept": [
                                                {
                                                    "code": "x-HUP",
                                                    "definition": "Hupa",
                                                    "display": "Hupa",
                                                },
                                                {
                                                    "code": "x-KTW",
                                                    "definition": "Cahto",
                                                    "display": "Cahto",
                                                },
                                            ],
                                            "definition": "CaliforniaAthapaskan",
                                            "display": "CaliforniaAthapaskan",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                        {
                                            "code": "_OregonAthapaskan",
                                            "concept": [
                                                {
                                                    "code": "x-TOL",
                                                    "definition": "Tolowa",
                                                    "display": "Tolowa",
                                                },
                                                {
                                                    "code": "x-TUU",
                                                    "definition": "Tututni",
                                                    "display": "Tututni",
                                                },
                                            ],
                                            "definition": "OregonAthapaskan",
                                            "display": "OregonAthapaskan",
                                            "property": [
                                                {
                                                    "code": "notSelectable",
                                                    "valueBoolean": True,
                                                }
                                            ],
                                        },
                                    ],
                                    "definition": "PacificCoastAthapaskan",
                                    "display": "PacificCoastAthapaskan",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_SouthernAlaska",
                                    "concept": [
                                        {
                                            "code": "x-AHT",
                                            "definition": "Ahtna",
                                            "display": "Ahtna",
                                        },
                                        {
                                            "code": "x-TFN",
                                            "definition": "Tanaina",
                                            "display": "Tanaina",
                                        },
                                    ],
                                    "definition": "SouthernAlaska",
                                    "display": "SouthernAlaska",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                            ],
                            "definition": "Athapaskan",
                            "display": "Athapaskan",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {"code": "x-EYA", "definition": "Eyak", "display": "Eyak"},
                    ],
                    "definition": "AthapaskanEyak",
                    "display": "AthapaskanEyak",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {"code": "x-TLI", "definition": "Tlingit", "display": "Tlingit"},
            ],
            "definition": "Nadene",
            "display": "Nadene",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Nadene

    Nadene
    """

    underscore_penutian = CodeSystemConcept(
        {
            "code": "_Penutian",
            "concept": [
                {
                    "code": "_Chinookan",
                    "concept": [
                        {
                            "code": "_UpperChinook",
                            "concept": [
                                {
                                    "code": "x-WAC",
                                    "definition": "Kiksht",
                                    "display": "Kiksht",
                                }
                            ],
                            "definition": "UpperChinook",
                            "display": "UpperChinook",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "Chinookan",
                    "display": "Chinookan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Coosan",
                    "concept": [
                        {"code": "x-COS", "definition": "Hanis", "display": "Hanis"}
                    ],
                    "definition": "Coosan",
                    "display": "Coosan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Maiduan",
                    "concept": [
                        {
                            "code": "x-MAI",
                            "definition": "Northwest Maidu",
                            "display": "Northwest Maidu",
                        },
                        {
                            "code": "x-NMU",
                            "definition": "Northeast Maidu",
                            "display": "Northeast Maidu",
                        },
                        {
                            "code": "x-NSZ",
                            "definition": "Nisenan",
                            "display": "Nisenan",
                        },
                    ],
                    "definition": "Maiduan",
                    "display": "Maiduan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_PlateauPenutian",
                    "concept": [
                        {
                            "code": "_Sahaptian",
                            "concept": [
                                {
                                    "code": "x-UMA",
                                    "definition": "Umatilla",
                                    "display": "Umatilla",
                                },
                                {
                                    "code": "x-WAA",
                                    "definition": "Walla Walla",
                                    "display": "Walla Walla",
                                },
                                {
                                    "code": "x-WAR",
                                    "definition": "Tenino",
                                    "display": "Tenino",
                                },
                                {
                                    "code": "x-YAK",
                                    "definition": "Yakima",
                                    "display": "Yakima",
                                },
                            ],
                            "definition": "Sahaptian",
                            "display": "Sahaptian",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "x-KLA",
                            "definition": "Klamath-Modoc",
                            "display": "Klamath-Modoc",
                        },
                        {
                            "code": "x-NEZ",
                            "definition": "Nez Perce",
                            "display": "Nez Perce",
                        },
                    ],
                    "definition": "PlateauPenutian",
                    "display": "PlateauPenutian",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Takelman",
                    "concept": [
                        {
                            "code": "_Kalapuyan",
                            "concept": [
                                {
                                    "code": "x-KAL",
                                    "definition": "Central Kalapuyan",
                                    "display": "Central Kalapuyan",
                                }
                            ],
                            "definition": "Kalapuyan",
                            "display": "Kalapuyan",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "Takelman",
                    "display": "Takelman",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Tsimshianic",
                    "concept": [
                        {
                            "code": "x-TSI",
                            "definition": "Coast Tsimshain",
                            "display": "Coast Tsimshain",
                        }
                    ],
                    "definition": "Tsimshianic",
                    "display": "Tsimshianic",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Utian",
                    "concept": [
                        {
                            "code": "_Miwokan",
                            "concept": [
                                {
                                    "code": "_EasternMiwok",
                                    "concept": [
                                        {
                                            "code": "x-CSM",
                                            "definition": "Central Sierra Miwok",
                                            "display": "Central Sierra Miwok",
                                        },
                                        {
                                            "code": "x-NSQ",
                                            "definition": "Northern Sierra Miwok",
                                            "display": "Northern Sierra Miwok",
                                        },
                                        {
                                            "code": "x-PMW",
                                            "definition": "Plains Miwok",
                                            "display": "Plains Miwok",
                                        },
                                        {
                                            "code": "x-SKD",
                                            "definition": "Southern Sierra Miwok",
                                            "display": "Southern Sierra Miwok",
                                        },
                                    ],
                                    "definition": "EasternMiwok",
                                    "display": "EasternMiwok",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_WesternMiwok",
                                    "concept": [
                                        {
                                            "code": "x-CSI",
                                            "definition": "Coast Miwok",
                                            "display": "Coast Miwok",
                                        },
                                        {
                                            "code": "x-LMW",
                                            "definition": "Lake Miwok",
                                            "display": "Lake Miwok",
                                        },
                                    ],
                                    "definition": "WesternMiwok",
                                    "display": "WesternMiwok",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                            ],
                            "definition": "Miwokan",
                            "display": "Miwokan",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "Utian",
                    "display": "Utian",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Wintuan",
                    "concept": [
                        {
                            "code": "x-WIT",
                            "definition": "Wintu-Nomlaki",
                            "display": "Wintu-Nomlaki",
                        }
                    ],
                    "definition": "Wintuan",
                    "display": "Wintuan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Yokutsan",
                    "concept": [
                        {
                            "code": "x-ENH",
                            "definition": "Kings River",
                            "display": "Kings River",
                        },
                        {
                            "code": "x-GSH",
                            "definition": "Gashowu",
                            "display": "Gashowu",
                        },
                        {
                            "code": "x-PYL",
                            "definition": "Poso Creek",
                            "display": "Poso Creek",
                        },
                        {
                            "code": "x-TKH",
                            "definition": "Tule-Kaweah",
                            "display": "Tule-Kaweah",
                        },
                    ],
                    "definition": "Yokutsan",
                    "display": "Yokutsan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Penutian",
            "display": "Penutian",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Penutian

    Penutian
    """

    underscore_pidgin = CodeSystemConcept(
        {
            "code": "_Pidgin",
            "concept": [
                {
                    "code": "x-CHH",
                    "definition": "Chinook Wawa",
                    "display": "Chinook Wawa",
                }
            ],
            "definition": "Pidgin",
            "display": "Pidgin",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Pidgin

    Pidgin
    """

    underscore_salishan = CodeSystemConcept(
        {
            "code": "_Salishan",
            "concept": [
                {
                    "code": "_CentralSalish",
                    "concept": [
                        {
                            "code": "x-CLM",
                            "definition": "Clallam",
                            "display": "Clallam",
                        },
                        {
                            "code": "x-LUT",
                            "definition": "Lushootseed",
                            "display": "Lushootseed",
                        },
                        {
                            "code": "x-STR",
                            "definition": "Northern Straits",
                            "display": "Northern Straits",
                        },
                    ],
                    "definition": "CentralSalish",
                    "display": "CentralSalish",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_InteriorSalish",
                    "concept": [
                        {
                            "code": "x-COL",
                            "definition": "Columbian",
                            "display": "Columbian",
                        },
                        {
                            "code": "x-CRD",
                            "definition": "Coeur D'alene",
                            "display": "Coeur D'alene",
                        },
                        {
                            "code": "x-FLA",
                            "definition": "Kalispel",
                            "display": "Kalispel",
                        },
                        {
                            "code": "x-OKA",
                            "definition": "Okanagan",
                            "display": "Okanagan",
                        },
                    ],
                    "definition": "InteriorSalish",
                    "display": "InteriorSalish",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Tsamosan",
                    "concept": [
                        {
                            "code": "x-CEA",
                            "definition": "Lower Chehalis",
                            "display": "Lower Chehalis",
                        },
                        {
                            "code": "x-CJH",
                            "definition": "Upper Chehalis",
                            "display": "Upper Chehalis",
                        },
                        {
                            "code": "x-COW",
                            "definition": "Cowlitz",
                            "display": "Cowlitz",
                        },
                        {
                            "code": "x-QUN",
                            "definition": "Quinault",
                            "display": "Quinault",
                        },
                    ],
                    "definition": "Tsamosan",
                    "display": "Tsamosan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Salishan",
            "display": "Salishan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Salishan

    Salishan
    """

    underscore_siouan_catawba = CodeSystemConcept(
        {
            "code": "_SiouanCatawba",
            "concept": [
                {
                    "code": "_Siouan",
                    "concept": [
                        {
                            "code": "_MississippiValley",
                            "concept": [
                                {
                                    "code": "_ChiwereWinnebago",
                                    "concept": [
                                        {
                                            "code": "x-IOW",
                                            "definition": "Chiwere",
                                            "display": "Chiwere",
                                        },
                                        {
                                            "code": "x-WIN",
                                            "definition": "Hocak",
                                            "display": "Hocak",
                                        },
                                    ],
                                    "definition": "ChiwereWinnebago",
                                    "display": "ChiwereWinnebago",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_Dakotan",
                                    "concept": [
                                        {
                                            "code": "x-ASB",
                                            "definition": "Assiniboine",
                                            "display": "Assiniboine",
                                        },
                                        {
                                            "code": "x-DHG",
                                            "definition": "Dakota",
                                            "display": "Dakota",
                                        },
                                        {
                                            "code": "x-LKT",
                                            "definition": "Lakota",
                                            "display": "Lakota",
                                        },
                                        {
                                            "code": "x-NKT",
                                            "definition": "Nakota",
                                            "display": "Nakota",
                                        },
                                    ],
                                    "definition": "Dakotan",
                                    "display": "Dakotan",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                                {
                                    "code": "_Dhegiha",
                                    "concept": [
                                        {
                                            "code": "x-KAA",
                                            "definition": "Kansa",
                                            "display": "Kansa",
                                        },
                                        {
                                            "code": "x-OMA",
                                            "definition": "Omaha-Ponca",
                                            "display": "Omaha-Ponca",
                                        },
                                        {
                                            "code": "x-OSA",
                                            "definition": "Osage",
                                            "display": "Osage",
                                        },
                                        {
                                            "code": "x-QUA",
                                            "definition": "Quapaw",
                                            "display": "Quapaw",
                                        },
                                    ],
                                    "definition": "Dhegiha",
                                    "display": "Dhegiha",
                                    "property": [
                                        {"code": "notSelectable", "valueBoolean": True}
                                    ],
                                },
                            ],
                            "definition": "MississippiValley",
                            "display": "MississippiValley",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_MissouriRiver",
                            "concept": [
                                {
                                    "code": "x-CRO",
                                    "definition": "Crow",
                                    "display": "Crow",
                                },
                                {
                                    "code": "x-HID",
                                    "definition": "Hidatsa",
                                    "display": "Hidatsa",
                                },
                            ],
                            "definition": "MissouriRiver",
                            "display": "MissouriRiver",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {"code": "x-MHQ", "definition": "Mandan", "display": "Mandan"},
                    ],
                    "definition": "Siouan",
                    "display": "Siouan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "SiouanCatawba",
            "display": "SiouanCatawba",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    SiouanCatawba

    SiouanCatawba
    """

    underscore_uto_aztecan = CodeSystemConcept(
        {
            "code": "_UtoAztecan",
            "concept": [
                {
                    "code": "_Numic",
                    "concept": [
                        {
                            "code": "_CentralNumic",
                            "concept": [
                                {
                                    "code": "x-COM",
                                    "definition": "Comanche",
                                    "display": "Comanche",
                                },
                                {
                                    "code": "x-PAR",
                                    "definition": "Panamint",
                                    "display": "Panamint",
                                },
                                {
                                    "code": "x-SHH",
                                    "definition": "Shoshone",
                                    "display": "Shoshone",
                                },
                            ],
                            "definition": "CentralNumic",
                            "display": "CentralNumic",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_SouthernNumic",
                            "concept": [
                                {
                                    "code": "x-KAW",
                                    "definition": "Kawaiisu",
                                    "display": "Kawaiisu",
                                },
                                {
                                    "code": "x-UTE",
                                    "definition": "Ute-Southern Paiute",
                                    "display": "Ute-Southern Paiute",
                                },
                            ],
                            "definition": "SouthernNumic",
                            "display": "SouthernNumic",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_WesternNumic",
                            "concept": [
                                {
                                    "code": "x-MON",
                                    "definition": "Mono",
                                    "display": "Mono",
                                },
                                {
                                    "code": "x-PAO",
                                    "definition": "Northern Paiute-Bannock",
                                    "display": "Northern Paiute-Bannock",
                                },
                            ],
                            "definition": "WesternNumic",
                            "display": "WesternNumic",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Numic",
                    "display": "Numic",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Takic",
                    "concept": [
                        {
                            "code": "_Cupan",
                            "concept": [
                                {
                                    "code": "x-CHL",
                                    "definition": "Cahuilla",
                                    "display": "Cahuilla",
                                },
                                {
                                    "code": "x-CUP",
                                    "definition": "Cupeno",
                                    "display": "Cupeno",
                                },
                                {
                                    "code": "x-LUI",
                                    "definition": "Luiseno",
                                    "display": "Luiseno",
                                },
                            ],
                            "definition": "Cupan",
                            "display": "Cupan",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                        {
                            "code": "_SerranoGabrielino",
                            "concept": [
                                {
                                    "code": "x-SER",
                                    "definition": "Serrano",
                                    "display": "Serrano",
                                }
                            ],
                            "definition": "SerranoGabrielino",
                            "display": "SerranoGabrielino",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        },
                    ],
                    "definition": "Takic",
                    "display": "Takic",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Taracahitan",
                    "concept": [
                        {
                            "code": "_Cahitan",
                            "concept": [
                                {
                                    "code": "x-YAQ",
                                    "definition": "Yaqui",
                                    "display": "Yaqui",
                                }
                            ],
                            "definition": "Cahitan",
                            "display": "Cahitan",
                            "property": [
                                {"code": "notSelectable", "valueBoolean": True}
                            ],
                        }
                    ],
                    "definition": "Taracahitan",
                    "display": "Taracahitan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_Tepiman",
                    "concept": [
                        {
                            "code": "x-PAP",
                            "definition": "Papago-Pima",
                            "display": "Papago-Pima",
                        }
                    ],
                    "definition": "Tepiman",
                    "display": "Tepiman",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {"code": "x-HOP", "definition": "Hopi", "display": "Hopi"},
                {
                    "code": "x-TUB",
                    "definition": "Tubatululabal",
                    "display": "Tubatululabal",
                },
            ],
            "definition": "UtoAztecan",
            "display": "UtoAztecan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    UtoAztecan

    UtoAztecan
    """

    underscore_wakashan = CodeSystemConcept(
        {
            "code": "_Wakashan",
            "concept": [
                {
                    "code": "_Nootkan",
                    "concept": [
                        {"code": "x-MYH", "definition": "Makah", "display": "Makah"}
                    ],
                    "definition": "Nootkan",
                    "display": "Nootkan",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                }
            ],
            "definition": "Wakashan",
            "display": "Wakashan",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Wakashan

    Wakashan
    """

    underscore_yukian = CodeSystemConcept(
        {
            "code": "_Yukian",
            "concept": [
                {"code": "x-WAO", "definition": "Wappo", "display": "Wappo"},
                {"code": "x-YUK", "definition": "Yuki", "display": "Yuki"},
            ],
            "definition": "Yukian",
            "display": "Yukian",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Yukian

    Yukian
    """

    x_hai = CodeSystemConcept(
        {"code": "x-HAI", "definition": "Haida", "display": "Haida"}
    )
    """
    Haida

    Haida
    """

    x_kun = CodeSystemConcept(
        {"code": "x-KUN", "definition": "Kootenai", "display": "Kootenai"}
    )
    """
    Kootenai

    Kootenai
    """

    x_psd = CodeSystemConcept(
        {
            "code": "x-PSD",
            "definition": "Plains Indian Sign Language",
            "display": "Plains Indian Sign Language",
        }
    )
    """
    Plains Indian Sign Language

    Plains Indian Sign Language
    """

    x_yuc = CodeSystemConcept(
        {"code": "x-YUC", "definition": "Yuchi", "display": "Yuchi"}
    )
    """
    Yuchi

    Yuchi
    """

    x_zun = CodeSystemConcept(
        {"code": "x-ZUN", "definition": "Zuni", "display": "Zuni"}
    )
    """
    Zuni

    Zuni
    """

    class Meta:
        resource = _resource
