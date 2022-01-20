from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3SpecimenType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3SpecimenType:
    """
    v3 Code System SpecimenType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-SpecimenType
    """

    underscore_specimen_entity_type = CodeSystemConcept(
        {
            "code": "_SpecimenEntityType",
            "concept": [
                {"code": "ABS", "definition": "Abcess", "display": "Abcess"},
                {
                    "code": "AMN",
                    "definition": "Amniotic fluid",
                    "display": "Amniotic fluid",
                },
                {"code": "ASP", "definition": "Aspirate", "display": "Aspirate"},
                {"code": "BBL", "definition": "Blood bag", "display": "Blood bag"},
                {"code": "BDY", "definition": "Whole body", "display": "Whole body"},
                {"code": "BIFL", "definition": "Bile fluid", "display": "Bile fluid"},
                {"code": "BLD", "definition": "Whole blood", "display": "Whole blood"},
                {
                    "code": "BLDA",
                    "definition": "Blood arterial",
                    "display": "Blood arterial",
                },
                {
                    "code": "BLDC",
                    "definition": "Blood capillary",
                    "display": "Blood capillary",
                },
                {
                    "code": "BLDCO",
                    "definition": "Blood - cord",
                    "display": "Blood - cord",
                },
                {
                    "code": "BLDV",
                    "definition": "Blood venous",
                    "display": "Blood venous",
                },
                {"code": "BON", "definition": "Bone", "display": "Bone"},
                {"code": "BPH", "definition": "Basophils", "display": "Basophils"},
                {
                    "code": "BPU",
                    "definition": "Blood product unit",
                    "display": "Blood product unit",
                },
                {"code": "BRN", "definition": "Burn", "display": "Burn"},
                {"code": "BRO", "definition": "Bronchial", "display": "Bronchial"},
                {
                    "code": "BRTH",
                    "definition": "Exhaled gas (=breath)",
                    "display": "Exhaled gas (=breath)",
                },
                {
                    "code": "CALC",
                    "definition": "Calculus (=Stone)",
                    "display": "Calculus (=Stone)",
                },
                {
                    "code": "CDM",
                    "definition": "Cardiac muscle",
                    "display": "Cardiac muscle",
                },
                {"code": "CNJT", "definition": "Conjunctiva", "display": "Conjunctiva"},
                {"code": "CNL", "definition": "Cannula", "display": "Cannula"},
                {"code": "COL", "definition": "Colostrum", "display": "Colostrum"},
                {"code": "CRN", "definition": "Cornea", "display": "Cornea"},
                {
                    "code": "CSF",
                    "definition": "Cerebral spinal fluid",
                    "display": "Cerebral spinal fluid",
                },
                {
                    "code": "CTP",
                    "definition": "Catheter tip",
                    "display": "Catheter tip",
                },
                {"code": "CUR", "definition": "Curettage", "display": "Curettage"},
                {
                    "code": "CVM",
                    "definition": "Cervical mucus",
                    "display": "Cervical mucus",
                },
                {"code": "CVX", "definition": "Cervix", "display": "Cervix"},
                {"code": "CYST", "definition": "Cyst", "display": "Cyst"},
                {
                    "code": "DIAF",
                    "definition": "Dialysis fluid",
                    "display": "Dialysis fluid",
                },
                {
                    "code": "DOSE",
                    "definition": "Dose med or substance",
                    "display": "Dose med or substance",
                },
                {"code": "DRN", "definition": "Drain", "display": "Drain"},
                {
                    "code": "DUFL",
                    "definition": "Duodenal fluid",
                    "display": "Duodenal fluid",
                },
                {"code": "EAR", "definition": "Ear", "display": "Ear"},
                {
                    "code": "EARW",
                    "definition": "Ear wax (cerumen)",
                    "display": "Ear wax (cerumen)",
                },
                {"code": "ELT", "definition": "Electrode", "display": "Electrode"},
                {"code": "ENDC", "definition": "Endocardium", "display": "Endocardium"},
                {"code": "ENDM", "definition": "Endometrium", "display": "Endometrium"},
                {"code": "EOS", "definition": "Eosinophils", "display": "Eosinophils"},
                {"code": "EYE", "definition": "Eye", "display": "Eye"},
                {"code": "FIB", "definition": "Fibroblasts", "display": "Fibroblasts"},
                {"code": "FIST", "definition": "Fistula", "display": "Fistula"},
                {"code": "FLT", "definition": "Filter", "display": "Filter"},
                {
                    "code": "FLU",
                    "definition": "Body fluid, unsp",
                    "display": "Body fluid, unsp",
                },
                {"code": "FOOD", "definition": "Food sample", "display": "Food sample"},
                {"code": "GAS", "definition": "Gas", "display": "Gas"},
                {
                    "code": "GAST",
                    "definition": "Gastric fluid/contents",
                    "display": "Gastric fluid/contents",
                },
                {"code": "GEN", "definition": "Genital", "display": "Genital"},
                {
                    "code": "GENC",
                    "definition": "Genital cervix",
                    "display": "Genital cervix",
                },
                {
                    "code": "GENF",
                    "definition": "Genital fluid",
                    "display": "Genital fluid",
                },
                {
                    "code": "GENL",
                    "definition": "Genital lochia",
                    "display": "Genital lochia",
                },
                {
                    "code": "GENV",
                    "definition": "Genital vaginal",
                    "display": "Genital vaginal",
                },
                {"code": "HAR", "definition": "Hair", "display": "Hair"},
                {"code": "IHG", "definition": "Inhaled Gas", "display": "Inhaled Gas"},
                {"code": "ISLT", "definition": "Isolate", "display": "Isolate"},
                {
                    "code": "IT",
                    "definition": "Intubation tube",
                    "display": "Intubation tube",
                },
                {"code": "LAM", "definition": "Lamella", "display": "Lamella"},
                {"code": "LIQ", "definition": "Liquid NOS", "display": "Liquid NOS"},
                {"code": "LN", "definition": "Line", "display": "Line"},
                {
                    "code": "LNA",
                    "definition": "Line arterial",
                    "display": "Line arterial",
                },
                {"code": "LNV", "definition": "Line venous", "display": "Line venous"},
                {"code": "LYM", "definition": "Lymphocytes", "display": "Lymphocytes"},
                {"code": "MAC", "definition": "Macrophages", "display": "Macrophages"},
                {
                    "code": "MAR",
                    "definition": "Marrow (bone)",
                    "display": "Marrow (bone)",
                },
                {
                    "code": "MBLD",
                    "definition": "Menstrual blood",
                    "display": "Menstrual blood",
                },
                {"code": "MEC", "definition": "Meconium", "display": "Meconium"},
                {"code": "MILK", "definition": "Breast milk", "display": "Breast milk"},
                {"code": "MLK", "definition": "Milk", "display": "Milk"},
                {"code": "NAIL", "definition": "Nail", "display": "Nail"},
                {
                    "code": "NOS",
                    "definition": "Nose (nasal passage)",
                    "display": "Nose (nasal passage)",
                },
                {
                    "code": "PAFL",
                    "definition": "Pancreatic fluid",
                    "display": "Pancreatic fluid",
                },
                {"code": "PAT", "definition": "Patient", "display": "Patient"},
                {"code": "PLAS", "definition": "Plasma", "display": "Plasma"},
                {"code": "PLB", "definition": "Plasma bag", "display": "Plasma bag"},
                {"code": "PLC", "definition": "Placenta", "display": "Placenta"},
                {
                    "code": "PLR",
                    "definition": "Pleural fluid (thoracentesis fld)",
                    "display": "Pleural fluid (thoracentesis fld)",
                },
                {
                    "code": "PMN",
                    "definition": "Polymorphonuclear neutrophils",
                    "display": "Polymorphonuclear neutrophils",
                },
                {
                    "code": "PPP",
                    "definition": "Platelet poor plasma",
                    "display": "Platelet poor plasma",
                },
                {
                    "code": "PRP",
                    "definition": "Platelet rich plasma",
                    "display": "Platelet rich plasma",
                },
                {
                    "code": "PRT",
                    "definition": "Peritoneal fluid /ascites",
                    "display": "Peritoneal fluid /ascites",
                },
                {"code": "PUS", "definition": "Pus", "display": "Pus"},
                {
                    "code": "RBC",
                    "definition": "Erythrocytes",
                    "display": "Erythrocytes",
                },
                {"code": "SAL", "definition": "Saliva", "display": "Saliva"},
                {"code": "SER", "definition": "Serum", "display": "Serum"},
                {
                    "code": "SKM",
                    "definition": "Skeletal muscle",
                    "display": "Skeletal muscle",
                },
                {"code": "SKN", "definition": "Skin", "display": "Skin"},
                {
                    "code": "SMN",
                    "definition": "Seminal fluid",
                    "display": "Seminal fluid",
                },
                {
                    "code": "SMPLS",
                    "definition": "Seminal plasma",
                    "display": "Seminal plasma",
                },
                {
                    "code": "SNV",
                    "definition": "Synovial fluid (Joint fluid)",
                    "display": "Synovial fluid (Joint fluid)",
                },
                {"code": "SPRM", "definition": "Spermatozoa", "display": "Spermatozoa"},
                {"code": "SPT", "definition": "Sputum", "display": "Sputum"},
                {
                    "code": "SPTC",
                    "definition": "Sputum - coughed",
                    "display": "Sputum - coughed",
                },
                {
                    "code": "SPTT",
                    "definition": "Sputum - tracheal aspirate",
                    "display": "Sputum - tracheal aspirate",
                },
                {
                    "code": "STL",
                    "definition": "Stool = Fecal",
                    "display": "Stool = Fecal",
                },
                {"code": "SWT", "definition": "Sweat", "display": "Sweat"},
                {"code": "TEAR", "definition": "Tears", "display": "Tears"},
                {
                    "code": "THRB",
                    "definition": "Thrombocyte (platelet)",
                    "display": "Thrombocyte (platelet)",
                },
                {"code": "THRT", "definition": "Throat", "display": "Throat"},
                {
                    "code": "TISG",
                    "definition": "Tissue gall bladder",
                    "display": "Tissue gall bladder",
                },
                {
                    "code": "TISPL",
                    "definition": "Tissue placenta",
                    "display": "Tissue placenta",
                },
                {
                    "code": "TISS",
                    "definition": "Tissue, unspecified",
                    "display": "Tissue, unspecified",
                },
                {
                    "code": "TISU",
                    "definition": "Tissue ulcer",
                    "display": "Tissue ulcer",
                },
                {
                    "code": "TLGI",
                    "definition": "Tissue large intestine",
                    "display": "Tissue large intestine",
                },
                {"code": "TLNG", "definition": "Tissue lung", "display": "Tissue lung"},
                {
                    "code": "TSMI",
                    "definition": "Tissue small intestine Tissue ulcer",
                    "display": "Tissue small intestine Tissue ulcer",
                },
                {
                    "code": "TUB",
                    "definition": "Tube, unspecified",
                    "display": "Tube, unspecified",
                },
                {"code": "ULC", "definition": "Ulcer", "display": "Ulcer"},
                {
                    "code": "UMB",
                    "definition": "Umbilical blood",
                    "display": "Umbilical blood",
                },
                {
                    "code": "UMED",
                    "definition": "Unknown medicine",
                    "display": "Unknown medicine",
                },
                {"code": "UR", "definition": "Urine", "display": "Urine"},
                {
                    "code": "URC",
                    "definition": "Urine clean catch",
                    "display": "Urine clean catch",
                },
                {
                    "code": "URNS",
                    "definition": "Urine sediment",
                    "display": "Urine sediment",
                },
                {
                    "code": "URT",
                    "definition": "Urine catheter",
                    "display": "Urine catheter",
                },
                {"code": "URTH", "definition": "Urethra", "display": "Urethra"},
                {
                    "code": "USUB",
                    "definition": "Unknown substance",
                    "display": "Unknown substance",
                },
                {"code": "VOM", "definition": "Vomitus", "display": "Vomitus"},
                {"code": "WAT", "definition": "Water", "display": "Water"},
                {"code": "WBC", "definition": "Leukocytes", "display": "Leukocytes"},
                {"code": "WICK", "definition": "Wick", "display": "Wick"},
                {"code": "WND", "definition": "Wound", "display": "Wound"},
                {
                    "code": "WNDA",
                    "definition": "Wound abscess",
                    "display": "Wound abscess",
                },
                {
                    "code": "WNDD",
                    "definition": "Wound drainage",
                    "display": "Wound drainage",
                },
                {
                    "code": "WNDE",
                    "definition": "Wound exudate",
                    "display": "Wound exudate",
                },
            ],
            "definition": "SpecimenEntityType",
            "display": "SpecimenEntityType",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    SpecimenEntityType

    SpecimenEntityType
    """

    class Meta:
        resource = _resource
