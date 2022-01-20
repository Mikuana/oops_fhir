from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SPDXLicense"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SPDXLicense:
    """
    SPDXLicense

    The license that applies to an Implementation Guide (using an SPDX
license Identifiers, or 'not-open-source'). The binding is required but
new SPDX license Identifiers are allowed to be used
(https://spdx.org/licenses/).

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/spdx-license
    """

    not_open_source = CodeSystemConcept(
        {
            "code": "not-open-source",
            "definition": "Not an open source license.",
            "display": "Not open source",
        }
    )
    """
    Not open source

    Not an open source license.
    """

    zero_bsd = CodeSystemConcept(
        {
            "code": "0BSD",
            "definition": "BSD Zero Clause License.",
            "display": "BSD Zero Clause License",
        }
    )
    """
    BSD Zero Clause License

    BSD Zero Clause License.
    """

    aal = CodeSystemConcept(
        {
            "code": "AAL",
            "definition": "Attribution Assurance License.",
            "display": "Attribution Assurance License",
        }
    )
    """
    Attribution Assurance License

    Attribution Assurance License.
    """

    abstyles = CodeSystemConcept(
        {
            "code": "Abstyles",
            "definition": "Abstyles License.",
            "display": "Abstyles License",
        }
    )
    """
    Abstyles License

    Abstyles License.
    """

    adobe_2006 = CodeSystemConcept(
        {
            "code": "Adobe-2006",
            "definition": "Adobe Systems Incorporated Source Code License Agreement.",
            "display": "Adobe Systems Incorporated Source Code License Agreement",
        }
    )
    """
    Adobe Systems Incorporated Source Code License Agreement

    Adobe Systems Incorporated Source Code License Agreement.
    """

    adobe_glyph = CodeSystemConcept(
        {
            "code": "Adobe-Glyph",
            "definition": "Adobe Glyph List License.",
            "display": "Adobe Glyph List License",
        }
    )
    """
    Adobe Glyph List License

    Adobe Glyph List License.
    """

    adsl = CodeSystemConcept(
        {
            "code": "ADSL",
            "definition": "Amazon Digital Services License.",
            "display": "Amazon Digital Services License",
        }
    )
    """
    Amazon Digital Services License

    Amazon Digital Services License.
    """

    afl_1_1 = CodeSystemConcept(
        {
            "code": "AFL-1.1",
            "definition": "Academic Free License v1.1.",
            "display": "Academic Free License v1.1",
        }
    )
    """
    Academic Free License v1.1

    Academic Free License v1.1.
    """

    afl_1_2 = CodeSystemConcept(
        {
            "code": "AFL-1.2",
            "definition": "Academic Free License v1.2.",
            "display": "Academic Free License v1.2",
        }
    )
    """
    Academic Free License v1.2

    Academic Free License v1.2.
    """

    afl_2_0 = CodeSystemConcept(
        {
            "code": "AFL-2.0",
            "definition": "Academic Free License v2.0.",
            "display": "Academic Free License v2.0",
        }
    )
    """
    Academic Free License v2.0

    Academic Free License v2.0.
    """

    afl_2_1 = CodeSystemConcept(
        {
            "code": "AFL-2.1",
            "definition": "Academic Free License v2.1.",
            "display": "Academic Free License v2.1",
        }
    )
    """
    Academic Free License v2.1

    Academic Free License v2.1.
    """

    afl_3_0 = CodeSystemConcept(
        {
            "code": "AFL-3.0",
            "definition": "Academic Free License v3.0.",
            "display": "Academic Free License v3.0",
        }
    )
    """
    Academic Free License v3.0

    Academic Free License v3.0.
    """

    afmparse = CodeSystemConcept(
        {
            "code": "Afmparse",
            "definition": "Afmparse License.",
            "display": "Afmparse License",
        }
    )
    """
    Afmparse License

    Afmparse License.
    """

    agpl_1_0_only = CodeSystemConcept(
        {
            "code": "AGPL-1.0-only",
            "definition": "Affero General Public License v1.0 only.",
            "display": "Affero General Public License v1.0 only",
        }
    )
    """
    Affero General Public License v1.0 only

    Affero General Public License v1.0 only.
    """

    agpl_1_0_or_later = CodeSystemConcept(
        {
            "code": "AGPL-1.0-or-later",
            "definition": "Affero General Public License v1.0 or later.",
            "display": "Affero General Public License v1.0 or later",
        }
    )
    """
    Affero General Public License v1.0 or later

    Affero General Public License v1.0 or later.
    """

    agpl_3_0_only = CodeSystemConcept(
        {
            "code": "AGPL-3.0-only",
            "definition": "GNU Affero General Public License v3.0 only.",
            "display": "GNU Affero General Public License v3.0 only",
        }
    )
    """
    GNU Affero General Public License v3.0 only

    GNU Affero General Public License v3.0 only.
    """

    agpl_3_0_or_later = CodeSystemConcept(
        {
            "code": "AGPL-3.0-or-later",
            "definition": "GNU Affero General Public License v3.0 or later.",
            "display": "GNU Affero General Public License v3.0 or later",
        }
    )
    """
    GNU Affero General Public License v3.0 or later

    GNU Affero General Public License v3.0 or later.
    """

    aladdin = CodeSystemConcept(
        {
            "code": "Aladdin",
            "definition": "Aladdin Free Public License.",
            "display": "Aladdin Free Public License",
        }
    )
    """
    Aladdin Free Public License

    Aladdin Free Public License.
    """

    amdplpa = CodeSystemConcept(
        {
            "code": "AMDPLPA",
            "definition": "AMD's plpa_map.c License.",
            "display": "AMD's plpa_map.c License",
        }
    )
    """
    AMD's plpa_map.c License

    AMD's plpa_map.c License.
    """

    aml = CodeSystemConcept(
        {
            "code": "AML",
            "definition": "Apple MIT License.",
            "display": "Apple MIT License",
        }
    )
    """
    Apple MIT License

    Apple MIT License.
    """

    ampas = CodeSystemConcept(
        {
            "code": "AMPAS",
            "definition": "Academy of Motion Picture Arts and Sciences BSD.",
            "display": "Academy of Motion Picture Arts and Sciences BSD",
        }
    )
    """
    Academy of Motion Picture Arts and Sciences BSD

    Academy of Motion Picture Arts and Sciences BSD.
    """

    antlr_pd = CodeSystemConcept(
        {
            "code": "ANTLR-PD",
            "definition": "ANTLR Software Rights Notice.",
            "display": "ANTLR Software Rights Notice",
        }
    )
    """
    ANTLR Software Rights Notice

    ANTLR Software Rights Notice.
    """

    apache_1_0 = CodeSystemConcept(
        {
            "code": "Apache-1.0",
            "definition": "Apache License 1.0.",
            "display": "Apache License 1.0",
        }
    )
    """
    Apache License 1.0

    Apache License 1.0.
    """

    apache_1_1 = CodeSystemConcept(
        {
            "code": "Apache-1.1",
            "definition": "Apache License 1.1.",
            "display": "Apache License 1.1",
        }
    )
    """
    Apache License 1.1

    Apache License 1.1.
    """

    apache_2_0 = CodeSystemConcept(
        {
            "code": "Apache-2.0",
            "definition": "Apache License 2.0.",
            "display": "Apache License 2.0",
        }
    )
    """
    Apache License 2.0

    Apache License 2.0.
    """

    apafml = CodeSystemConcept(
        {
            "code": "APAFML",
            "definition": "Adobe Postscript AFM License.",
            "display": "Adobe Postscript AFM License",
        }
    )
    """
    Adobe Postscript AFM License

    Adobe Postscript AFM License.
    """

    apl_1_0 = CodeSystemConcept(
        {
            "code": "APL-1.0",
            "definition": "Adaptive Public License 1.0.",
            "display": "Adaptive Public License 1.0",
        }
    )
    """
    Adaptive Public License 1.0

    Adaptive Public License 1.0.
    """

    apsl_1_0 = CodeSystemConcept(
        {
            "code": "APSL-1.0",
            "definition": "Apple Public Source License 1.0.",
            "display": "Apple Public Source License 1.0",
        }
    )
    """
    Apple Public Source License 1.0

    Apple Public Source License 1.0.
    """

    apsl_1_1 = CodeSystemConcept(
        {
            "code": "APSL-1.1",
            "definition": "Apple Public Source License 1.1.",
            "display": "Apple Public Source License 1.1",
        }
    )
    """
    Apple Public Source License 1.1

    Apple Public Source License 1.1.
    """

    apsl_1_2 = CodeSystemConcept(
        {
            "code": "APSL-1.2",
            "definition": "Apple Public Source License 1.2.",
            "display": "Apple Public Source License 1.2",
        }
    )
    """
    Apple Public Source License 1.2

    Apple Public Source License 1.2.
    """

    apsl_2_0 = CodeSystemConcept(
        {
            "code": "APSL-2.0",
            "definition": "Apple Public Source License 2.0.",
            "display": "Apple Public Source License 2.0",
        }
    )
    """
    Apple Public Source License 2.0

    Apple Public Source License 2.0.
    """

    artistic_1_0_cl8 = CodeSystemConcept(
        {
            "code": "Artistic-1.0-cl8",
            "definition": "Artistic License 1.0 w/clause 8.",
            "display": "Artistic License 1.0 w/clause 8",
        }
    )
    """
    Artistic License 1.0 w/clause 8

    Artistic License 1.0 w/clause 8.
    """

    artistic_1_0_perl = CodeSystemConcept(
        {
            "code": "Artistic-1.0-Perl",
            "definition": "Artistic License 1.0 (Perl).",
            "display": "Artistic License 1.0 (Perl)",
        }
    )
    """
    Artistic License 1.0 (Perl)

    Artistic License 1.0 (Perl).
    """

    artistic_1_0 = CodeSystemConcept(
        {
            "code": "Artistic-1.0",
            "definition": "Artistic License 1.0.",
            "display": "Artistic License 1.0",
        }
    )
    """
    Artistic License 1.0

    Artistic License 1.0.
    """

    artistic_2_0 = CodeSystemConcept(
        {
            "code": "Artistic-2.0",
            "definition": "Artistic License 2.0.",
            "display": "Artistic License 2.0",
        }
    )
    """
    Artistic License 2.0

    Artistic License 2.0.
    """

    bahyph = CodeSystemConcept(
        {"code": "Bahyph", "definition": "Bahyph License.", "display": "Bahyph License"}
    )
    """
    Bahyph License

    Bahyph License.
    """

    barr = CodeSystemConcept(
        {"code": "Barr", "definition": "Barr License.", "display": "Barr License"}
    )
    """
    Barr License

    Barr License.
    """

    beerware = CodeSystemConcept(
        {
            "code": "Beerware",
            "definition": "Beerware License.",
            "display": "Beerware License",
        }
    )
    """
    Beerware License

    Beerware License.
    """

    bit_torrent_1_0 = CodeSystemConcept(
        {
            "code": "BitTorrent-1.0",
            "definition": "BitTorrent Open Source License v1.0.",
            "display": "BitTorrent Open Source License v1.0",
        }
    )
    """
    BitTorrent Open Source License v1.0

    BitTorrent Open Source License v1.0.
    """

    bit_torrent_1_1 = CodeSystemConcept(
        {
            "code": "BitTorrent-1.1",
            "definition": "BitTorrent Open Source License v1.1.",
            "display": "BitTorrent Open Source License v1.1",
        }
    )
    """
    BitTorrent Open Source License v1.1

    BitTorrent Open Source License v1.1.
    """

    borceux = CodeSystemConcept(
        {
            "code": "Borceux",
            "definition": "Borceux license.",
            "display": "Borceux license",
        }
    )
    """
    Borceux license

    Borceux license.
    """

    bsd_1_clause = CodeSystemConcept(
        {
            "code": "BSD-1-Clause",
            "definition": "BSD 1-Clause License.",
            "display": "BSD 1-Clause License",
        }
    )
    """
    BSD 1-Clause License

    BSD 1-Clause License.
    """

    bsd_2_clause_free_bsd = CodeSystemConcept(
        {
            "code": "BSD-2-Clause-FreeBSD",
            "definition": "BSD 2-Clause FreeBSD License.",
            "display": "BSD 2-Clause FreeBSD License",
        }
    )
    """
    BSD 2-Clause FreeBSD License

    BSD 2-Clause FreeBSD License.
    """

    bsd_2_clause_net_bsd = CodeSystemConcept(
        {
            "code": "BSD-2-Clause-NetBSD",
            "definition": "BSD 2-Clause NetBSD License.",
            "display": "BSD 2-Clause NetBSD License",
        }
    )
    """
    BSD 2-Clause NetBSD License

    BSD 2-Clause NetBSD License.
    """

    bsd_2_clause_patent = CodeSystemConcept(
        {
            "code": "BSD-2-Clause-Patent",
            "definition": "BSD-2-Clause Plus Patent License.",
            "display": "BSD-2-Clause Plus Patent License",
        }
    )
    """
    BSD-2-Clause Plus Patent License

    BSD-2-Clause Plus Patent License.
    """

    bsd_2_clause = CodeSystemConcept(
        {
            "code": "BSD-2-Clause",
            "definition": 'BSD 2-Clause "Simplified" License.',
            "display": 'BSD 2-Clause "Simplified" License',
        }
    )
    """
    BSD 2-Clause "Simplified" License

    BSD 2-Clause "Simplified" License.
    """

    bsd_3_clause_attribution = CodeSystemConcept(
        {
            "code": "BSD-3-Clause-Attribution",
            "definition": "BSD with attribution.",
            "display": "BSD with attribution",
        }
    )
    """
    BSD with attribution

    BSD with attribution.
    """

    bsd_3_clause_clear = CodeSystemConcept(
        {
            "code": "BSD-3-Clause-Clear",
            "definition": "BSD 3-Clause Clear License.",
            "display": "BSD 3-Clause Clear License",
        }
    )
    """
    BSD 3-Clause Clear License

    BSD 3-Clause Clear License.
    """

    bsd_3_clause_lbnl = CodeSystemConcept(
        {
            "code": "BSD-3-Clause-LBNL",
            "definition": "Lawrence Berkeley National Labs BSD variant license.",
            "display": "Lawrence Berkeley National Labs BSD variant license",
        }
    )
    """
    Lawrence Berkeley National Labs BSD variant license

    Lawrence Berkeley National Labs BSD variant license.
    """

    bsd_3_clause_no_nuclear_license_2014 = CodeSystemConcept(
        {
            "code": "BSD-3-Clause-No-Nuclear-License-2014",
            "definition": "BSD 3-Clause No Nuclear License 2014.",
            "display": "BSD 3-Clause No Nuclear License 2014",
        }
    )
    """
    BSD 3-Clause No Nuclear License 2014

    BSD 3-Clause No Nuclear License 2014.
    """

    bsd_3_clause_no_nuclear_license = CodeSystemConcept(
        {
            "code": "BSD-3-Clause-No-Nuclear-License",
            "definition": "BSD 3-Clause No Nuclear License.",
            "display": "BSD 3-Clause No Nuclear License",
        }
    )
    """
    BSD 3-Clause No Nuclear License

    BSD 3-Clause No Nuclear License.
    """

    bsd_3_clause_no_nuclear_warranty = CodeSystemConcept(
        {
            "code": "BSD-3-Clause-No-Nuclear-Warranty",
            "definition": "BSD 3-Clause No Nuclear Warranty.",
            "display": "BSD 3-Clause No Nuclear Warranty",
        }
    )
    """
    BSD 3-Clause No Nuclear Warranty

    BSD 3-Clause No Nuclear Warranty.
    """

    bsd_3_clause = CodeSystemConcept(
        {
            "code": "BSD-3-Clause",
            "definition": 'BSD 3-Clause "New" or "Revised" License.',
            "display": 'BSD 3-Clause "New" or "Revised" License',
        }
    )
    """
    BSD 3-Clause "New" or "Revised" License

    BSD 3-Clause "New" or "Revised" License.
    """

    bsd_4_clause_uc = CodeSystemConcept(
        {
            "code": "BSD-4-Clause-UC",
            "definition": "BSD-4-Clause (University of California-Specific).",
            "display": "BSD-4-Clause (University of California-Specific)",
        }
    )
    """
    BSD-4-Clause (University of California-Specific)

    BSD-4-Clause (University of California-Specific).
    """

    bsd_4_clause = CodeSystemConcept(
        {
            "code": "BSD-4-Clause",
            "definition": 'BSD 4-Clause "Original" or "Old" License.',
            "display": 'BSD 4-Clause "Original" or "Old" License',
        }
    )
    """
    BSD 4-Clause "Original" or "Old" License

    BSD 4-Clause "Original" or "Old" License.
    """

    bsd_protection = CodeSystemConcept(
        {
            "code": "BSD-Protection",
            "definition": "BSD Protection License.",
            "display": "BSD Protection License",
        }
    )
    """
    BSD Protection License

    BSD Protection License.
    """

    bsd_source_code = CodeSystemConcept(
        {
            "code": "BSD-Source-Code",
            "definition": "BSD Source Code Attribution.",
            "display": "BSD Source Code Attribution",
        }
    )
    """
    BSD Source Code Attribution

    BSD Source Code Attribution.
    """

    bsl_1_0 = CodeSystemConcept(
        {
            "code": "BSL-1.0",
            "definition": "Boost Software License 1.0.",
            "display": "Boost Software License 1.0",
        }
    )
    """
    Boost Software License 1.0

    Boost Software License 1.0.
    """

    bzip2_1_0_5 = CodeSystemConcept(
        {
            "code": "bzip2-1.0.5",
            "definition": "bzip2 and libbzip2 License v1.0.5.",
            "display": "bzip2 and libbzip2 License v1.0.5",
        }
    )
    """
    bzip2 and libbzip2 License v1.0.5

    bzip2 and libbzip2 License v1.0.5.
    """

    bzip2_1_0_6 = CodeSystemConcept(
        {
            "code": "bzip2-1.0.6",
            "definition": "bzip2 and libbzip2 License v1.0.6.",
            "display": "bzip2 and libbzip2 License v1.0.6",
        }
    )
    """
    bzip2 and libbzip2 License v1.0.6

    bzip2 and libbzip2 License v1.0.6.
    """

    caldera = CodeSystemConcept(
        {
            "code": "Caldera",
            "definition": "Caldera License.",
            "display": "Caldera License",
        }
    )
    """
    Caldera License

    Caldera License.
    """

    catosl_1_1 = CodeSystemConcept(
        {
            "code": "CATOSL-1.1",
            "definition": "Computer Associates Trusted Open Source License 1.1.",
            "display": "Computer Associates Trusted Open Source License 1.1",
        }
    )
    """
    Computer Associates Trusted Open Source License 1.1

    Computer Associates Trusted Open Source License 1.1.
    """

    cc_by_1_0 = CodeSystemConcept(
        {
            "code": "CC-BY-1.0",
            "definition": "Creative Commons Attribution 1.0 Generic.",
            "display": "Creative Commons Attribution 1.0 Generic",
        }
    )
    """
    Creative Commons Attribution 1.0 Generic

    Creative Commons Attribution 1.0 Generic.
    """

    cc_by_2_0 = CodeSystemConcept(
        {
            "code": "CC-BY-2.0",
            "definition": "Creative Commons Attribution 2.0 Generic.",
            "display": "Creative Commons Attribution 2.0 Generic",
        }
    )
    """
    Creative Commons Attribution 2.0 Generic

    Creative Commons Attribution 2.0 Generic.
    """

    cc_by_2_5 = CodeSystemConcept(
        {
            "code": "CC-BY-2.5",
            "definition": "Creative Commons Attribution 2.5 Generic.",
            "display": "Creative Commons Attribution 2.5 Generic",
        }
    )
    """
    Creative Commons Attribution 2.5 Generic

    Creative Commons Attribution 2.5 Generic.
    """

    cc_by_3_0 = CodeSystemConcept(
        {
            "code": "CC-BY-3.0",
            "definition": "Creative Commons Attribution 3.0 Unported.",
            "display": "Creative Commons Attribution 3.0 Unported",
        }
    )
    """
    Creative Commons Attribution 3.0 Unported

    Creative Commons Attribution 3.0 Unported.
    """

    cc_by_4_0 = CodeSystemConcept(
        {
            "code": "CC-BY-4.0",
            "definition": "Creative Commons Attribution 4.0 International.",
            "display": "Creative Commons Attribution 4.0 International",
        }
    )
    """
    Creative Commons Attribution 4.0 International

    Creative Commons Attribution 4.0 International.
    """

    cc_by_nc_1_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-1.0",
            "definition": "Creative Commons Attribution Non Commercial 1.0 Generic.",
            "display": "Creative Commons Attribution Non Commercial 1.0 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial 1.0 Generic

    Creative Commons Attribution Non Commercial 1.0 Generic.
    """

    cc_by_nc_2_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-2.0",
            "definition": "Creative Commons Attribution Non Commercial 2.0 Generic.",
            "display": "Creative Commons Attribution Non Commercial 2.0 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial 2.0 Generic

    Creative Commons Attribution Non Commercial 2.0 Generic.
    """

    cc_by_nc_2_5 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-2.5",
            "definition": "Creative Commons Attribution Non Commercial 2.5 Generic.",
            "display": "Creative Commons Attribution Non Commercial 2.5 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial 2.5 Generic

    Creative Commons Attribution Non Commercial 2.5 Generic.
    """

    cc_by_nc_3_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-3.0",
            "definition": "Creative Commons Attribution Non Commercial 3.0 Unported.",
            "display": "Creative Commons Attribution Non Commercial 3.0 Unported",
        }
    )
    """
    Creative Commons Attribution Non Commercial 3.0 Unported

    Creative Commons Attribution Non Commercial 3.0 Unported.
    """

    cc_by_nc_4_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-4.0",
            "definition": "Creative Commons Attribution Non Commercial 4.0 International.",
            "display": "Creative Commons Attribution Non Commercial 4.0 International",
        }
    )
    """
    Creative Commons Attribution Non Commercial 4.0 International

    Creative Commons Attribution Non Commercial 4.0 International.
    """

    cc_by_nc_nd_1_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-ND-1.0",
            "definition": "Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic.",
            "display": "Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic

    Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic.
    """

    cc_by_nc_nd_2_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-ND-2.0",
            "definition": "Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic.",
            "display": "Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic

    Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic.
    """

    cc_by_nc_nd_2_5 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-ND-2.5",
            "definition": "Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic.",
            "display": "Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic

    Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic.
    """

    cc_by_nc_nd_3_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-ND-3.0",
            "definition": "Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported.",
            "display": "Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported",
        }
    )
    """
    Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported

    Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported.
    """

    cc_by_nc_nd_4_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-ND-4.0",
            "definition": "Creative Commons Attribution Non Commercial No Derivatives 4.0 International.",
            "display": "Creative Commons Attribution Non Commercial No Derivatives 4.0 International",
        }
    )
    """
    Creative Commons Attribution Non Commercial No Derivatives 4.0 International

    Creative Commons Attribution Non Commercial No Derivatives 4.0 International.
    """

    cc_by_nc_sa_1_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-SA-1.0",
            "definition": "Creative Commons Attribution Non Commercial Share Alike 1.0 Generic.",
            "display": "Creative Commons Attribution Non Commercial Share Alike 1.0 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial Share Alike 1.0 Generic

    Creative Commons Attribution Non Commercial Share Alike 1.0 Generic.
    """

    cc_by_nc_sa_2_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-SA-2.0",
            "definition": "Creative Commons Attribution Non Commercial Share Alike 2.0 Generic.",
            "display": "Creative Commons Attribution Non Commercial Share Alike 2.0 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial Share Alike 2.0 Generic

    Creative Commons Attribution Non Commercial Share Alike 2.0 Generic.
    """

    cc_by_nc_sa_2_5 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-SA-2.5",
            "definition": "Creative Commons Attribution Non Commercial Share Alike 2.5 Generic.",
            "display": "Creative Commons Attribution Non Commercial Share Alike 2.5 Generic",
        }
    )
    """
    Creative Commons Attribution Non Commercial Share Alike 2.5 Generic

    Creative Commons Attribution Non Commercial Share Alike 2.5 Generic.
    """

    cc_by_nc_sa_3_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-SA-3.0",
            "definition": "Creative Commons Attribution Non Commercial Share Alike 3.0 Unported.",
            "display": "Creative Commons Attribution Non Commercial Share Alike 3.0 Unported",
        }
    )
    """
    Creative Commons Attribution Non Commercial Share Alike 3.0 Unported

    Creative Commons Attribution Non Commercial Share Alike 3.0 Unported.
    """

    cc_by_nc_sa_4_0 = CodeSystemConcept(
        {
            "code": "CC-BY-NC-SA-4.0",
            "definition": "Creative Commons Attribution Non Commercial Share Alike 4.0 International.",
            "display": "Creative Commons Attribution Non Commercial Share Alike 4.0 International",
        }
    )
    """
    Creative Commons Attribution Non Commercial Share Alike 4.0 International

    Creative Commons Attribution Non Commercial Share Alike 4.0 International.
    """

    cc_by_nd_1_0 = CodeSystemConcept(
        {
            "code": "CC-BY-ND-1.0",
            "definition": "Creative Commons Attribution No Derivatives 1.0 Generic.",
            "display": "Creative Commons Attribution No Derivatives 1.0 Generic",
        }
    )
    """
    Creative Commons Attribution No Derivatives 1.0 Generic

    Creative Commons Attribution No Derivatives 1.0 Generic.
    """

    cc_by_nd_2_0 = CodeSystemConcept(
        {
            "code": "CC-BY-ND-2.0",
            "definition": "Creative Commons Attribution No Derivatives 2.0 Generic.",
            "display": "Creative Commons Attribution No Derivatives 2.0 Generic",
        }
    )
    """
    Creative Commons Attribution No Derivatives 2.0 Generic

    Creative Commons Attribution No Derivatives 2.0 Generic.
    """

    cc_by_nd_2_5 = CodeSystemConcept(
        {
            "code": "CC-BY-ND-2.5",
            "definition": "Creative Commons Attribution No Derivatives 2.5 Generic.",
            "display": "Creative Commons Attribution No Derivatives 2.5 Generic",
        }
    )
    """
    Creative Commons Attribution No Derivatives 2.5 Generic

    Creative Commons Attribution No Derivatives 2.5 Generic.
    """

    cc_by_nd_3_0 = CodeSystemConcept(
        {
            "code": "CC-BY-ND-3.0",
            "definition": "Creative Commons Attribution No Derivatives 3.0 Unported.",
            "display": "Creative Commons Attribution No Derivatives 3.0 Unported",
        }
    )
    """
    Creative Commons Attribution No Derivatives 3.0 Unported

    Creative Commons Attribution No Derivatives 3.0 Unported.
    """

    cc_by_nd_4_0 = CodeSystemConcept(
        {
            "code": "CC-BY-ND-4.0",
            "definition": "Creative Commons Attribution No Derivatives 4.0 International.",
            "display": "Creative Commons Attribution No Derivatives 4.0 International",
        }
    )
    """
    Creative Commons Attribution No Derivatives 4.0 International

    Creative Commons Attribution No Derivatives 4.0 International.
    """

    cc_by_sa_1_0 = CodeSystemConcept(
        {
            "code": "CC-BY-SA-1.0",
            "definition": "Creative Commons Attribution Share Alike 1.0 Generic.",
            "display": "Creative Commons Attribution Share Alike 1.0 Generic",
        }
    )
    """
    Creative Commons Attribution Share Alike 1.0 Generic

    Creative Commons Attribution Share Alike 1.0 Generic.
    """

    cc_by_sa_2_0 = CodeSystemConcept(
        {
            "code": "CC-BY-SA-2.0",
            "definition": "Creative Commons Attribution Share Alike 2.0 Generic.",
            "display": "Creative Commons Attribution Share Alike 2.0 Generic",
        }
    )
    """
    Creative Commons Attribution Share Alike 2.0 Generic

    Creative Commons Attribution Share Alike 2.0 Generic.
    """

    cc_by_sa_2_5 = CodeSystemConcept(
        {
            "code": "CC-BY-SA-2.5",
            "definition": "Creative Commons Attribution Share Alike 2.5 Generic.",
            "display": "Creative Commons Attribution Share Alike 2.5 Generic",
        }
    )
    """
    Creative Commons Attribution Share Alike 2.5 Generic

    Creative Commons Attribution Share Alike 2.5 Generic.
    """

    cc_by_sa_3_0 = CodeSystemConcept(
        {
            "code": "CC-BY-SA-3.0",
            "definition": "Creative Commons Attribution Share Alike 3.0 Unported.",
            "display": "Creative Commons Attribution Share Alike 3.0 Unported",
        }
    )
    """
    Creative Commons Attribution Share Alike 3.0 Unported

    Creative Commons Attribution Share Alike 3.0 Unported.
    """

    cc_by_sa_4_0 = CodeSystemConcept(
        {
            "code": "CC-BY-SA-4.0",
            "definition": "Creative Commons Attribution Share Alike 4.0 International.",
            "display": "Creative Commons Attribution Share Alike 4.0 International",
        }
    )
    """
    Creative Commons Attribution Share Alike 4.0 International

    Creative Commons Attribution Share Alike 4.0 International.
    """

    cc0_1_0 = CodeSystemConcept(
        {
            "code": "CC0-1.0",
            "definition": "Creative Commons Zero v1.0 Universal.",
            "display": "Creative Commons Zero v1.0 Universal",
        }
    )
    """
    Creative Commons Zero v1.0 Universal

    Creative Commons Zero v1.0 Universal.
    """

    cddl_1_0 = CodeSystemConcept(
        {
            "code": "CDDL-1.0",
            "definition": "Common Development and Distribution License 1.0.",
            "display": "Common Development and Distribution License 1.0",
        }
    )
    """
    Common Development and Distribution License 1.0

    Common Development and Distribution License 1.0.
    """

    cddl_1_1 = CodeSystemConcept(
        {
            "code": "CDDL-1.1",
            "definition": "Common Development and Distribution License 1.1.",
            "display": "Common Development and Distribution License 1.1",
        }
    )
    """
    Common Development and Distribution License 1.1

    Common Development and Distribution License 1.1.
    """

    cdla_permissive_1_0 = CodeSystemConcept(
        {
            "code": "CDLA-Permissive-1.0",
            "definition": "Community Data License Agreement Permissive 1.0.",
            "display": "Community Data License Agreement Permissive 1.0",
        }
    )
    """
    Community Data License Agreement Permissive 1.0

    Community Data License Agreement Permissive 1.0.
    """

    cdla_sharing_1_0 = CodeSystemConcept(
        {
            "code": "CDLA-Sharing-1.0",
            "definition": "Community Data License Agreement Sharing 1.0.",
            "display": "Community Data License Agreement Sharing 1.0",
        }
    )
    """
    Community Data License Agreement Sharing 1.0

    Community Data License Agreement Sharing 1.0.
    """

    cecill_1_0 = CodeSystemConcept(
        {
            "code": "CECILL-1.0",
            "definition": "CeCILL Free Software License Agreement v1.0.",
            "display": "CeCILL Free Software License Agreement v1.0",
        }
    )
    """
    CeCILL Free Software License Agreement v1.0

    CeCILL Free Software License Agreement v1.0.
    """

    cecill_1_1 = CodeSystemConcept(
        {
            "code": "CECILL-1.1",
            "definition": "CeCILL Free Software License Agreement v1.1.",
            "display": "CeCILL Free Software License Agreement v1.1",
        }
    )
    """
    CeCILL Free Software License Agreement v1.1

    CeCILL Free Software License Agreement v1.1.
    """

    cecill_2_0 = CodeSystemConcept(
        {
            "code": "CECILL-2.0",
            "definition": "CeCILL Free Software License Agreement v2.0.",
            "display": "CeCILL Free Software License Agreement v2.0",
        }
    )
    """
    CeCILL Free Software License Agreement v2.0

    CeCILL Free Software License Agreement v2.0.
    """

    cecill_2_1 = CodeSystemConcept(
        {
            "code": "CECILL-2.1",
            "definition": "CeCILL Free Software License Agreement v2.1.",
            "display": "CeCILL Free Software License Agreement v2.1",
        }
    )
    """
    CeCILL Free Software License Agreement v2.1

    CeCILL Free Software License Agreement v2.1.
    """

    cecill_b = CodeSystemConcept(
        {
            "code": "CECILL-B",
            "definition": "CeCILL-B Free Software License Agreement.",
            "display": "CeCILL-B Free Software License Agreement",
        }
    )
    """
    CeCILL-B Free Software License Agreement

    CeCILL-B Free Software License Agreement.
    """

    cecill_c = CodeSystemConcept(
        {
            "code": "CECILL-C",
            "definition": "CeCILL-C Free Software License Agreement.",
            "display": "CeCILL-C Free Software License Agreement",
        }
    )
    """
    CeCILL-C Free Software License Agreement

    CeCILL-C Free Software License Agreement.
    """

    cl_artistic = CodeSystemConcept(
        {
            "code": "ClArtistic",
            "definition": "Clarified Artistic License.",
            "display": "Clarified Artistic License",
        }
    )
    """
    Clarified Artistic License

    Clarified Artistic License.
    """

    cnri_jython = CodeSystemConcept(
        {
            "code": "CNRI-Jython",
            "definition": "CNRI Jython License.",
            "display": "CNRI Jython License",
        }
    )
    """
    CNRI Jython License

    CNRI Jython License.
    """

    cnri_python_gpl_compatible = CodeSystemConcept(
        {
            "code": "CNRI-Python-GPL-Compatible",
            "definition": "CNRI Python Open Source GPL Compatible License Agreement.",
            "display": "CNRI Python Open Source GPL Compatible License Agreement",
        }
    )
    """
    CNRI Python Open Source GPL Compatible License Agreement

    CNRI Python Open Source GPL Compatible License Agreement.
    """

    cnri_python = CodeSystemConcept(
        {
            "code": "CNRI-Python",
            "definition": "CNRI Python License.",
            "display": "CNRI Python License",
        }
    )
    """
    CNRI Python License

    CNRI Python License.
    """

    condor_1_1 = CodeSystemConcept(
        {
            "code": "Condor-1.1",
            "definition": "Condor Public License v1.1.",
            "display": "Condor Public License v1.1",
        }
    )
    """
    Condor Public License v1.1

    Condor Public License v1.1.
    """

    cpal_1_0 = CodeSystemConcept(
        {
            "code": "CPAL-1.0",
            "definition": "Common Public Attribution License 1.0.",
            "display": "Common Public Attribution License 1.0",
        }
    )
    """
    Common Public Attribution License 1.0

    Common Public Attribution License 1.0.
    """

    cpl_1_0 = CodeSystemConcept(
        {
            "code": "CPL-1.0",
            "definition": "Common Public License 1.0.",
            "display": "Common Public License 1.0",
        }
    )
    """
    Common Public License 1.0

    Common Public License 1.0.
    """

    cpol_1_02 = CodeSystemConcept(
        {
            "code": "CPOL-1.02",
            "definition": "Code Project Open License 1.02.",
            "display": "Code Project Open License 1.02",
        }
    )
    """
    Code Project Open License 1.02

    Code Project Open License 1.02.
    """

    crossword = CodeSystemConcept(
        {
            "code": "Crossword",
            "definition": "Crossword License.",
            "display": "Crossword License",
        }
    )
    """
    Crossword License

    Crossword License.
    """

    crystal_stacker = CodeSystemConcept(
        {
            "code": "CrystalStacker",
            "definition": "CrystalStacker License.",
            "display": "CrystalStacker License",
        }
    )
    """
    CrystalStacker License

    CrystalStacker License.
    """

    cua_opl_1_0 = CodeSystemConcept(
        {
            "code": "CUA-OPL-1.0",
            "definition": "CUA Office Public License v1.0.",
            "display": "CUA Office Public License v1.0",
        }
    )
    """
    CUA Office Public License v1.0

    CUA Office Public License v1.0.
    """

    cube = CodeSystemConcept(
        {"code": "Cube", "definition": "Cube License.", "display": "Cube License"}
    )
    """
    Cube License

    Cube License.
    """

    curl = CodeSystemConcept(
        {"code": "curl", "definition": "curl License.", "display": "curl License"}
    )
    """
    curl License

    curl License.
    """

    d_fsl_1_0 = CodeSystemConcept(
        {
            "code": "D-FSL-1.0",
            "definition": "Deutsche Freie Software Lizenz.",
            "display": "Deutsche Freie Software Lizenz",
        }
    )
    """
    Deutsche Freie Software Lizenz

    Deutsche Freie Software Lizenz.
    """

    diffmark = CodeSystemConcept(
        {
            "code": "diffmark",
            "definition": "diffmark license.",
            "display": "diffmark license",
        }
    )
    """
    diffmark license

    diffmark license.
    """

    doc = CodeSystemConcept(
        {"code": "DOC", "definition": "DOC License.", "display": "DOC License"}
    )
    """
    DOC License

    DOC License.
    """

    dotseqn = CodeSystemConcept(
        {
            "code": "Dotseqn",
            "definition": "Dotseqn License.",
            "display": "Dotseqn License",
        }
    )
    """
    Dotseqn License

    Dotseqn License.
    """

    dsdp = CodeSystemConcept(
        {"code": "DSDP", "definition": "DSDP License.", "display": "DSDP License"}
    )
    """
    DSDP License

    DSDP License.
    """

    dvipdfm = CodeSystemConcept(
        {
            "code": "dvipdfm",
            "definition": "dvipdfm License.",
            "display": "dvipdfm License",
        }
    )
    """
    dvipdfm License

    dvipdfm License.
    """

    ecl_1_0 = CodeSystemConcept(
        {
            "code": "ECL-1.0",
            "definition": "Educational Community License v1.0.",
            "display": "Educational Community License v1.0",
        }
    )
    """
    Educational Community License v1.0

    Educational Community License v1.0.
    """

    ecl_2_0 = CodeSystemConcept(
        {
            "code": "ECL-2.0",
            "definition": "Educational Community License v2.0.",
            "display": "Educational Community License v2.0",
        }
    )
    """
    Educational Community License v2.0

    Educational Community License v2.0.
    """

    efl_1_0 = CodeSystemConcept(
        {
            "code": "EFL-1.0",
            "definition": "Eiffel Forum License v1.0.",
            "display": "Eiffel Forum License v1.0",
        }
    )
    """
    Eiffel Forum License v1.0

    Eiffel Forum License v1.0.
    """

    efl_2_0 = CodeSystemConcept(
        {
            "code": "EFL-2.0",
            "definition": "Eiffel Forum License v2.0.",
            "display": "Eiffel Forum License v2.0",
        }
    )
    """
    Eiffel Forum License v2.0

    Eiffel Forum License v2.0.
    """

    e_genix = CodeSystemConcept(
        {
            "code": "eGenix",
            "definition": "eGenix.com Public License 1.1.0.",
            "display": "eGenix.com Public License 1.1.0",
        }
    )
    """
    eGenix.com Public License 1.1.0

    eGenix.com Public License 1.1.0.
    """

    entessa = CodeSystemConcept(
        {
            "code": "Entessa",
            "definition": "Entessa Public License v1.0.",
            "display": "Entessa Public License v1.0",
        }
    )
    """
    Entessa Public License v1.0

    Entessa Public License v1.0.
    """

    epl_1_0 = CodeSystemConcept(
        {
            "code": "EPL-1.0",
            "definition": "Eclipse Public License 1.0.",
            "display": "Eclipse Public License 1.0",
        }
    )
    """
    Eclipse Public License 1.0

    Eclipse Public License 1.0.
    """

    epl_2_0 = CodeSystemConcept(
        {
            "code": "EPL-2.0",
            "definition": "Eclipse Public License 2.0.",
            "display": "Eclipse Public License 2.0",
        }
    )
    """
    Eclipse Public License 2.0

    Eclipse Public License 2.0.
    """

    erl_pl_1_1 = CodeSystemConcept(
        {
            "code": "ErlPL-1.1",
            "definition": "Erlang Public License v1.1.",
            "display": "Erlang Public License v1.1",
        }
    )
    """
    Erlang Public License v1.1

    Erlang Public License v1.1.
    """

    eudatagrid = CodeSystemConcept(
        {
            "code": "EUDatagrid",
            "definition": "EU DataGrid Software License.",
            "display": "EU DataGrid Software License",
        }
    )
    """
    EU DataGrid Software License

    EU DataGrid Software License.
    """

    eupl_1_0 = CodeSystemConcept(
        {
            "code": "EUPL-1.0",
            "definition": "European Union Public License 1.0.",
            "display": "European Union Public License 1.0",
        }
    )
    """
    European Union Public License 1.0

    European Union Public License 1.0.
    """

    eupl_1_1 = CodeSystemConcept(
        {
            "code": "EUPL-1.1",
            "definition": "European Union Public License 1.1.",
            "display": "European Union Public License 1.1",
        }
    )
    """
    European Union Public License 1.1

    European Union Public License 1.1.
    """

    eupl_1_2 = CodeSystemConcept(
        {
            "code": "EUPL-1.2",
            "definition": "European Union Public License 1.2.",
            "display": "European Union Public License 1.2",
        }
    )
    """
    European Union Public License 1.2

    European Union Public License 1.2.
    """

    eurosym = CodeSystemConcept(
        {
            "code": "Eurosym",
            "definition": "Eurosym License.",
            "display": "Eurosym License",
        }
    )
    """
    Eurosym License

    Eurosym License.
    """

    fair = CodeSystemConcept(
        {"code": "Fair", "definition": "Fair License.", "display": "Fair License"}
    )
    """
    Fair License

    Fair License.
    """

    frameworx_1_0 = CodeSystemConcept(
        {
            "code": "Frameworx-1.0",
            "definition": "Frameworx Open License 1.0.",
            "display": "Frameworx Open License 1.0",
        }
    )
    """
    Frameworx Open License 1.0

    Frameworx Open License 1.0.
    """

    free_image = CodeSystemConcept(
        {
            "code": "FreeImage",
            "definition": "FreeImage Public License v1.0.",
            "display": "FreeImage Public License v1.0",
        }
    )
    """
    FreeImage Public License v1.0

    FreeImage Public License v1.0.
    """

    fsfap = CodeSystemConcept(
        {
            "code": "FSFAP",
            "definition": "FSF All Permissive License.",
            "display": "FSF All Permissive License",
        }
    )
    """
    FSF All Permissive License

    FSF All Permissive License.
    """

    fsful = CodeSystemConcept(
        {
            "code": "FSFUL",
            "definition": "FSF Unlimited License.",
            "display": "FSF Unlimited License",
        }
    )
    """
    FSF Unlimited License

    FSF Unlimited License.
    """

    fsfullr = CodeSystemConcept(
        {
            "code": "FSFULLR",
            "definition": "FSF Unlimited License (with License Retention).",
            "display": "FSF Unlimited License (with License Retention)",
        }
    )
    """
    FSF Unlimited License (with License Retention)

    FSF Unlimited License (with License Retention).
    """

    ftl = CodeSystemConcept(
        {
            "code": "FTL",
            "definition": "Freetype Project License.",
            "display": "Freetype Project License",
        }
    )
    """
    Freetype Project License

    Freetype Project License.
    """

    gfdl_1_1_only = CodeSystemConcept(
        {
            "code": "GFDL-1.1-only",
            "definition": "GNU Free Documentation License v1.1 only.",
            "display": "GNU Free Documentation License v1.1 only",
        }
    )
    """
    GNU Free Documentation License v1.1 only

    GNU Free Documentation License v1.1 only.
    """

    gfdl_1_1_or_later = CodeSystemConcept(
        {
            "code": "GFDL-1.1-or-later",
            "definition": "GNU Free Documentation License v1.1 or later.",
            "display": "GNU Free Documentation License v1.1 or later",
        }
    )
    """
    GNU Free Documentation License v1.1 or later

    GNU Free Documentation License v1.1 or later.
    """

    gfdl_1_2_only = CodeSystemConcept(
        {
            "code": "GFDL-1.2-only",
            "definition": "GNU Free Documentation License v1.2 only.",
            "display": "GNU Free Documentation License v1.2 only",
        }
    )
    """
    GNU Free Documentation License v1.2 only

    GNU Free Documentation License v1.2 only.
    """

    gfdl_1_2_or_later = CodeSystemConcept(
        {
            "code": "GFDL-1.2-or-later",
            "definition": "GNU Free Documentation License v1.2 or later.",
            "display": "GNU Free Documentation License v1.2 or later",
        }
    )
    """
    GNU Free Documentation License v1.2 or later

    GNU Free Documentation License v1.2 or later.
    """

    gfdl_1_3_only = CodeSystemConcept(
        {
            "code": "GFDL-1.3-only",
            "definition": "GNU Free Documentation License v1.3 only.",
            "display": "GNU Free Documentation License v1.3 only",
        }
    )
    """
    GNU Free Documentation License v1.3 only

    GNU Free Documentation License v1.3 only.
    """

    gfdl_1_3_or_later = CodeSystemConcept(
        {
            "code": "GFDL-1.3-or-later",
            "definition": "GNU Free Documentation License v1.3 or later.",
            "display": "GNU Free Documentation License v1.3 or later",
        }
    )
    """
    GNU Free Documentation License v1.3 or later

    GNU Free Documentation License v1.3 or later.
    """

    giftware = CodeSystemConcept(
        {
            "code": "Giftware",
            "definition": "Giftware License.",
            "display": "Giftware License",
        }
    )
    """
    Giftware License

    Giftware License.
    """

    gl2_ps = CodeSystemConcept(
        {"code": "GL2PS", "definition": "GL2PS License.", "display": "GL2PS License"}
    )
    """
    GL2PS License

    GL2PS License.
    """

    glide = CodeSystemConcept(
        {
            "code": "Glide",
            "definition": "3dfx Glide License.",
            "display": "3dfx Glide License",
        }
    )
    """
    3dfx Glide License

    3dfx Glide License.
    """

    glulxe = CodeSystemConcept(
        {"code": "Glulxe", "definition": "Glulxe License.", "display": "Glulxe License"}
    )
    """
    Glulxe License

    Glulxe License.
    """

    gnuplot = CodeSystemConcept(
        {
            "code": "gnuplot",
            "definition": "gnuplot License.",
            "display": "gnuplot License",
        }
    )
    """
    gnuplot License

    gnuplot License.
    """

    gpl_1_0_only = CodeSystemConcept(
        {
            "code": "GPL-1.0-only",
            "definition": "GNU General Public License v1.0 only.",
            "display": "GNU General Public License v1.0 only",
        }
    )
    """
    GNU General Public License v1.0 only

    GNU General Public License v1.0 only.
    """

    gpl_1_0_or_later = CodeSystemConcept(
        {
            "code": "GPL-1.0-or-later",
            "definition": "GNU General Public License v1.0 or later.",
            "display": "GNU General Public License v1.0 or later",
        }
    )
    """
    GNU General Public License v1.0 or later

    GNU General Public License v1.0 or later.
    """

    gpl_2_0_only = CodeSystemConcept(
        {
            "code": "GPL-2.0-only",
            "definition": "GNU General Public License v2.0 only.",
            "display": "GNU General Public License v2.0 only",
        }
    )
    """
    GNU General Public License v2.0 only

    GNU General Public License v2.0 only.
    """

    gpl_2_0_or_later = CodeSystemConcept(
        {
            "code": "GPL-2.0-or-later",
            "definition": "GNU General Public License v2.0 or later.",
            "display": "GNU General Public License v2.0 or later",
        }
    )
    """
    GNU General Public License v2.0 or later

    GNU General Public License v2.0 or later.
    """

    gpl_3_0_only = CodeSystemConcept(
        {
            "code": "GPL-3.0-only",
            "definition": "GNU General Public License v3.0 only.",
            "display": "GNU General Public License v3.0 only",
        }
    )
    """
    GNU General Public License v3.0 only

    GNU General Public License v3.0 only.
    """

    gpl_3_0_or_later = CodeSystemConcept(
        {
            "code": "GPL-3.0-or-later",
            "definition": "GNU General Public License v3.0 or later.",
            "display": "GNU General Public License v3.0 or later",
        }
    )
    """
    GNU General Public License v3.0 or later

    GNU General Public License v3.0 or later.
    """

    g_soap_1_3b = CodeSystemConcept(
        {
            "code": "gSOAP-1.3b",
            "definition": "gSOAP Public License v1.3b.",
            "display": "gSOAP Public License v1.3b",
        }
    )
    """
    gSOAP Public License v1.3b

    gSOAP Public License v1.3b.
    """

    haskell_report = CodeSystemConcept(
        {
            "code": "HaskellReport",
            "definition": "Haskell Language Report License.",
            "display": "Haskell Language Report License",
        }
    )
    """
    Haskell Language Report License

    Haskell Language Report License.
    """

    hpnd = CodeSystemConcept(
        {
            "code": "HPND",
            "definition": "Historical Permission Notice and Disclaimer.",
            "display": "Historical Permission Notice and Disclaimer",
        }
    )
    """
    Historical Permission Notice and Disclaimer

    Historical Permission Notice and Disclaimer.
    """

    ibm_pibs = CodeSystemConcept(
        {
            "code": "IBM-pibs",
            "definition": "IBM PowerPC Initialization and Boot Software.",
            "display": "IBM PowerPC Initialization and Boot Software",
        }
    )
    """
    IBM PowerPC Initialization and Boot Software

    IBM PowerPC Initialization and Boot Software.
    """

    icu = CodeSystemConcept(
        {"code": "ICU", "definition": "ICU License.", "display": "ICU License"}
    )
    """
    ICU License

    ICU License.
    """

    ijg = CodeSystemConcept(
        {
            "code": "IJG",
            "definition": "Independent JPEG Group License.",
            "display": "Independent JPEG Group License",
        }
    )
    """
    Independent JPEG Group License

    Independent JPEG Group License.
    """

    image_magick = CodeSystemConcept(
        {
            "code": "ImageMagick",
            "definition": "ImageMagick License.",
            "display": "ImageMagick License",
        }
    )
    """
    ImageMagick License

    ImageMagick License.
    """

    i_matix = CodeSystemConcept(
        {
            "code": "iMatix",
            "definition": "iMatix Standard Function Library Agreement.",
            "display": "iMatix Standard Function Library Agreement",
        }
    )
    """
    iMatix Standard Function Library Agreement

    iMatix Standard Function Library Agreement.
    """

    imlib2 = CodeSystemConcept(
        {"code": "Imlib2", "definition": "Imlib2 License.", "display": "Imlib2 License"}
    )
    """
    Imlib2 License

    Imlib2 License.
    """

    info_zip = CodeSystemConcept(
        {
            "code": "Info-ZIP",
            "definition": "Info-ZIP License.",
            "display": "Info-ZIP License",
        }
    )
    """
    Info-ZIP License

    Info-ZIP License.
    """

    intel_acpi = CodeSystemConcept(
        {
            "code": "Intel-ACPI",
            "definition": "Intel ACPI Software License Agreement.",
            "display": "Intel ACPI Software License Agreement",
        }
    )
    """
    Intel ACPI Software License Agreement

    Intel ACPI Software License Agreement.
    """

    intel = CodeSystemConcept(
        {
            "code": "Intel",
            "definition": "Intel Open Source License.",
            "display": "Intel Open Source License",
        }
    )
    """
    Intel Open Source License

    Intel Open Source License.
    """

    interbase_1_0 = CodeSystemConcept(
        {
            "code": "Interbase-1.0",
            "definition": "Interbase Public License v1.0.",
            "display": "Interbase Public License v1.0",
        }
    )
    """
    Interbase Public License v1.0

    Interbase Public License v1.0.
    """

    ipa = CodeSystemConcept(
        {
            "code": "IPA",
            "definition": "IPA Font License.",
            "display": "IPA Font License",
        }
    )
    """
    IPA Font License

    IPA Font License.
    """

    ipl_1_0 = CodeSystemConcept(
        {
            "code": "IPL-1.0",
            "definition": "IBM Public License v1.0.",
            "display": "IBM Public License v1.0",
        }
    )
    """
    IBM Public License v1.0

    IBM Public License v1.0.
    """

    isc = CodeSystemConcept(
        {"code": "ISC", "definition": "ISC License.", "display": "ISC License"}
    )
    """
    ISC License

    ISC License.
    """

    jas_per_2_0 = CodeSystemConcept(
        {
            "code": "JasPer-2.0",
            "definition": "JasPer License.",
            "display": "JasPer License",
        }
    )
    """
    JasPer License

    JasPer License.
    """

    json = CodeSystemConcept(
        {"code": "JSON", "definition": "JSON License.", "display": "JSON License"}
    )
    """
    JSON License

    JSON License.
    """

    lal_1_2 = CodeSystemConcept(
        {
            "code": "LAL-1.2",
            "definition": "Licence Art Libre 1.2.",
            "display": "Licence Art Libre 1.2",
        }
    )
    """
    Licence Art Libre 1.2

    Licence Art Libre 1.2.
    """

    lal_1_3 = CodeSystemConcept(
        {
            "code": "LAL-1.3",
            "definition": "Licence Art Libre 1.3.",
            "display": "Licence Art Libre 1.3",
        }
    )
    """
    Licence Art Libre 1.3

    Licence Art Libre 1.3.
    """

    latex2e = CodeSystemConcept(
        {
            "code": "Latex2e",
            "definition": "Latex2e License.",
            "display": "Latex2e License",
        }
    )
    """
    Latex2e License

    Latex2e License.
    """

    leptonica = CodeSystemConcept(
        {
            "code": "Leptonica",
            "definition": "Leptonica License.",
            "display": "Leptonica License",
        }
    )
    """
    Leptonica License

    Leptonica License.
    """

    lgpl_2_0_only = CodeSystemConcept(
        {
            "code": "LGPL-2.0-only",
            "definition": "GNU Library General Public License v2 only.",
            "display": "GNU Library General Public License v2 only",
        }
    )
    """
    GNU Library General Public License v2 only

    GNU Library General Public License v2 only.
    """

    lgpl_2_0_or_later = CodeSystemConcept(
        {
            "code": "LGPL-2.0-or-later",
            "definition": "GNU Library General Public License v2 or later.",
            "display": "GNU Library General Public License v2 or later",
        }
    )
    """
    GNU Library General Public License v2 or later

    GNU Library General Public License v2 or later.
    """

    lgpl_2_1_only = CodeSystemConcept(
        {
            "code": "LGPL-2.1-only",
            "definition": "GNU Lesser General Public License v2.1 only.",
            "display": "GNU Lesser General Public License v2.1 only",
        }
    )
    """
    GNU Lesser General Public License v2.1 only

    GNU Lesser General Public License v2.1 only.
    """

    lgpl_2_1_or_later = CodeSystemConcept(
        {
            "code": "LGPL-2.1-or-later",
            "definition": "GNU Lesser General Public License v2.1 or later.",
            "display": "GNU Lesser General Public License v2.1 or later",
        }
    )
    """
    GNU Lesser General Public License v2.1 or later

    GNU Lesser General Public License v2.1 or later.
    """

    lgpl_3_0_only = CodeSystemConcept(
        {
            "code": "LGPL-3.0-only",
            "definition": "GNU Lesser General Public License v3.0 only.",
            "display": "GNU Lesser General Public License v3.0 only",
        }
    )
    """
    GNU Lesser General Public License v3.0 only

    GNU Lesser General Public License v3.0 only.
    """

    lgpl_3_0_or_later = CodeSystemConcept(
        {
            "code": "LGPL-3.0-or-later",
            "definition": "GNU Lesser General Public License v3.0 or later.",
            "display": "GNU Lesser General Public License v3.0 or later",
        }
    )
    """
    GNU Lesser General Public License v3.0 or later

    GNU Lesser General Public License v3.0 or later.
    """

    lgpllr = CodeSystemConcept(
        {
            "code": "LGPLLR",
            "definition": "Lesser General Public License For Linguistic Resources.",
            "display": "Lesser General Public License For Linguistic Resources",
        }
    )
    """
    Lesser General Public License For Linguistic Resources

    Lesser General Public License For Linguistic Resources.
    """

    libpng = CodeSystemConcept(
        {"code": "Libpng", "definition": "libpng License.", "display": "libpng License"}
    )
    """
    libpng License

    libpng License.
    """

    libtiff = CodeSystemConcept(
        {
            "code": "libtiff",
            "definition": "libtiff License.",
            "display": "libtiff License",
        }
    )
    """
    libtiff License

    libtiff License.
    """

    li_li_q_p_1_1 = CodeSystemConcept(
        {
            "code": "LiLiQ-P-1.1",
            "definition": "Licence Libre du Québec – Permissive version 1.1.",
            "display": "Licence Libre du Québec – Permissive version 1.1",
        }
    )
    """
    Licence Libre du Québec – Permissive version 1.1

    Licence Libre du Québec – Permissive version 1.1.
    """

    li_li_q_r_1_1 = CodeSystemConcept(
        {
            "code": "LiLiQ-R-1.1",
            "definition": "Licence Libre du Québec – Réciprocité version 1.1.",
            "display": "Licence Libre du Québec – Réciprocité version 1.1",
        }
    )
    """
    Licence Libre du Québec – Réciprocité version 1.1

    Licence Libre du Québec – Réciprocité version 1.1.
    """

    li_li_q_rplus_1_1 = CodeSystemConcept(
        {
            "code": "LiLiQ-Rplus-1.1",
            "definition": "Licence Libre du Québec – Réciprocité forte version 1.1.",
            "display": "Licence Libre du Québec – Réciprocité forte version 1.1",
        }
    )
    """
    Licence Libre du Québec – Réciprocité forte version 1.1

    Licence Libre du Québec – Réciprocité forte version 1.1.
    """

    linux_open_ib = CodeSystemConcept(
        {
            "code": "Linux-OpenIB",
            "definition": "Linux Kernel Variant of OpenIB.org license.",
            "display": "Linux Kernel Variant of OpenIB.org license",
        }
    )
    """
    Linux Kernel Variant of OpenIB.org license

    Linux Kernel Variant of OpenIB.org license.
    """

    lpl_1_0 = CodeSystemConcept(
        {
            "code": "LPL-1.0",
            "definition": "Lucent Public License Version 1.0.",
            "display": "Lucent Public License Version 1.0",
        }
    )
    """
    Lucent Public License Version 1.0

    Lucent Public License Version 1.0.
    """

    lpl_1_02 = CodeSystemConcept(
        {
            "code": "LPL-1.02",
            "definition": "Lucent Public License v1.02.",
            "display": "Lucent Public License v1.02",
        }
    )
    """
    Lucent Public License v1.02

    Lucent Public License v1.02.
    """

    lppl_1_0 = CodeSystemConcept(
        {
            "code": "LPPL-1.0",
            "definition": "LaTeX Project Public License v1.0.",
            "display": "LaTeX Project Public License v1.0",
        }
    )
    """
    LaTeX Project Public License v1.0

    LaTeX Project Public License v1.0.
    """

    lppl_1_1 = CodeSystemConcept(
        {
            "code": "LPPL-1.1",
            "definition": "LaTeX Project Public License v1.1.",
            "display": "LaTeX Project Public License v1.1",
        }
    )
    """
    LaTeX Project Public License v1.1

    LaTeX Project Public License v1.1.
    """

    lppl_1_2 = CodeSystemConcept(
        {
            "code": "LPPL-1.2",
            "definition": "LaTeX Project Public License v1.2.",
            "display": "LaTeX Project Public License v1.2",
        }
    )
    """
    LaTeX Project Public License v1.2

    LaTeX Project Public License v1.2.
    """

    lppl_1_3a = CodeSystemConcept(
        {
            "code": "LPPL-1.3a",
            "definition": "LaTeX Project Public License v1.3a.",
            "display": "LaTeX Project Public License v1.3a",
        }
    )
    """
    LaTeX Project Public License v1.3a

    LaTeX Project Public License v1.3a.
    """

    lppl_1_3c = CodeSystemConcept(
        {
            "code": "LPPL-1.3c",
            "definition": "LaTeX Project Public License v1.3c.",
            "display": "LaTeX Project Public License v1.3c",
        }
    )
    """
    LaTeX Project Public License v1.3c

    LaTeX Project Public License v1.3c.
    """

    make_index = CodeSystemConcept(
        {
            "code": "MakeIndex",
            "definition": "MakeIndex License.",
            "display": "MakeIndex License",
        }
    )
    """
    MakeIndex License

    MakeIndex License.
    """

    mir_os = CodeSystemConcept(
        {"code": "MirOS", "definition": "MirOS License.", "display": "MirOS License"}
    )
    """
    MirOS License

    MirOS License.
    """

    mit_0 = CodeSystemConcept(
        {
            "code": "MIT-0",
            "definition": "MIT No Attribution.",
            "display": "MIT No Attribution",
        }
    )
    """
    MIT No Attribution

    MIT No Attribution.
    """

    mit_advertising = CodeSystemConcept(
        {
            "code": "MIT-advertising",
            "definition": "Enlightenment License (e16).",
            "display": "Enlightenment License (e16)",
        }
    )
    """
    Enlightenment License (e16)

    Enlightenment License (e16).
    """

    mit_cmu = CodeSystemConcept(
        {"code": "MIT-CMU", "definition": "CMU License.", "display": "CMU License"}
    )
    """
    CMU License

    CMU License.
    """

    mit_enna = CodeSystemConcept(
        {"code": "MIT-enna", "definition": "enna License.", "display": "enna License"}
    )
    """
    enna License

    enna License.
    """

    mit_feh = CodeSystemConcept(
        {"code": "MIT-feh", "definition": "feh License.", "display": "feh License"}
    )
    """
    feh License

    feh License.
    """

    mit = CodeSystemConcept(
        {"code": "MIT", "definition": "MIT License.", "display": "MIT License"}
    )
    """
    MIT License

    MIT License.
    """

    mitnfa = CodeSystemConcept(
        {
            "code": "MITNFA",
            "definition": "MIT +no-false-attribs license.",
            "display": "MIT +no-false-attribs license",
        }
    )
    """
    MIT +no-false-attribs license

    MIT +no-false-attribs license.
    """

    motosoto = CodeSystemConcept(
        {
            "code": "Motosoto",
            "definition": "Motosoto License.",
            "display": "Motosoto License",
        }
    )
    """
    Motosoto License

    Motosoto License.
    """

    mpich2 = CodeSystemConcept(
        {"code": "mpich2", "definition": "mpich2 License.", "display": "mpich2 License"}
    )
    """
    mpich2 License

    mpich2 License.
    """

    mpl_1_0 = CodeSystemConcept(
        {
            "code": "MPL-1.0",
            "definition": "Mozilla Public License 1.0.",
            "display": "Mozilla Public License 1.0",
        }
    )
    """
    Mozilla Public License 1.0

    Mozilla Public License 1.0.
    """

    mpl_1_1 = CodeSystemConcept(
        {
            "code": "MPL-1.1",
            "definition": "Mozilla Public License 1.1.",
            "display": "Mozilla Public License 1.1",
        }
    )
    """
    Mozilla Public License 1.1

    Mozilla Public License 1.1.
    """

    mpl_2_0_no_copyleft_exception = CodeSystemConcept(
        {
            "code": "MPL-2.0-no-copyleft-exception",
            "definition": "Mozilla Public License 2.0 (no copyleft exception).",
            "display": "Mozilla Public License 2.0 (no copyleft exception)",
        }
    )
    """
    Mozilla Public License 2.0 (no copyleft exception)

    Mozilla Public License 2.0 (no copyleft exception).
    """

    mpl_2_0 = CodeSystemConcept(
        {
            "code": "MPL-2.0",
            "definition": "Mozilla Public License 2.0.",
            "display": "Mozilla Public License 2.0",
        }
    )
    """
    Mozilla Public License 2.0

    Mozilla Public License 2.0.
    """

    ms_pl = CodeSystemConcept(
        {
            "code": "MS-PL",
            "definition": "Microsoft Public License.",
            "display": "Microsoft Public License",
        }
    )
    """
    Microsoft Public License

    Microsoft Public License.
    """

    ms_rl = CodeSystemConcept(
        {
            "code": "MS-RL",
            "definition": "Microsoft Reciprocal License.",
            "display": "Microsoft Reciprocal License",
        }
    )
    """
    Microsoft Reciprocal License

    Microsoft Reciprocal License.
    """

    mtll = CodeSystemConcept(
        {
            "code": "MTLL",
            "definition": "Matrix Template Library License.",
            "display": "Matrix Template Library License",
        }
    )
    """
    Matrix Template Library License

    Matrix Template Library License.
    """

    multics = CodeSystemConcept(
        {
            "code": "Multics",
            "definition": "Multics License.",
            "display": "Multics License",
        }
    )
    """
    Multics License

    Multics License.
    """

    mup = CodeSystemConcept(
        {"code": "Mup", "definition": "Mup License.", "display": "Mup License"}
    )
    """
    Mup License

    Mup License.
    """

    nasa_1_3 = CodeSystemConcept(
        {
            "code": "NASA-1.3",
            "definition": "NASA Open Source Agreement 1.3.",
            "display": "NASA Open Source Agreement 1.3",
        }
    )
    """
    NASA Open Source Agreement 1.3

    NASA Open Source Agreement 1.3.
    """

    naumen = CodeSystemConcept(
        {
            "code": "Naumen",
            "definition": "Naumen Public License.",
            "display": "Naumen Public License",
        }
    )
    """
    Naumen Public License

    Naumen Public License.
    """

    nbpl_1_0 = CodeSystemConcept(
        {
            "code": "NBPL-1.0",
            "definition": "Net Boolean Public License v1.",
            "display": "Net Boolean Public License v1",
        }
    )
    """
    Net Boolean Public License v1

    Net Boolean Public License v1.
    """

    ncsa = CodeSystemConcept(
        {
            "code": "NCSA",
            "definition": "University of Illinois/NCSA Open Source License.",
            "display": "University of Illinois/NCSA Open Source License",
        }
    )
    """
    University of Illinois/NCSA Open Source License

    University of Illinois/NCSA Open Source License.
    """

    net_snmp = CodeSystemConcept(
        {
            "code": "Net-SNMP",
            "definition": "Net-SNMP License.",
            "display": "Net-SNMP License",
        }
    )
    """
    Net-SNMP License

    Net-SNMP License.
    """

    net_cdf = CodeSystemConcept(
        {"code": "NetCDF", "definition": "NetCDF license.", "display": "NetCDF license"}
    )
    """
    NetCDF license

    NetCDF license.
    """

    newsletr = CodeSystemConcept(
        {
            "code": "Newsletr",
            "definition": "Newsletr License.",
            "display": "Newsletr License",
        }
    )
    """
    Newsletr License

    Newsletr License.
    """

    ngpl = CodeSystemConcept(
        {
            "code": "NGPL",
            "definition": "Nethack General Public License.",
            "display": "Nethack General Public License",
        }
    )
    """
    Nethack General Public License

    Nethack General Public License.
    """

    nlod_1_0 = CodeSystemConcept(
        {
            "code": "NLOD-1.0",
            "definition": "Norwegian Licence for Open Government Data.",
            "display": "Norwegian Licence for Open Government Data",
        }
    )
    """
    Norwegian Licence for Open Government Data

    Norwegian Licence for Open Government Data.
    """

    nlpl = CodeSystemConcept(
        {
            "code": "NLPL",
            "definition": "No Limit Public License.",
            "display": "No Limit Public License",
        }
    )
    """
    No Limit Public License

    No Limit Public License.
    """

    nokia = CodeSystemConcept(
        {
            "code": "Nokia",
            "definition": "Nokia Open Source License.",
            "display": "Nokia Open Source License",
        }
    )
    """
    Nokia Open Source License

    Nokia Open Source License.
    """

    nosl = CodeSystemConcept(
        {
            "code": "NOSL",
            "definition": "Netizen Open Source License.",
            "display": "Netizen Open Source License",
        }
    )
    """
    Netizen Open Source License

    Netizen Open Source License.
    """

    noweb = CodeSystemConcept(
        {"code": "Noweb", "definition": "Noweb License.", "display": "Noweb License"}
    )
    """
    Noweb License

    Noweb License.
    """

    npl_1_0 = CodeSystemConcept(
        {
            "code": "NPL-1.0",
            "definition": "Netscape Public License v1.0.",
            "display": "Netscape Public License v1.0",
        }
    )
    """
    Netscape Public License v1.0

    Netscape Public License v1.0.
    """

    npl_1_1 = CodeSystemConcept(
        {
            "code": "NPL-1.1",
            "definition": "Netscape Public License v1.1.",
            "display": "Netscape Public License v1.1",
        }
    )
    """
    Netscape Public License v1.1

    Netscape Public License v1.1.
    """

    nposl_3_0 = CodeSystemConcept(
        {
            "code": "NPOSL-3.0",
            "definition": "Non-Profit Open Software License 3.0.",
            "display": "Non-Profit Open Software License 3.0",
        }
    )
    """
    Non-Profit Open Software License 3.0

    Non-Profit Open Software License 3.0.
    """

    nrl = CodeSystemConcept(
        {"code": "NRL", "definition": "NRL License.", "display": "NRL License"}
    )
    """
    NRL License

    NRL License.
    """

    ntp = CodeSystemConcept(
        {"code": "NTP", "definition": "NTP License.", "display": "NTP License"}
    )
    """
    NTP License

    NTP License.
    """

    occt_pl = CodeSystemConcept(
        {
            "code": "OCCT-PL",
            "definition": "Open CASCADE Technology Public License.",
            "display": "Open CASCADE Technology Public License",
        }
    )
    """
    Open CASCADE Technology Public License

    Open CASCADE Technology Public License.
    """

    oclc_2_0 = CodeSystemConcept(
        {
            "code": "OCLC-2.0",
            "definition": "OCLC Research Public License 2.0.",
            "display": "OCLC Research Public License 2.0",
        }
    )
    """
    OCLC Research Public License 2.0

    OCLC Research Public License 2.0.
    """

    odb_l_1_0 = CodeSystemConcept(
        {
            "code": "ODbL-1.0",
            "definition": "ODC Open Database License v1.0.",
            "display": "ODC Open Database License v1.0",
        }
    )
    """
    ODC Open Database License v1.0

    ODC Open Database License v1.0.
    """

    ofl_1_0 = CodeSystemConcept(
        {
            "code": "OFL-1.0",
            "definition": "SIL Open Font License 1.0.",
            "display": "SIL Open Font License 1.0",
        }
    )
    """
    SIL Open Font License 1.0

    SIL Open Font License 1.0.
    """

    ofl_1_1 = CodeSystemConcept(
        {
            "code": "OFL-1.1",
            "definition": "SIL Open Font License 1.1.",
            "display": "SIL Open Font License 1.1",
        }
    )
    """
    SIL Open Font License 1.1

    SIL Open Font License 1.1.
    """

    ogtsl = CodeSystemConcept(
        {
            "code": "OGTSL",
            "definition": "Open Group Test Suite License.",
            "display": "Open Group Test Suite License",
        }
    )
    """
    Open Group Test Suite License

    Open Group Test Suite License.
    """

    oldap_1_1 = CodeSystemConcept(
        {
            "code": "OLDAP-1.1",
            "definition": "Open LDAP Public License v1.1.",
            "display": "Open LDAP Public License v1.1",
        }
    )
    """
    Open LDAP Public License v1.1

    Open LDAP Public License v1.1.
    """

    oldap_1_2 = CodeSystemConcept(
        {
            "code": "OLDAP-1.2",
            "definition": "Open LDAP Public License v1.2.",
            "display": "Open LDAP Public License v1.2",
        }
    )
    """
    Open LDAP Public License v1.2

    Open LDAP Public License v1.2.
    """

    oldap_1_3 = CodeSystemConcept(
        {
            "code": "OLDAP-1.3",
            "definition": "Open LDAP Public License v1.3.",
            "display": "Open LDAP Public License v1.3",
        }
    )
    """
    Open LDAP Public License v1.3

    Open LDAP Public License v1.3.
    """

    oldap_1_4 = CodeSystemConcept(
        {
            "code": "OLDAP-1.4",
            "definition": "Open LDAP Public License v1.4.",
            "display": "Open LDAP Public License v1.4",
        }
    )
    """
    Open LDAP Public License v1.4

    Open LDAP Public License v1.4.
    """

    oldap_2_0_1 = CodeSystemConcept(
        {
            "code": "OLDAP-2.0.1",
            "definition": "Open LDAP Public License v2.0.1.",
            "display": "Open LDAP Public License v2.0.1",
        }
    )
    """
    Open LDAP Public License v2.0.1

    Open LDAP Public License v2.0.1.
    """

    oldap_2_0 = CodeSystemConcept(
        {
            "code": "OLDAP-2.0",
            "definition": "Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B).",
            "display": "Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)",
        }
    )
    """
    Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)

    Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B).
    """

    oldap_2_1 = CodeSystemConcept(
        {
            "code": "OLDAP-2.1",
            "definition": "Open LDAP Public License v2.1.",
            "display": "Open LDAP Public License v2.1",
        }
    )
    """
    Open LDAP Public License v2.1

    Open LDAP Public License v2.1.
    """

    oldap_2_2_1 = CodeSystemConcept(
        {
            "code": "OLDAP-2.2.1",
            "definition": "Open LDAP Public License v2.2.1.",
            "display": "Open LDAP Public License v2.2.1",
        }
    )
    """
    Open LDAP Public License v2.2.1

    Open LDAP Public License v2.2.1.
    """

    oldap_2_2_2 = CodeSystemConcept(
        {
            "code": "OLDAP-2.2.2",
            "definition": "Open LDAP Public License 2.2.2.",
            "display": "Open LDAP Public License 2.2.2",
        }
    )
    """
    Open LDAP Public License 2.2.2

    Open LDAP Public License 2.2.2.
    """

    oldap_2_2 = CodeSystemConcept(
        {
            "code": "OLDAP-2.2",
            "definition": "Open LDAP Public License v2.2.",
            "display": "Open LDAP Public License v2.2",
        }
    )
    """
    Open LDAP Public License v2.2

    Open LDAP Public License v2.2.
    """

    oldap_2_3 = CodeSystemConcept(
        {
            "code": "OLDAP-2.3",
            "definition": "Open LDAP Public License v2.3.",
            "display": "Open LDAP Public License v2.3",
        }
    )
    """
    Open LDAP Public License v2.3

    Open LDAP Public License v2.3.
    """

    oldap_2_4 = CodeSystemConcept(
        {
            "code": "OLDAP-2.4",
            "definition": "Open LDAP Public License v2.4.",
            "display": "Open LDAP Public License v2.4",
        }
    )
    """
    Open LDAP Public License v2.4

    Open LDAP Public License v2.4.
    """

    oldap_2_5 = CodeSystemConcept(
        {
            "code": "OLDAP-2.5",
            "definition": "Open LDAP Public License v2.5.",
            "display": "Open LDAP Public License v2.5",
        }
    )
    """
    Open LDAP Public License v2.5

    Open LDAP Public License v2.5.
    """

    oldap_2_6 = CodeSystemConcept(
        {
            "code": "OLDAP-2.6",
            "definition": "Open LDAP Public License v2.6.",
            "display": "Open LDAP Public License v2.6",
        }
    )
    """
    Open LDAP Public License v2.6

    Open LDAP Public License v2.6.
    """

    oldap_2_7 = CodeSystemConcept(
        {
            "code": "OLDAP-2.7",
            "definition": "Open LDAP Public License v2.7.",
            "display": "Open LDAP Public License v2.7",
        }
    )
    """
    Open LDAP Public License v2.7

    Open LDAP Public License v2.7.
    """

    oldap_2_8 = CodeSystemConcept(
        {
            "code": "OLDAP-2.8",
            "definition": "Open LDAP Public License v2.8.",
            "display": "Open LDAP Public License v2.8",
        }
    )
    """
    Open LDAP Public License v2.8

    Open LDAP Public License v2.8.
    """

    oml = CodeSystemConcept(
        {
            "code": "OML",
            "definition": "Open Market License.",
            "display": "Open Market License",
        }
    )
    """
    Open Market License

    Open Market License.
    """

    open_ssl = CodeSystemConcept(
        {
            "code": "OpenSSL",
            "definition": "OpenSSL License.",
            "display": "OpenSSL License",
        }
    )
    """
    OpenSSL License

    OpenSSL License.
    """

    opl_1_0 = CodeSystemConcept(
        {
            "code": "OPL-1.0",
            "definition": "Open Public License v1.0.",
            "display": "Open Public License v1.0",
        }
    )
    """
    Open Public License v1.0

    Open Public License v1.0.
    """

    oset_pl_2_1 = CodeSystemConcept(
        {
            "code": "OSET-PL-2.1",
            "definition": "OSET Public License version 2.1.",
            "display": "OSET Public License version 2.1",
        }
    )
    """
    OSET Public License version 2.1

    OSET Public License version 2.1.
    """

    osl_1_0 = CodeSystemConcept(
        {
            "code": "OSL-1.0",
            "definition": "Open Software License 1.0.",
            "display": "Open Software License 1.0",
        }
    )
    """
    Open Software License 1.0

    Open Software License 1.0.
    """

    osl_1_1 = CodeSystemConcept(
        {
            "code": "OSL-1.1",
            "definition": "Open Software License 1.1.",
            "display": "Open Software License 1.1",
        }
    )
    """
    Open Software License 1.1

    Open Software License 1.1.
    """

    osl_2_0 = CodeSystemConcept(
        {
            "code": "OSL-2.0",
            "definition": "Open Software License 2.0.",
            "display": "Open Software License 2.0",
        }
    )
    """
    Open Software License 2.0

    Open Software License 2.0.
    """

    osl_2_1 = CodeSystemConcept(
        {
            "code": "OSL-2.1",
            "definition": "Open Software License 2.1.",
            "display": "Open Software License 2.1",
        }
    )
    """
    Open Software License 2.1

    Open Software License 2.1.
    """

    osl_3_0 = CodeSystemConcept(
        {
            "code": "OSL-3.0",
            "definition": "Open Software License 3.0.",
            "display": "Open Software License 3.0",
        }
    )
    """
    Open Software License 3.0

    Open Software License 3.0.
    """

    pddl_1_0 = CodeSystemConcept(
        {
            "code": "PDDL-1.0",
            "definition": "ODC Public Domain Dedication & License 1.0.",
            "display": "ODC Public Domain Dedication & License 1.0",
        }
    )
    """
    ODC Public Domain Dedication & License 1.0

    ODC Public Domain Dedication & License 1.0.
    """

    php_3_0 = CodeSystemConcept(
        {
            "code": "PHP-3.0",
            "definition": "PHP License v3.0.",
            "display": "PHP License v3.0",
        }
    )
    """
    PHP License v3.0

    PHP License v3.0.
    """

    php_3_01 = CodeSystemConcept(
        {
            "code": "PHP-3.01",
            "definition": "PHP License v3.01.",
            "display": "PHP License v3.01",
        }
    )
    """
    PHP License v3.01

    PHP License v3.01.
    """

    plexus = CodeSystemConcept(
        {
            "code": "Plexus",
            "definition": "Plexus Classworlds License.",
            "display": "Plexus Classworlds License",
        }
    )
    """
    Plexus Classworlds License

    Plexus Classworlds License.
    """

    postgre_sql = CodeSystemConcept(
        {
            "code": "PostgreSQL",
            "definition": "PostgreSQL License.",
            "display": "PostgreSQL License",
        }
    )
    """
    PostgreSQL License

    PostgreSQL License.
    """

    psfrag = CodeSystemConcept(
        {"code": "psfrag", "definition": "psfrag License.", "display": "psfrag License"}
    )
    """
    psfrag License

    psfrag License.
    """

    psutils = CodeSystemConcept(
        {
            "code": "psutils",
            "definition": "psutils License.",
            "display": "psutils License",
        }
    )
    """
    psutils License

    psutils License.
    """

    python_2_0 = CodeSystemConcept(
        {
            "code": "Python-2.0",
            "definition": "Python License 2.0.",
            "display": "Python License 2.0",
        }
    )
    """
    Python License 2.0

    Python License 2.0.
    """

    qhull = CodeSystemConcept(
        {"code": "Qhull", "definition": "Qhull License.", "display": "Qhull License"}
    )
    """
    Qhull License

    Qhull License.
    """

    qpl_1_0 = CodeSystemConcept(
        {
            "code": "QPL-1.0",
            "definition": "Q Public License 1.0.",
            "display": "Q Public License 1.0",
        }
    )
    """
    Q Public License 1.0

    Q Public License 1.0.
    """

    rdisc = CodeSystemConcept(
        {"code": "Rdisc", "definition": "Rdisc License.", "display": "Rdisc License"}
    )
    """
    Rdisc License

    Rdisc License.
    """

    rhe_cos_1_1 = CodeSystemConcept(
        {
            "code": "RHeCos-1.1",
            "definition": "Red Hat eCos Public License v1.1.",
            "display": "Red Hat eCos Public License v1.1",
        }
    )
    """
    Red Hat eCos Public License v1.1

    Red Hat eCos Public License v1.1.
    """

    rpl_1_1 = CodeSystemConcept(
        {
            "code": "RPL-1.1",
            "definition": "Reciprocal Public License 1.1.",
            "display": "Reciprocal Public License 1.1",
        }
    )
    """
    Reciprocal Public License 1.1

    Reciprocal Public License 1.1.
    """

    rpl_1_5 = CodeSystemConcept(
        {
            "code": "RPL-1.5",
            "definition": "Reciprocal Public License 1.5.",
            "display": "Reciprocal Public License 1.5",
        }
    )
    """
    Reciprocal Public License 1.5

    Reciprocal Public License 1.5.
    """

    rpsl_1_0 = CodeSystemConcept(
        {
            "code": "RPSL-1.0",
            "definition": "RealNetworks Public Source License v1.0.",
            "display": "RealNetworks Public Source License v1.0",
        }
    )
    """
    RealNetworks Public Source License v1.0

    RealNetworks Public Source License v1.0.
    """

    rsa_md = CodeSystemConcept(
        {
            "code": "RSA-MD",
            "definition": "RSA Message-Digest License.",
            "display": "RSA Message-Digest License",
        }
    )
    """
    RSA Message-Digest License

    RSA Message-Digest License.
    """

    rscpl = CodeSystemConcept(
        {
            "code": "RSCPL",
            "definition": "Ricoh Source Code Public License.",
            "display": "Ricoh Source Code Public License",
        }
    )
    """
    Ricoh Source Code Public License

    Ricoh Source Code Public License.
    """

    ruby = CodeSystemConcept(
        {"code": "Ruby", "definition": "Ruby License.", "display": "Ruby License"}
    )
    """
    Ruby License

    Ruby License.
    """

    sax_pd = CodeSystemConcept(
        {
            "code": "SAX-PD",
            "definition": "Sax Public Domain Notice.",
            "display": "Sax Public Domain Notice",
        }
    )
    """
    Sax Public Domain Notice

    Sax Public Domain Notice.
    """

    saxpath = CodeSystemConcept(
        {
            "code": "Saxpath",
            "definition": "Saxpath License.",
            "display": "Saxpath License",
        }
    )
    """
    Saxpath License

    Saxpath License.
    """

    scea = CodeSystemConcept(
        {
            "code": "SCEA",
            "definition": "SCEA Shared Source License.",
            "display": "SCEA Shared Source License",
        }
    )
    """
    SCEA Shared Source License

    SCEA Shared Source License.
    """

    sendmail = CodeSystemConcept(
        {
            "code": "Sendmail",
            "definition": "Sendmail License.",
            "display": "Sendmail License",
        }
    )
    """
    Sendmail License

    Sendmail License.
    """

    sgi_b_1_0 = CodeSystemConcept(
        {
            "code": "SGI-B-1.0",
            "definition": "SGI Free Software License B v1.0.",
            "display": "SGI Free Software License B v1.0",
        }
    )
    """
    SGI Free Software License B v1.0

    SGI Free Software License B v1.0.
    """

    sgi_b_1_1 = CodeSystemConcept(
        {
            "code": "SGI-B-1.1",
            "definition": "SGI Free Software License B v1.1.",
            "display": "SGI Free Software License B v1.1",
        }
    )
    """
    SGI Free Software License B v1.1

    SGI Free Software License B v1.1.
    """

    sgi_b_2_0 = CodeSystemConcept(
        {
            "code": "SGI-B-2.0",
            "definition": "SGI Free Software License B v2.0.",
            "display": "SGI Free Software License B v2.0",
        }
    )
    """
    SGI Free Software License B v2.0

    SGI Free Software License B v2.0.
    """

    sim_pl_2_0 = CodeSystemConcept(
        {
            "code": "SimPL-2.0",
            "definition": "Simple Public License 2.0.",
            "display": "Simple Public License 2.0",
        }
    )
    """
    Simple Public License 2.0

    Simple Public License 2.0.
    """

    sissl_1_2 = CodeSystemConcept(
        {
            "code": "SISSL-1.2",
            "definition": "Sun Industry Standards Source License v1.2.",
            "display": "Sun Industry Standards Source License v1.2",
        }
    )
    """
    Sun Industry Standards Source License v1.2

    Sun Industry Standards Source License v1.2.
    """

    sissl = CodeSystemConcept(
        {
            "code": "SISSL",
            "definition": "Sun Industry Standards Source License v1.1.",
            "display": "Sun Industry Standards Source License v1.1",
        }
    )
    """
    Sun Industry Standards Source License v1.1

    Sun Industry Standards Source License v1.1.
    """

    sleepycat = CodeSystemConcept(
        {
            "code": "Sleepycat",
            "definition": "Sleepycat License.",
            "display": "Sleepycat License",
        }
    )
    """
    Sleepycat License

    Sleepycat License.
    """

    smlnj = CodeSystemConcept(
        {
            "code": "SMLNJ",
            "definition": "Standard ML of New Jersey License.",
            "display": "Standard ML of New Jersey License",
        }
    )
    """
    Standard ML of New Jersey License

    Standard ML of New Jersey License.
    """

    smppl = CodeSystemConcept(
        {
            "code": "SMPPL",
            "definition": "Secure Messaging Protocol Public License.",
            "display": "Secure Messaging Protocol Public License",
        }
    )
    """
    Secure Messaging Protocol Public License

    Secure Messaging Protocol Public License.
    """

    snia = CodeSystemConcept(
        {
            "code": "SNIA",
            "definition": "SNIA Public License 1.1.",
            "display": "SNIA Public License 1.1",
        }
    )
    """
    SNIA Public License 1.1

    SNIA Public License 1.1.
    """

    spencer_86 = CodeSystemConcept(
        {
            "code": "Spencer-86",
            "definition": "Spencer License 86.",
            "display": "Spencer License 86",
        }
    )
    """
    Spencer License 86

    Spencer License 86.
    """

    spencer_94 = CodeSystemConcept(
        {
            "code": "Spencer-94",
            "definition": "Spencer License 94.",
            "display": "Spencer License 94",
        }
    )
    """
    Spencer License 94

    Spencer License 94.
    """

    spencer_99 = CodeSystemConcept(
        {
            "code": "Spencer-99",
            "definition": "Spencer License 99.",
            "display": "Spencer License 99",
        }
    )
    """
    Spencer License 99

    Spencer License 99.
    """

    spl_1_0 = CodeSystemConcept(
        {
            "code": "SPL-1.0",
            "definition": "Sun Public License v1.0.",
            "display": "Sun Public License v1.0",
        }
    )
    """
    Sun Public License v1.0

    Sun Public License v1.0.
    """

    sugar_crm_1_1_3 = CodeSystemConcept(
        {
            "code": "SugarCRM-1.1.3",
            "definition": "SugarCRM Public License v1.1.3.",
            "display": "SugarCRM Public License v1.1.3",
        }
    )
    """
    SugarCRM Public License v1.1.3

    SugarCRM Public License v1.1.3.
    """

    swl = CodeSystemConcept(
        {
            "code": "SWL",
            "definition": "Scheme Widget Library (SWL) Software License Agreement.",
            "display": "Scheme Widget Library (SWL) Software License Agreement",
        }
    )
    """
    Scheme Widget Library (SWL) Software License Agreement

    Scheme Widget Library (SWL) Software License Agreement.
    """

    tcl = CodeSystemConcept(
        {"code": "TCL", "definition": "TCL/TK License.", "display": "TCL/TK License"}
    )
    """
    TCL/TK License

    TCL/TK License.
    """

    tcp_wrappers = CodeSystemConcept(
        {
            "code": "TCP-wrappers",
            "definition": "TCP Wrappers License.",
            "display": "TCP Wrappers License",
        }
    )
    """
    TCP Wrappers License

    TCP Wrappers License.
    """

    tmate = CodeSystemConcept(
        {
            "code": "TMate",
            "definition": "TMate Open Source License.",
            "display": "TMate Open Source License",
        }
    )
    """
    TMate Open Source License

    TMate Open Source License.
    """

    torque_1_1 = CodeSystemConcept(
        {
            "code": "TORQUE-1.1",
            "definition": "TORQUE v2.5+ Software License v1.1.",
            "display": "TORQUE v2.5+ Software License v1.1",
        }
    )
    """
    TORQUE v2.5+ Software License v1.1

    TORQUE v2.5+ Software License v1.1.
    """

    tosl = CodeSystemConcept(
        {
            "code": "TOSL",
            "definition": "Trusster Open Source License.",
            "display": "Trusster Open Source License",
        }
    )
    """
    Trusster Open Source License

    Trusster Open Source License.
    """

    unicode_dfs_2015 = CodeSystemConcept(
        {
            "code": "Unicode-DFS-2015",
            "definition": "Unicode License Agreement - Data Files and Software (2015).",
            "display": "Unicode License Agreement - Data Files and Software (2015)",
        }
    )
    """
    Unicode License Agreement - Data Files and Software (2015)

    Unicode License Agreement - Data Files and Software (2015).
    """

    unicode_dfs_2016 = CodeSystemConcept(
        {
            "code": "Unicode-DFS-2016",
            "definition": "Unicode License Agreement - Data Files and Software (2016).",
            "display": "Unicode License Agreement - Data Files and Software (2016)",
        }
    )
    """
    Unicode License Agreement - Data Files and Software (2016)

    Unicode License Agreement - Data Files and Software (2016).
    """

    unicode_tou = CodeSystemConcept(
        {
            "code": "Unicode-TOU",
            "definition": "Unicode Terms of Use.",
            "display": "Unicode Terms of Use",
        }
    )
    """
    Unicode Terms of Use

    Unicode Terms of Use.
    """

    unlicense = CodeSystemConcept(
        {
            "code": "Unlicense",
            "definition": "The Unlicense.",
            "display": "The Unlicense",
        }
    )
    """
    The Unlicense

    The Unlicense.
    """

    upl_1_0 = CodeSystemConcept(
        {
            "code": "UPL-1.0",
            "definition": "Universal Permissive License v1.0.",
            "display": "Universal Permissive License v1.0",
        }
    )
    """
    Universal Permissive License v1.0

    Universal Permissive License v1.0.
    """

    vim = CodeSystemConcept(
        {"code": "Vim", "definition": "Vim License.", "display": "Vim License"}
    )
    """
    Vim License

    Vim License.
    """

    vostrom = CodeSystemConcept(
        {
            "code": "VOSTROM",
            "definition": "VOSTROM Public License for Open Source.",
            "display": "VOSTROM Public License for Open Source",
        }
    )
    """
    VOSTROM Public License for Open Source

    VOSTROM Public License for Open Source.
    """

    vsl_1_0 = CodeSystemConcept(
        {
            "code": "VSL-1.0",
            "definition": "Vovida Software License v1.0.",
            "display": "Vovida Software License v1.0",
        }
    )
    """
    Vovida Software License v1.0

    Vovida Software License v1.0.
    """

    w3_c_19980720 = CodeSystemConcept(
        {
            "code": "W3C-19980720",
            "definition": "W3C Software Notice and License (1998-07-20).",
            "display": "W3C Software Notice and License (1998-07-20)",
        }
    )
    """
    W3C Software Notice and License (1998-07-20)

    W3C Software Notice and License (1998-07-20).
    """

    w3_c_20150513 = CodeSystemConcept(
        {
            "code": "W3C-20150513",
            "definition": "W3C Software Notice and Document License (2015-05-13).",
            "display": "W3C Software Notice and Document License (2015-05-13)",
        }
    )
    """
    W3C Software Notice and Document License (2015-05-13)

    W3C Software Notice and Document License (2015-05-13).
    """

    w3_c = CodeSystemConcept(
        {
            "code": "W3C",
            "definition": "W3C Software Notice and License (2002-12-31).",
            "display": "W3C Software Notice and License (2002-12-31)",
        }
    )
    """
    W3C Software Notice and License (2002-12-31)

    W3C Software Notice and License (2002-12-31).
    """

    watcom_1_0 = CodeSystemConcept(
        {
            "code": "Watcom-1.0",
            "definition": "Sybase Open Watcom Public License 1.0.",
            "display": "Sybase Open Watcom Public License 1.0",
        }
    )
    """
    Sybase Open Watcom Public License 1.0

    Sybase Open Watcom Public License 1.0.
    """

    wsuipa = CodeSystemConcept(
        {"code": "Wsuipa", "definition": "Wsuipa License.", "display": "Wsuipa License"}
    )
    """
    Wsuipa License

    Wsuipa License.
    """

    wtfpl = CodeSystemConcept(
        {
            "code": "WTFPL",
            "definition": "Do What The F*ck You Want To Public License.",
            "display": "Do What The F*ck You Want To Public License",
        }
    )
    """
    Do What The F*ck You Want To Public License

    Do What The F*ck You Want To Public License.
    """

    x11 = CodeSystemConcept(
        {"code": "X11", "definition": "X11 License.", "display": "X11 License"}
    )
    """
    X11 License

    X11 License.
    """

    xerox = CodeSystemConcept(
        {"code": "Xerox", "definition": "Xerox License.", "display": "Xerox License"}
    )
    """
    Xerox License

    Xerox License.
    """

    xfree86_1_1 = CodeSystemConcept(
        {
            "code": "XFree86-1.1",
            "definition": "XFree86 License 1.1.",
            "display": "XFree86 License 1.1",
        }
    )
    """
    XFree86 License 1.1

    XFree86 License 1.1.
    """

    xinetd = CodeSystemConcept(
        {"code": "xinetd", "definition": "xinetd License.", "display": "xinetd License"}
    )
    """
    xinetd License

    xinetd License.
    """

    xnet = CodeSystemConcept(
        {"code": "Xnet", "definition": "X.Net License.", "display": "X.Net License"}
    )
    """
    X.Net License

    X.Net License.
    """

    xpp = CodeSystemConcept(
        {"code": "xpp", "definition": "XPP License.", "display": "XPP License"}
    )
    """
    XPP License

    XPP License.
    """

    xskat = CodeSystemConcept(
        {"code": "XSkat", "definition": "XSkat License.", "display": "XSkat License"}
    )
    """
    XSkat License

    XSkat License.
    """

    ypl_1_0 = CodeSystemConcept(
        {
            "code": "YPL-1.0",
            "definition": "Yahoo! Public License v1.0.",
            "display": "Yahoo! Public License v1.0",
        }
    )
    """
    Yahoo! Public License v1.0

    Yahoo! Public License v1.0.
    """

    ypl_1_1 = CodeSystemConcept(
        {
            "code": "YPL-1.1",
            "definition": "Yahoo! Public License v1.1.",
            "display": "Yahoo! Public License v1.1",
        }
    )
    """
    Yahoo! Public License v1.1

    Yahoo! Public License v1.1.
    """

    zed = CodeSystemConcept(
        {"code": "Zed", "definition": "Zed License.", "display": "Zed License"}
    )
    """
    Zed License

    Zed License.
    """

    zend_2_0 = CodeSystemConcept(
        {
            "code": "Zend-2.0",
            "definition": "Zend License v2.0.",
            "display": "Zend License v2.0",
        }
    )
    """
    Zend License v2.0

    Zend License v2.0.
    """

    zimbra_1_3 = CodeSystemConcept(
        {
            "code": "Zimbra-1.3",
            "definition": "Zimbra Public License v1.3.",
            "display": "Zimbra Public License v1.3",
        }
    )
    """
    Zimbra Public License v1.3

    Zimbra Public License v1.3.
    """

    zimbra_1_4 = CodeSystemConcept(
        {
            "code": "Zimbra-1.4",
            "definition": "Zimbra Public License v1.4.",
            "display": "Zimbra Public License v1.4",
        }
    )
    """
    Zimbra Public License v1.4

    Zimbra Public License v1.4.
    """

    zlib_acknowledgement = CodeSystemConcept(
        {
            "code": "zlib-acknowledgement",
            "definition": "zlib/libpng License with Acknowledgement.",
            "display": "zlib/libpng License with Acknowledgement",
        }
    )
    """
    zlib/libpng License with Acknowledgement

    zlib/libpng License with Acknowledgement.
    """

    zlib = CodeSystemConcept(
        {"code": "Zlib", "definition": "zlib License.", "display": "zlib License"}
    )
    """
    zlib License

    zlib License.
    """

    zpl_1_1 = CodeSystemConcept(
        {
            "code": "ZPL-1.1",
            "definition": "Zope Public License 1.1.",
            "display": "Zope Public License 1.1",
        }
    )
    """
    Zope Public License 1.1

    Zope Public License 1.1.
    """

    zpl_2_0 = CodeSystemConcept(
        {
            "code": "ZPL-2.0",
            "definition": "Zope Public License 2.0.",
            "display": "Zope Public License 2.0",
        }
    )
    """
    Zope Public License 2.0

    Zope Public License 2.0.
    """

    zpl_2_1 = CodeSystemConcept(
        {
            "code": "ZPL-2.1",
            "definition": "Zope Public License 2.1.",
            "display": "Zope Public License 2.1",
        }
    )
    """
    Zope Public License 2.1

    Zope Public License 2.1.
    """

    class Meta:
        resource = _resource
