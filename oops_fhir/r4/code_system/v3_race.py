from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3Race"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3Race:
    """
    v3 Code System Race

     In the United States, federal standards for classifying data on race
determine the categories used by federal agencies and exert a strong
influence on categorization by state and local agencies and private
sector organizations.  The federal standards do not conceptually define
race, and they recognize the absence of an anthropological or scientific
basis for racial classification.  Instead, the federal standards
acknowledge that race is a social-political construct in which an
individual's own identification with one more race categories is
preferred to observer identification. The standards use a variety of
features to define five minimum race categories. Among these features
are descent from "the original peoples" of a specified region or nation.
The minimum race categories are American Indian or Alaska Native, Asian,
Black or African American, Native Hawaiian or Other Pacific Islander,
and White.  The federal standards stipulate that race data need not be
limited to the five minimum categories, but any expansion must be
collapsible to those categories.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-Race
    """

    one002_5 = CodeSystemConcept(
        {
            "code": "1002-5",
            "concept": [
                {
                    "code": "1004-1",
                    "concept": [
                        {
                            "code": "1006-6",
                            "definition": "Abenaki",
                            "display": "Abenaki",
                        },
                        {
                            "code": "1008-2",
                            "definition": "Algonquian",
                            "display": "Algonquian",
                        },
                        {
                            "code": "1010-8",
                            "concept": [
                                {
                                    "code": "1011-6",
                                    "definition": "Chiricahua",
                                    "display": "Chiricahua",
                                },
                                {
                                    "code": "1012-4",
                                    "definition": "Fort Sill Apache",
                                    "display": "Fort Sill Apache",
                                },
                                {
                                    "code": "1013-2",
                                    "definition": "Jicarilla Apache",
                                    "display": "Jicarilla Apache",
                                },
                                {
                                    "code": "1014-0",
                                    "definition": "Lipan Apache",
                                    "display": "Lipan Apache",
                                },
                                {
                                    "code": "1015-7",
                                    "definition": "Mescalero Apache",
                                    "display": "Mescalero Apache",
                                },
                                {
                                    "code": "1016-5",
                                    "definition": "Oklahoma Apache",
                                    "display": "Oklahoma Apache",
                                },
                                {
                                    "code": "1017-3",
                                    "definition": "Payson Apache",
                                    "display": "Payson Apache",
                                },
                                {
                                    "code": "1018-1",
                                    "definition": "San Carlos Apache",
                                    "display": "San Carlos Apache",
                                },
                                {
                                    "code": "1019-9",
                                    "definition": "White Mountain Apache",
                                    "display": "White Mountain Apache",
                                },
                            ],
                            "definition": "Apache",
                            "display": "Apache",
                        },
                        {
                            "code": "1021-5",
                            "concept": [
                                {
                                    "code": "1022-3",
                                    "definition": "Northern Arapaho",
                                    "display": "Northern Arapaho",
                                },
                                {
                                    "code": "1023-1",
                                    "definition": "Southern Arapaho",
                                    "display": "Southern Arapaho",
                                },
                                {
                                    "code": "1024-9",
                                    "definition": "Wind River Arapaho",
                                    "display": "Wind River Arapaho",
                                },
                            ],
                            "definition": "Arapaho",
                            "display": "Arapaho",
                        },
                        {
                            "code": "1026-4",
                            "definition": "Arikara",
                            "display": "Arikara",
                        },
                        {
                            "code": "1028-0",
                            "definition": "Assiniboine",
                            "display": "Assiniboine",
                        },
                        {
                            "code": "1030-6",
                            "concept": [
                                {
                                    "code": "1031-4",
                                    "definition": "Fort Peck Assiniboine Sioux",
                                    "display": "Fort Peck Assiniboine Sioux",
                                }
                            ],
                            "definition": "Assiniboine Sioux",
                            "display": "Assiniboine Sioux",
                        },
                        {
                            "code": "1033-0",
                            "definition": "Bannock",
                            "display": "Bannock",
                        },
                        {
                            "code": "1035-5",
                            "definition": "Blackfeet",
                            "display": "Blackfeet",
                        },
                        {
                            "code": "1037-1",
                            "definition": "Brotherton",
                            "display": "Brotherton",
                        },
                        {
                            "code": "1039-7",
                            "definition": "Burt Lake Band",
                            "display": "Burt Lake Band",
                        },
                        {
                            "code": "1041-3",
                            "concept": [
                                {
                                    "code": "1042-1",
                                    "definition": "Oklahoma Cado",
                                    "display": "Oklahoma Cado",
                                }
                            ],
                            "definition": "Caddo",
                            "display": "Caddo",
                        },
                        {
                            "code": "1044-7",
                            "concept": [
                                {
                                    "code": "1045-4",
                                    "definition": "Agua Caliente Cahuilla",
                                    "display": "Agua Caliente Cahuilla",
                                },
                                {
                                    "code": "1046-2",
                                    "definition": "Augustine",
                                    "display": "Augustine",
                                },
                                {
                                    "code": "1047-0",
                                    "definition": "Cabazon",
                                    "display": "Cabazon",
                                },
                                {
                                    "code": "1048-8",
                                    "definition": "Los Coyotes",
                                    "display": "Los Coyotes",
                                },
                                {
                                    "code": "1049-6",
                                    "definition": "Morongo",
                                    "display": "Morongo",
                                },
                                {
                                    "code": "1050-4",
                                    "definition": "Santa Rosa Cahuilla",
                                    "display": "Santa Rosa Cahuilla",
                                },
                                {
                                    "code": "1051-2",
                                    "definition": "Torres-Martinez",
                                    "display": "Torres-Martinez",
                                },
                            ],
                            "definition": "Cahuilla",
                            "display": "Cahuilla",
                        },
                        {
                            "code": "1053-8",
                            "concept": [
                                {
                                    "code": "1054-6",
                                    "definition": "Cahto",
                                    "display": "Cahto",
                                },
                                {
                                    "code": "1055-3",
                                    "definition": "Chimariko",
                                    "display": "Chimariko",
                                },
                                {
                                    "code": "1056-1",
                                    "definition": "Coast Miwok",
                                    "display": "Coast Miwok",
                                },
                                {
                                    "code": "1057-9",
                                    "definition": "Digger",
                                    "display": "Digger",
                                },
                                {
                                    "code": "1058-7",
                                    "definition": "Kawaiisu",
                                    "display": "Kawaiisu",
                                },
                                {
                                    "code": "1059-5",
                                    "definition": "Kern River",
                                    "display": "Kern River",
                                },
                                {
                                    "code": "1060-3",
                                    "definition": "Mattole",
                                    "display": "Mattole",
                                },
                                {
                                    "code": "1061-1",
                                    "definition": "Red Wood",
                                    "display": "Red Wood",
                                },
                                {
                                    "code": "1062-9",
                                    "definition": "Santa Rosa",
                                    "display": "Santa Rosa",
                                },
                                {
                                    "code": "1063-7",
                                    "definition": "Takelma",
                                    "display": "Takelma",
                                },
                                {
                                    "code": "1064-5",
                                    "definition": "Wappo",
                                    "display": "Wappo",
                                },
                                {
                                    "code": "1065-2",
                                    "definition": "Yana",
                                    "display": "Yana",
                                },
                                {
                                    "code": "1066-0",
                                    "definition": "Yuki",
                                    "display": "Yuki",
                                },
                            ],
                            "definition": "California Tribes",
                            "display": "California Tribes",
                        },
                        {
                            "code": "1068-6",
                            "concept": [
                                {
                                    "code": "1069-4",
                                    "definition": "Canadian Indian",
                                    "display": "Canadian Indian",
                                },
                                {
                                    "code": "1070-2",
                                    "definition": "Central American Indian",
                                    "display": "Central American Indian",
                                },
                                {
                                    "code": "1071-0",
                                    "definition": "French American Indian",
                                    "display": "French American Indian",
                                },
                                {
                                    "code": "1072-8",
                                    "definition": "Mexican American Indian",
                                    "display": "Mexican American Indian",
                                },
                                {
                                    "code": "1073-6",
                                    "definition": "South American Indian",
                                    "display": "South American Indian",
                                },
                            ],
                            "definition": "Canadian and Latin American Indian",
                            "display": "Canadian and Latin American Indian",
                        },
                        {
                            "code": "1074-4",
                            "definition": "Spanish American Indian",
                            "display": "Spanish American Indian",
                        },
                        {
                            "code": "1076-9",
                            "concept": [
                                {
                                    "code": "1741-8",
                                    "definition": "Alatna",
                                    "display": "Alatna",
                                },
                                {
                                    "code": "1742-6",
                                    "definition": "Alexander",
                                    "display": "Alexander",
                                },
                                {
                                    "code": "1743-4",
                                    "definition": "Allakaket",
                                    "display": "Allakaket",
                                },
                                {
                                    "code": "1744-2",
                                    "definition": "Alanvik",
                                    "display": "Alanvik",
                                },
                                {
                                    "code": "1745-9",
                                    "definition": "Anvik",
                                    "display": "Anvik",
                                },
                                {
                                    "code": "1746-7",
                                    "definition": "Arctic",
                                    "display": "Arctic",
                                },
                                {
                                    "code": "1747-5",
                                    "definition": "Beaver",
                                    "display": "Beaver",
                                },
                                {
                                    "code": "1748-3",
                                    "definition": "Birch Creek",
                                    "display": "Birch Creek",
                                },
                                {
                                    "code": "1749-1",
                                    "definition": "Cantwell",
                                    "display": "Cantwell",
                                },
                                {
                                    "code": "1750-9",
                                    "definition": "Chalkyitsik",
                                    "display": "Chalkyitsik",
                                },
                                {
                                    "code": "1751-7",
                                    "definition": "Chickaloon",
                                    "display": "Chickaloon",
                                },
                                {
                                    "code": "1752-5",
                                    "definition": "Chistochina",
                                    "display": "Chistochina",
                                },
                                {
                                    "code": "1753-3",
                                    "definition": "Chitina",
                                    "display": "Chitina",
                                },
                                {
                                    "code": "1754-1",
                                    "definition": "Circle",
                                    "display": "Circle",
                                },
                                {
                                    "code": "1755-8",
                                    "definition": "Cook Inlet",
                                    "display": "Cook Inlet",
                                },
                                {
                                    "code": "1756-6",
                                    "definition": "Copper Center",
                                    "display": "Copper Center",
                                },
                                {
                                    "code": "1757-4",
                                    "definition": "Copper River",
                                    "display": "Copper River",
                                },
                                {
                                    "code": "1758-2",
                                    "definition": "Dot Lake",
                                    "display": "Dot Lake",
                                },
                                {
                                    "code": "1759-0",
                                    "definition": "Doyon",
                                    "display": "Doyon",
                                },
                                {
                                    "code": "1760-8",
                                    "definition": "Eagle",
                                    "display": "Eagle",
                                },
                                {
                                    "code": "1761-6",
                                    "definition": "Eklutna",
                                    "display": "Eklutna",
                                },
                                {
                                    "code": "1762-4",
                                    "definition": "Evansville",
                                    "display": "Evansville",
                                },
                                {
                                    "code": "1763-2",
                                    "definition": "Fort Yukon",
                                    "display": "Fort Yukon",
                                },
                                {
                                    "code": "1764-0",
                                    "definition": "Gakona",
                                    "display": "Gakona",
                                },
                                {
                                    "code": "1765-7",
                                    "definition": "Galena",
                                    "display": "Galena",
                                },
                                {
                                    "code": "1766-5",
                                    "definition": "Grayling",
                                    "display": "Grayling",
                                },
                                {
                                    "code": "1767-3",
                                    "definition": "Gulkana",
                                    "display": "Gulkana",
                                },
                                {
                                    "code": "1768-1",
                                    "definition": "Healy Lake",
                                    "display": "Healy Lake",
                                },
                                {
                                    "code": "1769-9",
                                    "definition": "Holy Cross",
                                    "display": "Holy Cross",
                                },
                                {
                                    "code": "1770-7",
                                    "definition": "Hughes",
                                    "display": "Hughes",
                                },
                                {
                                    "code": "1771-5",
                                    "definition": "Huslia",
                                    "display": "Huslia",
                                },
                                {
                                    "code": "1772-3",
                                    "definition": "Iliamna",
                                    "display": "Iliamna",
                                },
                                {
                                    "code": "1773-1",
                                    "definition": "Kaltag",
                                    "display": "Kaltag",
                                },
                                {
                                    "code": "1774-9",
                                    "definition": "Kluti Kaah",
                                    "display": "Kluti Kaah",
                                },
                                {
                                    "code": "1775-6",
                                    "definition": "Knik",
                                    "display": "Knik",
                                },
                                {
                                    "code": "1776-4",
                                    "definition": "Koyukuk",
                                    "display": "Koyukuk",
                                },
                                {
                                    "code": "1777-2",
                                    "definition": "Lake Minchumina",
                                    "display": "Lake Minchumina",
                                },
                                {
                                    "code": "1778-0",
                                    "definition": "Lime",
                                    "display": "Lime",
                                },
                                {
                                    "code": "1779-8",
                                    "definition": "Mcgrath",
                                    "display": "Mcgrath",
                                },
                                {
                                    "code": "1780-6",
                                    "definition": "Manley Hot Springs",
                                    "display": "Manley Hot Springs",
                                },
                                {
                                    "code": "1781-4",
                                    "definition": "Mentasta Lake",
                                    "display": "Mentasta Lake",
                                },
                                {
                                    "code": "1782-2",
                                    "definition": "Minto",
                                    "display": "Minto",
                                },
                                {
                                    "code": "1783-0",
                                    "definition": "Nenana",
                                    "display": "Nenana",
                                },
                                {
                                    "code": "1784-8",
                                    "definition": "Nikolai",
                                    "display": "Nikolai",
                                },
                                {
                                    "code": "1785-5",
                                    "definition": "Ninilchik",
                                    "display": "Ninilchik",
                                },
                                {
                                    "code": "1786-3",
                                    "definition": "Nondalton",
                                    "display": "Nondalton",
                                },
                                {
                                    "code": "1787-1",
                                    "definition": "Northway",
                                    "display": "Northway",
                                },
                                {
                                    "code": "1788-9",
                                    "definition": "Nulato",
                                    "display": "Nulato",
                                },
                                {
                                    "code": "1789-7",
                                    "definition": "Pedro Bay",
                                    "display": "Pedro Bay",
                                },
                                {
                                    "code": "1790-5",
                                    "definition": "Rampart",
                                    "display": "Rampart",
                                },
                                {
                                    "code": "1791-3",
                                    "definition": "Ruby",
                                    "display": "Ruby",
                                },
                                {
                                    "code": "1792-1",
                                    "definition": "Salamatof",
                                    "display": "Salamatof",
                                },
                                {
                                    "code": "1793-9",
                                    "definition": "Seldovia",
                                    "display": "Seldovia",
                                },
                                {
                                    "code": "1794-7",
                                    "definition": "Slana",
                                    "display": "Slana",
                                },
                                {
                                    "code": "1795-4",
                                    "definition": "Shageluk",
                                    "display": "Shageluk",
                                },
                                {
                                    "code": "1796-2",
                                    "definition": "Stevens",
                                    "display": "Stevens",
                                },
                                {
                                    "code": "1797-0",
                                    "definition": "Stony River",
                                    "display": "Stony River",
                                },
                                {
                                    "code": "1798-8",
                                    "definition": "Takotna",
                                    "display": "Takotna",
                                },
                                {
                                    "code": "1799-6",
                                    "definition": "Tanacross",
                                    "display": "Tanacross",
                                },
                                {
                                    "code": "1800-2",
                                    "definition": "Tanaina",
                                    "display": "Tanaina",
                                },
                                {
                                    "code": "1801-0",
                                    "definition": "Tanana",
                                    "display": "Tanana",
                                },
                                {
                                    "code": "1802-8",
                                    "definition": "Tanana Chiefs",
                                    "display": "Tanana Chiefs",
                                },
                                {
                                    "code": "1803-6",
                                    "definition": "Tazlina",
                                    "display": "Tazlina",
                                },
                                {
                                    "code": "1804-4",
                                    "definition": "Telida",
                                    "display": "Telida",
                                },
                                {
                                    "code": "1805-1",
                                    "definition": "Tetlin",
                                    "display": "Tetlin",
                                },
                                {
                                    "code": "1806-9",
                                    "definition": "Tok",
                                    "display": "Tok",
                                },
                                {
                                    "code": "1807-7",
                                    "definition": "Tyonek",
                                    "display": "Tyonek",
                                },
                                {
                                    "code": "1808-5",
                                    "definition": "Venetie",
                                    "display": "Venetie",
                                },
                                {
                                    "code": "1809-3",
                                    "definition": "Wiseman",
                                    "display": "Wiseman",
                                },
                            ],
                            "definition": "Catawba",
                            "display": "Catawba",
                        },
                        {"code": "1078-5", "definition": "Cayuse", "display": "Cayuse"},
                        {
                            "code": "1080-1",
                            "definition": "Chehalis",
                            "display": "Chehalis",
                        },
                        {
                            "code": "1082-7",
                            "concept": [
                                {
                                    "code": "1083-5",
                                    "definition": "Hoh",
                                    "display": "Hoh",
                                },
                                {
                                    "code": "1084-3",
                                    "definition": "Quileute",
                                    "display": "Quileute",
                                },
                            ],
                            "definition": "Chemakuan",
                            "display": "Chemakuan",
                        },
                        {
                            "code": "1086-8",
                            "definition": "Chemehuevi",
                            "display": "Chemehuevi",
                        },
                        {
                            "code": "1088-4",
                            "concept": [
                                {
                                    "code": "1089-2",
                                    "definition": "Cherokee Alabama",
                                    "display": "Cherokee Alabama",
                                },
                                {
                                    "code": "1090-0",
                                    "definition": "Cherokees of Northeast Alabama",
                                    "display": "Cherokees of Northeast Alabama",
                                },
                                {
                                    "code": "1091-8",
                                    "definition": "Cherokees of Southeast Alabama",
                                    "display": "Cherokees of Southeast Alabama",
                                },
                                {
                                    "code": "1092-6",
                                    "definition": "Eastern Cherokee",
                                    "display": "Eastern Cherokee",
                                },
                                {
                                    "code": "1093-4",
                                    "definition": "Echota Cherokee",
                                    "display": "Echota Cherokee",
                                },
                                {
                                    "code": "1094-2",
                                    "definition": "Etowah Cherokee",
                                    "display": "Etowah Cherokee",
                                },
                                {
                                    "code": "1095-9",
                                    "definition": "Northern Cherokee",
                                    "display": "Northern Cherokee",
                                },
                                {
                                    "code": "1096-7",
                                    "definition": "Tuscola",
                                    "display": "Tuscola",
                                },
                                {
                                    "code": "1097-5",
                                    "definition": "United Keetowah Band of Cherokee",
                                    "display": "United Keetowah Band of Cherokee",
                                },
                                {
                                    "code": "1098-3",
                                    "definition": "Western Cherokee",
                                    "display": "Western Cherokee",
                                },
                            ],
                            "definition": "Cherokee",
                            "display": "Cherokee",
                        },
                        {
                            "code": "1100-7",
                            "definition": "Cherokee Shawnee",
                            "display": "Cherokee Shawnee",
                        },
                        {
                            "code": "1102-3",
                            "concept": [
                                {
                                    "code": "1103-1",
                                    "definition": "Northern Cheyenne",
                                    "display": "Northern Cheyenne",
                                },
                                {
                                    "code": "1104-9",
                                    "definition": "Southern Cheyenne",
                                    "display": "Southern Cheyenne",
                                },
                            ],
                            "definition": "Cheyenne",
                            "display": "Cheyenne",
                        },
                        {
                            "code": "1106-4",
                            "definition": "Cheyenne-Arapaho",
                            "display": "Cheyenne-Arapaho",
                        },
                        {
                            "code": "1108-0",
                            "concept": [
                                {
                                    "code": "1109-8",
                                    "definition": "Eastern Chickahominy",
                                    "display": "Eastern Chickahominy",
                                },
                                {
                                    "code": "1110-6",
                                    "definition": "Western Chickahominy",
                                    "display": "Western Chickahominy",
                                },
                            ],
                            "definition": "Chickahominy",
                            "display": "Chickahominy",
                        },
                        {
                            "code": "1112-2",
                            "definition": "Chickasaw",
                            "display": "Chickasaw",
                        },
                        {
                            "code": "1114-8",
                            "concept": [
                                {
                                    "code": "1115-5",
                                    "definition": "Clatsop",
                                    "display": "Clatsop",
                                },
                                {
                                    "code": "1116-3",
                                    "definition": "Columbia River Chinook",
                                    "display": "Columbia River Chinook",
                                },
                                {
                                    "code": "1117-1",
                                    "definition": "Kathlamet",
                                    "display": "Kathlamet",
                                },
                                {
                                    "code": "1118-9",
                                    "definition": "Upper Chinook",
                                    "display": "Upper Chinook",
                                },
                                {
                                    "code": "1119-7",
                                    "definition": "Wakiakum Chinook",
                                    "display": "Wakiakum Chinook",
                                },
                                {
                                    "code": "1120-5",
                                    "definition": "Willapa Chinook",
                                    "display": "Willapa Chinook",
                                },
                                {
                                    "code": "1121-3",
                                    "definition": "Wishram",
                                    "display": "Wishram",
                                },
                            ],
                            "definition": "Chinook",
                            "display": "Chinook",
                        },
                        {
                            "code": "1123-9",
                            "concept": [
                                {
                                    "code": "1124-7",
                                    "definition": "Bad River",
                                    "display": "Bad River",
                                },
                                {
                                    "code": "1125-4",
                                    "definition": "Bay Mills Chippewa",
                                    "display": "Bay Mills Chippewa",
                                },
                                {
                                    "code": "1126-2",
                                    "definition": "Bois Forte",
                                    "display": "Bois Forte",
                                },
                                {
                                    "code": "1127-0",
                                    "definition": "Burt Lake Chippewa",
                                    "display": "Burt Lake Chippewa",
                                },
                                {
                                    "code": "1128-8",
                                    "definition": "Fond du Lac",
                                    "display": "Fond du Lac",
                                },
                                {
                                    "code": "1129-6",
                                    "definition": "Grand Portage",
                                    "display": "Grand Portage",
                                },
                                {
                                    "code": "1130-4",
                                    "definition": "Grand Traverse Band of Ottawa-Chippewa",
                                    "display": "Grand Traverse Band of Ottawa-Chippewa",
                                },
                                {
                                    "code": "1131-2",
                                    "definition": "Keweenaw",
                                    "display": "Keweenaw",
                                },
                                {
                                    "code": "1132-0",
                                    "definition": "Lac Courte Oreilles",
                                    "display": "Lac Courte Oreilles",
                                },
                                {
                                    "code": "1133-8",
                                    "definition": "Lac du Flambeau",
                                    "display": "Lac du Flambeau",
                                },
                                {
                                    "code": "1134-6",
                                    "definition": "Lac Vieux Desert Chippewa",
                                    "display": "Lac Vieux Desert Chippewa",
                                },
                                {
                                    "code": "1135-3",
                                    "definition": "Lake Superior",
                                    "display": "Lake Superior",
                                },
                                {
                                    "code": "1136-1",
                                    "definition": "Leech Lake",
                                    "display": "Leech Lake",
                                },
                                {
                                    "code": "1137-9",
                                    "definition": "Little Shell Chippewa",
                                    "display": "Little Shell Chippewa",
                                },
                                {
                                    "code": "1138-7",
                                    "definition": "Mille Lacs",
                                    "display": "Mille Lacs",
                                },
                                {
                                    "code": "1139-5",
                                    "definition": "Minnesota Chippewa",
                                    "display": "Minnesota Chippewa",
                                },
                                {
                                    "code": "1140-3",
                                    "definition": "Ontonagon",
                                    "display": "Ontonagon",
                                },
                                {
                                    "code": "1141-1",
                                    "definition": "Red Cliff Chippewa",
                                    "display": "Red Cliff Chippewa",
                                },
                                {
                                    "code": "1142-9",
                                    "definition": "Red Lake Chippewa",
                                    "display": "Red Lake Chippewa",
                                },
                                {
                                    "code": "1143-7",
                                    "definition": "Saginaw Chippewa",
                                    "display": "Saginaw Chippewa",
                                },
                                {
                                    "code": "1144-5",
                                    "definition": "St. Croix Chippewa",
                                    "display": "St. Croix Chippewa",
                                },
                                {
                                    "code": "1145-2",
                                    "definition": "Sault Ste. Marie Chippewa",
                                    "display": "Sault Ste. Marie Chippewa",
                                },
                                {
                                    "code": "1146-0",
                                    "definition": "Sokoagon Chippewa",
                                    "display": "Sokoagon Chippewa",
                                },
                                {
                                    "code": "1147-8",
                                    "definition": "Turtle Mountain",
                                    "display": "Turtle Mountain",
                                },
                                {
                                    "code": "1148-6",
                                    "definition": "White Earth",
                                    "display": "White Earth",
                                },
                            ],
                            "definition": "Chippewa",
                            "display": "Chippewa",
                        },
                        {
                            "code": "1150-2",
                            "concept": [
                                {
                                    "code": "1151-0",
                                    "definition": "Rocky Boy's Chippewa Cree",
                                    "display": "Rocky Boy's Chippewa Cree",
                                }
                            ],
                            "definition": "Chippewa Cree",
                            "display": "Chippewa Cree",
                        },
                        {
                            "code": "1153-6",
                            "definition": "Chitimacha",
                            "display": "Chitimacha",
                        },
                        {
                            "code": "1155-1",
                            "concept": [
                                {
                                    "code": "1156-9",
                                    "definition": "Clifton Choctaw",
                                    "display": "Clifton Choctaw",
                                },
                                {
                                    "code": "1157-7",
                                    "definition": "Jena Choctaw",
                                    "display": "Jena Choctaw",
                                },
                                {
                                    "code": "1158-5",
                                    "definition": "Mississippi Choctaw",
                                    "display": "Mississippi Choctaw",
                                },
                                {
                                    "code": "1159-3",
                                    "definition": "Mowa Band of Choctaw",
                                    "display": "Mowa Band of Choctaw",
                                },
                                {
                                    "code": "1160-1",
                                    "definition": "Oklahoma Choctaw",
                                    "display": "Oklahoma Choctaw",
                                },
                            ],
                            "definition": "Choctaw",
                            "display": "Choctaw",
                        },
                        {
                            "code": "1162-7",
                            "concept": [
                                {
                                    "code": "1163-5",
                                    "definition": "Santa Ynez",
                                    "display": "Santa Ynez",
                                }
                            ],
                            "definition": "Chumash",
                            "display": "Chumash",
                        },
                        {
                            "code": "1165-0",
                            "definition": "Clear Lake",
                            "display": "Clear Lake",
                        },
                        {
                            "code": "1167-6",
                            "definition": "Coeur D'Alene",
                            "display": "Coeur D'Alene",
                        },
                        {
                            "code": "1169-2",
                            "definition": "Coharie",
                            "display": "Coharie",
                        },
                        {
                            "code": "1171-8",
                            "definition": "Colorado River",
                            "display": "Colorado River",
                        },
                        {
                            "code": "1173-4",
                            "definition": "Colville",
                            "display": "Colville",
                        },
                        {
                            "code": "1175-9",
                            "concept": [
                                {
                                    "code": "1176-7",
                                    "definition": "Oklahoma Comanche",
                                    "display": "Oklahoma Comanche",
                                }
                            ],
                            "definition": "Comanche",
                            "display": "Comanche",
                        },
                        {
                            "code": "1178-3",
                            "definition": "Coos, Lower Umpqua, Siuslaw",
                            "display": "Coos, Lower Umpqua, Siuslaw",
                        },
                        {"code": "1180-9", "definition": "Coos", "display": "Coos"},
                        {
                            "code": "1182-5",
                            "definition": "Coquilles",
                            "display": "Coquilles",
                        },
                        {
                            "code": "1184-1",
                            "definition": "Costanoan",
                            "display": "Costanoan",
                        },
                        {
                            "code": "1186-6",
                            "concept": [
                                {
                                    "code": "1187-4",
                                    "definition": "Alabama Coushatta",
                                    "display": "Alabama Coushatta",
                                }
                            ],
                            "definition": "Coushatta",
                            "display": "Coushatta",
                        },
                        {
                            "code": "1189-0",
                            "definition": "Cowlitz",
                            "display": "Cowlitz",
                        },
                        {"code": "1191-6", "definition": "Cree", "display": "Cree"},
                        {
                            "code": "1193-2",
                            "concept": [
                                {
                                    "code": "1194-0",
                                    "definition": "Alabama Creek",
                                    "display": "Alabama Creek",
                                },
                                {
                                    "code": "1195-7",
                                    "definition": "Alabama Quassarte",
                                    "display": "Alabama Quassarte",
                                },
                                {
                                    "code": "1196-5",
                                    "definition": "Eastern Creek",
                                    "display": "Eastern Creek",
                                },
                                {
                                    "code": "1197-3",
                                    "definition": "Eastern Muscogee",
                                    "display": "Eastern Muscogee",
                                },
                                {
                                    "code": "1198-1",
                                    "definition": "Kialegee",
                                    "display": "Kialegee",
                                },
                                {
                                    "code": "1199-9",
                                    "definition": "Lower Muscogee",
                                    "display": "Lower Muscogee",
                                },
                                {
                                    "code": "1200-5",
                                    "definition": "Machis Lower Creek Indian",
                                    "display": "Machis Lower Creek Indian",
                                },
                                {
                                    "code": "1201-3",
                                    "definition": "Poarch Band",
                                    "display": "Poarch Band",
                                },
                                {
                                    "code": "1202-1",
                                    "definition": "Principal Creek Indian Nation",
                                    "display": "Principal Creek Indian Nation",
                                },
                                {
                                    "code": "1203-9",
                                    "definition": "Star Clan of Muscogee Creeks",
                                    "display": "Star Clan of Muscogee Creeks",
                                },
                                {
                                    "code": "1204-7",
                                    "definition": "Thlopthlocco",
                                    "display": "Thlopthlocco",
                                },
                                {
                                    "code": "1205-4",
                                    "definition": "Tuckabachee",
                                    "display": "Tuckabachee",
                                },
                            ],
                            "definition": "Creek",
                            "display": "Creek",
                        },
                        {
                            "code": "1207-0",
                            "definition": "Croatan",
                            "display": "Croatan",
                        },
                        {"code": "1209-6", "definition": "Crow", "display": "Crow"},
                        {
                            "code": "1211-2",
                            "concept": [
                                {
                                    "code": "1212-0",
                                    "definition": "Agua Caliente",
                                    "display": "Agua Caliente",
                                }
                            ],
                            "definition": "Cupeno",
                            "display": "Cupeno",
                        },
                        {
                            "code": "1214-6",
                            "concept": [
                                {
                                    "code": "1215-3",
                                    "definition": "Eastern Delaware",
                                    "display": "Eastern Delaware",
                                },
                                {
                                    "code": "1216-1",
                                    "definition": "Lenni-Lenape",
                                    "display": "Lenni-Lenape",
                                },
                                {
                                    "code": "1217-9",
                                    "definition": "Munsee",
                                    "display": "Munsee",
                                },
                                {
                                    "code": "1218-7",
                                    "definition": "Oklahoma Delaware",
                                    "display": "Oklahoma Delaware",
                                },
                                {
                                    "code": "1219-5",
                                    "definition": "Rampough Mountain",
                                    "display": "Rampough Mountain",
                                },
                                {
                                    "code": "1220-3",
                                    "definition": "Sand Hill",
                                    "display": "Sand Hill",
                                },
                            ],
                            "definition": "Delaware",
                            "display": "Delaware",
                        },
                        {
                            "code": "1222-9",
                            "concept": [
                                {
                                    "code": "1223-7",
                                    "definition": "Campo",
                                    "display": "Campo",
                                },
                                {
                                    "code": "1224-5",
                                    "definition": "Capitan Grande",
                                    "display": "Capitan Grande",
                                },
                                {
                                    "code": "1225-2",
                                    "definition": "Cuyapaipe",
                                    "display": "Cuyapaipe",
                                },
                                {
                                    "code": "1226-0",
                                    "definition": "La Posta",
                                    "display": "La Posta",
                                },
                                {
                                    "code": "1227-8",
                                    "definition": "Manzanita",
                                    "display": "Manzanita",
                                },
                                {
                                    "code": "1228-6",
                                    "definition": "Mesa Grande",
                                    "display": "Mesa Grande",
                                },
                                {
                                    "code": "1229-4",
                                    "definition": "San Pasqual",
                                    "display": "San Pasqual",
                                },
                                {
                                    "code": "1230-2",
                                    "definition": "Santa Ysabel",
                                    "display": "Santa Ysabel",
                                },
                                {
                                    "code": "1231-0",
                                    "definition": "Sycuan",
                                    "display": "Sycuan",
                                },
                            ],
                            "definition": "Diegueno",
                            "display": "Diegueno",
                        },
                        {
                            "code": "1233-6",
                            "concept": [
                                {
                                    "code": "1234-4",
                                    "definition": "Attacapa",
                                    "display": "Attacapa",
                                },
                                {
                                    "code": "1235-1",
                                    "definition": "Biloxi",
                                    "display": "Biloxi",
                                },
                                {
                                    "code": "1236-9",
                                    "definition": "Georgetown",
                                    "display": "Georgetown",
                                },
                                {
                                    "code": "1237-7",
                                    "definition": "Moor",
                                    "display": "Moor",
                                },
                                {
                                    "code": "1238-5",
                                    "definition": "Nansemond",
                                    "display": "Nansemond",
                                },
                                {
                                    "code": "1239-3",
                                    "definition": "Natchez",
                                    "display": "Natchez",
                                },
                                {
                                    "code": "1240-1",
                                    "definition": "Nausu Waiwash",
                                    "display": "Nausu Waiwash",
                                },
                                {
                                    "code": "1241-9",
                                    "definition": "Nipmuc",
                                    "display": "Nipmuc",
                                },
                                {
                                    "code": "1242-7",
                                    "definition": "Paugussett",
                                    "display": "Paugussett",
                                },
                                {
                                    "code": "1243-5",
                                    "definition": "Pocomoke Acohonock",
                                    "display": "Pocomoke Acohonock",
                                },
                                {
                                    "code": "1244-3",
                                    "definition": "Southeastern Indians",
                                    "display": "Southeastern Indians",
                                },
                                {
                                    "code": "1245-0",
                                    "definition": "Susquehanock",
                                    "display": "Susquehanock",
                                },
                                {
                                    "code": "1246-8",
                                    "definition": "Tunica Biloxi",
                                    "display": "Tunica Biloxi",
                                },
                                {
                                    "code": "1247-6",
                                    "definition": "Waccamaw-Siousan",
                                    "display": "Waccamaw-Siousan",
                                },
                                {
                                    "code": "1248-4",
                                    "definition": "Wicomico",
                                    "display": "Wicomico",
                                },
                            ],
                            "definition": "Eastern Tribes",
                            "display": "Eastern Tribes",
                        },
                        {
                            "code": "1250-0",
                            "definition": "Esselen",
                            "display": "Esselen",
                        },
                        {
                            "code": "1252-6",
                            "definition": "Fort Belknap",
                            "display": "Fort Belknap",
                        },
                        {
                            "code": "1254-2",
                            "definition": "Fort Berthold",
                            "display": "Fort Berthold",
                        },
                        {
                            "code": "1256-7",
                            "definition": "Fort Mcdowell",
                            "display": "Fort Mcdowell",
                        },
                        {
                            "code": "1258-3",
                            "definition": "Fort Hall",
                            "display": "Fort Hall",
                        },
                        {
                            "code": "1260-9",
                            "definition": "Gabrieleno",
                            "display": "Gabrieleno",
                        },
                        {
                            "code": "1262-5",
                            "definition": "Grand Ronde",
                            "display": "Grand Ronde",
                        },
                        {
                            "code": "1264-1",
                            "concept": [
                                {
                                    "code": "1265-8",
                                    "definition": "Atsina",
                                    "display": "Atsina",
                                }
                            ],
                            "definition": "Gros Ventres",
                            "display": "Gros Ventres",
                        },
                        {"code": "1267-4", "definition": "Haliwa", "display": "Haliwa"},
                        {
                            "code": "1269-0",
                            "definition": "Hidatsa",
                            "display": "Hidatsa",
                        },
                        {
                            "code": "1271-6",
                            "concept": [
                                {
                                    "code": "1272-4",
                                    "definition": "Trinity",
                                    "display": "Trinity",
                                },
                                {
                                    "code": "1273-2",
                                    "definition": "Whilkut",
                                    "display": "Whilkut",
                                },
                            ],
                            "definition": "Hoopa",
                            "display": "Hoopa",
                        },
                        {
                            "code": "1275-7",
                            "definition": "Hoopa Extension",
                            "display": "Hoopa Extension",
                        },
                        {"code": "1277-3", "definition": "Houma", "display": "Houma"},
                        {
                            "code": "1279-9",
                            "definition": "Inaja-Cosmit",
                            "display": "Inaja-Cosmit",
                        },
                        {
                            "code": "1281-5",
                            "concept": [
                                {
                                    "code": "1282-3",
                                    "definition": "Iowa of Kansas-Nebraska",
                                    "display": "Iowa of Kansas-Nebraska",
                                },
                                {
                                    "code": "1283-1",
                                    "definition": "Iowa of Oklahoma",
                                    "display": "Iowa of Oklahoma",
                                },
                            ],
                            "definition": "Iowa",
                            "display": "Iowa",
                        },
                        {
                            "code": "1285-6",
                            "concept": [
                                {
                                    "code": "1286-4",
                                    "definition": "Cayuga",
                                    "display": "Cayuga",
                                },
                                {
                                    "code": "1287-2",
                                    "definition": "Mohawk",
                                    "display": "Mohawk",
                                },
                                {
                                    "code": "1288-0",
                                    "definition": "Oneida",
                                    "display": "Oneida",
                                },
                                {
                                    "code": "1289-8",
                                    "definition": "Onondaga",
                                    "display": "Onondaga",
                                },
                                {
                                    "code": "1290-6",
                                    "definition": "Seneca",
                                    "display": "Seneca",
                                },
                                {
                                    "code": "1291-4",
                                    "definition": "Seneca Nation",
                                    "display": "Seneca Nation",
                                },
                                {
                                    "code": "1292-2",
                                    "definition": "Seneca-Cayuga",
                                    "display": "Seneca-Cayuga",
                                },
                                {
                                    "code": "1293-0",
                                    "definition": "Tonawanda Seneca",
                                    "display": "Tonawanda Seneca",
                                },
                                {
                                    "code": "1294-8",
                                    "definition": "Tuscarora",
                                    "display": "Tuscarora",
                                },
                                {
                                    "code": "1295-5",
                                    "definition": "Wyandotte",
                                    "display": "Wyandotte",
                                },
                            ],
                            "definition": "Iroquois",
                            "display": "Iroquois",
                        },
                        {
                            "code": "1297-1",
                            "definition": "Juaneno",
                            "display": "Juaneno",
                        },
                        {
                            "code": "1299-7",
                            "definition": "Kalispel",
                            "display": "Kalispel",
                        },
                        {"code": "1301-1", "definition": "Karuk", "display": "Karuk"},
                        {"code": "1303-7", "definition": "Kaw", "display": "Kaw"},
                        {
                            "code": "1305-2",
                            "concept": [
                                {
                                    "code": "1306-0",
                                    "definition": "Oklahoma Kickapoo",
                                    "display": "Oklahoma Kickapoo",
                                },
                                {
                                    "code": "1307-8",
                                    "definition": "Texas Kickapoo",
                                    "display": "Texas Kickapoo",
                                },
                            ],
                            "definition": "Kickapoo",
                            "display": "Kickapoo",
                        },
                        {
                            "code": "1309-4",
                            "concept": [
                                {
                                    "code": "1310-2",
                                    "definition": "Oklahoma Kiowa",
                                    "display": "Oklahoma Kiowa",
                                }
                            ],
                            "definition": "Kiowa",
                            "display": "Kiowa",
                        },
                        {
                            "code": "1312-8",
                            "concept": [
                                {
                                    "code": "1313-6",
                                    "definition": "Jamestown",
                                    "display": "Jamestown",
                                },
                                {
                                    "code": "1314-4",
                                    "definition": "Lower Elwha",
                                    "display": "Lower Elwha",
                                },
                                {
                                    "code": "1315-1",
                                    "definition": "Port Gamble Klallam",
                                    "display": "Port Gamble Klallam",
                                },
                            ],
                            "definition": "Klallam",
                            "display": "Klallam",
                        },
                        {
                            "code": "1317-7",
                            "definition": "Klamath",
                            "display": "Klamath",
                        },
                        {"code": "1319-3", "definition": "Konkow", "display": "Konkow"},
                        {
                            "code": "1321-9",
                            "definition": "Kootenai",
                            "display": "Kootenai",
                        },
                        {"code": "1323-5", "definition": "Lassik", "display": "Lassik"},
                        {
                            "code": "1325-0",
                            "concept": [
                                {
                                    "code": "1326-8",
                                    "definition": "Matinecock",
                                    "display": "Matinecock",
                                },
                                {
                                    "code": "1327-6",
                                    "definition": "Montauk",
                                    "display": "Montauk",
                                },
                                {
                                    "code": "1328-4",
                                    "definition": "Poospatuck",
                                    "display": "Poospatuck",
                                },
                                {
                                    "code": "1329-2",
                                    "definition": "Setauket",
                                    "display": "Setauket",
                                },
                            ],
                            "definition": "Long Island",
                            "display": "Long Island",
                        },
                        {
                            "code": "1331-8",
                            "concept": [
                                {
                                    "code": "1332-6",
                                    "definition": "La Jolla",
                                    "display": "La Jolla",
                                },
                                {
                                    "code": "1333-4",
                                    "definition": "Pala",
                                    "display": "Pala",
                                },
                                {
                                    "code": "1334-2",
                                    "definition": "Pauma",
                                    "display": "Pauma",
                                },
                                {
                                    "code": "1335-9",
                                    "definition": "Pechanga",
                                    "display": "Pechanga",
                                },
                                {
                                    "code": "1336-7",
                                    "definition": "Soboba",
                                    "display": "Soboba",
                                },
                                {
                                    "code": "1337-5",
                                    "definition": "Twenty-Nine Palms",
                                    "display": "Twenty-Nine Palms",
                                },
                                {
                                    "code": "1338-3",
                                    "definition": "Temecula",
                                    "display": "Temecula",
                                },
                            ],
                            "definition": "Luiseno",
                            "display": "Luiseno",
                        },
                        {"code": "1340-9", "definition": "Lumbee", "display": "Lumbee"},
                        {"code": "1342-5", "definition": "Lummi", "display": "Lummi"},
                        {
                            "code": "1344-1",
                            "concept": [
                                {
                                    "code": "1345-8",
                                    "definition": "Mountain Maidu",
                                    "display": "Mountain Maidu",
                                },
                                {
                                    "code": "1346-6",
                                    "definition": "Nishinam",
                                    "display": "Nishinam",
                                },
                            ],
                            "definition": "Maidu",
                            "display": "Maidu",
                        },
                        {"code": "1348-2", "definition": "Makah", "display": "Makah"},
                        {
                            "code": "1350-8",
                            "definition": "Maliseet",
                            "display": "Maliseet",
                        },
                        {"code": "1352-4", "definition": "Mandan", "display": "Mandan"},
                        {
                            "code": "1354-0",
                            "definition": "Mattaponi",
                            "display": "Mattaponi",
                        },
                        {
                            "code": "1356-5",
                            "definition": "Menominee",
                            "display": "Menominee",
                        },
                        {
                            "code": "1358-1",
                            "concept": [
                                {
                                    "code": "1359-9",
                                    "definition": "Illinois Miami",
                                    "display": "Illinois Miami",
                                },
                                {
                                    "code": "1360-7",
                                    "definition": "Indiana Miami",
                                    "display": "Indiana Miami",
                                },
                                {
                                    "code": "1361-5",
                                    "definition": "Oklahoma Miami",
                                    "display": "Oklahoma Miami",
                                },
                            ],
                            "definition": "Miami",
                            "display": "Miami",
                        },
                        {
                            "code": "1363-1",
                            "definition": "Miccosukee",
                            "display": "Miccosukee",
                        },
                        {
                            "code": "1365-6",
                            "concept": [
                                {
                                    "code": "1366-4",
                                    "definition": "Aroostook",
                                    "display": "Aroostook",
                                }
                            ],
                            "definition": "Micmac",
                            "display": "Micmac",
                        },
                        {
                            "code": "1368-0",
                            "definition": "Mission Indians",
                            "display": "Mission Indians",
                        },
                        {"code": "1370-6", "definition": "Miwok", "display": "Miwok"},
                        {"code": "1372-2", "definition": "Modoc", "display": "Modoc"},
                        {
                            "code": "1374-8",
                            "definition": "Mohegan",
                            "display": "Mohegan",
                        },
                        {"code": "1376-3", "definition": "Mono", "display": "Mono"},
                        {
                            "code": "1378-9",
                            "definition": "Nanticoke",
                            "display": "Nanticoke",
                        },
                        {
                            "code": "1380-5",
                            "definition": "Narragansett",
                            "display": "Narragansett",
                        },
                        {
                            "code": "1382-1",
                            "concept": [
                                {
                                    "code": "1383-9",
                                    "definition": "Alamo Navajo",
                                    "display": "Alamo Navajo",
                                },
                                {
                                    "code": "1384-7",
                                    "definition": "Canoncito Navajo",
                                    "display": "Canoncito Navajo",
                                },
                                {
                                    "code": "1385-4",
                                    "definition": "Ramah Navajo",
                                    "display": "Ramah Navajo",
                                },
                            ],
                            "definition": "Navajo",
                            "display": "Navajo",
                        },
                        {
                            "code": "1387-0",
                            "definition": "Nez Perce",
                            "display": "Nez Perce",
                        },
                        {
                            "code": "1389-6",
                            "definition": "Nomalaki",
                            "display": "Nomalaki",
                        },
                        {
                            "code": "1391-2",
                            "concept": [
                                {
                                    "code": "1392-0",
                                    "definition": "Alsea",
                                    "display": "Alsea",
                                },
                                {
                                    "code": "1393-8",
                                    "definition": "Celilo",
                                    "display": "Celilo",
                                },
                                {
                                    "code": "1394-6",
                                    "definition": "Columbia",
                                    "display": "Columbia",
                                },
                                {
                                    "code": "1395-3",
                                    "definition": "Kalapuya",
                                    "display": "Kalapuya",
                                },
                                {
                                    "code": "1396-1",
                                    "definition": "Molala",
                                    "display": "Molala",
                                },
                                {
                                    "code": "1397-9",
                                    "definition": "Talakamish",
                                    "display": "Talakamish",
                                },
                                {
                                    "code": "1398-7",
                                    "definition": "Tenino",
                                    "display": "Tenino",
                                },
                                {
                                    "code": "1399-5",
                                    "definition": "Tillamook",
                                    "display": "Tillamook",
                                },
                                {
                                    "code": "1400-1",
                                    "definition": "Wenatchee",
                                    "display": "Wenatchee",
                                },
                                {
                                    "code": "1401-9",
                                    "definition": "Yahooskin",
                                    "display": "Yahooskin",
                                },
                            ],
                            "definition": "Northwest Tribes",
                            "display": "Northwest Tribes",
                        },
                        {"code": "1403-5", "definition": "Omaha", "display": "Omaha"},
                        {
                            "code": "1405-0",
                            "definition": "Oregon Athabaskan",
                            "display": "Oregon Athabaskan",
                        },
                        {"code": "1407-6", "definition": "Osage", "display": "Osage"},
                        {
                            "code": "1409-2",
                            "definition": "Otoe-Missouria",
                            "display": "Otoe-Missouria",
                        },
                        {
                            "code": "1411-8",
                            "concept": [
                                {
                                    "code": "1412-6",
                                    "definition": "Burt Lake Ottawa",
                                    "display": "Burt Lake Ottawa",
                                },
                                {
                                    "code": "1413-4",
                                    "definition": "Michigan Ottawa",
                                    "display": "Michigan Ottawa",
                                },
                                {
                                    "code": "1414-2",
                                    "definition": "Oklahoma Ottawa",
                                    "display": "Oklahoma Ottawa",
                                },
                            ],
                            "definition": "Ottawa",
                            "display": "Ottawa",
                        },
                        {
                            "code": "1416-7",
                            "concept": [
                                {
                                    "code": "1417-5",
                                    "definition": "Bishop",
                                    "display": "Bishop",
                                },
                                {
                                    "code": "1418-3",
                                    "definition": "Bridgeport",
                                    "display": "Bridgeport",
                                },
                                {
                                    "code": "1419-1",
                                    "definition": "Burns Paiute",
                                    "display": "Burns Paiute",
                                },
                                {
                                    "code": "1420-9",
                                    "definition": "Cedarville",
                                    "display": "Cedarville",
                                },
                                {
                                    "code": "1421-7",
                                    "definition": "Fort Bidwell",
                                    "display": "Fort Bidwell",
                                },
                                {
                                    "code": "1422-5",
                                    "definition": "Fort Independence",
                                    "display": "Fort Independence",
                                },
                                {
                                    "code": "1423-3",
                                    "definition": "Kaibab",
                                    "display": "Kaibab",
                                },
                                {
                                    "code": "1424-1",
                                    "definition": "Las Vegas",
                                    "display": "Las Vegas",
                                },
                                {
                                    "code": "1425-8",
                                    "definition": "Lone Pine",
                                    "display": "Lone Pine",
                                },
                                {
                                    "code": "1426-6",
                                    "definition": "Lovelock",
                                    "display": "Lovelock",
                                },
                                {
                                    "code": "1427-4",
                                    "definition": "Malheur Paiute",
                                    "display": "Malheur Paiute",
                                },
                                {
                                    "code": "1428-2",
                                    "definition": "Moapa",
                                    "display": "Moapa",
                                },
                                {
                                    "code": "1429-0",
                                    "definition": "Northern Paiute",
                                    "display": "Northern Paiute",
                                },
                                {
                                    "code": "1430-8",
                                    "definition": "Owens Valley",
                                    "display": "Owens Valley",
                                },
                                {
                                    "code": "1431-6",
                                    "definition": "Pyramid Lake",
                                    "display": "Pyramid Lake",
                                },
                                {
                                    "code": "1432-4",
                                    "definition": "San Juan Southern Paiute",
                                    "display": "San Juan Southern Paiute",
                                },
                                {
                                    "code": "1433-2",
                                    "definition": "Southern Paiute",
                                    "display": "Southern Paiute",
                                },
                                {
                                    "code": "1434-0",
                                    "definition": "Summit Lake",
                                    "display": "Summit Lake",
                                },
                                {
                                    "code": "1435-7",
                                    "definition": "Utu Utu Gwaitu Paiute",
                                    "display": "Utu Utu Gwaitu Paiute",
                                },
                                {
                                    "code": "1436-5",
                                    "definition": "Walker River",
                                    "display": "Walker River",
                                },
                                {
                                    "code": "1437-3",
                                    "definition": "Yerington Paiute",
                                    "display": "Yerington Paiute",
                                },
                            ],
                            "definition": "Paiute",
                            "display": "Paiute",
                        },
                        {
                            "code": "1439-9",
                            "definition": "Pamunkey",
                            "display": "Pamunkey",
                        },
                        {
                            "code": "1441-5",
                            "concept": [
                                {
                                    "code": "1442-3",
                                    "definition": "Indian Township",
                                    "display": "Indian Township",
                                },
                                {
                                    "code": "1443-1",
                                    "definition": "Pleasant Point Passamaquoddy",
                                    "display": "Pleasant Point Passamaquoddy",
                                },
                            ],
                            "definition": "Passamaquoddy",
                            "display": "Passamaquoddy",
                        },
                        {
                            "code": "1445-6",
                            "concept": [
                                {
                                    "code": "1446-4",
                                    "definition": "Oklahoma Pawnee",
                                    "display": "Oklahoma Pawnee",
                                }
                            ],
                            "definition": "Pawnee",
                            "display": "Pawnee",
                        },
                        {
                            "code": "1448-0",
                            "definition": "Penobscot",
                            "display": "Penobscot",
                        },
                        {
                            "code": "1450-6",
                            "concept": [
                                {
                                    "code": "1451-4",
                                    "definition": "Oklahoma Peoria",
                                    "display": "Oklahoma Peoria",
                                }
                            ],
                            "definition": "Peoria",
                            "display": "Peoria",
                        },
                        {
                            "code": "1453-0",
                            "concept": [
                                {
                                    "code": "1454-8",
                                    "definition": "Marshantucket Pequot",
                                    "display": "Marshantucket Pequot",
                                }
                            ],
                            "definition": "Pequot",
                            "display": "Pequot",
                        },
                        {
                            "code": "1456-3",
                            "concept": [
                                {
                                    "code": "1457-1",
                                    "definition": "Gila River Pima-Maricopa",
                                    "display": "Gila River Pima-Maricopa",
                                },
                                {
                                    "code": "1458-9",
                                    "definition": "Salt River Pima-Maricopa",
                                    "display": "Salt River Pima-Maricopa",
                                },
                            ],
                            "definition": "Pima",
                            "display": "Pima",
                        },
                        {
                            "code": "1460-5",
                            "definition": "Piscataway",
                            "display": "Piscataway",
                        },
                        {
                            "code": "1462-1",
                            "definition": "Pit River",
                            "display": "Pit River",
                        },
                        {
                            "code": "1464-7",
                            "concept": [
                                {
                                    "code": "1465-4",
                                    "definition": "Central Pomo",
                                    "display": "Central Pomo",
                                },
                                {
                                    "code": "1466-2",
                                    "definition": "Dry Creek",
                                    "display": "Dry Creek",
                                },
                                {
                                    "code": "1467-0",
                                    "definition": "Eastern Pomo",
                                    "display": "Eastern Pomo",
                                },
                                {
                                    "code": "1468-8",
                                    "definition": "Kashia",
                                    "display": "Kashia",
                                },
                                {
                                    "code": "1469-6",
                                    "definition": "Northern Pomo",
                                    "display": "Northern Pomo",
                                },
                                {
                                    "code": "1470-4",
                                    "definition": "Scotts Valley",
                                    "display": "Scotts Valley",
                                },
                                {
                                    "code": "1471-2",
                                    "definition": "Stonyford",
                                    "display": "Stonyford",
                                },
                                {
                                    "code": "1472-0",
                                    "definition": "Sulphur Bank",
                                    "display": "Sulphur Bank",
                                },
                            ],
                            "definition": "Pomo",
                            "display": "Pomo",
                        },
                        {
                            "code": "1474-6",
                            "concept": [
                                {
                                    "code": "1475-3",
                                    "definition": "Nebraska Ponca",
                                    "display": "Nebraska Ponca",
                                },
                                {
                                    "code": "1476-1",
                                    "definition": "Oklahoma Ponca",
                                    "display": "Oklahoma Ponca",
                                },
                            ],
                            "definition": "Ponca",
                            "display": "Ponca",
                        },
                        {
                            "code": "1478-7",
                            "concept": [
                                {
                                    "code": "1479-5",
                                    "definition": "Citizen Band Potawatomi",
                                    "display": "Citizen Band Potawatomi",
                                },
                                {
                                    "code": "1480-3",
                                    "definition": "Forest County",
                                    "display": "Forest County",
                                },
                                {
                                    "code": "1481-1",
                                    "definition": "Hannahville",
                                    "display": "Hannahville",
                                },
                                {
                                    "code": "1482-9",
                                    "definition": "Huron Potawatomi",
                                    "display": "Huron Potawatomi",
                                },
                                {
                                    "code": "1483-7",
                                    "definition": "Pokagon Potawatomi",
                                    "display": "Pokagon Potawatomi",
                                },
                                {
                                    "code": "1484-5",
                                    "definition": "Prairie Band",
                                    "display": "Prairie Band",
                                },
                                {
                                    "code": "1485-2",
                                    "definition": "Wisconsin Potawatomi",
                                    "display": "Wisconsin Potawatomi",
                                },
                            ],
                            "definition": "Potawatomi",
                            "display": "Potawatomi",
                        },
                        {
                            "code": "1487-8",
                            "definition": "Powhatan",
                            "display": "Powhatan",
                        },
                        {
                            "code": "1489-4",
                            "concept": [
                                {
                                    "code": "1490-2",
                                    "definition": "Acoma",
                                    "display": "Acoma",
                                },
                                {
                                    "code": "1491-0",
                                    "definition": "Arizona Tewa",
                                    "display": "Arizona Tewa",
                                },
                                {
                                    "code": "1492-8",
                                    "definition": "Cochiti",
                                    "display": "Cochiti",
                                },
                                {
                                    "code": "1493-6",
                                    "definition": "Hopi",
                                    "display": "Hopi",
                                },
                                {
                                    "code": "1494-4",
                                    "definition": "Isleta",
                                    "display": "Isleta",
                                },
                                {
                                    "code": "1495-1",
                                    "definition": "Jemez",
                                    "display": "Jemez",
                                },
                                {
                                    "code": "1496-9",
                                    "definition": "Keres",
                                    "display": "Keres",
                                },
                                {
                                    "code": "1497-7",
                                    "definition": "Laguna",
                                    "display": "Laguna",
                                },
                                {
                                    "code": "1498-5",
                                    "definition": "Nambe",
                                    "display": "Nambe",
                                },
                                {
                                    "code": "1499-3",
                                    "definition": "Picuris",
                                    "display": "Picuris",
                                },
                                {
                                    "code": "1500-8",
                                    "definition": "Piro",
                                    "display": "Piro",
                                },
                                {
                                    "code": "1501-6",
                                    "definition": "Pojoaque",
                                    "display": "Pojoaque",
                                },
                                {
                                    "code": "1502-4",
                                    "definition": "San Felipe",
                                    "display": "San Felipe",
                                },
                                {
                                    "code": "1503-2",
                                    "definition": "San Ildefonso",
                                    "display": "San Ildefonso",
                                },
                                {
                                    "code": "1504-0",
                                    "definition": "San Juan Pueblo",
                                    "display": "San Juan Pueblo",
                                },
                                {
                                    "code": "1505-7",
                                    "definition": "San Juan De",
                                    "display": "San Juan De",
                                },
                                {
                                    "code": "1506-5",
                                    "definition": "San Juan",
                                    "display": "San Juan",
                                },
                                {
                                    "code": "1507-3",
                                    "definition": "Sandia",
                                    "display": "Sandia",
                                },
                                {
                                    "code": "1508-1",
                                    "definition": "Santa Ana",
                                    "display": "Santa Ana",
                                },
                                {
                                    "code": "1509-9",
                                    "definition": "Santa Clara",
                                    "display": "Santa Clara",
                                },
                                {
                                    "code": "1510-7",
                                    "definition": "Santo Domingo",
                                    "display": "Santo Domingo",
                                },
                                {
                                    "code": "1511-5",
                                    "definition": "Taos",
                                    "display": "Taos",
                                },
                                {
                                    "code": "1512-3",
                                    "definition": "Tesuque",
                                    "display": "Tesuque",
                                },
                                {
                                    "code": "1513-1",
                                    "definition": "Tewa",
                                    "display": "Tewa",
                                },
                                {
                                    "code": "1514-9",
                                    "definition": "Tigua",
                                    "display": "Tigua",
                                },
                                {
                                    "code": "1515-6",
                                    "definition": "Zia",
                                    "display": "Zia",
                                },
                                {
                                    "code": "1516-4",
                                    "definition": "Zuni",
                                    "display": "Zuni",
                                },
                            ],
                            "definition": "Pueblo",
                            "display": "Pueblo",
                        },
                        {
                            "code": "1518-0",
                            "concept": [
                                {
                                    "code": "1519-8",
                                    "definition": "Duwamish",
                                    "display": "Duwamish",
                                },
                                {
                                    "code": "1520-6",
                                    "definition": "Kikiallus",
                                    "display": "Kikiallus",
                                },
                                {
                                    "code": "1521-4",
                                    "definition": "Lower Skagit",
                                    "display": "Lower Skagit",
                                },
                                {
                                    "code": "1522-2",
                                    "definition": "Muckleshoot",
                                    "display": "Muckleshoot",
                                },
                                {
                                    "code": "1523-0",
                                    "definition": "Nisqually",
                                    "display": "Nisqually",
                                },
                                {
                                    "code": "1524-8",
                                    "definition": "Nooksack",
                                    "display": "Nooksack",
                                },
                                {
                                    "code": "1525-5",
                                    "definition": "Port Madison",
                                    "display": "Port Madison",
                                },
                                {
                                    "code": "1526-3",
                                    "definition": "Puyallup",
                                    "display": "Puyallup",
                                },
                                {
                                    "code": "1527-1",
                                    "definition": "Samish",
                                    "display": "Samish",
                                },
                                {
                                    "code": "1528-9",
                                    "definition": "Sauk-Suiattle",
                                    "display": "Sauk-Suiattle",
                                },
                                {
                                    "code": "1529-7",
                                    "definition": "Skokomish",
                                    "display": "Skokomish",
                                },
                                {
                                    "code": "1530-5",
                                    "definition": "Skykomish",
                                    "display": "Skykomish",
                                },
                                {
                                    "code": "1531-3",
                                    "definition": "Snohomish",
                                    "display": "Snohomish",
                                },
                                {
                                    "code": "1532-1",
                                    "definition": "Snoqualmie",
                                    "display": "Snoqualmie",
                                },
                                {
                                    "code": "1533-9",
                                    "definition": "Squaxin Island",
                                    "display": "Squaxin Island",
                                },
                                {
                                    "code": "1534-7",
                                    "definition": "Steilacoom",
                                    "display": "Steilacoom",
                                },
                                {
                                    "code": "1535-4",
                                    "definition": "Stillaguamish",
                                    "display": "Stillaguamish",
                                },
                                {
                                    "code": "1536-2",
                                    "definition": "Suquamish",
                                    "display": "Suquamish",
                                },
                                {
                                    "code": "1537-0",
                                    "definition": "Swinomish",
                                    "display": "Swinomish",
                                },
                                {
                                    "code": "1538-8",
                                    "definition": "Tulalip",
                                    "display": "Tulalip",
                                },
                                {
                                    "code": "1539-6",
                                    "definition": "Upper Skagit",
                                    "display": "Upper Skagit",
                                },
                            ],
                            "definition": "Puget Sound Salish",
                            "display": "Puget Sound Salish",
                        },
                        {"code": "1541-2", "definition": "Quapaw", "display": "Quapaw"},
                        {
                            "code": "1543-8",
                            "definition": "Quinault",
                            "display": "Quinault",
                        },
                        {
                            "code": "1545-3",
                            "definition": "Rappahannock",
                            "display": "Rappahannock",
                        },
                        {
                            "code": "1547-9",
                            "definition": "Reno-Sparks",
                            "display": "Reno-Sparks",
                        },
                        {
                            "code": "1549-5",
                            "definition": "Round Valley",
                            "display": "Round Valley",
                        },
                        {
                            "code": "1551-1",
                            "concept": [
                                {
                                    "code": "1552-9",
                                    "definition": "Iowa Sac and Fox",
                                    "display": "Iowa Sac and Fox",
                                },
                                {
                                    "code": "1553-7",
                                    "definition": "Missouri Sac and Fox",
                                    "display": "Missouri Sac and Fox",
                                },
                                {
                                    "code": "1554-5",
                                    "definition": "Oklahoma Sac and Fox",
                                    "display": "Oklahoma Sac and Fox",
                                },
                            ],
                            "definition": "Sac and Fox",
                            "display": "Sac and Fox",
                        },
                        {
                            "code": "1556-0",
                            "definition": "Salinan",
                            "display": "Salinan",
                        },
                        {"code": "1558-6", "definition": "Salish", "display": "Salish"},
                        {
                            "code": "1560-2",
                            "definition": "Salish and Kootenai",
                            "display": "Salish and Kootenai",
                        },
                        {
                            "code": "1562-8",
                            "definition": "Schaghticoke",
                            "display": "Schaghticoke",
                        },
                        {
                            "code": "1564-4",
                            "definition": "Scott Valley",
                            "display": "Scott Valley",
                        },
                        {
                            "code": "1566-9",
                            "concept": [
                                {
                                    "code": "1567-7",
                                    "definition": "Big Cypress",
                                    "display": "Big Cypress",
                                },
                                {
                                    "code": "1568-5",
                                    "definition": "Brighton",
                                    "display": "Brighton",
                                },
                                {
                                    "code": "1569-3",
                                    "definition": "Florida Seminole",
                                    "display": "Florida Seminole",
                                },
                                {
                                    "code": "1570-1",
                                    "definition": "Hollywood Seminole",
                                    "display": "Hollywood Seminole",
                                },
                                {
                                    "code": "1571-9",
                                    "definition": "Oklahoma Seminole",
                                    "display": "Oklahoma Seminole",
                                },
                            ],
                            "definition": "Seminole",
                            "display": "Seminole",
                        },
                        {
                            "code": "1573-5",
                            "concept": [
                                {
                                    "code": "1574-3",
                                    "definition": "San Manual",
                                    "display": "San Manual",
                                }
                            ],
                            "definition": "Serrano",
                            "display": "Serrano",
                        },
                        {"code": "1576-8", "definition": "Shasta", "display": "Shasta"},
                        {
                            "code": "1578-4",
                            "concept": [
                                {
                                    "code": "1579-2",
                                    "definition": "Absentee Shawnee",
                                    "display": "Absentee Shawnee",
                                },
                                {
                                    "code": "1580-0",
                                    "definition": "Eastern Shawnee",
                                    "display": "Eastern Shawnee",
                                },
                            ],
                            "definition": "Shawnee",
                            "display": "Shawnee",
                        },
                        {
                            "code": "1582-6",
                            "definition": "Shinnecock",
                            "display": "Shinnecock",
                        },
                        {
                            "code": "1584-2",
                            "definition": "Shoalwater Bay",
                            "display": "Shoalwater Bay",
                        },
                        {
                            "code": "1586-7",
                            "concept": [
                                {
                                    "code": "1587-5",
                                    "definition": "Battle Mountain",
                                    "display": "Battle Mountain",
                                },
                                {
                                    "code": "1588-3",
                                    "definition": "Duckwater",
                                    "display": "Duckwater",
                                },
                                {
                                    "code": "1589-1",
                                    "definition": "Elko",
                                    "display": "Elko",
                                },
                                {
                                    "code": "1590-9",
                                    "definition": "Ely",
                                    "display": "Ely",
                                },
                                {
                                    "code": "1591-7",
                                    "definition": "Goshute",
                                    "display": "Goshute",
                                },
                                {
                                    "code": "1592-5",
                                    "definition": "Panamint",
                                    "display": "Panamint",
                                },
                                {
                                    "code": "1593-3",
                                    "definition": "Ruby Valley",
                                    "display": "Ruby Valley",
                                },
                                {
                                    "code": "1594-1",
                                    "definition": "Skull Valley",
                                    "display": "Skull Valley",
                                },
                                {
                                    "code": "1595-8",
                                    "definition": "South Fork Shoshone",
                                    "display": "South Fork Shoshone",
                                },
                                {
                                    "code": "1596-6",
                                    "definition": "Te-Moak Western Shoshone",
                                    "display": "Te-Moak Western Shoshone",
                                },
                                {
                                    "code": "1597-4",
                                    "definition": "Timbi-Sha Shoshone",
                                    "display": "Timbi-Sha Shoshone",
                                },
                                {
                                    "code": "1598-2",
                                    "definition": "Washakie",
                                    "display": "Washakie",
                                },
                                {
                                    "code": "1599-0",
                                    "definition": "Wind River Shoshone",
                                    "display": "Wind River Shoshone",
                                },
                                {
                                    "code": "1600-6",
                                    "definition": "Yomba",
                                    "display": "Yomba",
                                },
                            ],
                            "definition": "Shoshone",
                            "display": "Shoshone",
                        },
                        {
                            "code": "1602-2",
                            "concept": [
                                {
                                    "code": "1603-0",
                                    "definition": "Duck Valley",
                                    "display": "Duck Valley",
                                },
                                {
                                    "code": "1604-8",
                                    "definition": "Fallon",
                                    "display": "Fallon",
                                },
                                {
                                    "code": "1605-5",
                                    "definition": "Fort McDermitt",
                                    "display": "Fort McDermitt",
                                },
                            ],
                            "definition": "Shoshone Paiute",
                            "display": "Shoshone Paiute",
                        },
                        {"code": "1607-1", "definition": "Siletz", "display": "Siletz"},
                        {
                            "code": "1609-7",
                            "concept": [
                                {
                                    "code": "1610-5",
                                    "definition": "Blackfoot Sioux",
                                    "display": "Blackfoot Sioux",
                                },
                                {
                                    "code": "1611-3",
                                    "definition": "Brule Sioux",
                                    "display": "Brule Sioux",
                                },
                                {
                                    "code": "1612-1",
                                    "definition": "Cheyenne River Sioux",
                                    "display": "Cheyenne River Sioux",
                                },
                                {
                                    "code": "1613-9",
                                    "definition": "Crow Creek Sioux",
                                    "display": "Crow Creek Sioux",
                                },
                                {
                                    "code": "1614-7",
                                    "definition": "Dakota Sioux",
                                    "display": "Dakota Sioux",
                                },
                                {
                                    "code": "1615-4",
                                    "definition": "Flandreau Santee",
                                    "display": "Flandreau Santee",
                                },
                                {
                                    "code": "1616-2",
                                    "definition": "Fort Peck",
                                    "display": "Fort Peck",
                                },
                                {
                                    "code": "1617-0",
                                    "definition": "Lake Traverse Sioux",
                                    "display": "Lake Traverse Sioux",
                                },
                                {
                                    "code": "1618-8",
                                    "definition": "Lower Brule Sioux",
                                    "display": "Lower Brule Sioux",
                                },
                                {
                                    "code": "1619-6",
                                    "definition": "Lower Sioux",
                                    "display": "Lower Sioux",
                                },
                                {
                                    "code": "1620-4",
                                    "definition": "Mdewakanton Sioux",
                                    "display": "Mdewakanton Sioux",
                                },
                                {
                                    "code": "1621-2",
                                    "definition": "Miniconjou",
                                    "display": "Miniconjou",
                                },
                                {
                                    "code": "1622-0",
                                    "definition": "Oglala Sioux",
                                    "display": "Oglala Sioux",
                                },
                                {
                                    "code": "1623-8",
                                    "definition": "Pine Ridge Sioux",
                                    "display": "Pine Ridge Sioux",
                                },
                                {
                                    "code": "1624-6",
                                    "definition": "Pipestone Sioux",
                                    "display": "Pipestone Sioux",
                                },
                                {
                                    "code": "1625-3",
                                    "definition": "Prairie Island Sioux",
                                    "display": "Prairie Island Sioux",
                                },
                                {
                                    "code": "1626-1",
                                    "definition": "Prior Lake Sioux",
                                    "display": "Prior Lake Sioux",
                                },
                                {
                                    "code": "1627-9",
                                    "definition": "Rosebud Sioux",
                                    "display": "Rosebud Sioux",
                                },
                                {
                                    "code": "1628-7",
                                    "definition": "Sans Arc Sioux",
                                    "display": "Sans Arc Sioux",
                                },
                                {
                                    "code": "1629-5",
                                    "definition": "Santee Sioux",
                                    "display": "Santee Sioux",
                                },
                                {
                                    "code": "1630-3",
                                    "definition": "Sisseton-Wahpeton",
                                    "display": "Sisseton-Wahpeton",
                                },
                                {
                                    "code": "1631-1",
                                    "definition": "Sisseton Sioux",
                                    "display": "Sisseton Sioux",
                                },
                                {
                                    "code": "1632-9",
                                    "definition": "Spirit Lake Sioux",
                                    "display": "Spirit Lake Sioux",
                                },
                                {
                                    "code": "1633-7",
                                    "definition": "Standing Rock Sioux",
                                    "display": "Standing Rock Sioux",
                                },
                                {
                                    "code": "1634-5",
                                    "definition": "Teton Sioux",
                                    "display": "Teton Sioux",
                                },
                                {
                                    "code": "1635-2",
                                    "definition": "Two Kettle Sioux",
                                    "display": "Two Kettle Sioux",
                                },
                                {
                                    "code": "1636-0",
                                    "definition": "Upper Sioux",
                                    "display": "Upper Sioux",
                                },
                                {
                                    "code": "1637-8",
                                    "definition": "Wahpekute Sioux",
                                    "display": "Wahpekute Sioux",
                                },
                                {
                                    "code": "1638-6",
                                    "definition": "Wahpeton Sioux",
                                    "display": "Wahpeton Sioux",
                                },
                                {
                                    "code": "1639-4",
                                    "definition": "Wazhaza Sioux",
                                    "display": "Wazhaza Sioux",
                                },
                                {
                                    "code": "1640-2",
                                    "definition": "Yankton Sioux",
                                    "display": "Yankton Sioux",
                                },
                                {
                                    "code": "1641-0",
                                    "definition": "Yanktonai Sioux",
                                    "display": "Yanktonai Sioux",
                                },
                            ],
                            "definition": "Sioux",
                            "display": "Sioux",
                        },
                        {
                            "code": "1643-6",
                            "definition": "Siuslaw",
                            "display": "Siuslaw",
                        },
                        {
                            "code": "1645-1",
                            "definition": "Spokane",
                            "display": "Spokane",
                        },
                        {
                            "code": "1647-7",
                            "definition": "Stewart",
                            "display": "Stewart",
                        },
                        {
                            "code": "1649-3",
                            "definition": "Stockbridge",
                            "display": "Stockbridge",
                        },
                        {
                            "code": "1651-9",
                            "definition": "Susanville",
                            "display": "Susanville",
                        },
                        {
                            "code": "1653-5",
                            "concept": [
                                {
                                    "code": "1654-3",
                                    "definition": "Ak-Chin",
                                    "display": "Ak-Chin",
                                },
                                {
                                    "code": "1655-0",
                                    "definition": "Gila Bend",
                                    "display": "Gila Bend",
                                },
                                {
                                    "code": "1656-8",
                                    "definition": "San Xavier",
                                    "display": "San Xavier",
                                },
                                {
                                    "code": "1657-6",
                                    "definition": "Sells",
                                    "display": "Sells",
                                },
                            ],
                            "definition": "Tohono O'Odham",
                            "display": "Tohono O'Odham",
                        },
                        {"code": "1659-2", "definition": "Tolowa", "display": "Tolowa"},
                        {
                            "code": "1661-8",
                            "definition": "Tonkawa",
                            "display": "Tonkawa",
                        },
                        {"code": "1663-4", "definition": "Tygh", "display": "Tygh"},
                        {
                            "code": "1665-9",
                            "definition": "Umatilla",
                            "display": "Umatilla",
                        },
                        {
                            "code": "1667-5",
                            "concept": [
                                {
                                    "code": "1668-3",
                                    "definition": "Cow Creek Umpqua",
                                    "display": "Cow Creek Umpqua",
                                }
                            ],
                            "definition": "Umpqua",
                            "display": "Umpqua",
                        },
                        {
                            "code": "1670-9",
                            "concept": [
                                {
                                    "code": "1671-7",
                                    "definition": "Allen Canyon",
                                    "display": "Allen Canyon",
                                },
                                {
                                    "code": "1672-5",
                                    "definition": "Uintah Ute",
                                    "display": "Uintah Ute",
                                },
                                {
                                    "code": "1673-3",
                                    "definition": "Ute Mountain Ute",
                                    "display": "Ute Mountain Ute",
                                },
                            ],
                            "definition": "Ute",
                            "display": "Ute",
                        },
                        {
                            "code": "1675-8",
                            "definition": "Wailaki",
                            "display": "Wailaki",
                        },
                        {
                            "code": "1677-4",
                            "definition": "Walla-Walla",
                            "display": "Walla-Walla",
                        },
                        {
                            "code": "1679-0",
                            "concept": [
                                {
                                    "code": "1680-8",
                                    "definition": "Gay Head Wampanoag",
                                    "display": "Gay Head Wampanoag",
                                },
                                {
                                    "code": "1681-6",
                                    "definition": "Mashpee Wampanoag",
                                    "display": "Mashpee Wampanoag",
                                },
                            ],
                            "definition": "Wampanoag",
                            "display": "Wampanoag",
                        },
                        {
                            "code": "1683-2",
                            "definition": "Warm Springs",
                            "display": "Warm Springs",
                        },
                        {
                            "code": "1685-7",
                            "definition": "Wascopum",
                            "display": "Wascopum",
                        },
                        {
                            "code": "1687-3",
                            "concept": [
                                {
                                    "code": "1688-1",
                                    "definition": "Alpine",
                                    "display": "Alpine",
                                },
                                {
                                    "code": "1689-9",
                                    "definition": "Carson",
                                    "display": "Carson",
                                },
                                {
                                    "code": "1690-7",
                                    "definition": "Dresslerville",
                                    "display": "Dresslerville",
                                },
                            ],
                            "definition": "Washoe",
                            "display": "Washoe",
                        },
                        {
                            "code": "1692-3",
                            "definition": "Wichita",
                            "display": "Wichita",
                        },
                        {
                            "code": "1694-9",
                            "definition": "Wind River",
                            "display": "Wind River",
                        },
                        {
                            "code": "1696-4",
                            "concept": [
                                {
                                    "code": "1697-2",
                                    "definition": "Ho-chunk",
                                    "display": "Ho-chunk",
                                },
                                {
                                    "code": "1698-0",
                                    "definition": "Nebraska Winnebago",
                                    "display": "Nebraska Winnebago",
                                },
                            ],
                            "definition": "Winnebago",
                            "display": "Winnebago",
                        },
                        {
                            "code": "1700-4",
                            "definition": "Winnemucca",
                            "display": "Winnemucca",
                        },
                        {"code": "1702-0", "definition": "Wintun", "display": "Wintun"},
                        {
                            "code": "1704-6",
                            "concept": [
                                {
                                    "code": "1705-3",
                                    "definition": "Table Bluff",
                                    "display": "Table Bluff",
                                }
                            ],
                            "definition": "Wiyot",
                            "display": "Wiyot",
                        },
                        {"code": "1707-9", "definition": "Yakama", "display": "Yakama"},
                        {
                            "code": "1709-5",
                            "definition": "Yakama Cowlitz",
                            "display": "Yakama Cowlitz",
                        },
                        {
                            "code": "1711-1",
                            "concept": [
                                {
                                    "code": "1712-9",
                                    "definition": "Barrio Libre",
                                    "display": "Barrio Libre",
                                },
                                {
                                    "code": "1713-7",
                                    "definition": "Pascua Yaqui",
                                    "display": "Pascua Yaqui",
                                },
                            ],
                            "definition": "Yaqui",
                            "display": "Yaqui",
                        },
                        {
                            "code": "1715-2",
                            "definition": "Yavapai Apache",
                            "display": "Yavapai Apache",
                        },
                        {
                            "code": "1717-8",
                            "concept": [
                                {
                                    "code": "1718-6",
                                    "definition": "Chukchansi",
                                    "display": "Chukchansi",
                                },
                                {
                                    "code": "1719-4",
                                    "definition": "Tachi",
                                    "display": "Tachi",
                                },
                                {
                                    "code": "1720-2",
                                    "definition": "Tule River",
                                    "display": "Tule River",
                                },
                            ],
                            "definition": "Yokuts",
                            "display": "Yokuts",
                        },
                        {"code": "1722-8", "definition": "Yuchi", "display": "Yuchi"},
                        {
                            "code": "1724-4",
                            "concept": [
                                {
                                    "code": "1725-1",
                                    "definition": "Cocopah",
                                    "display": "Cocopah",
                                },
                                {
                                    "code": "1726-9",
                                    "definition": "Havasupai",
                                    "display": "Havasupai",
                                },
                                {
                                    "code": "1727-7",
                                    "definition": "Hualapai",
                                    "display": "Hualapai",
                                },
                                {
                                    "code": "1728-5",
                                    "definition": "Maricopa",
                                    "display": "Maricopa",
                                },
                                {
                                    "code": "1729-3",
                                    "definition": "Mohave",
                                    "display": "Mohave",
                                },
                                {
                                    "code": "1730-1",
                                    "definition": "Quechan",
                                    "display": "Quechan",
                                },
                                {
                                    "code": "1731-9",
                                    "definition": "Yavapai",
                                    "display": "Yavapai",
                                },
                            ],
                            "definition": "Yuman",
                            "display": "Yuman",
                        },
                        {
                            "code": "1732-7",
                            "concept": [
                                {
                                    "code": "1733-5",
                                    "definition": "Coast Yurok",
                                    "display": "Coast Yurok",
                                }
                            ],
                            "definition": "Yurok",
                            "display": "Yurok",
                        },
                    ],
                    "definition": "American Indian",
                    "display": "American Indian",
                },
                {
                    "code": "1735-0",
                    "concept": [
                        {
                            "code": "1737-6",
                            "concept": [
                                {
                                    "code": "1739-2",
                                    "concept": [
                                        {
                                            "code": "1740-0",
                                            "definition": "Ahtna",
                                            "display": "Ahtna",
                                        }
                                    ],
                                    "definition": "Alaskan Athabascan",
                                    "display": "Alaskan Athabascan",
                                },
                                {
                                    "code": "1811-9",
                                    "concept": [
                                        {
                                            "code": "1813-5",
                                            "concept": [
                                                {
                                                    "code": "1814-3",
                                                    "definition": "Angoon",
                                                    "display": "Angoon",
                                                },
                                                {
                                                    "code": "1815-0",
                                                    "definition": "Central Council of Tlingit and Haida Tribes",
                                                    "display": "Central Council of Tlingit and Haida Tribes",
                                                },
                                                {
                                                    "code": "1816-8",
                                                    "definition": "Chilkat",
                                                    "display": "Chilkat",
                                                },
                                                {
                                                    "code": "1817-6",
                                                    "definition": "Chilkoot",
                                                    "display": "Chilkoot",
                                                },
                                                {
                                                    "code": "1818-4",
                                                    "definition": "Craig",
                                                    "display": "Craig",
                                                },
                                                {
                                                    "code": "1819-2",
                                                    "definition": "Douglas",
                                                    "display": "Douglas",
                                                },
                                                {
                                                    "code": "1820-0",
                                                    "definition": "Haida",
                                                    "display": "Haida",
                                                },
                                                {
                                                    "code": "1821-8",
                                                    "definition": "Hoonah",
                                                    "display": "Hoonah",
                                                },
                                                {
                                                    "code": "1822-6",
                                                    "definition": "Hydaburg",
                                                    "display": "Hydaburg",
                                                },
                                                {
                                                    "code": "1823-4",
                                                    "definition": "Kake",
                                                    "display": "Kake",
                                                },
                                                {
                                                    "code": "1824-2",
                                                    "definition": "Kasaan",
                                                    "display": "Kasaan",
                                                },
                                                {
                                                    "code": "1825-9",
                                                    "definition": "Kenaitze",
                                                    "display": "Kenaitze",
                                                },
                                                {
                                                    "code": "1826-7",
                                                    "definition": "Ketchikan",
                                                    "display": "Ketchikan",
                                                },
                                                {
                                                    "code": "1827-5",
                                                    "definition": "Klawock",
                                                    "display": "Klawock",
                                                },
                                                {
                                                    "code": "1828-3",
                                                    "definition": "Pelican",
                                                    "display": "Pelican",
                                                },
                                                {
                                                    "code": "1829-1",
                                                    "definition": "Petersburg",
                                                    "display": "Petersburg",
                                                },
                                                {
                                                    "code": "1830-9",
                                                    "definition": "Saxman",
                                                    "display": "Saxman",
                                                },
                                                {
                                                    "code": "1831-7",
                                                    "definition": "Sitka",
                                                    "display": "Sitka",
                                                },
                                                {
                                                    "code": "1832-5",
                                                    "definition": "Tenakee Springs",
                                                    "display": "Tenakee Springs",
                                                },
                                                {
                                                    "code": "1833-3",
                                                    "definition": "Tlingit",
                                                    "display": "Tlingit",
                                                },
                                                {
                                                    "code": "1834-1",
                                                    "definition": "Wrangell",
                                                    "display": "Wrangell",
                                                },
                                                {
                                                    "code": "1835-8",
                                                    "definition": "Yakutat",
                                                    "display": "Yakutat",
                                                },
                                            ],
                                            "definition": "Tlingit-Haida",
                                            "display": "Tlingit-Haida",
                                        },
                                        {
                                            "code": "1837-4",
                                            "concept": [
                                                {
                                                    "code": "1838-2",
                                                    "definition": "Metlakatla",
                                                    "display": "Metlakatla",
                                                }
                                            ],
                                            "definition": "Tsimshian",
                                            "display": "Tsimshian",
                                        },
                                    ],
                                    "definition": "Southeast Alaska",
                                    "display": "Southeast Alaska",
                                },
                            ],
                            "definition": "Alaska Indian",
                            "display": "Alaska Indian",
                        },
                        {
                            "code": "1840-8",
                            "concept": [
                                {
                                    "code": "1842-4",
                                    "definition": "Greenland Eskimo",
                                    "display": "Greenland Eskimo",
                                },
                                {
                                    "code": "1844-0",
                                    "concept": [
                                        {
                                            "code": "1845-7",
                                            "definition": "Ambler",
                                            "display": "Ambler",
                                        },
                                        {
                                            "code": "1846-5",
                                            "definition": "Anaktuvuk",
                                            "display": "Anaktuvuk",
                                        },
                                        {
                                            "code": "1847-3",
                                            "definition": "Anaktuvuk Pass",
                                            "display": "Anaktuvuk Pass",
                                        },
                                        {
                                            "code": "1848-1",
                                            "definition": "Arctic Slope Inupiat",
                                            "display": "Arctic Slope Inupiat",
                                        },
                                        {
                                            "code": "1849-9",
                                            "definition": "Arctic Slope Corporation",
                                            "display": "Arctic Slope Corporation",
                                        },
                                        {
                                            "code": "1850-7",
                                            "definition": "Atqasuk",
                                            "display": "Atqasuk",
                                        },
                                        {
                                            "code": "1851-5",
                                            "definition": "Barrow",
                                            "display": "Barrow",
                                        },
                                        {
                                            "code": "1852-3",
                                            "definition": "Bering Straits Inupiat",
                                            "display": "Bering Straits Inupiat",
                                        },
                                        {
                                            "code": "1853-1",
                                            "definition": "Brevig Mission",
                                            "display": "Brevig Mission",
                                        },
                                        {
                                            "code": "1854-9",
                                            "definition": "Buckland",
                                            "display": "Buckland",
                                        },
                                        {
                                            "code": "1855-6",
                                            "definition": "Chinik",
                                            "display": "Chinik",
                                        },
                                        {
                                            "code": "1856-4",
                                            "definition": "Council",
                                            "display": "Council",
                                        },
                                        {
                                            "code": "1857-2",
                                            "definition": "Deering",
                                            "display": "Deering",
                                        },
                                        {
                                            "code": "1858-0",
                                            "definition": "Elim",
                                            "display": "Elim",
                                        },
                                        {
                                            "code": "1859-8",
                                            "definition": "Golovin",
                                            "display": "Golovin",
                                        },
                                        {
                                            "code": "1860-6",
                                            "definition": "Inalik Diomede",
                                            "display": "Inalik Diomede",
                                        },
                                        {
                                            "code": "1861-4",
                                            "definition": "Inupiaq",
                                            "display": "Inupiaq",
                                        },
                                        {
                                            "code": "1862-2",
                                            "definition": "Kaktovik",
                                            "display": "Kaktovik",
                                        },
                                        {
                                            "code": "1863-0",
                                            "definition": "Kawerak",
                                            "display": "Kawerak",
                                        },
                                        {
                                            "code": "1864-8",
                                            "definition": "Kiana",
                                            "display": "Kiana",
                                        },
                                        {
                                            "code": "1865-5",
                                            "definition": "Kivalina",
                                            "display": "Kivalina",
                                        },
                                        {
                                            "code": "1866-3",
                                            "definition": "Kobuk",
                                            "display": "Kobuk",
                                        },
                                        {
                                            "code": "1867-1",
                                            "definition": "Kotzebue",
                                            "display": "Kotzebue",
                                        },
                                        {
                                            "code": "1868-9",
                                            "definition": "Koyuk",
                                            "display": "Koyuk",
                                        },
                                        {
                                            "code": "1869-7",
                                            "definition": "Kwiguk",
                                            "display": "Kwiguk",
                                        },
                                        {
                                            "code": "1870-5",
                                            "definition": "Mauneluk Inupiat",
                                            "display": "Mauneluk Inupiat",
                                        },
                                        {
                                            "code": "1871-3",
                                            "definition": "Nana Inupiat",
                                            "display": "Nana Inupiat",
                                        },
                                        {
                                            "code": "1872-1",
                                            "definition": "Noatak",
                                            "display": "Noatak",
                                        },
                                        {
                                            "code": "1873-9",
                                            "definition": "Nome",
                                            "display": "Nome",
                                        },
                                        {
                                            "code": "1874-7",
                                            "definition": "Noorvik",
                                            "display": "Noorvik",
                                        },
                                        {
                                            "code": "1875-4",
                                            "definition": "Nuiqsut",
                                            "display": "Nuiqsut",
                                        },
                                        {
                                            "code": "1876-2",
                                            "definition": "Point Hope",
                                            "display": "Point Hope",
                                        },
                                        {
                                            "code": "1877-0",
                                            "definition": "Point Lay",
                                            "display": "Point Lay",
                                        },
                                        {
                                            "code": "1878-8",
                                            "definition": "Selawik",
                                            "display": "Selawik",
                                        },
                                        {
                                            "code": "1879-6",
                                            "definition": "Shaktoolik",
                                            "display": "Shaktoolik",
                                        },
                                        {
                                            "code": "1880-4",
                                            "definition": "Shishmaref",
                                            "display": "Shishmaref",
                                        },
                                        {
                                            "code": "1881-2",
                                            "definition": "Shungnak",
                                            "display": "Shungnak",
                                        },
                                        {
                                            "code": "1882-0",
                                            "definition": "Solomon",
                                            "display": "Solomon",
                                        },
                                        {
                                            "code": "1883-8",
                                            "definition": "Teller",
                                            "display": "Teller",
                                        },
                                        {
                                            "code": "1884-6",
                                            "definition": "Unalakleet",
                                            "display": "Unalakleet",
                                        },
                                        {
                                            "code": "1885-3",
                                            "definition": "Wainwright",
                                            "display": "Wainwright",
                                        },
                                        {
                                            "code": "1886-1",
                                            "definition": "Wales",
                                            "display": "Wales",
                                        },
                                        {
                                            "code": "1887-9",
                                            "definition": "White Mountain",
                                            "display": "White Mountain",
                                        },
                                        {
                                            "code": "1888-7",
                                            "definition": "White Mountain Inupiat",
                                            "display": "White Mountain Inupiat",
                                        },
                                        {
                                            "code": "1889-5",
                                            "definition": "Mary's Igloo",
                                            "display": "Mary's Igloo",
                                        },
                                    ],
                                    "definition": "Inupiat Eskimo",
                                    "display": "Inupiat Eskimo",
                                },
                                {
                                    "code": "1891-1",
                                    "concept": [
                                        {
                                            "code": "1892-9",
                                            "definition": "Gambell",
                                            "display": "Gambell",
                                        },
                                        {
                                            "code": "1893-7",
                                            "definition": "Savoonga",
                                            "display": "Savoonga",
                                        },
                                        {
                                            "code": "1894-5",
                                            "definition": "Siberian Yupik",
                                            "display": "Siberian Yupik",
                                        },
                                    ],
                                    "definition": "Siberian Eskimo",
                                    "display": "Siberian Eskimo",
                                },
                                {
                                    "code": "1896-0",
                                    "concept": [
                                        {
                                            "code": "1897-8",
                                            "definition": "Akiachak",
                                            "display": "Akiachak",
                                        },
                                        {
                                            "code": "1898-6",
                                            "definition": "Akiak",
                                            "display": "Akiak",
                                        },
                                        {
                                            "code": "1899-4",
                                            "definition": "Alakanuk",
                                            "display": "Alakanuk",
                                        },
                                        {
                                            "code": "1900-0",
                                            "definition": "Aleknagik",
                                            "display": "Aleknagik",
                                        },
                                        {
                                            "code": "1901-8",
                                            "definition": "Andreafsky",
                                            "display": "Andreafsky",
                                        },
                                        {
                                            "code": "1902-6",
                                            "definition": "Aniak",
                                            "display": "Aniak",
                                        },
                                        {
                                            "code": "1903-4",
                                            "definition": "Atmautluak",
                                            "display": "Atmautluak",
                                        },
                                        {
                                            "code": "1904-2",
                                            "definition": "Bethel",
                                            "display": "Bethel",
                                        },
                                        {
                                            "code": "1905-9",
                                            "definition": "Bill Moore's Slough",
                                            "display": "Bill Moore's Slough",
                                        },
                                        {
                                            "code": "1906-7",
                                            "definition": "Bristol Bay Yupik",
                                            "display": "Bristol Bay Yupik",
                                        },
                                        {
                                            "code": "1907-5",
                                            "definition": "Calista Yupik",
                                            "display": "Calista Yupik",
                                        },
                                        {
                                            "code": "1908-3",
                                            "definition": "Chefornak",
                                            "display": "Chefornak",
                                        },
                                        {
                                            "code": "1909-1",
                                            "definition": "Chevak",
                                            "display": "Chevak",
                                        },
                                        {
                                            "code": "1910-9",
                                            "definition": "Chuathbaluk",
                                            "display": "Chuathbaluk",
                                        },
                                        {
                                            "code": "1911-7",
                                            "definition": "Clark's Point",
                                            "display": "Clark's Point",
                                        },
                                        {
                                            "code": "1912-5",
                                            "definition": "Crooked Creek",
                                            "display": "Crooked Creek",
                                        },
                                        {
                                            "code": "1913-3",
                                            "definition": "Dillingham",
                                            "display": "Dillingham",
                                        },
                                        {
                                            "code": "1914-1",
                                            "definition": "Eek",
                                            "display": "Eek",
                                        },
                                        {
                                            "code": "1915-8",
                                            "definition": "Ekuk",
                                            "display": "Ekuk",
                                        },
                                        {
                                            "code": "1916-6",
                                            "definition": "Ekwok",
                                            "display": "Ekwok",
                                        },
                                        {
                                            "code": "1917-4",
                                            "definition": "Emmonak",
                                            "display": "Emmonak",
                                        },
                                        {
                                            "code": "1918-2",
                                            "definition": "Goodnews Bay",
                                            "display": "Goodnews Bay",
                                        },
                                        {
                                            "code": "1919-0",
                                            "definition": "Hooper Bay",
                                            "display": "Hooper Bay",
                                        },
                                        {
                                            "code": "1920-8",
                                            "definition": "Iqurmuit (Russian Mission)",
                                            "display": "Iqurmuit (Russian Mission)",
                                        },
                                        {
                                            "code": "1921-6",
                                            "definition": "Kalskag",
                                            "display": "Kalskag",
                                        },
                                        {
                                            "code": "1922-4",
                                            "definition": "Kasigluk",
                                            "display": "Kasigluk",
                                        },
                                        {
                                            "code": "1923-2",
                                            "definition": "Kipnuk",
                                            "display": "Kipnuk",
                                        },
                                        {
                                            "code": "1924-0",
                                            "definition": "Koliganek",
                                            "display": "Koliganek",
                                        },
                                        {
                                            "code": "1925-7",
                                            "definition": "Kongiganak",
                                            "display": "Kongiganak",
                                        },
                                        {
                                            "code": "1926-5",
                                            "definition": "Kotlik",
                                            "display": "Kotlik",
                                        },
                                        {
                                            "code": "1927-3",
                                            "definition": "Kwethluk",
                                            "display": "Kwethluk",
                                        },
                                        {
                                            "code": "1928-1",
                                            "definition": "Kwigillingok",
                                            "display": "Kwigillingok",
                                        },
                                        {
                                            "code": "1929-9",
                                            "definition": "Levelock",
                                            "display": "Levelock",
                                        },
                                        {
                                            "code": "1930-7",
                                            "definition": "Lower Kalskag",
                                            "display": "Lower Kalskag",
                                        },
                                        {
                                            "code": "1931-5",
                                            "definition": "Manokotak",
                                            "display": "Manokotak",
                                        },
                                        {
                                            "code": "1932-3",
                                            "definition": "Marshall",
                                            "display": "Marshall",
                                        },
                                        {
                                            "code": "1933-1",
                                            "definition": "Mekoryuk",
                                            "display": "Mekoryuk",
                                        },
                                        {
                                            "code": "1934-9",
                                            "definition": "Mountain Village",
                                            "display": "Mountain Village",
                                        },
                                        {
                                            "code": "1935-6",
                                            "definition": "Naknek",
                                            "display": "Naknek",
                                        },
                                        {
                                            "code": "1936-4",
                                            "definition": "Napaumute",
                                            "display": "Napaumute",
                                        },
                                        {
                                            "code": "1937-2",
                                            "definition": "Napakiak",
                                            "display": "Napakiak",
                                        },
                                        {
                                            "code": "1938-0",
                                            "definition": "Napaskiak",
                                            "display": "Napaskiak",
                                        },
                                        {
                                            "code": "1939-8",
                                            "definition": "Newhalen",
                                            "display": "Newhalen",
                                        },
                                        {
                                            "code": "1940-6",
                                            "definition": "New Stuyahok",
                                            "display": "New Stuyahok",
                                        },
                                        {
                                            "code": "1941-4",
                                            "definition": "Newtok",
                                            "display": "Newtok",
                                        },
                                        {
                                            "code": "1942-2",
                                            "definition": "Nightmute",
                                            "display": "Nightmute",
                                        },
                                        {
                                            "code": "1943-0",
                                            "definition": "Nunapitchukv",
                                            "display": "Nunapitchukv",
                                        },
                                        {
                                            "code": "1944-8",
                                            "definition": "Oscarville",
                                            "display": "Oscarville",
                                        },
                                        {
                                            "code": "1945-5",
                                            "definition": "Pilot Station",
                                            "display": "Pilot Station",
                                        },
                                        {
                                            "code": "1946-3",
                                            "definition": "Pitkas Point",
                                            "display": "Pitkas Point",
                                        },
                                        {
                                            "code": "1947-1",
                                            "definition": "Platinum",
                                            "display": "Platinum",
                                        },
                                        {
                                            "code": "1948-9",
                                            "definition": "Portage Creek",
                                            "display": "Portage Creek",
                                        },
                                        {
                                            "code": "1949-7",
                                            "definition": "Quinhagak",
                                            "display": "Quinhagak",
                                        },
                                        {
                                            "code": "1950-5",
                                            "definition": "Red Devil",
                                            "display": "Red Devil",
                                        },
                                        {
                                            "code": "1951-3",
                                            "definition": "St. Michael",
                                            "display": "St. Michael",
                                        },
                                        {
                                            "code": "1952-1",
                                            "definition": "Scammon Bay",
                                            "display": "Scammon Bay",
                                        },
                                        {
                                            "code": "1953-9",
                                            "definition": "Sheldon's Point",
                                            "display": "Sheldon's Point",
                                        },
                                        {
                                            "code": "1954-7",
                                            "definition": "Sleetmute",
                                            "display": "Sleetmute",
                                        },
                                        {
                                            "code": "1955-4",
                                            "definition": "Stebbins",
                                            "display": "Stebbins",
                                        },
                                        {
                                            "code": "1956-2",
                                            "definition": "Togiak",
                                            "display": "Togiak",
                                        },
                                        {
                                            "code": "1957-0",
                                            "definition": "Toksook",
                                            "display": "Toksook",
                                        },
                                        {
                                            "code": "1958-8",
                                            "definition": "Tulukskak",
                                            "display": "Tulukskak",
                                        },
                                        {
                                            "code": "1959-6",
                                            "definition": "Tuntutuliak",
                                            "display": "Tuntutuliak",
                                        },
                                        {
                                            "code": "1960-4",
                                            "definition": "Tununak",
                                            "display": "Tununak",
                                        },
                                        {
                                            "code": "1961-2",
                                            "definition": "Twin Hills",
                                            "display": "Twin Hills",
                                        },
                                        {
                                            "code": "1962-0",
                                            "definition": "Georgetown",
                                            "display": "Georgetown",
                                        },
                                        {
                                            "code": "1963-8",
                                            "definition": "St. Mary's",
                                            "display": "St. Mary's",
                                        },
                                        {
                                            "code": "1964-6",
                                            "definition": "Umkumiate",
                                            "display": "Umkumiate",
                                        },
                                    ],
                                    "definition": "Yupik Eskimo",
                                    "display": "Yupik Eskimo",
                                },
                            ],
                            "definition": "Eskimo",
                            "display": "Eskimo",
                        },
                        {
                            "code": "1966-1",
                            "concept": [
                                {
                                    "code": "1968-7",
                                    "concept": [
                                        {
                                            "code": "1969-5",
                                            "definition": "Tatitlek",
                                            "display": "Tatitlek",
                                        },
                                        {
                                            "code": "1970-3",
                                            "definition": "Ugashik",
                                            "display": "Ugashik",
                                        },
                                    ],
                                    "definition": "Alutiiq Aleut",
                                    "display": "Alutiiq Aleut",
                                },
                                {
                                    "code": "1972-9",
                                    "concept": [
                                        {
                                            "code": "1973-7",
                                            "definition": "Chignik",
                                            "display": "Chignik",
                                        },
                                        {
                                            "code": "1974-5",
                                            "definition": "Chignik Lake",
                                            "display": "Chignik Lake",
                                        },
                                        {
                                            "code": "1975-2",
                                            "definition": "Egegik",
                                            "display": "Egegik",
                                        },
                                        {
                                            "code": "1976-0",
                                            "definition": "Igiugig",
                                            "display": "Igiugig",
                                        },
                                        {
                                            "code": "1977-8",
                                            "definition": "Ivanof Bay",
                                            "display": "Ivanof Bay",
                                        },
                                        {
                                            "code": "1978-6",
                                            "definition": "King Salmon",
                                            "display": "King Salmon",
                                        },
                                        {
                                            "code": "1979-4",
                                            "definition": "Kokhanok",
                                            "display": "Kokhanok",
                                        },
                                        {
                                            "code": "1980-2",
                                            "definition": "Perryville",
                                            "display": "Perryville",
                                        },
                                        {
                                            "code": "1981-0",
                                            "definition": "Pilot Point",
                                            "display": "Pilot Point",
                                        },
                                        {
                                            "code": "1982-8",
                                            "definition": "Port Heiden",
                                            "display": "Port Heiden",
                                        },
                                    ],
                                    "definition": "Bristol Bay Aleut",
                                    "display": "Bristol Bay Aleut",
                                },
                                {
                                    "code": "1984-4",
                                    "concept": [
                                        {
                                            "code": "1985-1",
                                            "definition": "Chenega",
                                            "display": "Chenega",
                                        },
                                        {
                                            "code": "1986-9",
                                            "definition": "Chugach Corporation",
                                            "display": "Chugach Corporation",
                                        },
                                        {
                                            "code": "1987-7",
                                            "definition": "English Bay",
                                            "display": "English Bay",
                                        },
                                        {
                                            "code": "1988-5",
                                            "definition": "Port Graham",
                                            "display": "Port Graham",
                                        },
                                    ],
                                    "definition": "Chugach Aleut",
                                    "display": "Chugach Aleut",
                                },
                                {
                                    "code": "1990-1",
                                    "definition": "Eyak",
                                    "display": "Eyak",
                                },
                                {
                                    "code": "1992-7",
                                    "concept": [
                                        {
                                            "code": "1993-5",
                                            "definition": "Akhiok",
                                            "display": "Akhiok",
                                        },
                                        {
                                            "code": "1994-3",
                                            "definition": "Agdaagux",
                                            "display": "Agdaagux",
                                        },
                                        {
                                            "code": "1995-0",
                                            "definition": "Karluk",
                                            "display": "Karluk",
                                        },
                                        {
                                            "code": "1996-8",
                                            "definition": "Kodiak",
                                            "display": "Kodiak",
                                        },
                                        {
                                            "code": "1997-6",
                                            "definition": "Larsen Bay",
                                            "display": "Larsen Bay",
                                        },
                                        {
                                            "code": "1998-4",
                                            "definition": "Old Harbor",
                                            "display": "Old Harbor",
                                        },
                                        {
                                            "code": "1999-2",
                                            "definition": "Ouzinkie",
                                            "display": "Ouzinkie",
                                        },
                                        {
                                            "code": "2000-8",
                                            "definition": "Port Lions",
                                            "display": "Port Lions",
                                        },
                                    ],
                                    "definition": "Koniag Aleut",
                                    "display": "Koniag Aleut",
                                },
                                {
                                    "code": "2002-4",
                                    "definition": "Sugpiaq",
                                    "display": "Sugpiaq",
                                },
                                {
                                    "code": "2004-0",
                                    "definition": "Suqpigaq",
                                    "display": "Suqpigaq",
                                },
                                {
                                    "code": "2006-5",
                                    "concept": [
                                        {
                                            "code": "2007-3",
                                            "definition": "Akutan",
                                            "display": "Akutan",
                                        },
                                        {
                                            "code": "2008-1",
                                            "definition": "Aleut Corporation",
                                            "display": "Aleut Corporation",
                                        },
                                        {
                                            "code": "2009-9",
                                            "definition": "Aleutian",
                                            "display": "Aleutian",
                                        },
                                        {
                                            "code": "2010-7",
                                            "definition": "Aleutian Islander",
                                            "display": "Aleutian Islander",
                                        },
                                        {
                                            "code": "2011-5",
                                            "definition": "Atka",
                                            "display": "Atka",
                                        },
                                        {
                                            "code": "2012-3",
                                            "definition": "Belkofski",
                                            "display": "Belkofski",
                                        },
                                        {
                                            "code": "2013-1",
                                            "definition": "Chignik Lagoon",
                                            "display": "Chignik Lagoon",
                                        },
                                        {
                                            "code": "2014-9",
                                            "definition": "King Cove",
                                            "display": "King Cove",
                                        },
                                        {
                                            "code": "2015-6",
                                            "definition": "False Pass",
                                            "display": "False Pass",
                                        },
                                        {
                                            "code": "2016-4",
                                            "definition": "Nelson Lagoon",
                                            "display": "Nelson Lagoon",
                                        },
                                        {
                                            "code": "2017-2",
                                            "definition": "Nikolski",
                                            "display": "Nikolski",
                                        },
                                        {
                                            "code": "2018-0",
                                            "definition": "Pauloff Harbor",
                                            "display": "Pauloff Harbor",
                                        },
                                        {
                                            "code": "2019-8",
                                            "definition": "Qagan Toyagungin",
                                            "display": "Qagan Toyagungin",
                                        },
                                        {
                                            "code": "2020-6",
                                            "definition": "Qawalangin",
                                            "display": "Qawalangin",
                                        },
                                        {
                                            "code": "2021-4",
                                            "definition": "St. George",
                                            "display": "St. George",
                                        },
                                        {
                                            "code": "2022-2",
                                            "definition": "St. Paul",
                                            "display": "St. Paul",
                                        },
                                        {
                                            "code": "2023-0",
                                            "definition": "Sand Point",
                                            "display": "Sand Point",
                                        },
                                        {
                                            "code": "2024-8",
                                            "definition": "South Naknek",
                                            "display": "South Naknek",
                                        },
                                        {
                                            "code": "2025-5",
                                            "definition": "Unalaska",
                                            "display": "Unalaska",
                                        },
                                        {
                                            "code": "2026-3",
                                            "definition": "Unga",
                                            "display": "Unga",
                                        },
                                    ],
                                    "definition": "Unangan Aleut",
                                    "display": "Unangan Aleut",
                                },
                            ],
                            "definition": "Aleut",
                            "display": "Aleut",
                        },
                    ],
                    "definition": "Alaska Native",
                    "display": "Alaska Native",
                },
            ],
            "definition": "American Indian or Alaska Native",
            "display": "American Indian or Alaska Native",
        }
    )
    """
    American Indian or Alaska Native

    American Indian or Alaska Native
    """

    two028_9 = CodeSystemConcept(
        {
            "code": "2028-9",
            "concept": [
                {
                    "code": "2029-7",
                    "definition": "Asian Indian",
                    "display": "Asian Indian",
                },
                {
                    "code": "2030-5",
                    "definition": "Bangladeshi",
                    "display": "Bangladeshi",
                },
                {"code": "2031-3", "definition": "Bhutanese", "display": "Bhutanese"},
                {"code": "2032-1", "definition": "Burmese", "display": "Burmese"},
                {"code": "2033-9", "definition": "Cambodian", "display": "Cambodian"},
                {"code": "2034-7", "definition": "Chinese", "display": "Chinese"},
                {"code": "2035-4", "definition": "Taiwanese", "display": "Taiwanese"},
                {"code": "2036-2", "definition": "Filipino", "display": "Filipino"},
                {"code": "2037-0", "definition": "Hmong", "display": "Hmong"},
                {"code": "2038-8", "definition": "Indonesian", "display": "Indonesian"},
                {"code": "2039-6", "definition": "Japanese", "display": "Japanese"},
                {"code": "2040-4", "definition": "Korean", "display": "Korean"},
                {"code": "2041-2", "definition": "Laotian", "display": "Laotian"},
                {"code": "2042-0", "definition": "Malaysian", "display": "Malaysian"},
                {"code": "2043-8", "definition": "Okinawan", "display": "Okinawan"},
                {"code": "2044-6", "definition": "Pakistani", "display": "Pakistani"},
                {"code": "2045-3", "definition": "Sri Lankan", "display": "Sri Lankan"},
                {"code": "2046-1", "definition": "Thai", "display": "Thai"},
                {"code": "2047-9", "definition": "Vietnamese", "display": "Vietnamese"},
                {"code": "2048-7", "definition": "Iwo Jiman", "display": "Iwo Jiman"},
                {"code": "2049-5", "definition": "Maldivian", "display": "Maldivian"},
                {"code": "2050-3", "definition": "Nepalese", "display": "Nepalese"},
                {
                    "code": "2051-1",
                    "definition": "Singaporean",
                    "display": "Singaporean",
                },
                {"code": "2052-9", "definition": "Madagascar", "display": "Madagascar"},
            ],
            "definition": "Asian",
            "display": "Asian",
        }
    )
    """
    Asian

    Asian
    """

    two054_5 = CodeSystemConcept(
        {
            "code": "2054-5",
            "concept": [
                {"code": "2056-0", "definition": "Black", "display": "Black"},
                {
                    "code": "2058-6",
                    "definition": "African American",
                    "display": "African American",
                },
                {
                    "code": "2060-2",
                    "concept": [
                        {
                            "code": "2061-0",
                            "definition": "Botswanan",
                            "display": "Botswanan",
                        },
                        {
                            "code": "2062-8",
                            "definition": "Ethiopian",
                            "display": "Ethiopian",
                        },
                        {
                            "code": "2063-6",
                            "definition": "Liberian",
                            "display": "Liberian",
                        },
                        {
                            "code": "2064-4",
                            "definition": "Namibian",
                            "display": "Namibian",
                        },
                        {
                            "code": "2065-1",
                            "definition": "Nigerian",
                            "display": "Nigerian",
                        },
                        {
                            "code": "2066-9",
                            "definition": "Zairean",
                            "display": "Zairean",
                        },
                    ],
                    "definition": "African",
                    "display": "African",
                },
                {"code": "2067-7", "definition": "Bahamian", "display": "Bahamian"},
                {"code": "2068-5", "definition": "Barbadian", "display": "Barbadian"},
                {"code": "2069-3", "definition": "Dominican", "display": "Dominican"},
                {
                    "code": "2070-1",
                    "definition": "Dominica Islander",
                    "display": "Dominica Islander",
                },
                {"code": "2071-9", "definition": "Haitian", "display": "Haitian"},
                {"code": "2072-7", "definition": "Jamaican", "display": "Jamaican"},
                {"code": "2073-5", "definition": "Tobagoan", "display": "Tobagoan"},
                {
                    "code": "2074-3",
                    "definition": "Trinidadian",
                    "display": "Trinidadian",
                },
                {
                    "code": "2075-0",
                    "definition": "West Indian",
                    "display": "West Indian",
                },
            ],
            "definition": "Black or African American",
            "display": "Black or African American",
        }
    )
    """
    Black or African American

    Black or African American
    """

    two076_8 = CodeSystemConcept(
        {
            "code": "2076-8",
            "concept": [
                {
                    "code": "2078-4",
                    "concept": [
                        {
                            "code": "2079-2",
                            "definition": "Native Hawaiian",
                            "display": "Native Hawaiian",
                        },
                        {"code": "2080-0", "definition": "Samoan", "display": "Samoan"},
                        {
                            "code": "2081-8",
                            "definition": "Tahitian",
                            "display": "Tahitian",
                        },
                        {"code": "2082-6", "definition": "Tongan", "display": "Tongan"},
                        {
                            "code": "2083-4",
                            "definition": "Tokelauan",
                            "display": "Tokelauan",
                        },
                    ],
                    "definition": "Polynesian",
                    "display": "Polynesian",
                },
                {
                    "code": "2085-9",
                    "concept": [
                        {
                            "code": "2086-7",
                            "definition": "Guamanian or Chamorro",
                            "display": "Guamanian or Chamorro",
                        },
                        {
                            "code": "2087-5",
                            "definition": "Guamanian",
                            "display": "Guamanian",
                        },
                        {
                            "code": "2088-3",
                            "definition": "Chamorro",
                            "display": "Chamorro",
                        },
                        {
                            "code": "2089-1",
                            "definition": "Mariana Islander",
                            "display": "Mariana Islander",
                        },
                        {
                            "code": "2090-9",
                            "definition": "Marshallese",
                            "display": "Marshallese",
                        },
                        {
                            "code": "2091-7",
                            "definition": "Palauan",
                            "display": "Palauan",
                        },
                        {
                            "code": "2092-5",
                            "definition": "Carolinian",
                            "display": "Carolinian",
                        },
                        {
                            "code": "2093-3",
                            "definition": "Kosraean",
                            "display": "Kosraean",
                        },
                        {
                            "code": "2094-1",
                            "definition": "Pohnpeian",
                            "display": "Pohnpeian",
                        },
                        {
                            "code": "2095-8",
                            "definition": "Saipanese",
                            "display": "Saipanese",
                        },
                        {
                            "code": "2096-6",
                            "definition": "Kiribati",
                            "display": "Kiribati",
                        },
                        {
                            "code": "2097-4",
                            "definition": "Chuukese",
                            "display": "Chuukese",
                        },
                        {"code": "2098-2", "definition": "Yapese", "display": "Yapese"},
                    ],
                    "definition": "Micronesian",
                    "display": "Micronesian",
                },
                {
                    "code": "2100-6",
                    "concept": [
                        {"code": "2101-4", "definition": "Fijian", "display": "Fijian"},
                        {
                            "code": "2102-2",
                            "definition": "Papua New Guinean",
                            "display": "Papua New Guinean",
                        },
                        {
                            "code": "2103-0",
                            "definition": "Solomon Islander",
                            "display": "Solomon Islander",
                        },
                        {
                            "code": "2104-8",
                            "definition": "New Hebrides",
                            "display": "New Hebrides",
                        },
                    ],
                    "definition": "Melanesian",
                    "display": "Melanesian",
                },
                {
                    "code": "2500-7",
                    "definition": "Note that this term remains in the table for completeness, even though within HL7, the notion of Other code is deprecated.",
                    "display": "Other Pacific Islander",
                },
            ],
            "definition": "Native Hawaiian or Other Pacific Islander",
            "display": "Native Hawaiian or Other Pacific Islander",
        }
    )
    """
    Native Hawaiian or Other Pacific Islander

    Native Hawaiian or Other Pacific Islander
    """

    two106_3 = CodeSystemConcept(
        {
            "code": "2106-3",
            "concept": [
                {
                    "code": "2108-9",
                    "concept": [
                        {
                            "code": "2109-7",
                            "definition": "Armenian",
                            "display": "Armenian",
                        },
                        {
                            "code": "2110-5",
                            "definition": "English",
                            "display": "English",
                        },
                        {"code": "2111-3", "definition": "French", "display": "French"},
                        {"code": "2112-1", "definition": "German", "display": "German"},
                        {"code": "2113-9", "definition": "Irish", "display": "Irish"},
                        {
                            "code": "2114-7",
                            "definition": "Italian",
                            "display": "Italian",
                        },
                        {"code": "2115-4", "definition": "Polish", "display": "Polish"},
                        {
                            "code": "2116-2",
                            "definition": "Scottish",
                            "display": "Scottish",
                        },
                    ],
                    "definition": "European",
                    "display": "European",
                },
                {
                    "code": "2118-8",
                    "concept": [
                        {
                            "code": "2119-6",
                            "definition": "Assyrian",
                            "display": "Assyrian",
                        },
                        {
                            "code": "2120-4",
                            "definition": "Egyptian",
                            "display": "Egyptian",
                        },
                        {
                            "code": "2121-2",
                            "definition": "Iranian",
                            "display": "Iranian",
                        },
                        {"code": "2122-0", "definition": "Iraqi", "display": "Iraqi"},
                        {
                            "code": "2123-8",
                            "definition": "Lebanese",
                            "display": "Lebanese",
                        },
                        {
                            "code": "2124-6",
                            "definition": "Palestinian",
                            "display": "Palestinian",
                        },
                        {"code": "2125-3", "definition": "Syrian", "display": "Syrian"},
                        {
                            "code": "2126-1",
                            "definition": "Afghanistani",
                            "display": "Afghanistani",
                        },
                        {
                            "code": "2127-9",
                            "definition": "Israeili",
                            "display": "Israeili",
                        },
                    ],
                    "definition": "Middle Eastern or North African",
                    "display": "Middle Eastern or North African",
                },
                {"code": "2129-5", "definition": "Arab", "display": "Arab"},
            ],
            "definition": "White",
            "display": "White",
        }
    )
    """
    White

    White
    """

    two131_1 = CodeSystemConcept(
        {
            "code": "2131-1",
            "definition": "Note that this term remains in the table for completeness, even though within HL7, the notion of Other code is deprecated.",
            "display": "Other Race",
        }
    )
    """
    Other Race

    Note that this term remains in the table for completeness, even though within HL7, the notion of Other code is deprecated.
    """

    class Meta:
        resource = _resource
