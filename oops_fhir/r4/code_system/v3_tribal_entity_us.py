from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TribalEntityUS"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TribalEntityUS:
    """
    v3 Code System TribalEntityUS

     INDIAN ENTITIES RECOGNIZED AND ELIGIBLE TO RECEIVE SERVICES FROM THE
UNITED STATES BUREAU OF INDIAN AFFAIRS

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TribalEntityUS
    """

    underscore_native_entity_alaska = CodeSystemConcept(
        {
            "code": "_NativeEntityAlaska",
            "concept": [
                {
                    "code": "338",
                    "definition": "Village of Afognak",
                    "display": "Village of Afognak",
                },
                {
                    "code": "339",
                    "definition": "Agdaagux Tribe of King Cove",
                    "display": "Agdaagux Tribe of King Cove",
                },
                {
                    "code": "340",
                    "definition": "Native Village of Akhiok",
                    "display": "Native Village of Akhiok",
                },
                {
                    "code": "341",
                    "definition": "Akiachak Native Community",
                    "display": "Akiachak Native Community",
                },
                {
                    "code": "342",
                    "definition": "Akiak Native Community",
                    "display": "Akiak Native Community",
                },
                {
                    "code": "343",
                    "definition": "Native Village of Akutan",
                    "display": "Native Village of Akutan",
                },
                {
                    "code": "344",
                    "definition": "Village of Alakanuk",
                    "display": "Village of Alakanuk",
                },
                {
                    "code": "345",
                    "definition": "Alatna Village",
                    "display": "Alatna Village",
                },
                {
                    "code": "346",
                    "definition": "Native Village of Aleknagik",
                    "display": "Native Village of Aleknagik",
                },
                {
                    "code": "347",
                    "definition": "Algaaciq Native Village (St. Mary's)",
                    "display": "Algaaciq Native Village (St. Mary's)",
                },
                {
                    "code": "348",
                    "definition": "Allakaket Village",
                    "display": "Allakaket Village",
                },
                {
                    "code": "349",
                    "definition": "Native Village of Ambler",
                    "display": "Native Village of Ambler",
                },
                {
                    "code": "350",
                    "definition": "Village of Anaktuvuk Pass",
                    "display": "Village of Anaktuvuk Pass",
                },
                {
                    "code": "351",
                    "definition": "Yupiit of Andreafski",
                    "display": "Yupiit of Andreafski",
                },
                {
                    "code": "352",
                    "definition": "Angoon Community Association",
                    "display": "Angoon Community Association",
                },
                {
                    "code": "353",
                    "definition": "Village of Aniak",
                    "display": "Village of Aniak",
                },
                {
                    "code": "354",
                    "definition": "Anvik Village",
                    "display": "Anvik Village",
                },
                {
                    "code": "355",
                    "definition": "Arctic Village (See Native Village of Venetie Trib",
                    "display": "Arctic Village (See Native Village of Venetie Trib",
                },
                {
                    "code": "356",
                    "definition": "Asa carsarmiut Tribe (formerly Native Village of M",
                    "display": "Asa carsarmiut Tribe (formerly Native Village of M",
                },
                {
                    "code": "357",
                    "definition": "Native Village of Atka",
                    "display": "Native Village of Atka",
                },
                {
                    "code": "358",
                    "definition": "Village of Atmautluak",
                    "display": "Village of Atmautluak",
                },
                {
                    "code": "359",
                    "definition": "Atqasuk Village (Atkasook)",
                    "display": "Atqasuk Village (Atkasook)",
                },
                {
                    "code": "360",
                    "definition": "Native Village of Barrow Inupiat Traditional Gover",
                    "display": "Native Village of Barrow Inupiat Traditional Gover",
                },
                {
                    "code": "361",
                    "definition": "Beaver Village",
                    "display": "Beaver Village",
                },
                {
                    "code": "362",
                    "definition": "Native Village of Belkofski",
                    "display": "Native Village of Belkofski",
                },
                {
                    "code": "363",
                    "definition": "Village of Bill Moore's Slough",
                    "display": "Village of Bill Moore's Slough",
                },
                {
                    "code": "364",
                    "definition": "Birch Creek Tribe",
                    "display": "Birch Creek Tribe",
                },
                {
                    "code": "365",
                    "definition": "Native Village of Brevig Mission",
                    "display": "Native Village of Brevig Mission",
                },
                {
                    "code": "366",
                    "definition": "Native Village of Buckland",
                    "display": "Native Village of Buckland",
                },
                {
                    "code": "367",
                    "definition": "Native Village of Cantwell",
                    "display": "Native Village of Cantwell",
                },
                {
                    "code": "368",
                    "definition": "Native Village of Chanega (aka Chenega)",
                    "display": "Native Village of Chanega (aka Chenega)",
                },
                {
                    "code": "369",
                    "definition": "Chalkyitsik Village",
                    "display": "Chalkyitsik Village",
                },
                {
                    "code": "370",
                    "definition": "Village of Chefornak",
                    "display": "Village of Chefornak",
                },
                {
                    "code": "371",
                    "definition": "Chevak Native Village",
                    "display": "Chevak Native Village",
                },
                {
                    "code": "372",
                    "definition": "Chickaloon Native Village",
                    "display": "Chickaloon Native Village",
                },
                {
                    "code": "373",
                    "definition": "Native Village of Chignik",
                    "display": "Native Village of Chignik",
                },
                {
                    "code": "374",
                    "definition": "Native Village of Chignik Lagoon",
                    "display": "Native Village of Chignik Lagoon",
                },
                {
                    "code": "375",
                    "definition": "Chignik Lake Village",
                    "display": "Chignik Lake Village",
                },
                {
                    "code": "376",
                    "definition": "Chilkat Indian Village (Klukwan)",
                    "display": "Chilkat Indian Village (Klukwan)",
                },
                {
                    "code": "377",
                    "definition": "Chilkoot Indian Association (Haines)",
                    "display": "Chilkoot Indian Association (Haines)",
                },
                {
                    "code": "378",
                    "definition": "Chinik Eskimo Community (Golovin)",
                    "display": "Chinik Eskimo Community (Golovin)",
                },
                {
                    "code": "379",
                    "definition": "Native Village of Chistochina",
                    "display": "Native Village of Chistochina",
                },
                {
                    "code": "380",
                    "definition": "Native Village of Chitina",
                    "display": "Native Village of Chitina",
                },
                {
                    "code": "381",
                    "definition": "Native Village of Chuathbaluk (Russian Mission, Ku",
                    "display": "Native Village of Chuathbaluk (Russian Mission, Ku",
                },
                {
                    "code": "382",
                    "definition": "Chuloonawick Native Village",
                    "display": "Chuloonawick Native Village",
                },
                {
                    "code": "383",
                    "definition": "Circle Native Community",
                    "display": "Circle Native Community",
                },
                {
                    "code": "384",
                    "definition": "Village of Clark's Point",
                    "display": "Village of Clark's Point",
                },
                {
                    "code": "385",
                    "definition": "Native Village of Council",
                    "display": "Native Village of Council",
                },
                {
                    "code": "386",
                    "definition": "Craig Community Association",
                    "display": "Craig Community Association",
                },
                {
                    "code": "387",
                    "definition": "Village of Crooked Creek",
                    "display": "Village of Crooked Creek",
                },
                {
                    "code": "388",
                    "definition": "Curyung Tribal Council (formerly Native Village of",
                    "display": "Curyung Tribal Council (formerly Native Village of",
                },
                {
                    "code": "389",
                    "definition": "Native Village of Deering",
                    "display": "Native Village of Deering",
                },
                {
                    "code": "390",
                    "definition": "Native Village of Diomede (aka Inalik)",
                    "display": "Native Village of Diomede (aka Inalik)",
                },
                {
                    "code": "391",
                    "definition": "Village of Dot Lake",
                    "display": "Village of Dot Lake",
                },
                {
                    "code": "392",
                    "definition": "Douglas Indian Association",
                    "display": "Douglas Indian Association",
                },
                {
                    "code": "393",
                    "definition": "Native Village of Eagle",
                    "display": "Native Village of Eagle",
                },
                {
                    "code": "394",
                    "definition": "Native Village of Eek",
                    "display": "Native Village of Eek",
                },
                {
                    "code": "395",
                    "definition": "Egegik Village",
                    "display": "Egegik Village",
                },
                {
                    "code": "396",
                    "definition": "Eklutna Native Village",
                    "display": "Eklutna Native Village",
                },
                {
                    "code": "397",
                    "definition": "Native Village of Ekuk",
                    "display": "Native Village of Ekuk",
                },
                {
                    "code": "398",
                    "definition": "Ekwok Village",
                    "display": "Ekwok Village",
                },
                {
                    "code": "399",
                    "definition": "Native Village of Elim",
                    "display": "Native Village of Elim",
                },
                {
                    "code": "400",
                    "definition": "Emmonak Village",
                    "display": "Emmonak Village",
                },
                {
                    "code": "401",
                    "definition": "Evansville Village (aka Bettles Field)",
                    "display": "Evansville Village (aka Bettles Field)",
                },
                {
                    "code": "402",
                    "definition": "Native Village of Eyak (Cordova)",
                    "display": "Native Village of Eyak (Cordova)",
                },
                {
                    "code": "403",
                    "definition": "Native Village of False Pass",
                    "display": "Native Village of False Pass",
                },
                {
                    "code": "404",
                    "definition": "Native Village of Fort Yukon",
                    "display": "Native Village of Fort Yukon",
                },
                {
                    "code": "405",
                    "definition": "Native Village of Gakona",
                    "display": "Native Village of Gakona",
                },
                {
                    "code": "406",
                    "definition": "Galena Village (aka Louden Village)",
                    "display": "Galena Village (aka Louden Village)",
                },
                {
                    "code": "407",
                    "definition": "Native Village of Gambell",
                    "display": "Native Village of Gambell",
                },
                {
                    "code": "408",
                    "definition": "Native Village of Georgetown",
                    "display": "Native Village of Georgetown",
                },
                {
                    "code": "409",
                    "definition": "Native Village of Goodnews Bay",
                    "display": "Native Village of Goodnews Bay",
                },
                {
                    "code": "410",
                    "definition": "Organized Village of Grayling (aka Holikachuk)",
                    "display": "Organized Village of Grayling (aka Holikachuk)",
                },
                {
                    "code": "411",
                    "definition": "Gulkana Village",
                    "display": "Gulkana Village",
                },
                {
                    "code": "412",
                    "definition": "Native Village of Hamilton",
                    "display": "Native Village of Hamilton",
                },
                {
                    "code": "413",
                    "definition": "Healy Lake Village",
                    "display": "Healy Lake Village",
                },
                {
                    "code": "414",
                    "definition": "Holy Cross Village",
                    "display": "Holy Cross Village",
                },
                {
                    "code": "415",
                    "definition": "Hoonah Indian Association",
                    "display": "Hoonah Indian Association",
                },
                {
                    "code": "416",
                    "definition": "Native Village of Hooper Bay",
                    "display": "Native Village of Hooper Bay",
                },
                {
                    "code": "417",
                    "definition": "Hughes Village",
                    "display": "Hughes Village",
                },
                {
                    "code": "418",
                    "definition": "Huslia Village",
                    "display": "Huslia Village",
                },
                {
                    "code": "419",
                    "definition": "Hydaburg Cooperative Association",
                    "display": "Hydaburg Cooperative Association",
                },
                {
                    "code": "420",
                    "definition": "Igiugig Village",
                    "display": "Igiugig Village",
                },
                {
                    "code": "421",
                    "definition": "Village of Iliamna",
                    "display": "Village of Iliamna",
                },
                {
                    "code": "422",
                    "definition": "Inupiat Community of the Arctic Slope",
                    "display": "Inupiat Community of the Arctic Slope",
                },
                {
                    "code": "423",
                    "definition": "Iqurmuit Traditional Council (formerly Native Vill",
                    "display": "Iqurmuit Traditional Council (formerly Native Vill",
                },
                {
                    "code": "424",
                    "definition": "Ivanoff Bay Village",
                    "display": "Ivanoff Bay Village",
                },
                {
                    "code": "425",
                    "definition": "Kaguyak Village",
                    "display": "Kaguyak Village",
                },
                {
                    "code": "426",
                    "definition": "Organized Village of Kake",
                    "display": "Organized Village of Kake",
                },
                {
                    "code": "427",
                    "definition": "Kaktovik Village (aka Barter Island)",
                    "display": "Kaktovik Village (aka Barter Island)",
                },
                {
                    "code": "428",
                    "definition": "Village of Kalskag",
                    "display": "Village of Kalskag",
                },
                {
                    "code": "429",
                    "definition": "Village of Kaltag",
                    "display": "Village of Kaltag",
                },
                {
                    "code": "430",
                    "definition": "Native Village of Kanatak",
                    "display": "Native Village of Kanatak",
                },
                {
                    "code": "431",
                    "definition": "Native Village of Karluk",
                    "display": "Native Village of Karluk",
                },
                {
                    "code": "432",
                    "definition": "Organized Village of Kasaan",
                    "display": "Organized Village of Kasaan",
                },
                {
                    "code": "433",
                    "definition": "Native Village of Kasigluk",
                    "display": "Native Village of Kasigluk",
                },
                {
                    "code": "434",
                    "definition": "Kenaitze Indian Tribe",
                    "display": "Kenaitze Indian Tribe",
                },
                {
                    "code": "435",
                    "definition": "Ketchikan Indian Corporation",
                    "display": "Ketchikan Indian Corporation",
                },
                {
                    "code": "436",
                    "definition": "Native Village of Kiana",
                    "display": "Native Village of Kiana",
                },
                {
                    "code": "437",
                    "definition": "King Island Native Community",
                    "display": "King Island Native Community",
                },
                {
                    "code": "438",
                    "definition": "King Salmon Tribe",
                    "display": "King Salmon Tribe",
                },
                {
                    "code": "439",
                    "definition": "Native Village of Kipnuk",
                    "display": "Native Village of Kipnuk",
                },
                {
                    "code": "440",
                    "definition": "Native Village of Kivalina",
                    "display": "Native Village of Kivalina",
                },
                {
                    "code": "441",
                    "definition": "Klawock Cooperative Association",
                    "display": "Klawock Cooperative Association",
                },
                {
                    "code": "442",
                    "definition": "Native Village of Kluti Kaah (aka Copper Center)",
                    "display": "Native Village of Kluti Kaah (aka Copper Center)",
                },
                {"code": "443", "definition": "Knik Tribe", "display": "Knik Tribe"},
                {
                    "code": "444",
                    "definition": "Native Village of Kobuk",
                    "display": "Native Village of Kobuk",
                },
                {
                    "code": "445",
                    "definition": "Kokhanok Village",
                    "display": "Kokhanok Village",
                },
                {
                    "code": "446",
                    "definition": "Native Village of Kongiganak",
                    "display": "Native Village of Kongiganak",
                },
                {
                    "code": "447",
                    "definition": "Village of Kotlik",
                    "display": "Village of Kotlik",
                },
                {
                    "code": "448",
                    "definition": "Native Village of Kotzebue",
                    "display": "Native Village of Kotzebue",
                },
                {
                    "code": "449",
                    "definition": "Native Village of Koyuk",
                    "display": "Native Village of Koyuk",
                },
                {
                    "code": "450",
                    "definition": "Koyukuk Native Village",
                    "display": "Koyukuk Native Village",
                },
                {
                    "code": "451",
                    "definition": "Organized Village of Kwethluk",
                    "display": "Organized Village of Kwethluk",
                },
                {
                    "code": "452",
                    "definition": "Native Village of Kwigillingok",
                    "display": "Native Village of Kwigillingok",
                },
                {
                    "code": "453",
                    "definition": "Native Village of Kwinhagak (aka Quinhagak)",
                    "display": "Native Village of Kwinhagak (aka Quinhagak)",
                },
                {
                    "code": "454",
                    "definition": "Native Village of Larsen Bay",
                    "display": "Native Village of Larsen Bay",
                },
                {
                    "code": "455",
                    "definition": "Levelock Village",
                    "display": "Levelock Village",
                },
                {
                    "code": "456",
                    "definition": "Lesnoi Village (aka Woody Island)",
                    "display": "Lesnoi Village (aka Woody Island)",
                },
                {
                    "code": "457",
                    "definition": "Lime Village",
                    "display": "Lime Village",
                },
                {
                    "code": "458",
                    "definition": "Village of Lower Kalskag",
                    "display": "Village of Lower Kalskag",
                },
                {
                    "code": "459",
                    "definition": "Manley Hot Springs Village",
                    "display": "Manley Hot Springs Village",
                },
                {
                    "code": "460",
                    "definition": "Manokotak Village",
                    "display": "Manokotak Village",
                },
                {
                    "code": "461",
                    "definition": "Native Village of Marshall (aka Fortuna Ledge)",
                    "display": "Native Village of Marshall (aka Fortuna Ledge)",
                },
                {
                    "code": "462",
                    "definition": "Native Village of Mary's Igloo",
                    "display": "Native Village of Mary's Igloo",
                },
                {
                    "code": "463",
                    "definition": "McGrath Native Village",
                    "display": "McGrath Native Village",
                },
                {
                    "code": "464",
                    "definition": "Native Village of Mekoryuk",
                    "display": "Native Village of Mekoryuk",
                },
                {
                    "code": "465",
                    "definition": "Mentasta Traditional Council",
                    "display": "Mentasta Traditional Council",
                },
                {
                    "code": "466",
                    "definition": "Metlakatla Indian Community, Annette Island Reserv",
                    "display": "Metlakatla Indian Community, Annette Island Reserv",
                },
                {
                    "code": "467",
                    "definition": "Native Village of Minto",
                    "display": "Native Village of Minto",
                },
                {
                    "code": "468",
                    "definition": "Naknek Native Village",
                    "display": "Naknek Native Village",
                },
                {
                    "code": "469",
                    "definition": "Native Village of Nanwalek (aka English Bay)",
                    "display": "Native Village of Nanwalek (aka English Bay)",
                },
                {
                    "code": "470",
                    "definition": "Native Village of Napaimute",
                    "display": "Native Village of Napaimute",
                },
                {
                    "code": "471",
                    "definition": "Native Village of Napakiak",
                    "display": "Native Village of Napakiak",
                },
                {
                    "code": "472",
                    "definition": "Native Village of Napaskiak",
                    "display": "Native Village of Napaskiak",
                },
                {
                    "code": "473",
                    "definition": "Native Village of Nelson Lagoon",
                    "display": "Native Village of Nelson Lagoon",
                },
                {
                    "code": "474",
                    "definition": "Nenana Native Association",
                    "display": "Nenana Native Association",
                },
                {
                    "code": "475",
                    "definition": "New Koliganek Village Council (formerly Koliganek",
                    "display": "New Koliganek Village Council (formerly Koliganek",
                },
                {
                    "code": "476",
                    "definition": "New Stuyahok Village",
                    "display": "New Stuyahok Village",
                },
                {
                    "code": "477",
                    "definition": "Newhalen Village",
                    "display": "Newhalen Village",
                },
                {
                    "code": "478",
                    "definition": "Newtok Village",
                    "display": "Newtok Village",
                },
                {
                    "code": "479",
                    "definition": "Native Village of Nightmute",
                    "display": "Native Village of Nightmute",
                },
                {
                    "code": "480",
                    "definition": "Nikolai Village",
                    "display": "Nikolai Village",
                },
                {
                    "code": "481",
                    "definition": "Native Village of Nikolski",
                    "display": "Native Village of Nikolski",
                },
                {
                    "code": "482",
                    "definition": "Ninilchik Village",
                    "display": "Ninilchik Village",
                },
                {
                    "code": "483",
                    "definition": "Native Village of Noatak",
                    "display": "Native Village of Noatak",
                },
                {
                    "code": "484",
                    "definition": "Nome Eskimo Community",
                    "display": "Nome Eskimo Community",
                },
                {
                    "code": "485",
                    "definition": "Nondalton Village",
                    "display": "Nondalton Village",
                },
                {
                    "code": "486",
                    "definition": "Noorvik Native Community",
                    "display": "Noorvik Native Community",
                },
                {
                    "code": "487",
                    "definition": "Northway Village",
                    "display": "Northway Village",
                },
                {
                    "code": "488",
                    "definition": "Native Village of Nuiqsut (aka Nooiksut)",
                    "display": "Native Village of Nuiqsut (aka Nooiksut)",
                },
                {
                    "code": "489",
                    "definition": "Nulato Village",
                    "display": "Nulato Village",
                },
                {
                    "code": "490",
                    "definition": "Nunakauyarmiut Tribe (formerly Native Village of T",
                    "display": "Nunakauyarmiut Tribe (formerly Native Village of T",
                },
                {
                    "code": "491",
                    "definition": "Native Village of Nunapitchuk",
                    "display": "Native Village of Nunapitchuk",
                },
                {
                    "code": "492",
                    "definition": "Village of Ohogamiut",
                    "display": "Village of Ohogamiut",
                },
                {
                    "code": "493",
                    "definition": "Village of Old Harbor",
                    "display": "Village of Old Harbor",
                },
                {
                    "code": "494",
                    "definition": "Orutsararmuit Native Village (aka Bethel)",
                    "display": "Orutsararmuit Native Village (aka Bethel)",
                },
                {
                    "code": "495",
                    "definition": "Oscarville Traditional Village",
                    "display": "Oscarville Traditional Village",
                },
                {
                    "code": "496",
                    "definition": "Native Village of Ouzinkie",
                    "display": "Native Village of Ouzinkie",
                },
                {
                    "code": "497",
                    "definition": "Native Village of Paimiut",
                    "display": "Native Village of Paimiut",
                },
                {
                    "code": "498",
                    "definition": "Pauloff Harbor Village",
                    "display": "Pauloff Harbor Village",
                },
                {
                    "code": "499",
                    "definition": "Pedro Bay Village",
                    "display": "Pedro Bay Village",
                },
                {
                    "code": "500",
                    "definition": "Native Village of Perryville",
                    "display": "Native Village of Perryville",
                },
                {
                    "code": "501",
                    "definition": "Petersburg Indian Association",
                    "display": "Petersburg Indian Association",
                },
                {
                    "code": "502",
                    "definition": "Native Village of Pilot Point",
                    "display": "Native Village of Pilot Point",
                },
                {
                    "code": "503",
                    "definition": "Pilot Station Traditional Village",
                    "display": "Pilot Station Traditional Village",
                },
                {
                    "code": "504",
                    "definition": "Native Village of Pitka's Point",
                    "display": "Native Village of Pitka's Point",
                },
                {
                    "code": "505",
                    "definition": "Platinum Traditional Village",
                    "display": "Platinum Traditional Village",
                },
                {
                    "code": "506",
                    "definition": "Native Village of Point Hope",
                    "display": "Native Village of Point Hope",
                },
                {
                    "code": "507",
                    "definition": "Native Village of Point Lay",
                    "display": "Native Village of Point Lay",
                },
                {
                    "code": "508",
                    "definition": "Native Village of Port Graham",
                    "display": "Native Village of Port Graham",
                },
                {
                    "code": "509",
                    "definition": "Native Village of Port Heiden",
                    "display": "Native Village of Port Heiden",
                },
                {
                    "code": "510",
                    "definition": "Native Village of Port Lions",
                    "display": "Native Village of Port Lions",
                },
                {
                    "code": "511",
                    "definition": "Portage Creek Village (aka Ohgsenakale)",
                    "display": "Portage Creek Village (aka Ohgsenakale)",
                },
                {
                    "code": "512",
                    "definition": "Pribilof Islands Aleut Communities of St. Paul & S",
                    "display": "Pribilof Islands Aleut Communities of St. Paul & S",
                },
                {
                    "code": "513",
                    "definition": "Qagan Tayagungin Tribe of Sand Point Village",
                    "display": "Qagan Tayagungin Tribe of Sand Point Village",
                },
                {
                    "code": "514",
                    "definition": "Qawalangin Tribe of Unalaska",
                    "display": "Qawalangin Tribe of Unalaska",
                },
                {
                    "code": "515",
                    "definition": "Rampart Village",
                    "display": "Rampart Village",
                },
                {
                    "code": "516",
                    "definition": "Village of Red Devil",
                    "display": "Village of Red Devil",
                },
                {
                    "code": "517",
                    "definition": "Native Village of Ruby",
                    "display": "Native Village of Ruby",
                },
                {
                    "code": "518",
                    "definition": "Saint George Island(See Pribilof Islands Aleut Com",
                    "display": "Saint George Island(See Pribilof Islands Aleut Com",
                },
                {
                    "code": "519",
                    "definition": "Native Village of Saint Michael",
                    "display": "Native Village of Saint Michael",
                },
                {
                    "code": "520",
                    "definition": "Saint Paul Island (See Pribilof Islands Aleut Comm",
                    "display": "Saint Paul Island (See Pribilof Islands Aleut Comm",
                },
                {
                    "code": "521",
                    "definition": "Village of Salamatoff",
                    "display": "Village of Salamatoff",
                },
                {
                    "code": "522",
                    "definition": "Native Village of Savoonga",
                    "display": "Native Village of Savoonga",
                },
                {
                    "code": "523",
                    "definition": "Organized Village of Saxman",
                    "display": "Organized Village of Saxman",
                },
                {
                    "code": "524",
                    "definition": "Native Village of Scammon Bay",
                    "display": "Native Village of Scammon Bay",
                },
                {
                    "code": "525",
                    "definition": "Native Village of Selawik",
                    "display": "Native Village of Selawik",
                },
                {
                    "code": "526",
                    "definition": "Seldovia Village Tribe",
                    "display": "Seldovia Village Tribe",
                },
                {
                    "code": "527",
                    "definition": "Shageluk Native Village",
                    "display": "Shageluk Native Village",
                },
                {
                    "code": "528",
                    "definition": "Native Village of Shaktoolik",
                    "display": "Native Village of Shaktoolik",
                },
                {
                    "code": "529",
                    "definition": "Native Village of Sheldon's Point",
                    "display": "Native Village of Sheldon's Point",
                },
                {
                    "code": "530",
                    "definition": "Native Village of Shishmaref",
                    "display": "Native Village of Shishmaref",
                },
                {
                    "code": "531",
                    "definition": "Shoonaq Tribe of Kodiak",
                    "display": "Shoonaq Tribe of Kodiak",
                },
                {
                    "code": "532",
                    "definition": "Native Village of Shungnak",
                    "display": "Native Village of Shungnak",
                },
                {
                    "code": "533",
                    "definition": "Sitka Tribe of Alaska",
                    "display": "Sitka Tribe of Alaska",
                },
                {
                    "code": "534",
                    "definition": "Skagway Village",
                    "display": "Skagway Village",
                },
                {
                    "code": "535",
                    "definition": "Village of Sleetmute",
                    "display": "Village of Sleetmute",
                },
                {
                    "code": "536",
                    "definition": "Village of Solomon",
                    "display": "Village of Solomon",
                },
                {
                    "code": "537",
                    "definition": "South Naknek Village",
                    "display": "South Naknek Village",
                },
                {
                    "code": "538",
                    "definition": "Stebbins Community Association",
                    "display": "Stebbins Community Association",
                },
                {
                    "code": "539",
                    "definition": "Native Village of Stevens",
                    "display": "Native Village of Stevens",
                },
                {
                    "code": "540",
                    "definition": "Village of Stony River",
                    "display": "Village of Stony River",
                },
                {
                    "code": "541",
                    "definition": "Takotna Village",
                    "display": "Takotna Village",
                },
                {
                    "code": "542",
                    "definition": "Native Village of Tanacross",
                    "display": "Native Village of Tanacross",
                },
                {
                    "code": "543",
                    "definition": "Native Village of Tanana",
                    "display": "Native Village of Tanana",
                },
                {
                    "code": "544",
                    "definition": "Native Village of Tatitlek",
                    "display": "Native Village of Tatitlek",
                },
                {
                    "code": "545",
                    "definition": "Native Village of Tazlina",
                    "display": "Native Village of Tazlina",
                },
                {
                    "code": "546",
                    "definition": "Telida Village",
                    "display": "Telida Village",
                },
                {
                    "code": "547",
                    "definition": "Native Village of Teller",
                    "display": "Native Village of Teller",
                },
                {
                    "code": "548",
                    "definition": "Native Village of Tetlin",
                    "display": "Native Village of Tetlin",
                },
                {
                    "code": "549",
                    "definition": "Central Council of the Tlingit and Haida Indian Tb",
                    "display": "Central Council of the Tlingit and Haida Indian Tb",
                },
                {
                    "code": "550",
                    "definition": "Traditional Village of Togiak",
                    "display": "Traditional Village of Togiak",
                },
                {
                    "code": "551",
                    "definition": "Tuluksak Native Community",
                    "display": "Tuluksak Native Community",
                },
                {
                    "code": "552",
                    "definition": "Native Village of Tuntutuliak",
                    "display": "Native Village of Tuntutuliak",
                },
                {
                    "code": "553",
                    "definition": "Native Village of Tununak",
                    "display": "Native Village of Tununak",
                },
                {
                    "code": "554",
                    "definition": "Twin Hills Village",
                    "display": "Twin Hills Village",
                },
                {
                    "code": "555",
                    "definition": "Native Village of Tyonek",
                    "display": "Native Village of Tyonek",
                },
                {
                    "code": "556",
                    "definition": "Ugashik Village",
                    "display": "Ugashik Village",
                },
                {
                    "code": "557",
                    "definition": "Umkumiute Native Village",
                    "display": "Umkumiute Native Village",
                },
                {
                    "code": "558",
                    "definition": "Native Village of Unalakleet",
                    "display": "Native Village of Unalakleet",
                },
                {
                    "code": "559",
                    "definition": "Native Village of Unga",
                    "display": "Native Village of Unga",
                },
                {
                    "code": "560",
                    "definition": "Village of Venetie (See Native Village of Venetie",
                    "display": "Village of Venetie (See Native Village of Venetie",
                },
                {
                    "code": "561",
                    "definition": "Native Village of Venetie Tribal Government (Arcti",
                    "display": "Native Village of Venetie Tribal Government (Arcti",
                },
                {
                    "code": "562",
                    "definition": "Village of Wainwright",
                    "display": "Village of Wainwright",
                },
                {
                    "code": "563",
                    "definition": "Native Village of Wales",
                    "display": "Native Village of Wales",
                },
                {
                    "code": "564",
                    "definition": "Native Village of White Mountain",
                    "display": "Native Village of White Mountain",
                },
                {
                    "code": "565",
                    "definition": "Wrangell Cooperative Association",
                    "display": "Wrangell Cooperative Association",
                },
                {
                    "code": "566",
                    "definition": "Yakutat Tlingit Tribe",
                    "display": "Yakutat Tlingit Tribe",
                },
            ],
            "definition": "NATIVE ENTITIES WITHIN THE STATE OF ALASKA RECOGNIZED AND ELIGIBLE TO RECEIVE SERVICES FROM THE UNITED STATES BUREAU OF INDIAN AFFAIRS",
            "display": "NativeEntityAlaska",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    NativeEntityAlaska

    NATIVE ENTITIES WITHIN THE STATE OF ALASKA RECOGNIZED AND ELIGIBLE TO RECEIVE SERVICES FROM THE UNITED STATES BUREAU OF INDIAN AFFAIRS
    """

    underscore_native_entity_contiguous = CodeSystemConcept(
        {
            "code": "_NativeEntityContiguous",
            "concept": [
                {
                    "code": "1",
                    "definition": "Absentee-Shawnee Tribe of Indians of Oklahoma",
                    "display": "Absentee-Shawnee Tribe of Indians of Oklahoma",
                },
                {
                    "code": "10",
                    "definition": "Assiniboine and Sioux Tribes of the Fort Peck Indi",
                    "display": "Assiniboine and Sioux Tribes of the Fort Peck Indi",
                },
                {
                    "code": "100",
                    "definition": "Havasupai Tribe of the Havasupai Reservation, Ariz",
                    "display": "Havasupai Tribe of the Havasupai Reservation, Ariz",
                },
                {
                    "code": "101",
                    "definition": "Ho-Chunk Nation of Wisconsin (formerly known as th",
                    "display": "Ho-Chunk Nation of Wisconsin (formerly known as th",
                },
                {
                    "code": "102",
                    "definition": "Hoh Indian Tribe of the Hoh Indian Reservation, Wa",
                    "display": "Hoh Indian Tribe of the Hoh Indian Reservation, Wa",
                },
                {
                    "code": "103",
                    "definition": "Hoopa Valley Tribe, California",
                    "display": "Hoopa Valley Tribe, California",
                },
                {
                    "code": "104",
                    "definition": "Hopi Tribe of Arizona",
                    "display": "Hopi Tribe of Arizona",
                },
                {
                    "code": "105",
                    "definition": "Hopland Band of Pomo Indians of the Hopland Ranche",
                    "display": "Hopland Band of Pomo Indians of the Hopland Ranche",
                },
                {
                    "code": "106",
                    "definition": "Houlton Band of Maliseet Indians of Maine",
                    "display": "Houlton Band of Maliseet Indians of Maine",
                },
                {
                    "code": "107",
                    "definition": "Hualapai Indian Tribe of the Hualapai Indian Reser",
                    "display": "Hualapai Indian Tribe of the Hualapai Indian Reser",
                },
                {
                    "code": "108",
                    "definition": "Huron Potawatomi, Inc., Michigan",
                    "display": "Huron Potawatomi, Inc., Michigan",
                },
                {
                    "code": "109",
                    "definition": "Inaja Band of Diegueno Mission Indians of the Inaj",
                    "display": "Inaja Band of Diegueno Mission Indians of the Inaj",
                },
                {
                    "code": "11",
                    "definition": "Augustine Band of Cahuilla Mission Indians of the",
                    "display": "Augustine Band of Cahuilla Mission Indians of the",
                },
                {
                    "code": "110",
                    "definition": "Ione Band of Miwok Indians of California",
                    "display": "Ione Band of Miwok Indians of California",
                },
                {
                    "code": "111",
                    "definition": "Iowa Tribe of Kansas and Nebraska",
                    "display": "Iowa Tribe of Kansas and Nebraska",
                },
                {
                    "code": "112",
                    "definition": "Iowa Tribe of Oklahoma",
                    "display": "Iowa Tribe of Oklahoma",
                },
                {
                    "code": "113",
                    "definition": "Jackson Rancheria of Me-Wuk Indians of California",
                    "display": "Jackson Rancheria of Me-Wuk Indians of California",
                },
                {
                    "code": "114",
                    "definition": "Jamestown S'Klallam Tribe of Washington",
                    "display": "Jamestown S'Klallam Tribe of Washington",
                },
                {
                    "code": "115",
                    "definition": "Jamul Indian Village of California",
                    "display": "Jamul Indian Village of California",
                },
                {
                    "code": "116",
                    "definition": "Jena Band of Choctaw Indians, Louisiana",
                    "display": "Jena Band of Choctaw Indians, Louisiana",
                },
                {
                    "code": "117",
                    "definition": "Jicarilla Apache Tribe of the Jicarilla Apache Ind",
                    "display": "Jicarilla Apache Tribe of the Jicarilla Apache Ind",
                },
                {
                    "code": "118",
                    "definition": "Kaibab Band of Paiute Indians of the Kaibab Indian",
                    "display": "Kaibab Band of Paiute Indians of the Kaibab Indian",
                },
                {
                    "code": "119",
                    "definition": "Kalispel Indian Community of the Kalispel Reservat",
                    "display": "Kalispel Indian Community of the Kalispel Reservat",
                },
                {
                    "code": "12",
                    "definition": "Bad River Band of the Lake Superior Tribe of Chipp",
                    "display": "Bad River Band of the Lake Superior Tribe of Chipp",
                },
                {
                    "code": "120",
                    "definition": "Karuk Tribe of California",
                    "display": "Karuk Tribe of California",
                },
                {
                    "code": "121",
                    "definition": "Kashia Band of Pomo Indians of the Stewarts Point",
                    "display": "Kashia Band of Pomo Indians of the Stewarts Point",
                },
                {
                    "code": "122",
                    "definition": "Kaw Nation, Oklahoma",
                    "display": "Kaw Nation, Oklahoma",
                },
                {
                    "code": "123",
                    "definition": "Keweenaw Bay Indian Community of L'Anse and Ontona",
                    "display": "Keweenaw Bay Indian Community of L'Anse and Ontona",
                },
                {
                    "code": "124",
                    "definition": "Kialegee Tribal Town, Oklahoma",
                    "display": "Kialegee Tribal Town, Oklahoma",
                },
                {
                    "code": "125",
                    "definition": "Kickapoo Tribe of Indians of the Kickapoo Reservat",
                    "display": "Kickapoo Tribe of Indians of the Kickapoo Reservat",
                },
                {
                    "code": "126",
                    "definition": "Kickapoo Tribe of Oklahoma",
                    "display": "Kickapoo Tribe of Oklahoma",
                },
                {
                    "code": "127",
                    "definition": "Kickapoo Traditional Tribe of Texas",
                    "display": "Kickapoo Traditional Tribe of Texas",
                },
                {
                    "code": "128",
                    "definition": "Kiowa Indian Tribe of Oklahoma",
                    "display": "Kiowa Indian Tribe of Oklahoma",
                },
                {
                    "code": "129",
                    "definition": "Klamath Indian Tribe of Oregon",
                    "display": "Klamath Indian Tribe of Oregon",
                },
                {
                    "code": "13",
                    "definition": "Bay Mills Indian Community of the Sault Ste. Marie",
                    "display": "Bay Mills Indian Community of the Sault Ste. Marie",
                },
                {
                    "code": "130",
                    "definition": "Kootenai Tribe of Idaho",
                    "display": "Kootenai Tribe of Idaho",
                },
                {
                    "code": "131",
                    "definition": "La Jolla Band of Luiseno Mission Indians of the La",
                    "display": "La Jolla Band of Luiseno Mission Indians of the La",
                },
                {
                    "code": "132",
                    "definition": "La Posta Band of Diegueno Mission Indians of the L",
                    "display": "La Posta Band of Diegueno Mission Indians of the L",
                },
                {
                    "code": "133",
                    "definition": "Lac Courte Oreilles Band of Lake Superior Chippewa",
                    "display": "Lac Courte Oreilles Band of Lake Superior Chippewa",
                },
                {
                    "code": "134",
                    "definition": "Lac du Flambeau Band of Lake Superior Chippewa Ind",
                    "display": "Lac du Flambeau Band of Lake Superior Chippewa Ind",
                },
                {
                    "code": "135",
                    "definition": "Lac Vieux Desert Band of Lake Superior Chippewa In",
                    "display": "Lac Vieux Desert Band of Lake Superior Chippewa In",
                },
                {
                    "code": "136",
                    "definition": "Las Vegas Tribe of Paiute Indians of the Las Vegas",
                    "display": "Las Vegas Tribe of Paiute Indians of the Las Vegas",
                },
                {
                    "code": "137",
                    "definition": "Little River Band of Ottawa Indians of Michigan",
                    "display": "Little River Band of Ottawa Indians of Michigan",
                },
                {
                    "code": "138",
                    "definition": "Little Traverse Bay Bands of Odawa Indians of Mich",
                    "display": "Little Traverse Bay Bands of Odawa Indians of Mich",
                },
                {
                    "code": "139",
                    "definition": "Lower Lake Rancheria, California",
                    "display": "Lower Lake Rancheria, California",
                },
                {
                    "code": "14",
                    "definition": "Bear River Band of the Rohnerville Rancheria, Cali",
                    "display": "Bear River Band of the Rohnerville Rancheria, Cali",
                },
                {
                    "code": "140",
                    "definition": "Los Coyotes Band of Cahuilla Mission Indians of th",
                    "display": "Los Coyotes Band of Cahuilla Mission Indians of th",
                },
                {
                    "code": "141",
                    "definition": "Lovelock Paiute Tribe of the Lovelock Indian Colon",
                    "display": "Lovelock Paiute Tribe of the Lovelock Indian Colon",
                },
                {
                    "code": "142",
                    "definition": "Lower Brule Sioux Tribe of the Lower Brule Reserva",
                    "display": "Lower Brule Sioux Tribe of the Lower Brule Reserva",
                },
                {
                    "code": "143",
                    "definition": "Lower Elwha Tribal Community of the Lower Elwha Re",
                    "display": "Lower Elwha Tribal Community of the Lower Elwha Re",
                },
                {
                    "code": "144",
                    "definition": "Lower Sioux Indian Community of Minnesota Mdewakan",
                    "display": "Lower Sioux Indian Community of Minnesota Mdewakan",
                },
                {
                    "code": "145",
                    "definition": "Lummi Tribe of the Lummi Reservation, Washington",
                    "display": "Lummi Tribe of the Lummi Reservation, Washington",
                },
                {
                    "code": "146",
                    "definition": "Lytton Rancheria of California",
                    "display": "Lytton Rancheria of California",
                },
                {
                    "code": "147",
                    "definition": "Makah Indian Tribe of the Makah Indian Reservation",
                    "display": "Makah Indian Tribe of the Makah Indian Reservation",
                },
                {
                    "code": "148",
                    "definition": "Manchester Band of Pomo Indians of the Manchester-",
                    "display": "Manchester Band of Pomo Indians of the Manchester-",
                },
                {
                    "code": "149",
                    "definition": "Manzanita Band of Diegueno Mission Indians of the",
                    "display": "Manzanita Band of Diegueno Mission Indians of the",
                },
                {
                    "code": "15",
                    "definition": "Berry Creek Rancheria of Maidu Indians of Californ",
                    "display": "Berry Creek Rancheria of Maidu Indians of Californ",
                },
                {
                    "code": "150",
                    "definition": "Mashantucket Pequot Tribe of Connecticut",
                    "display": "Mashantucket Pequot Tribe of Connecticut",
                },
                {
                    "code": "151",
                    "definition": "Match-e-be-nash-she-wish Band of Pottawatomi India",
                    "display": "Match-e-be-nash-she-wish Band of Pottawatomi India",
                },
                {
                    "code": "152",
                    "definition": "Mechoopda Indian Tribe of Chico Rancheria, Califor",
                    "display": "Mechoopda Indian Tribe of Chico Rancheria, Califor",
                },
                {
                    "code": "153",
                    "definition": "Menominee Indian Tribe of Wisconsin",
                    "display": "Menominee Indian Tribe of Wisconsin",
                },
                {
                    "code": "154",
                    "definition": "Mesa Grande Band of Diegueno Mission Indians of th",
                    "display": "Mesa Grande Band of Diegueno Mission Indians of th",
                },
                {
                    "code": "155",
                    "definition": "Mescalero Apache Tribe of the Mescalero Reservatio",
                    "display": "Mescalero Apache Tribe of the Mescalero Reservatio",
                },
                {
                    "code": "156",
                    "definition": "Miami Tribe of Oklahoma",
                    "display": "Miami Tribe of Oklahoma",
                },
                {
                    "code": "157",
                    "definition": "Miccosukee Tribe of Indians of Florida",
                    "display": "Miccosukee Tribe of Indians of Florida",
                },
                {
                    "code": "158",
                    "definition": "Middletown Rancheria of Pomo Indians of California",
                    "display": "Middletown Rancheria of Pomo Indians of California",
                },
                {
                    "code": "159",
                    "definition": "Minnesota Chippewa Tribe, Minnesota (Six component",
                    "display": "Minnesota Chippewa Tribe, Minnesota (Six component",
                },
                {
                    "code": "16",
                    "definition": "Big Lagoon Rancheria, California",
                    "display": "Big Lagoon Rancheria, California",
                },
                {
                    "code": "160",
                    "definition": "Bois Forte Band (Nett Lake); Fond du Lac Band; Gra",
                    "display": "Bois Forte Band (Nett Lake); Fond du Lac Band; Gra",
                },
                {
                    "code": "161",
                    "definition": "Mississippi Band of Choctaw Indians, Mississippi",
                    "display": "Mississippi Band of Choctaw Indians, Mississippi",
                },
                {
                    "code": "162",
                    "definition": "Moapa Band of Paiute Indians of the Moapa River In",
                    "display": "Moapa Band of Paiute Indians of the Moapa River In",
                },
                {
                    "code": "163",
                    "definition": "Modoc Tribe of Oklahoma",
                    "display": "Modoc Tribe of Oklahoma",
                },
                {
                    "code": "164",
                    "definition": "Mohegan Indian Tribe of Connecticut",
                    "display": "Mohegan Indian Tribe of Connecticut",
                },
                {
                    "code": "165",
                    "definition": "Mooretown Rancheria of Maidu Indians of California",
                    "display": "Mooretown Rancheria of Maidu Indians of California",
                },
                {
                    "code": "166",
                    "definition": "Morongo Band of Cahuilla Mission Indians of the Mo",
                    "display": "Morongo Band of Cahuilla Mission Indians of the Mo",
                },
                {
                    "code": "167",
                    "definition": "Muckleshoot Indian Tribe of the Muckleshoot Reserv",
                    "display": "Muckleshoot Indian Tribe of the Muckleshoot Reserv",
                },
                {
                    "code": "168",
                    "definition": "Muscogee (Creek) Nation, Oklahoma",
                    "display": "Muscogee (Creek) Nation, Oklahoma",
                },
                {
                    "code": "169",
                    "definition": "Narragansett Indian Tribe of Rhode Island",
                    "display": "Narragansett Indian Tribe of Rhode Island",
                },
                {
                    "code": "17",
                    "definition": "Big Pine Band of Owens Valley Paiute Shoshone Indi",
                    "display": "Big Pine Band of Owens Valley Paiute Shoshone Indi",
                },
                {
                    "code": "170",
                    "definition": "Navajo Nation, Arizona, New Mexico & Utah",
                    "display": "Navajo Nation, Arizona, New Mexico & Utah",
                },
                {
                    "code": "171",
                    "definition": "Nez Perce Tribe of Idaho",
                    "display": "Nez Perce Tribe of Idaho",
                },
                {
                    "code": "172",
                    "definition": "Nisqually Indian Tribe of the Nisqually Reservatio",
                    "display": "Nisqually Indian Tribe of the Nisqually Reservatio",
                },
                {
                    "code": "173",
                    "definition": "Nooksack Indian Tribe of Washington",
                    "display": "Nooksack Indian Tribe of Washington",
                },
                {
                    "code": "174",
                    "definition": "Northern Cheyenne Tribe of the Northern Cheyenne I",
                    "display": "Northern Cheyenne Tribe of the Northern Cheyenne I",
                },
                {
                    "code": "175",
                    "definition": "Northfork Rancheria of Mono Indians of California",
                    "display": "Northfork Rancheria of Mono Indians of California",
                },
                {
                    "code": "176",
                    "definition": "Northwestern Band of Shoshoni Nation of Utah (Wash",
                    "display": "Northwestern Band of Shoshoni Nation of Utah (Wash",
                },
                {
                    "code": "177",
                    "definition": "Oglala Sioux Tribe of the Pine Ridge Reservation,",
                    "display": "Oglala Sioux Tribe of the Pine Ridge Reservation,",
                },
                {
                    "code": "178",
                    "definition": "Omaha Tribe of Nebraska",
                    "display": "Omaha Tribe of Nebraska",
                },
                {
                    "code": "179",
                    "definition": "Oneida Nation of New York",
                    "display": "Oneida Nation of New York",
                },
                {
                    "code": "18",
                    "definition": "Big Sandy Rancheria of Mono Indians of California",
                    "display": "Big Sandy Rancheria of Mono Indians of California",
                },
                {
                    "code": "180",
                    "definition": "Oneida Tribe of Wisconsin",
                    "display": "Oneida Tribe of Wisconsin",
                },
                {
                    "code": "181",
                    "definition": "Onondaga Nation of New York",
                    "display": "Onondaga Nation of New York",
                },
                {
                    "code": "182",
                    "definition": "Osage Tribe, Oklahoma",
                    "display": "Osage Tribe, Oklahoma",
                },
                {
                    "code": "183",
                    "definition": "Ottawa Tribe of Oklahoma",
                    "display": "Ottawa Tribe of Oklahoma",
                },
                {
                    "code": "184",
                    "definition": "Otoe-Missouria Tribe of Indians, Oklahoma",
                    "display": "Otoe-Missouria Tribe of Indians, Oklahoma",
                },
                {
                    "code": "185",
                    "definition": "Paiute Indian Tribe of Utah",
                    "display": "Paiute Indian Tribe of Utah",
                },
                {
                    "code": "186",
                    "definition": "Paiute-Shoshone Indians of the Bishop Community of",
                    "display": "Paiute-Shoshone Indians of the Bishop Community of",
                },
                {
                    "code": "187",
                    "definition": "Paiute-Shoshone Tribe of the Fallon Reservation an",
                    "display": "Paiute-Shoshone Tribe of the Fallon Reservation an",
                },
                {
                    "code": "188",
                    "definition": "Paiute-Shoshone Indians of the Lone Pine Community",
                    "display": "Paiute-Shoshone Indians of the Lone Pine Community",
                },
                {
                    "code": "189",
                    "definition": "Pala Band of Luiseno Mission Indians of the Pala R",
                    "display": "Pala Band of Luiseno Mission Indians of the Pala R",
                },
                {
                    "code": "19",
                    "definition": "Big Valley Band of Pomo Indians of the Big Valley",
                    "display": "Big Valley Band of Pomo Indians of the Big Valley",
                },
                {
                    "code": "190",
                    "definition": "Pascua Yaqui Tribe of Arizona",
                    "display": "Pascua Yaqui Tribe of Arizona",
                },
                {
                    "code": "191",
                    "definition": "Paskenta Band of Nomlaki Indians of California",
                    "display": "Paskenta Band of Nomlaki Indians of California",
                },
                {
                    "code": "192",
                    "definition": "Passamaquoddy Tribe of Maine",
                    "display": "Passamaquoddy Tribe of Maine",
                },
                {
                    "code": "193",
                    "definition": "Pauma Band of Luiseno Mission Indians of the Pauma",
                    "display": "Pauma Band of Luiseno Mission Indians of the Pauma",
                },
                {
                    "code": "194",
                    "definition": "Pawnee Nation of Oklahoma",
                    "display": "Pawnee Nation of Oklahoma",
                },
                {
                    "code": "195",
                    "definition": "Pechanga Band of Luiseno Mission Indians of the Pe",
                    "display": "Pechanga Band of Luiseno Mission Indians of the Pe",
                },
                {
                    "code": "196",
                    "definition": "Penobscot Tribe of Maine",
                    "display": "Penobscot Tribe of Maine",
                },
                {
                    "code": "197",
                    "definition": "Peoria Tribe of Indians of Oklahoma",
                    "display": "Peoria Tribe of Indians of Oklahoma",
                },
                {
                    "code": "198",
                    "definition": "Picayune Rancheria of Chukchansi Indians of Califo",
                    "display": "Picayune Rancheria of Chukchansi Indians of Califo",
                },
                {
                    "code": "199",
                    "definition": "Pinoleville Rancheria of Pomo Indians of Californi",
                    "display": "Pinoleville Rancheria of Pomo Indians of Californi",
                },
                {
                    "code": "2",
                    "definition": "Agua Caliente Band of Cahuilla Indians of the Agua",
                    "display": "Agua Caliente Band of Cahuilla Indians of the Agua",
                },
                {
                    "code": "20",
                    "definition": "Blackfeet Tribe of the Blackfeet Indian Reservatio",
                    "display": "Blackfeet Tribe of the Blackfeet Indian Reservatio",
                },
                {
                    "code": "200",
                    "definition": "Pit River Tribe, California (includes Big Bend, Lo",
                    "display": "Pit River Tribe, California (includes Big Bend, Lo",
                },
                {
                    "code": "201",
                    "definition": "Poarch Band of Creek Indians of Alabama",
                    "display": "Poarch Band of Creek Indians of Alabama",
                },
                {
                    "code": "202",
                    "definition": "Pokagon Band of Potawatomi Indians of Michigan",
                    "display": "Pokagon Band of Potawatomi Indians of Michigan",
                },
                {
                    "code": "203",
                    "definition": "Ponca Tribe of Indians of Oklahoma",
                    "display": "Ponca Tribe of Indians of Oklahoma",
                },
                {
                    "code": "204",
                    "definition": "Ponca Tribe of Nebraska",
                    "display": "Ponca Tribe of Nebraska",
                },
                {
                    "code": "205",
                    "definition": "Port Gamble Indian Community of the Port Gamble Re",
                    "display": "Port Gamble Indian Community of the Port Gamble Re",
                },
                {
                    "code": "206",
                    "definition": "Potter Valley Rancheria of Pomo Indians of Califor",
                    "display": "Potter Valley Rancheria of Pomo Indians of Califor",
                },
                {
                    "code": "207",
                    "definition": "Prairie Band of Potawatomi Indians, Kansas",
                    "display": "Prairie Band of Potawatomi Indians, Kansas",
                },
                {
                    "code": "208",
                    "definition": "Prairie Island Indian Community of Minnesota Mdewa",
                    "display": "Prairie Island Indian Community of Minnesota Mdewa",
                },
                {
                    "code": "209",
                    "definition": "Pueblo of Acoma, New Mexico",
                    "display": "Pueblo of Acoma, New Mexico",
                },
                {
                    "code": "21",
                    "definition": "Blue Lake Rancheria, California",
                    "display": "Blue Lake Rancheria, California",
                },
                {
                    "code": "210",
                    "definition": "Pueblo of Cochiti, New Mexico",
                    "display": "Pueblo of Cochiti, New Mexico",
                },
                {
                    "code": "211",
                    "definition": "Pueblo of Jemez, New Mexico",
                    "display": "Pueblo of Jemez, New Mexico",
                },
                {
                    "code": "212",
                    "definition": "Pueblo of Isleta, New Mexico",
                    "display": "Pueblo of Isleta, New Mexico",
                },
                {
                    "code": "213",
                    "definition": "Pueblo of Laguna, New Mexico",
                    "display": "Pueblo of Laguna, New Mexico",
                },
                {
                    "code": "214",
                    "definition": "Pueblo of Nambe, New Mexico",
                    "display": "Pueblo of Nambe, New Mexico",
                },
                {
                    "code": "215",
                    "definition": "Pueblo of Picuris, New Mexico",
                    "display": "Pueblo of Picuris, New Mexico",
                },
                {
                    "code": "216",
                    "definition": "Pueblo of Pojoaque, New Mexico",
                    "display": "Pueblo of Pojoaque, New Mexico",
                },
                {
                    "code": "217",
                    "definition": "Pueblo of San Felipe, New Mexico",
                    "display": "Pueblo of San Felipe, New Mexico",
                },
                {
                    "code": "218",
                    "definition": "Pueblo of San Juan, New Mexico",
                    "display": "Pueblo of San Juan, New Mexico",
                },
                {
                    "code": "219",
                    "definition": "Pueblo of San Ildefonso, New Mexico",
                    "display": "Pueblo of San Ildefonso, New Mexico",
                },
                {
                    "code": "22",
                    "definition": "Bridgeport Paiute Indian Colony of California",
                    "display": "Bridgeport Paiute Indian Colony of California",
                },
                {
                    "code": "220",
                    "definition": "Pueblo of Sandia, New Mexico",
                    "display": "Pueblo of Sandia, New Mexico",
                },
                {
                    "code": "221",
                    "definition": "Pueblo of Santa Ana, New Mexico",
                    "display": "Pueblo of Santa Ana, New Mexico",
                },
                {
                    "code": "222",
                    "definition": "Pueblo of Santa Clara, New Mexico",
                    "display": "Pueblo of Santa Clara, New Mexico",
                },
                {
                    "code": "223",
                    "definition": "Pueblo of Santo Domingo, New Mexico",
                    "display": "Pueblo of Santo Domingo, New Mexico",
                },
                {
                    "code": "224",
                    "definition": "Pueblo of Taos, New Mexico",
                    "display": "Pueblo of Taos, New Mexico",
                },
                {
                    "code": "225",
                    "definition": "Pueblo of Tesuque, New Mexico",
                    "display": "Pueblo of Tesuque, New Mexico",
                },
                {
                    "code": "226",
                    "definition": "Pueblo of Zia, New Mexico",
                    "display": "Pueblo of Zia, New Mexico",
                },
                {
                    "code": "227",
                    "definition": "Puyallup Tribe of the Puyallup Reservation, Washin",
                    "display": "Puyallup Tribe of the Puyallup Reservation, Washin",
                },
                {
                    "code": "228",
                    "definition": "Pyramid Lake Paiute Tribe of the Pyramid Lake Rese",
                    "display": "Pyramid Lake Paiute Tribe of the Pyramid Lake Rese",
                },
                {
                    "code": "229",
                    "definition": "Quapaw Tribe of Indians, Oklahoma",
                    "display": "Quapaw Tribe of Indians, Oklahoma",
                },
                {
                    "code": "23",
                    "definition": "Buena Vista Rancheria of Me-Wuk Indians of Califor",
                    "display": "Buena Vista Rancheria of Me-Wuk Indians of Califor",
                },
                {
                    "code": "230",
                    "definition": "Quartz Valley Indian Community of the Quartz Valle",
                    "display": "Quartz Valley Indian Community of the Quartz Valle",
                },
                {
                    "code": "231",
                    "definition": "Quechan Tribe of the Fort Yuma Indian Reservation,",
                    "display": "Quechan Tribe of the Fort Yuma Indian Reservation,",
                },
                {
                    "code": "232",
                    "definition": "Quileute Tribe of the Quileute Reservation, Washin",
                    "display": "Quileute Tribe of the Quileute Reservation, Washin",
                },
                {
                    "code": "233",
                    "definition": "Quinault Tribe of the Quinault Reservation, Washin",
                    "display": "Quinault Tribe of the Quinault Reservation, Washin",
                },
                {
                    "code": "234",
                    "definition": "Ramona Band or Village of Cahuilla Mission Indians",
                    "display": "Ramona Band or Village of Cahuilla Mission Indians",
                },
                {
                    "code": "235",
                    "definition": "Red Cliff Band of Lake Superior Chippewa Indians o",
                    "display": "Red Cliff Band of Lake Superior Chippewa Indians o",
                },
                {
                    "code": "236",
                    "definition": "Red Lake Band of Chippewa Indians of the Red Lake",
                    "display": "Red Lake Band of Chippewa Indians of the Red Lake",
                },
                {
                    "code": "237",
                    "definition": "Redding Rancheria, California",
                    "display": "Redding Rancheria, California",
                },
                {
                    "code": "238",
                    "definition": "Redwood Valley Rancheria of Pomo Indians of Califo",
                    "display": "Redwood Valley Rancheria of Pomo Indians of Califo",
                },
                {
                    "code": "239",
                    "definition": "Reno-Sparks Indian Colony, Nevada",
                    "display": "Reno-Sparks Indian Colony, Nevada",
                },
                {
                    "code": "24",
                    "definition": "Burns Paiute Tribe of the Burns Paiute Indian Colo",
                    "display": "Burns Paiute Tribe of the Burns Paiute Indian Colo",
                },
                {
                    "code": "240",
                    "definition": "Resighini Rancheria, California (formerly known as",
                    "display": "Resighini Rancheria, California (formerly known as",
                },
                {
                    "code": "241",
                    "definition": "Rincon Band of Luiseno Mission Indians of the Rinc",
                    "display": "Rincon Band of Luiseno Mission Indians of the Rinc",
                },
                {
                    "code": "242",
                    "definition": "Robinson Rancheria of Pomo Indians of California",
                    "display": "Robinson Rancheria of Pomo Indians of California",
                },
                {
                    "code": "243",
                    "definition": "Rosebud Sioux Tribe of the Rosebud Indian Reservat",
                    "display": "Rosebud Sioux Tribe of the Rosebud Indian Reservat",
                },
                {
                    "code": "244",
                    "definition": "Round Valley Indian Tribes of the Round Valley Res",
                    "display": "Round Valley Indian Tribes of the Round Valley Res",
                },
                {
                    "code": "245",
                    "definition": "Rumsey Indian Rancheria of Wintun Indians of Calif",
                    "display": "Rumsey Indian Rancheria of Wintun Indians of Calif",
                },
                {
                    "code": "246",
                    "definition": "Sac and Fox Tribe of the Mississippi in Iowa",
                    "display": "Sac and Fox Tribe of the Mississippi in Iowa",
                },
                {
                    "code": "247",
                    "definition": "Sac and Fox Nation of Missouri in Kansas and Nebra",
                    "display": "Sac and Fox Nation of Missouri in Kansas and Nebra",
                },
                {
                    "code": "248",
                    "definition": "Sac and Fox Nation, Oklahoma",
                    "display": "Sac and Fox Nation, Oklahoma",
                },
                {
                    "code": "249",
                    "definition": "Saginaw Chippewa Indian Tribe of Michigan, Isabell",
                    "display": "Saginaw Chippewa Indian Tribe of Michigan, Isabell",
                },
                {
                    "code": "25",
                    "definition": "Cabazon Band of Cahuilla Mission Indians of the Ca",
                    "display": "Cabazon Band of Cahuilla Mission Indians of the Ca",
                },
                {
                    "code": "250",
                    "definition": "Salt River Pima-Maricopa Indian Community of the S",
                    "display": "Salt River Pima-Maricopa Indian Community of the S",
                },
                {
                    "code": "251",
                    "definition": "Samish Indian Tribe, Washington",
                    "display": "Samish Indian Tribe, Washington",
                },
                {
                    "code": "252",
                    "definition": "San Carlos Apache Tribe of the San Carlos Reservat",
                    "display": "San Carlos Apache Tribe of the San Carlos Reservat",
                },
                {
                    "code": "253",
                    "definition": "San Juan Southern Paiute Tribe of Arizona",
                    "display": "San Juan Southern Paiute Tribe of Arizona",
                },
                {
                    "code": "254",
                    "definition": "San Manual Band of Serrano Mission Indians of the",
                    "display": "San Manual Band of Serrano Mission Indians of the",
                },
                {
                    "code": "255",
                    "definition": "San Pasqual Band of Diegueno Mission Indians of Ca",
                    "display": "San Pasqual Band of Diegueno Mission Indians of Ca",
                },
                {
                    "code": "256",
                    "definition": "Santa Rosa Indian Community of the Santa Rosa Ranc",
                    "display": "Santa Rosa Indian Community of the Santa Rosa Ranc",
                },
                {
                    "code": "257",
                    "definition": "Santa Rosa Band of Cahuilla Mission Indians of the",
                    "display": "Santa Rosa Band of Cahuilla Mission Indians of the",
                },
                {
                    "code": "258",
                    "definition": "Santa Ynez Band of Chumash Mission Indians of the",
                    "display": "Santa Ynez Band of Chumash Mission Indians of the",
                },
                {
                    "code": "259",
                    "definition": "Santa Ysabel Band of Diegueno Mission Indians of t",
                    "display": "Santa Ysabel Band of Diegueno Mission Indians of t",
                },
                {
                    "code": "26",
                    "definition": "Cachil DeHe Band of Wintun Indians of the Colusa I",
                    "display": "Cachil DeHe Band of Wintun Indians of the Colusa I",
                },
                {
                    "code": "260",
                    "definition": "Santee Sioux Tribe of the Santee Reservation of Ne",
                    "display": "Santee Sioux Tribe of the Santee Reservation of Ne",
                },
                {
                    "code": "261",
                    "definition": "Sauk-Suiattle Indian Tribe of Washington",
                    "display": "Sauk-Suiattle Indian Tribe of Washington",
                },
                {
                    "code": "262",
                    "definition": "Sault Ste. Marie Tribe of Chippewa Indians of Mich",
                    "display": "Sault Ste. Marie Tribe of Chippewa Indians of Mich",
                },
                {
                    "code": "263",
                    "definition": "Scotts Valley Band of Pomo Indians of California",
                    "display": "Scotts Valley Band of Pomo Indians of California",
                },
                {
                    "code": "264",
                    "definition": "Seminole Nation of Oklahoma",
                    "display": "Seminole Nation of Oklahoma",
                },
                {
                    "code": "265",
                    "definition": "Seminole Tribe of Florida, Dania, Big Cypress, Bri",
                    "display": "Seminole Tribe of Florida, Dania, Big Cypress, Bri",
                },
                {
                    "code": "266",
                    "definition": "Seneca Nation of New York",
                    "display": "Seneca Nation of New York",
                },
                {
                    "code": "267",
                    "definition": "Seneca-Cayuga Tribe of Oklahoma",
                    "display": "Seneca-Cayuga Tribe of Oklahoma",
                },
                {
                    "code": "268",
                    "definition": "Shakopee Mdewakanton Sioux Community of Minnesota",
                    "display": "Shakopee Mdewakanton Sioux Community of Minnesota",
                },
                {
                    "code": "269",
                    "definition": "Shawnee Tribe, Oklahoma",
                    "display": "Shawnee Tribe, Oklahoma",
                },
                {
                    "code": "27",
                    "definition": "Caddo Indian Tribe of Oklahoma",
                    "display": "Caddo Indian Tribe of Oklahoma",
                },
                {
                    "code": "270",
                    "definition": "Sherwood Valley Rancheria of Pomo Indians of Calif",
                    "display": "Sherwood Valley Rancheria of Pomo Indians of Calif",
                },
                {
                    "code": "271",
                    "definition": "Shingle Springs Band of Miwok Indians, Shingle Spr",
                    "display": "Shingle Springs Band of Miwok Indians, Shingle Spr",
                },
                {
                    "code": "272",
                    "definition": "Shoalwater Bay Tribe of the Shoalwater Bay Indian",
                    "display": "Shoalwater Bay Tribe of the Shoalwater Bay Indian",
                },
                {
                    "code": "273",
                    "definition": "Shoshone Tribe of the Wind River Reservation, Wyom",
                    "display": "Shoshone Tribe of the Wind River Reservation, Wyom",
                },
                {
                    "code": "274",
                    "definition": "Shoshone-Bannock Tribes of the Fort Hall Reservati",
                    "display": "Shoshone-Bannock Tribes of the Fort Hall Reservati",
                },
                {
                    "code": "275",
                    "definition": "Shoshone-Paiute Tribes of the Duck Valley Reservat",
                    "display": "Shoshone-Paiute Tribes of the Duck Valley Reservat",
                },
                {
                    "code": "276",
                    "definition": "Sisseton-Wahpeton Sioux Tribe of the Lake Traverse",
                    "display": "Sisseton-Wahpeton Sioux Tribe of the Lake Traverse",
                },
                {
                    "code": "277",
                    "definition": "Skokomish Indian Tribe of the Skokomish Reservatio",
                    "display": "Skokomish Indian Tribe of the Skokomish Reservatio",
                },
                {
                    "code": "278",
                    "definition": "Skull Valley Band of Goshute Indians of Utah",
                    "display": "Skull Valley Band of Goshute Indians of Utah",
                },
                {
                    "code": "279",
                    "definition": "Smith River Rancheria, California",
                    "display": "Smith River Rancheria, California",
                },
                {
                    "code": "28",
                    "definition": "Cahuilla Band of Mission Indians of the Cahuilla R",
                    "display": "Cahuilla Band of Mission Indians of the Cahuilla R",
                },
                {
                    "code": "280",
                    "definition": "Snoqualmie Tribe, Washington",
                    "display": "Snoqualmie Tribe, Washington",
                },
                {
                    "code": "281",
                    "definition": "Soboba Band of Luiseno Indians, California (former",
                    "display": "Soboba Band of Luiseno Indians, California (former",
                },
                {
                    "code": "282",
                    "definition": "Sokaogon Chippewa Community of the Mole Lake Band",
                    "display": "Sokaogon Chippewa Community of the Mole Lake Band",
                },
                {
                    "code": "283",
                    "definition": "Southern Ute Indian Tribe of the Southern Ute Rese",
                    "display": "Southern Ute Indian Tribe of the Southern Ute Rese",
                },
                {
                    "code": "284",
                    "definition": "Spirit Lake Tribe, North Dakota (formerly known as",
                    "display": "Spirit Lake Tribe, North Dakota (formerly known as",
                },
                {
                    "code": "285",
                    "definition": "Spokane Tribe of the Spokane Reservation, Washingt",
                    "display": "Spokane Tribe of the Spokane Reservation, Washingt",
                },
                {
                    "code": "286",
                    "definition": "Squaxin Island Tribe of the Squaxin Island Reserva",
                    "display": "Squaxin Island Tribe of the Squaxin Island Reserva",
                },
                {
                    "code": "287",
                    "definition": "St. Croix Chippewa Indians of Wisconsin, St. Croix",
                    "display": "St. Croix Chippewa Indians of Wisconsin, St. Croix",
                },
                {
                    "code": "288",
                    "definition": "St. Regis Band of Mohawk Indians of New York",
                    "display": "St. Regis Band of Mohawk Indians of New York",
                },
                {
                    "code": "289",
                    "definition": "Standing Rock Sioux Tribe of North & South Dakota",
                    "display": "Standing Rock Sioux Tribe of North & South Dakota",
                },
                {
                    "code": "29",
                    "definition": "Cahto Indian Tribe of the Laytonville Rancheria, C",
                    "display": "Cahto Indian Tribe of the Laytonville Rancheria, C",
                },
                {
                    "code": "290",
                    "definition": "Stockbridge-Munsee Community of Mohican Indians of",
                    "display": "Stockbridge-Munsee Community of Mohican Indians of",
                },
                {
                    "code": "291",
                    "definition": "Stillaguamish Tribe of Washington",
                    "display": "Stillaguamish Tribe of Washington",
                },
                {
                    "code": "292",
                    "definition": "Summit Lake Paiute Tribe of Nevada",
                    "display": "Summit Lake Paiute Tribe of Nevada",
                },
                {
                    "code": "293",
                    "definition": "Suquamish Indian Tribe of the Port Madison Reserva",
                    "display": "Suquamish Indian Tribe of the Port Madison Reserva",
                },
                {
                    "code": "294",
                    "definition": "Susanville Indian Rancheria, California",
                    "display": "Susanville Indian Rancheria, California",
                },
                {
                    "code": "295",
                    "definition": "Swinomish Indians of the Swinomish Reservation, Wa",
                    "display": "Swinomish Indians of the Swinomish Reservation, Wa",
                },
                {
                    "code": "296",
                    "definition": "Sycuan Band of Diegueno Mission Indians of Califor",
                    "display": "Sycuan Band of Diegueno Mission Indians of Califor",
                },
                {
                    "code": "297",
                    "definition": "Table Bluff Reservation - Wiyot Tribe, California",
                    "display": "Table Bluff Reservation - Wiyot Tribe, California",
                },
                {
                    "code": "298",
                    "definition": "Table Mountain Rancheria of California",
                    "display": "Table Mountain Rancheria of California",
                },
                {
                    "code": "299",
                    "definition": "Te-Moak Tribe of Western Shoshone Indians of Nevad",
                    "display": "Te-Moak Tribe of Western Shoshone Indians of Nevad",
                },
                {
                    "code": "3",
                    "definition": "Ak Chin Indian Community of the Maricopa (Ak Chin)",
                    "display": "Ak Chin Indian Community of the Maricopa (Ak Chin)",
                },
                {
                    "code": "30",
                    "definition": "California Valley Miwok Tribe, California (formerl",
                    "display": "California Valley Miwok Tribe, California (formerl",
                },
                {
                    "code": "300",
                    "definition": "Thlopthlocco Tribal Town, Oklahoma",
                    "display": "Thlopthlocco Tribal Town, Oklahoma",
                },
                {
                    "code": "301",
                    "definition": "Three Affiliated Tribes of the Fort Berthold Reser",
                    "display": "Three Affiliated Tribes of the Fort Berthold Reser",
                },
                {
                    "code": "302",
                    "definition": "Tohono O'odham Nation of Arizona",
                    "display": "Tohono O'odham Nation of Arizona",
                },
                {
                    "code": "303",
                    "definition": "Tonawanda Band of Seneca Indians of New York",
                    "display": "Tonawanda Band of Seneca Indians of New York",
                },
                {
                    "code": "304",
                    "definition": "Tonkawa Tribe of Indians of Oklahoma",
                    "display": "Tonkawa Tribe of Indians of Oklahoma",
                },
                {
                    "code": "305",
                    "definition": "Tonto Apache Tribe of Arizona",
                    "display": "Tonto Apache Tribe of Arizona",
                },
                {
                    "code": "306",
                    "definition": "Torres-Martinez Band of Cahuilla Mission Indians o",
                    "display": "Torres-Martinez Band of Cahuilla Mission Indians o",
                },
                {
                    "code": "307",
                    "definition": "Tule River Indian Tribe of the Tule River Reservat",
                    "display": "Tule River Indian Tribe of the Tule River Reservat",
                },
                {
                    "code": "308",
                    "definition": "Tulalip Tribes of the Tulalip Reservation, Washing",
                    "display": "Tulalip Tribes of the Tulalip Reservation, Washing",
                },
                {
                    "code": "309",
                    "definition": "Tunica-Biloxi Indian Tribe of Louisiana",
                    "display": "Tunica-Biloxi Indian Tribe of Louisiana",
                },
                {
                    "code": "31",
                    "definition": "Campo Band of Diegueno Mission Indians of the Camp",
                    "display": "Campo Band of Diegueno Mission Indians of the Camp",
                },
                {
                    "code": "310",
                    "definition": "Tuolumne Band of Me-Wuk Indians of the Tuolumne Ra",
                    "display": "Tuolumne Band of Me-Wuk Indians of the Tuolumne Ra",
                },
                {
                    "code": "311",
                    "definition": "Turtle Mountain Band of Chippewa Indians of North",
                    "display": "Turtle Mountain Band of Chippewa Indians of North",
                },
                {
                    "code": "312",
                    "definition": "Tuscarora Nation of New York",
                    "display": "Tuscarora Nation of New York",
                },
                {
                    "code": "313",
                    "definition": "Twenty-Nine Palms Band of Mission Indians of Calif",
                    "display": "Twenty-Nine Palms Band of Mission Indians of Calif",
                },
                {
                    "code": "314",
                    "definition": "United Auburn Indian Community of the Auburn Ranch",
                    "display": "United Auburn Indian Community of the Auburn Ranch",
                },
                {
                    "code": "315",
                    "definition": "United Keetoowah Band of Cherokee Indians of Oklah",
                    "display": "United Keetoowah Band of Cherokee Indians of Oklah",
                },
                {
                    "code": "316",
                    "definition": "Upper Lake Band of Pomo Indians of Upper Lake Ranc",
                    "display": "Upper Lake Band of Pomo Indians of Upper Lake Ranc",
                },
                {
                    "code": "317",
                    "definition": "Upper Sioux Indian Community of the Upper Sioux Re",
                    "display": "Upper Sioux Indian Community of the Upper Sioux Re",
                },
                {
                    "code": "318",
                    "definition": "Upper Skagit Indian Tribe of Washington",
                    "display": "Upper Skagit Indian Tribe of Washington",
                },
                {
                    "code": "319",
                    "definition": "Ute Indian Tribe of the Uintah & Ouray Reservation",
                    "display": "Ute Indian Tribe of the Uintah & Ouray Reservation",
                },
                {
                    "code": "32",
                    "definition": "Capitan Grande Band of Diegueno Mission Indians of",
                    "display": "Capitan Grande Band of Diegueno Mission Indians of",
                },
                {
                    "code": "320",
                    "definition": "Ute Mountain Tribe of the Ute Mountain Reservation",
                    "display": "Ute Mountain Tribe of the Ute Mountain Reservation",
                },
                {
                    "code": "321",
                    "definition": "Utu Utu Gwaitu Paiute Tribe of the Benton Paiute R",
                    "display": "Utu Utu Gwaitu Paiute Tribe of the Benton Paiute R",
                },
                {
                    "code": "322",
                    "definition": "Walker River Paiute Tribe of the Walker River Rese",
                    "display": "Walker River Paiute Tribe of the Walker River Rese",
                },
                {
                    "code": "323",
                    "definition": "Wampanoag Tribe of Gay Head (Aquinnah) of Massachu",
                    "display": "Wampanoag Tribe of Gay Head (Aquinnah) of Massachu",
                },
                {
                    "code": "324",
                    "definition": "Washoe Tribe of Nevada & California (Carson Colony",
                    "display": "Washoe Tribe of Nevada & California (Carson Colony",
                },
                {
                    "code": "325",
                    "definition": "White Mountain Apache Tribe of the Fort Apache Res",
                    "display": "White Mountain Apache Tribe of the Fort Apache Res",
                },
                {
                    "code": "326",
                    "definition": "Wichita and Affiliated Tribes (Wichita, Keechi, Wa",
                    "display": "Wichita and Affiliated Tribes (Wichita, Keechi, Wa",
                },
                {
                    "code": "327",
                    "definition": "Winnebago Tribe of Nebraska",
                    "display": "Winnebago Tribe of Nebraska",
                },
                {
                    "code": "328",
                    "definition": "Winnemucca Indian Colony of Nevada",
                    "display": "Winnemucca Indian Colony of Nevada",
                },
                {
                    "code": "329",
                    "definition": "Wyandotte Tribe of Oklahoma",
                    "display": "Wyandotte Tribe of Oklahoma",
                },
                {
                    "code": "33",
                    "definition": "Barona Group of Capitan Grande Band of Mission Ind",
                    "display": "Barona Group of Capitan Grande Band of Mission Ind",
                },
                {
                    "code": "330",
                    "definition": "Yankton Sioux Tribe of South Dakota",
                    "display": "Yankton Sioux Tribe of South Dakota",
                },
                {
                    "code": "331",
                    "definition": "Yavapai-Apache Nation of the Camp Verde Indian Res",
                    "display": "Yavapai-Apache Nation of the Camp Verde Indian Res",
                },
                {
                    "code": "332",
                    "definition": "Yavapai-Prescott Tribe of the Yavapai Reservation,",
                    "display": "Yavapai-Prescott Tribe of the Yavapai Reservation,",
                },
                {
                    "code": "333",
                    "definition": "Yerington Paiute Tribe of the Yerington Colony & C",
                    "display": "Yerington Paiute Tribe of the Yerington Colony & C",
                },
                {
                    "code": "334",
                    "definition": "Yomba Shoshone Tribe of the Yomba Reservation, Nev",
                    "display": "Yomba Shoshone Tribe of the Yomba Reservation, Nev",
                },
                {
                    "code": "335",
                    "definition": "Ysleta Del Sur Pueblo of Texas",
                    "display": "Ysleta Del Sur Pueblo of Texas",
                },
                {
                    "code": "336",
                    "definition": "Yurok Tribe of the Yurok Reservation, California",
                    "display": "Yurok Tribe of the Yurok Reservation, California",
                },
                {
                    "code": "337",
                    "definition": "Zuni Tribe of the Zuni Reservation, New Mexico",
                    "display": "Zuni Tribe of the Zuni Reservation, New Mexico",
                },
                {
                    "code": "34",
                    "definition": "Viejas (Baron Long) Group of Capitan Grande Band o",
                    "display": "Viejas (Baron Long) Group of Capitan Grande Band o",
                },
                {
                    "code": "35",
                    "definition": "Catawba Indian Nation (aka Catawba Tribe of South",
                    "display": "Catawba Indian Nation (aka Catawba Tribe of South",
                },
                {
                    "code": "36",
                    "definition": "Cayuga Nation of New York",
                    "display": "Cayuga Nation of New York",
                },
                {
                    "code": "37",
                    "definition": "Cedarville Rancheria, California",
                    "display": "Cedarville Rancheria, California",
                },
                {
                    "code": "38",
                    "definition": "Chemehuevi Indian Tribe of the Chemehuevi Reservat",
                    "display": "Chemehuevi Indian Tribe of the Chemehuevi Reservat",
                },
                {
                    "code": "39",
                    "definition": "Cher-Ae Heights Indian Community of the Trinidad R",
                    "display": "Cher-Ae Heights Indian Community of the Trinidad R",
                },
                {
                    "code": "4",
                    "definition": "Alabama-Coushatta Tribes of Texas",
                    "display": "Alabama-Coushatta Tribes of Texas",
                },
                {
                    "code": "40",
                    "definition": "Cherokee Nation, Oklahoma",
                    "display": "Cherokee Nation, Oklahoma",
                },
                {
                    "code": "41",
                    "definition": "Cheyenne-Arapaho Tribes of Oklahoma",
                    "display": "Cheyenne-Arapaho Tribes of Oklahoma",
                },
                {
                    "code": "42",
                    "definition": "Cheyenne River Sioux Tribe of the Cheyenne River R",
                    "display": "Cheyenne River Sioux Tribe of the Cheyenne River R",
                },
                {
                    "code": "43",
                    "definition": "Chickasaw Nation, Oklahoma",
                    "display": "Chickasaw Nation, Oklahoma",
                },
                {
                    "code": "44",
                    "definition": "Chicken Ranch Rancheria of Me-Wuk Indians of Calif",
                    "display": "Chicken Ranch Rancheria of Me-Wuk Indians of Calif",
                },
                {
                    "code": "45",
                    "definition": "Chippewa-Cree Indians of the Rocky Boy's Reservati",
                    "display": "Chippewa-Cree Indians of the Rocky Boy's Reservati",
                },
                {
                    "code": "46",
                    "definition": "Chitimacha Tribe of Louisiana",
                    "display": "Chitimacha Tribe of Louisiana",
                },
                {
                    "code": "47",
                    "definition": "Choctaw Nation of Oklahoma",
                    "display": "Choctaw Nation of Oklahoma",
                },
                {
                    "code": "48",
                    "definition": "Citizen Potawatomi Nation, Oklahoma",
                    "display": "Citizen Potawatomi Nation, Oklahoma",
                },
                {
                    "code": "49",
                    "definition": "Cloverdale Rancheria of Pomo Indians of California",
                    "display": "Cloverdale Rancheria of Pomo Indians of California",
                },
                {
                    "code": "5",
                    "definition": "Alabama-Quassarte Tribal Town, Oklahoma",
                    "display": "Alabama-Quassarte Tribal Town, Oklahoma",
                },
                {
                    "code": "50",
                    "definition": "Cocopah Tribe of Arizona",
                    "display": "Cocopah Tribe of Arizona",
                },
                {
                    "code": "51",
                    "definition": "Coeur D'Alene Tribe of the Coeur D'Alene Reservati",
                    "display": "Coeur D'Alene Tribe of the Coeur D'Alene Reservati",
                },
                {
                    "code": "52",
                    "definition": "Cold Springs Rancheria of Mono Indians of Californ",
                    "display": "Cold Springs Rancheria of Mono Indians of Californ",
                },
                {
                    "code": "53",
                    "definition": "Colorado River Indian Tribes of the Colorado River",
                    "display": "Colorado River Indian Tribes of the Colorado River",
                },
                {
                    "code": "54",
                    "definition": "Comanche Indian Tribe, Oklahoma",
                    "display": "Comanche Indian Tribe, Oklahoma",
                },
                {
                    "code": "55",
                    "definition": "Confederated Salish & Kootenai Tribes of the Flath",
                    "display": "Confederated Salish & Kootenai Tribes of the Flath",
                },
                {
                    "code": "56",
                    "definition": "Confederated Tribes of the Chehalis Reservation, W",
                    "display": "Confederated Tribes of the Chehalis Reservation, W",
                },
                {
                    "code": "57",
                    "definition": "Confederated Tribes of the Colville Reservation, W",
                    "display": "Confederated Tribes of the Colville Reservation, W",
                },
                {
                    "code": "58",
                    "definition": "Confederated Tribes of the Coos, Lower Umpqua and",
                    "display": "Confederated Tribes of the Coos, Lower Umpqua and",
                },
                {
                    "code": "59",
                    "definition": "Confederated Tribes of the Goshute Reservation, Ne",
                    "display": "Confederated Tribes of the Goshute Reservation, Ne",
                },
                {
                    "code": "6",
                    "definition": "Alturas Indian Rancheria, California",
                    "display": "Alturas Indian Rancheria, California",
                },
                {
                    "code": "60",
                    "definition": "Confederated Tribes of the Grand Ronde Community o",
                    "display": "Confederated Tribes of the Grand Ronde Community o",
                },
                {
                    "code": "61",
                    "definition": "Confederated Tribes of the Siletz Reservation, Ore",
                    "display": "Confederated Tribes of the Siletz Reservation, Ore",
                },
                {
                    "code": "62",
                    "definition": "Confederated Tribes of the Umatilla Reservation, O",
                    "display": "Confederated Tribes of the Umatilla Reservation, O",
                },
                {
                    "code": "63",
                    "definition": "Confederated Tribes of the Warm Springs Reservatio",
                    "display": "Confederated Tribes of the Warm Springs Reservatio",
                },
                {
                    "code": "64",
                    "definition": "Confederated Tribes and Bands of the Yakama Indian",
                    "display": "Confederated Tribes and Bands of the Yakama Indian",
                },
                {
                    "code": "65",
                    "definition": "Coquille Tribe of Oregon",
                    "display": "Coquille Tribe of Oregon",
                },
                {
                    "code": "66",
                    "definition": "Cortina Indian Rancheria of Wintun Indians of Cali",
                    "display": "Cortina Indian Rancheria of Wintun Indians of Cali",
                },
                {
                    "code": "67",
                    "definition": "Coushatta Tribe of Louisiana",
                    "display": "Coushatta Tribe of Louisiana",
                },
                {
                    "code": "68",
                    "definition": "Cow Creek Band of Umpqua Indians of Oregon",
                    "display": "Cow Creek Band of Umpqua Indians of Oregon",
                },
                {
                    "code": "69",
                    "definition": "Coyote Valley Band of Pomo Indians of California",
                    "display": "Coyote Valley Band of Pomo Indians of California",
                },
                {
                    "code": "7",
                    "definition": "Apache Tribe of Oklahoma",
                    "display": "Apache Tribe of Oklahoma",
                },
                {
                    "code": "70",
                    "definition": "Crow Tribe of Montana",
                    "display": "Crow Tribe of Montana",
                },
                {
                    "code": "71",
                    "definition": "Crow Creek Sioux Tribe of the Crow Creek Reservati",
                    "display": "Crow Creek Sioux Tribe of the Crow Creek Reservati",
                },
                {
                    "code": "72",
                    "definition": "Cuyapaipe Community of Diegueno Mission Indians of",
                    "display": "Cuyapaipe Community of Diegueno Mission Indians of",
                },
                {
                    "code": "73",
                    "definition": "Death Valley Timbi-Sha Shoshone Band of California",
                    "display": "Death Valley Timbi-Sha Shoshone Band of California",
                },
                {
                    "code": "74",
                    "definition": "Delaware Nation, Oklahoma (formerly Delaware Tribe",
                    "display": "Delaware Nation, Oklahoma (formerly Delaware Tribe",
                },
                {
                    "code": "75",
                    "definition": "Delaware Tribe of Indians, Oklahoma",
                    "display": "Delaware Tribe of Indians, Oklahoma",
                },
                {
                    "code": "76",
                    "definition": "Dry Creek Rancheria of Pomo Indians of California",
                    "display": "Dry Creek Rancheria of Pomo Indians of California",
                },
                {
                    "code": "77",
                    "definition": "Duckwater Shoshone Tribe of the Duckwater Reservat",
                    "display": "Duckwater Shoshone Tribe of the Duckwater Reservat",
                },
                {
                    "code": "78",
                    "definition": "Eastern Band of Cherokee Indians of North Carolina",
                    "display": "Eastern Band of Cherokee Indians of North Carolina",
                },
                {
                    "code": "79",
                    "definition": "Eastern Shawnee Tribe of Oklahoma",
                    "display": "Eastern Shawnee Tribe of Oklahoma",
                },
                {
                    "code": "8",
                    "definition": "Arapahoe Tribe of the Wind River Reservation, Wyom",
                    "display": "Arapahoe Tribe of the Wind River Reservation, Wyom",
                },
                {
                    "code": "80",
                    "definition": "Elem Indian Colony of Pomo Indians of the Sulphur",
                    "display": "Elem Indian Colony of Pomo Indians of the Sulphur",
                },
                {
                    "code": "81",
                    "definition": "Elk Valley Rancheria, California",
                    "display": "Elk Valley Rancheria, California",
                },
                {
                    "code": "82",
                    "definition": "Ely Shoshone Tribe of Nevada",
                    "display": "Ely Shoshone Tribe of Nevada",
                },
                {
                    "code": "83",
                    "definition": "Enterprise Rancheria of Maidu Indians of Californi",
                    "display": "Enterprise Rancheria of Maidu Indians of Californi",
                },
                {
                    "code": "84",
                    "definition": "Flandreau Santee Sioux Tribe of South Dakota",
                    "display": "Flandreau Santee Sioux Tribe of South Dakota",
                },
                {
                    "code": "85",
                    "definition": "Forest County Potawatomi Community of Wisconsin Po",
                    "display": "Forest County Potawatomi Community of Wisconsin Po",
                },
                {
                    "code": "86",
                    "definition": "Fort Belknap Indian Community of the Fort Belknap",
                    "display": "Fort Belknap Indian Community of the Fort Belknap",
                },
                {
                    "code": "87",
                    "definition": "Fort Bidwell Indian Community of the Fort Bidwell",
                    "display": "Fort Bidwell Indian Community of the Fort Bidwell",
                },
                {
                    "code": "88",
                    "definition": "Fort Independence Indian Community of Paiute India",
                    "display": "Fort Independence Indian Community of Paiute India",
                },
                {
                    "code": "89",
                    "definition": "Fort McDermitt Paiute and Shoshone Tribes of the F",
                    "display": "Fort McDermitt Paiute and Shoshone Tribes of the F",
                },
                {
                    "code": "9",
                    "definition": "Aroostook Band of Micmac Indians of Maine",
                    "display": "Aroostook Band of Micmac Indians of Maine",
                },
                {
                    "code": "90",
                    "definition": "Fort McDowell Yavapai Nation, Arizona (formerly th",
                    "display": "Fort McDowell Yavapai Nation, Arizona (formerly th",
                },
                {
                    "code": "91",
                    "definition": "Fort Mojave Indian Tribe of Arizona, California",
                    "display": "Fort Mojave Indian Tribe of Arizona, California",
                },
                {
                    "code": "92",
                    "definition": "Fort Sill Apache Tribe of Oklahoma",
                    "display": "Fort Sill Apache Tribe of Oklahoma",
                },
                {
                    "code": "93",
                    "definition": "Gila River Indian Community of the Gila River Indi",
                    "display": "Gila River Indian Community of the Gila River Indi",
                },
                {
                    "code": "94",
                    "definition": "Grand Traverse Band of Ottawa & Chippewa Indians o",
                    "display": "Grand Traverse Band of Ottawa & Chippewa Indians o",
                },
                {
                    "code": "95",
                    "definition": "Graton Rancheria, California",
                    "display": "Graton Rancheria, California",
                },
                {
                    "code": "96",
                    "definition": "Greenville Rancheria of Maidu Indians of Californi",
                    "display": "Greenville Rancheria of Maidu Indians of Californi",
                },
                {
                    "code": "97",
                    "definition": "Grindstone Indian Rancheria of Wintun-Wailaki Indi",
                    "display": "Grindstone Indian Rancheria of Wintun-Wailaki Indi",
                },
                {
                    "code": "98",
                    "definition": "Guidiville Rancheria of California",
                    "display": "Guidiville Rancheria of California",
                },
                {
                    "code": "99",
                    "definition": "Hannahville Indian Community of Wisconsin Potawato",
                    "display": "Hannahville Indian Community of Wisconsin Potawato",
                },
            ],
            "definition": "NATIVE ENTITIES WITHIN THE CONTIGUOUS 48 STATES",
            "display": "NativeEntityContiguous",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    NativeEntityContiguous

    NATIVE ENTITIES WITHIN THE CONTIGUOUS 48 STATES
    """

    class Meta:
        resource = _resource
