from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3VaccineManufacturer"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3VaccineManufacturer:
    """
    v3 Code System VaccineManufacturer

     The manufacturer of a vaccine.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-VaccineManufacturer
    """

    ab = CodeSystemConcept(
        {
            "code": "AB",
            "definition": "Abbott Laboratories (includes Ross Products Division)",
            "display": "Abbott Laboratories (includes Ross Products Division)",
        }
    )
    """
    Abbott Laboratories (includes Ross Products Division)

    Abbott Laboratories (includes Ross Products Division)
    """

    ad = CodeSystemConcept(
        {
            "code": "AD",
            "definition": "Adams Laboratories",
            "display": "Adams Laboratories",
        }
    )
    """
    Adams Laboratories

    Adams Laboratories
    """

    alp = CodeSystemConcept(
        {
            "code": "ALP",
            "definition": "Alpha Therapeutic Corporation",
            "display": "Alpha Therapeutic Corporation",
        }
    )
    """
    Alpha Therapeutic Corporation

    Alpha Therapeutic Corporation
    """

    ar = CodeSystemConcept(
        {
            "code": "AR",
            "definition": "Armour [Inactive-use CEN]",
            "display": "Armour [Inactive - use CEN]",
        }
    )
    """
    Armour [Inactive - use CEN]

    Armour [Inactive-use CEN]
    """

    avi = CodeSystemConcept(
        {"code": "AVI", "definition": "Aviron", "display": "Aviron"}
    )
    """
    Aviron

    Aviron
    """

    ba = CodeSystemConcept(
        {
            "code": "BA",
            "definition": "Baxter Healthcare Corporation",
            "display": "Baxter Healthcare Corporation",
        }
    )
    """
    Baxter Healthcare Corporation

    Baxter Healthcare Corporation
    """

    bay = CodeSystemConcept(
        {
            "code": "BAY",
            "definition": "Bayer Corporation (includes Miles, Inc. and Cutter Laboratories)",
            "display": "Bayer Corporation (includes Miles, Inc. and Cutter Laboratories)",
        }
    )
    """
    Bayer Corporation (includes Miles, Inc. and Cutter Laboratories)

    Bayer Corporation (includes Miles, Inc. and Cutter Laboratories)
    """

    bp = CodeSystemConcept(
        {
            "code": "BP",
            "definition": "Berna Products [Inactive-use BPC]",
            "display": "Berna Products [Inactive - use BPC]",
        }
    )
    """
    Berna Products [Inactive - use BPC]

    Berna Products [Inactive-use BPC]
    """

    bpc = CodeSystemConcept(
        {
            "code": "BPC",
            "definition": "Berna Products Corporation (includes Swiss Serum and Vaccine Institute Berne)",
            "display": "Berna Products Corporation (includes Swiss Serum and Vaccine Institute Berne)",
        }
    )
    """
    Berna Products Corporation (includes Swiss Serum and Vaccine Institute Berne)

    Berna Products Corporation (includes Swiss Serum and Vaccine Institute Berne)
    """

    cen = CodeSystemConcept(
        {
            "code": "CEN",
            "definition": "Centeon L.L.C. (includes Armour Pharmaceutical Company)",
            "display": "Centeon L.L.C. (includes Armour Pharmaceutical Company)",
        }
    )
    """
    Centeon L.L.C. (includes Armour Pharmaceutical Company)

    Centeon L.L.C. (includes Armour Pharmaceutical Company)
    """

    chi = CodeSystemConcept(
        {
            "code": "CHI",
            "definition": "Chiron Corporation",
            "display": "Chiron Corporation",
        }
    )
    """
    Chiron Corporation

    Chiron Corporation
    """

    con = CodeSystemConcept(
        {
            "code": "CON",
            "definition": "Connaught [Inactive-use PMC]",
            "display": "Connaught [Inactive - use PMC]",
        }
    )
    """
    Connaught [Inactive - use PMC]

    Connaught [Inactive-use PMC]
    """

    evn = CodeSystemConcept(
        {
            "code": "EVN",
            "definition": "Evans Medical Limited (an affiliate of Medeva Pharmaceuticals, Inc.)",
            "display": "Evans Medical Limited (an affiliate of Medeva Pharmaceuticals, Inc.)",
        }
    )
    """
    Evans Medical Limited (an affiliate of Medeva Pharmaceuticals, Inc.)

    Evans Medical Limited (an affiliate of Medeva Pharmaceuticals, Inc.)
    """

    gre = CodeSystemConcept(
        {
            "code": "GRE",
            "definition": "Greer Laboratories, Inc.",
            "display": "Greer Laboratories, Inc.",
        }
    )
    """
    Greer Laboratories, Inc.

    Greer Laboratories, Inc.
    """

    iag = CodeSystemConcept(
        {
            "code": "IAG",
            "definition": "Immuno International AG",
            "display": "Immuno International AG",
        }
    )
    """
    Immuno International AG

    Immuno International AG
    """

    im = CodeSystemConcept(
        {
            "code": "IM",
            "definition": "Merieux [Inactive-use PMC]",
            "display": "Merieux [Inactive - use PMC]",
        }
    )
    """
    Merieux [Inactive - use PMC]

    Merieux [Inactive-use PMC]
    """

    ius = CodeSystemConcept(
        {
            "code": "IUS",
            "definition": "Immuno-U.S., Inc.",
            "display": "Immuno-U.S., Inc.",
        }
    )
    """
    Immuno-U.S., Inc.

    Immuno-U.S., Inc.
    """

    jpn = CodeSystemConcept(
        {
            "code": "JPN",
            "definition": "The Research Foundation for Microbial Diseases of Osaka University (BIKEN)",
            "display": "The Research Foundation for Microbial Diseases of Osaka University (BIKEN)",
        }
    )
    """
    The Research Foundation for Microbial Diseases of Osaka University (BIKEN)

    The Research Foundation for Microbial Diseases of Osaka University (BIKEN)
    """

    kgc = CodeSystemConcept(
        {
            "code": "KGC",
            "definition": "Korea Green Cross Corporation",
            "display": "Korea Green Cross Corporation",
        }
    )
    """
    Korea Green Cross Corporation

    Korea Green Cross Corporation
    """

    led = CodeSystemConcept(
        {
            "code": "LED",
            "definition": "Lederle [Inactive-use WAL]",
            "display": "Lederle [Inactive - use WAL]",
        }
    )
    """
    Lederle [Inactive - use WAL]

    Lederle [Inactive-use WAL]
    """

    ma = CodeSystemConcept(
        {
            "code": "MA",
            "definition": "Massachusetts Public Health Biologic Laboratories",
            "display": "Massachusetts Public Health Biologic Laboratories",
        }
    )
    """
    Massachusetts Public Health Biologic Laboratories

    Massachusetts Public Health Biologic Laboratories
    """

    med = CodeSystemConcept(
        {"code": "MED", "definition": "MedImmune, Inc.", "display": "MedImmune, Inc."}
    )
    """
    MedImmune, Inc.

    MedImmune, Inc.
    """

    mil = CodeSystemConcept(
        {
            "code": "MIL",
            "definition": "Miles [Inactive-use BAY]",
            "display": "Miles [Inactive - use BAY]",
        }
    )
    """
    Miles [Inactive - use BAY]

    Miles [Inactive-use BAY]
    """

    mip = CodeSystemConcept(
        {
            "code": "MIP",
            "definition": "Bioport Corporation (formerly Michigan Biologic Products Institute)",
            "display": "Bioport Corporation (formerly Michigan Biologic Products Institute)",
        }
    )
    """
    Bioport Corporation (formerly Michigan Biologic Products Institute)

    Bioport Corporation (formerly Michigan Biologic Products Institute)
    """

    msd = CodeSystemConcept(
        {
            "code": "MSD",
            "definition": "Merck & Co., Inc.",
            "display": "Merck and Co., Inc.",
        }
    )
    """
    Merck and Co., Inc.

    Merck & Co., Inc.
    """

    nab = CodeSystemConcept(
        {
            "code": "NAB",
            "definition": "NABI (formerly North American Biologicals, Inc.)",
            "display": "NABI (formerly North American Biologicals, Inc.)",
        }
    )
    """
    NABI (formerly North American Biologicals, Inc.)

    NABI (formerly North American Biologicals, Inc.)
    """

    nav = CodeSystemConcept(
        {
            "code": "NAV",
            "definition": "North American Vaccine, Inc.",
            "display": "North American Vaccine, Inc.",
        }
    )
    """
    North American Vaccine, Inc.

    North American Vaccine, Inc.
    """

    nov = CodeSystemConcept(
        {
            "code": "NOV",
            "definition": "Novartis Pharmaceutical Corporation (includes Ciba-Geigy Limited and Sandoz Limited)",
            "display": "Novartis Pharmaceutical Corporation (includes Ciba-Geigy Limited and Sandoz Limited)",
        }
    )
    """
    Novartis Pharmaceutical Corporation (includes Ciba-Geigy Limited and Sandoz Limited)

    Novartis Pharmaceutical Corporation (includes Ciba-Geigy Limited and Sandoz Limited)
    """

    nyb = CodeSystemConcept(
        {
            "code": "NYB",
            "definition": "New York Blood Center",
            "display": "New York Blood Center",
        }
    )
    """
    New York Blood Center

    New York Blood Center
    """

    ort = CodeSystemConcept(
        {
            "code": "ORT",
            "definition": "Ortho Diagnostic Systems, Inc.",
            "display": "Ortho Diagnostic Systems, Inc.",
        }
    )
    """
    Ortho Diagnostic Systems, Inc.

    Ortho Diagnostic Systems, Inc.
    """

    otc = CodeSystemConcept(
        {
            "code": "OTC",
            "definition": "Organon Teknika Corporation",
            "display": "Organon Teknika Corporation",
        }
    )
    """
    Organon Teknika Corporation

    Organon Teknika Corporation
    """

    pd = CodeSystemConcept(
        {
            "code": "PD",
            "definition": "Parkedale Pharmaceuticals (formerly Parke-Davis)",
            "display": "Parkedale Pharmaceuticals (formerly Parke-Davis)",
        }
    )
    """
    Parkedale Pharmaceuticals (formerly Parke-Davis)

    Parkedale Pharmaceuticals (formerly Parke-Davis)
    """

    pmc = CodeSystemConcept(
        {
            "code": "PMC",
            "definition": "Aventis Pasteur Inc. (formerly Pasteur Merieux Connaught; includes Connaught Laboratories and Pasteur Merieux)",
            "display": "Aventis Pasteur Inc. (formerly Pasteur Merieux Connaught; includes Connaught Laboratories and Pasteur Merieux)",
        }
    )
    """
    Aventis Pasteur Inc. (formerly Pasteur Merieux Connaught; includes Connaught Laboratories and Pasteur Merieux)

    Aventis Pasteur Inc. (formerly Pasteur Merieux Connaught; includes Connaught Laboratories and Pasteur Merieux)
    """

    prx = CodeSystemConcept(
        {
            "code": "PRX",
            "definition": "Praxis Biologics [Inactive-use WAL]",
            "display": "Praxis Biologics [Inactive - use WAL]",
        }
    )
    """
    Praxis Biologics [Inactive - use WAL]

    Praxis Biologics [Inactive-use WAL]
    """

    scl = CodeSystemConcept(
        {"code": "SCL", "definition": "Sclavo, Inc.", "display": "Sclavo, Inc."}
    )
    """
    Sclavo, Inc.

    Sclavo, Inc.
    """

    si = CodeSystemConcept(
        {
            "code": "SI",
            "definition": "Swiss Serum and Vaccine Inst. [Inactive-use BPC]",
            "display": "Swiss Serum and Vaccine Inst. [Inactive - use BPC]",
        }
    )
    """
    Swiss Serum and Vaccine Inst. [Inactive - use BPC]

    Swiss Serum and Vaccine Inst. [Inactive-use BPC]
    """

    skb = CodeSystemConcept(
        {
            "code": "SKB",
            "definition": "SmithKline Beecham",
            "display": "SmithKline Beecham",
        }
    )
    """
    SmithKline Beecham

    SmithKline Beecham
    """

    usa = CodeSystemConcept(
        {
            "code": "USA",
            "definition": "United States Army Medical Research and Materiel Command",
            "display": "United States Army Medical Research and Materiel Command",
        }
    )
    """
    United States Army Medical Research and Materiel Command

    United States Army Medical Research and Materiel Command
    """

    wa = CodeSystemConcept(
        {
            "code": "WA",
            "definition": "Wyeth-Ayerst [Inactive-use WAL]",
            "display": "Wyeth-Ayerst [Inactive - use WAL]",
        }
    )
    """
    Wyeth-Ayerst [Inactive - use WAL]

    Wyeth-Ayerst [Inactive-use WAL]
    """

    wal = CodeSystemConcept(
        {
            "code": "WAL",
            "definition": "Wyeth-Ayerst (includes Wyeth-Lederle Vaccines and Pediatrics, Wyeth Laboratories, Lederle Laboratories, and Praxis Biologics)",
            "display": "Wyeth-Ayerst (includes Wyeth-Lederle Vaccines and Pediatrics, Wyeth Laboratories, Lederle Laboratories, and Praxis Biologics)",
        }
    )
    """
    Wyeth-Ayerst (includes Wyeth-Lederle Vaccines and Pediatrics, Wyeth Laboratories, Lederle Laboratories, and Praxis Biologics)

    Wyeth-Ayerst (includes Wyeth-Lederle Vaccines and Pediatrics, Wyeth Laboratories, Lederle Laboratories, and Praxis Biologics)
    """

    class Meta:
        resource = _resource
