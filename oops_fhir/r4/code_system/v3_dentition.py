from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3Dentition"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3Dentition:
    """
    v3 Code System Dentition

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-Dentition
    """

    artificial_dentition = CodeSystemConcept(
        {
            "code": "ArtificialDentition",
            "concept": [
                {
                    "code": "TID10a",
                    "definition": "Maxillary left lateral incisor abutment",
                    "display": "10a",
                },
                {
                    "code": "TID10i",
                    "definition": "Maxillary left lateral incisor implant",
                    "display": "10i",
                },
                {
                    "code": "TID10p",
                    "definition": "Maxillary left lateral incisor prosthesis",
                    "display": "10p",
                },
                {
                    "code": "TID10pd",
                    "definition": "Maxillary left lateral incisor distal prosthesis",
                    "display": "10pd",
                },
                {
                    "code": "TID10pm",
                    "definition": "Maxillary left lateral incisor mesial prosthesis",
                    "display": "10pm",
                },
                {
                    "code": "TID11a",
                    "definition": "Maxillary left canine abutment",
                    "display": "11a",
                },
                {
                    "code": "TID11i",
                    "definition": "Maxillary left canine implant",
                    "display": "11i",
                },
                {
                    "code": "TID11p",
                    "definition": "Maxillary left canine prosthesis",
                    "display": "11p",
                },
                {
                    "code": "TID11pd",
                    "definition": "Maxillary left canine distal prosthesis",
                    "display": "11pd",
                },
                {
                    "code": "TID11pm",
                    "definition": "Maxillary left canine mesial prosthesis",
                    "display": "11pm",
                },
                {
                    "code": "TID12a",
                    "definition": "Maxillary left first premolar abutment",
                    "display": "12a",
                },
                {
                    "code": "TID12i",
                    "definition": "Maxillary left first premolar implant",
                    "display": "12i",
                },
                {
                    "code": "TID12p",
                    "definition": "Maxillary left first premolar prosthesis",
                    "display": "12p",
                },
                {
                    "code": "TID12pd",
                    "definition": "Maxillary left first premolar distal prosthesis",
                    "display": "12pd",
                },
                {
                    "code": "TID12pm",
                    "definition": "Maxillary left first premolar mesial prosthesis",
                    "display": "12pm",
                },
                {
                    "code": "TID13a",
                    "definition": "Maxillary left second premolar abutment",
                    "display": "13a",
                },
                {
                    "code": "TID13i",
                    "definition": "Maxillary left second premolar implant",
                    "display": "13i",
                },
                {
                    "code": "TID13p",
                    "definition": "Maxillary left second premolar prosthesis",
                    "display": "13p",
                },
                {
                    "code": "TID13pd",
                    "definition": "Maxillary left second premolar distal prosthesis",
                    "display": "13pd",
                },
                {
                    "code": "TID13pm",
                    "definition": "Maxillary left second premolar mesial prosthesis",
                    "display": "13pm",
                },
                {
                    "code": "TID14a",
                    "definition": "Maxillary left first molar abutment",
                    "display": "14a",
                },
                {
                    "code": "TID14i",
                    "definition": "Maxillary left first molar implant",
                    "display": "14i",
                },
                {
                    "code": "TID14p",
                    "definition": "Maxillary left first molar prosthesis",
                    "display": "14p",
                },
                {
                    "code": "TID14pd",
                    "definition": "Maxillary left first molar distal prosthesis",
                    "display": "14pd",
                },
                {
                    "code": "TID14pm",
                    "definition": "Maxillary left first molar mesial prosthesis",
                    "display": "14pm",
                },
                {
                    "code": "TID15a",
                    "definition": "Maxillary left second molar abutment",
                    "display": "15a",
                },
                {
                    "code": "TID15i",
                    "definition": "Maxillary left second molar implant",
                    "display": "15i",
                },
                {
                    "code": "TID15p",
                    "definition": "Maxillary left second molar prosthesis",
                    "display": "15p",
                },
                {
                    "code": "TID15pd",
                    "definition": "Maxillary left second molar distal prosthesis",
                    "display": "15pd",
                },
                {
                    "code": "TID15pm",
                    "definition": "Maxillary left second molar mesial prosthesis",
                    "display": "15pm",
                },
                {
                    "code": "TID16a",
                    "definition": "Maxillary left third molar abutment",
                    "display": "16a",
                },
                {
                    "code": "TID16i",
                    "definition": "Maxillary left third molar implant",
                    "display": "16i",
                },
                {
                    "code": "TID16p",
                    "definition": "Maxillary left third molar prosthesis",
                    "display": "16p",
                },
                {
                    "code": "TID16pd",
                    "definition": "Maxillary left third molar distal prosthesis",
                    "display": "16pd",
                },
                {
                    "code": "TID16pm",
                    "definition": "Maxillary left third molar mesial prosthesis",
                    "display": "16pm",
                },
                {
                    "code": "TID17a",
                    "definition": "Mandibular left third molar abutment",
                    "display": "17a",
                },
                {
                    "code": "TID17ad",
                    "definition": "Mandibular left third molar abutment distal hemisection",
                    "display": "17ad",
                },
                {
                    "code": "TID17am",
                    "definition": "Mandibular left third molar abutment mesial hemisection",
                    "display": "17am",
                },
                {
                    "code": "TID17i",
                    "definition": "Mandibular left third molar implant",
                    "display": "17i",
                },
                {
                    "code": "TID17id",
                    "definition": "Mandibular left third molar implant distal hemisection",
                    "display": "17id",
                },
                {
                    "code": "TID17im",
                    "definition": "Mandibular left third molar implant mesial hemisection",
                    "display": "17im",
                },
                {
                    "code": "TID17p",
                    "definition": "Mandibular left third molar prosthesis",
                    "display": "17p",
                },
                {
                    "code": "TID17pd",
                    "definition": "Mandibular left third molar distal prosthesis",
                    "display": "17pd",
                },
                {
                    "code": "TID17pm",
                    "definition": "Mandibular left third molar mesial prosthesis",
                    "display": "17pm",
                },
                {
                    "code": "TID18a",
                    "definition": "Mandibular left second molar abutment",
                    "display": "18a",
                },
                {
                    "code": "TID18ad",
                    "definition": "Mandibular left second molar abutment distal hemisection",
                    "display": "18ad",
                },
                {
                    "code": "TID18am",
                    "definition": "Mandibular left second molar abutment mesial hemisection",
                    "display": "18am",
                },
                {
                    "code": "TID18i",
                    "definition": "Mandibular left second molar implant",
                    "display": "18i",
                },
                {
                    "code": "TID18id",
                    "definition": "Mandibular left second molar implant distal hemisection",
                    "display": "18id",
                },
                {
                    "code": "TID18im",
                    "definition": "Mandibular left second molar implant mesial hemisection",
                    "display": "18im",
                },
                {
                    "code": "TID18p",
                    "definition": "Mandibular left second molar prosthesis",
                    "display": "18p",
                },
                {
                    "code": "TID18pd",
                    "definition": "Mandibular left second molar distal prosthesis",
                    "display": "18pd",
                },
                {
                    "code": "TID18pm",
                    "definition": "Mandibular left second molar mesial prosthesis",
                    "display": "18pm",
                },
                {
                    "code": "TID19a",
                    "definition": "Mandibular left first molar abutment",
                    "display": "19a",
                },
                {
                    "code": "TID19ad",
                    "definition": "Mandibular left first molar abutment distal hemisection",
                    "display": "19ad",
                },
                {
                    "code": "TID19am",
                    "definition": "Mandibular left first molar abutment mesial hemisection",
                    "display": "19am",
                },
                {
                    "code": "TID19i",
                    "definition": "Mandibular left first molar implant",
                    "display": "19i",
                },
                {
                    "code": "TID19id",
                    "definition": "Mandibular left first molar implant distal hemisection",
                    "display": "19id",
                },
                {
                    "code": "TID19im",
                    "definition": "Mandibular left first molar implant mesial hemisection",
                    "display": "19im",
                },
                {
                    "code": "TID19p",
                    "definition": "Mandibular left first molar prosthesis",
                    "display": "19p",
                },
                {
                    "code": "TID19pd",
                    "definition": "Mandibular left first molar distal prosthesis",
                    "display": "19pd",
                },
                {
                    "code": "TID19pm",
                    "definition": "Mandibular left first molar mesial prosthesis",
                    "display": "19pm",
                },
                {
                    "code": "TID1a",
                    "definition": "Maxillary right third molar abutment",
                    "display": "1a",
                },
                {
                    "code": "TID1i",
                    "definition": "Maxillary right third molar implant",
                    "display": "1i",
                },
                {
                    "code": "TID1p",
                    "definition": "Maxillary right third molar prosthesis",
                    "display": "1p",
                },
                {
                    "code": "TID1pd",
                    "definition": "Maxillary right third molar distal prosthesis",
                    "display": "1pd",
                },
                {
                    "code": "TID1pm",
                    "definition": "Maxillary right third molar mesial prosthesis",
                    "display": "1pm",
                },
                {
                    "code": "TID20a",
                    "definition": "Mandibular left second premolar abutment",
                    "display": "20a",
                },
                {
                    "code": "TID20i",
                    "definition": "Mandibular left second premolar implant",
                    "display": "20i",
                },
                {
                    "code": "TID20p",
                    "definition": "Mandibular left second premolar prosthesis",
                    "display": "20p",
                },
                {
                    "code": "TID20pd",
                    "definition": "Mandibular left second premolar distal prosthesis",
                    "display": "20pd",
                },
                {
                    "code": "TID20pm",
                    "definition": "Mandibular left second premolar mesial prosthesis",
                    "display": "20pm",
                },
                {
                    "code": "TID21a",
                    "definition": "Mandibular left first premolar abutment",
                    "display": "21a",
                },
                {
                    "code": "TID21i",
                    "definition": "Mandibular left first premolar implant",
                    "display": "21i",
                },
                {
                    "code": "TID21p",
                    "definition": "Mandibular left first premolar prosthesis",
                    "display": "21p",
                },
                {
                    "code": "TID21pd",
                    "definition": "Mandibular left first premolar distal prosthesis",
                    "display": "21pd",
                },
                {
                    "code": "TID21pm",
                    "definition": "Mandibular left first premolar mesial prosthesis",
                    "display": "21pm",
                },
                {
                    "code": "TID22a",
                    "definition": "Mandibular left canine abutment",
                    "display": "22a",
                },
                {
                    "code": "TID22i",
                    "definition": "Mandibular left canine implant",
                    "display": "22i",
                },
                {
                    "code": "TID22p",
                    "definition": "Mandibular left canine prosthesis",
                    "display": "22p",
                },
                {
                    "code": "TID22pd",
                    "definition": "Mandibular left canine distal prosthesis",
                    "display": "22pd",
                },
                {
                    "code": "TID22pm",
                    "definition": "Mandibular left canine mesial prosthesis",
                    "display": "22pm",
                },
                {
                    "code": "TID23a",
                    "definition": "Mandibular left lateral incisor abutment",
                    "display": "23a",
                },
                {
                    "code": "TID23i",
                    "definition": "Mandibular left lateral incisor implant",
                    "display": "23i",
                },
                {
                    "code": "TID23p",
                    "definition": "Mandibular left lateral incisor prosthesis",
                    "display": "23p",
                },
                {
                    "code": "TID23pd",
                    "definition": "Mandibular left lateral incisor distal prosthesis",
                    "display": "23pd",
                },
                {
                    "code": "TID23pm",
                    "definition": "Mandibular left lateral incisor mesial prosthesis",
                    "display": "23pm",
                },
                {
                    "code": "TID24a",
                    "definition": "Mandibular left central incisor abutment",
                    "display": "24a",
                },
                {
                    "code": "TID24i",
                    "definition": "Mandibular left central incisor implant",
                    "display": "24i",
                },
                {
                    "code": "TID24p",
                    "definition": "Mandibular left central incisor prosthesis",
                    "display": "24p",
                },
                {
                    "code": "TID24pd",
                    "definition": "Mandibular left central incisor distal prosthesis",
                    "display": "24pd",
                },
                {
                    "code": "TID24pm",
                    "definition": "Mandibular left central incisor mesial prosthesis",
                    "display": "24pm",
                },
                {
                    "code": "TID25a",
                    "definition": "Mandibular right central incisor abutment",
                    "display": "25a",
                },
                {
                    "code": "TID25i",
                    "definition": "Mandibular right central incisor implant",
                    "display": "25i",
                },
                {
                    "code": "TID25p",
                    "definition": "Mandibular right central incisor prosthesis",
                    "display": "25p",
                },
                {
                    "code": "TID25pd",
                    "definition": "Mandibular right central incisor distal prosthesis",
                    "display": "25pd",
                },
                {
                    "code": "TID25pm",
                    "definition": "Mandibular right central incisor mesial prosthesis",
                    "display": "25pm",
                },
                {
                    "code": "TID26a",
                    "definition": "Mandibular right lateral incisor abutment",
                    "display": "26a",
                },
                {
                    "code": "TID26i",
                    "definition": "Mandibular right lateral incisor implant",
                    "display": "26i",
                },
                {
                    "code": "TID26p",
                    "definition": "Mandibular right lateral incisor prosthesis",
                    "display": "26p",
                },
                {
                    "code": "TID26pd",
                    "definition": "Mandibular right lateral incisor distal prosthesis",
                    "display": "26pd",
                },
                {
                    "code": "TID26pm",
                    "definition": "Mandibular right lateral incisor mesial prosthesis",
                    "display": "26pm",
                },
                {
                    "code": "TID27a",
                    "definition": "Mandibular right canine abutment",
                    "display": "27a",
                },
                {
                    "code": "TID27i",
                    "definition": "Mandibular right canine implant",
                    "display": "27i",
                },
                {
                    "code": "TID27p",
                    "definition": "Mandibular right canine prosthesis",
                    "display": "27p",
                },
                {
                    "code": "TID27pd",
                    "definition": "Mandibular right canine distal prosthesis",
                    "display": "27pd",
                },
                {
                    "code": "TID27pm",
                    "definition": "Mandibular right canine mesial prosthesis",
                    "display": "27pm",
                },
                {
                    "code": "TID28a",
                    "definition": "Mandibular right first premolar abutment",
                    "display": "28a",
                },
                {
                    "code": "TID28i",
                    "definition": "Mandibular right first premolar implant",
                    "display": "28i",
                },
                {
                    "code": "TID28p",
                    "definition": "Mandibular right first premolar prosthesis",
                    "display": "28p",
                },
                {
                    "code": "TID28pd",
                    "definition": "Mandibular right first premolar distal prosthesis",
                    "display": "28pd",
                },
                {
                    "code": "TID28pm",
                    "definition": "Mandibular right first premolar mesial prosthesis",
                    "display": "28pm",
                },
                {
                    "code": "TID29a",
                    "definition": "Mandibular right second premolar abutment",
                    "display": "29a",
                },
                {
                    "code": "TID29i",
                    "definition": "Mandibular right second premolar implant",
                    "display": "29i",
                },
                {
                    "code": "TID29p",
                    "definition": "Mandibular right second premolar prosthesis",
                    "display": "29p",
                },
                {
                    "code": "TID29pd",
                    "definition": "Mandibular right second premolar distal prosthesis",
                    "display": "29pd",
                },
                {
                    "code": "TID29pm",
                    "definition": "Mandibular right second premolar mesial prosthesis",
                    "display": "29pm",
                },
                {
                    "code": "TID2a",
                    "definition": "Maxillary right second molar abutment",
                    "display": "2a",
                },
                {
                    "code": "TID2i",
                    "definition": "Maxillary right second molar implant",
                    "display": "2i",
                },
                {
                    "code": "TID2p",
                    "definition": "Maxillary right second molar prosthesis",
                    "display": "2p",
                },
                {
                    "code": "TID2pd",
                    "definition": "Maxillary right second molar distal prosthesis",
                    "display": "2pd",
                },
                {
                    "code": "TID2pm",
                    "definition": "Maxillary right second molar mesial prosthesis",
                    "display": "2pm",
                },
                {
                    "code": "TID30a",
                    "definition": "Mandibular right first molar abutment",
                    "display": "30a",
                },
                {
                    "code": "TID30ad",
                    "definition": "Mandibular right first molar abutment distal hemisection",
                    "display": "30ad",
                },
                {
                    "code": "TID30am",
                    "definition": "Mandibular right first molar abutment mesial hemisection",
                    "display": "30am",
                },
                {
                    "code": "TID30i",
                    "definition": "Mandibular right first molar implant",
                    "display": "30i",
                },
                {
                    "code": "TID30id",
                    "definition": "Mandibular right first molar implant distal hemisection",
                    "display": "30id",
                },
                {
                    "code": "TID30im",
                    "definition": "Mandibular right first molar implant mesial hemisection",
                    "display": "30im",
                },
                {
                    "code": "TID30p",
                    "definition": "Mandibular right first molar prosthesis",
                    "display": "30p",
                },
                {
                    "code": "TID30pd",
                    "definition": "Mandibular right first molar distal prosthesis",
                    "display": "30pd",
                },
                {
                    "code": "TID30pm",
                    "definition": "Mandibular right first molar mesial prosthesis",
                    "display": "30pm",
                },
                {
                    "code": "TID31a",
                    "definition": "Mandibular right second molar abutment",
                    "display": "31a",
                },
                {
                    "code": "TID31ad",
                    "definition": "Mandibular right second molar abutment distal hemisection",
                    "display": "31ad",
                },
                {
                    "code": "TID31am",
                    "definition": "Mandibular right second molar abutment mesial hemisection",
                    "display": "31am",
                },
                {
                    "code": "TID31i",
                    "definition": "Mandibular right second molar implant",
                    "display": "31i",
                },
                {
                    "code": "TID31id",
                    "definition": "Mandibular right second molar implant distal hemisection",
                    "display": "31id",
                },
                {
                    "code": "TID31im",
                    "definition": "Mandibular right second molar implant mesial hemisection",
                    "display": "31im",
                },
                {
                    "code": "TID31p",
                    "definition": "Mandibular right second molar prosthesis",
                    "display": "31p",
                },
                {
                    "code": "TID31pd",
                    "definition": "Mandibular right second molar distal prosthesis",
                    "display": "31pd",
                },
                {
                    "code": "TID31pm",
                    "definition": "Mandibular right second molar mesial prosthesis",
                    "display": "31pm",
                },
                {
                    "code": "TID32a",
                    "definition": "Mandibular right third molar abutment",
                    "display": "32a",
                },
                {
                    "code": "TID32ad",
                    "definition": "Mandibular right third molar abutment distal hemisection",
                    "display": "32ad",
                },
                {
                    "code": "TID32am",
                    "definition": "Mandibular right third molar abutment mesial hemisection",
                    "display": "32am",
                },
                {
                    "code": "TID32i",
                    "definition": "Mandibular right third molar implant",
                    "display": "32i",
                },
                {
                    "code": "TID32id",
                    "definition": "Mandibular right third molar implant distal hemisection",
                    "display": "32id",
                },
                {
                    "code": "TID32im",
                    "definition": "Mandibular right third molar implant mesial hemisection",
                    "display": "32im",
                },
                {
                    "code": "TID32p",
                    "definition": "Mandibular right third molar prosthesis",
                    "display": "32p",
                },
                {
                    "code": "TID32pd",
                    "definition": "Mandibular right third molar distal prosthesis",
                    "display": "32pd",
                },
                {
                    "code": "TID32pm",
                    "definition": "Mandibular right third molar mesial prosthesis",
                    "display": "32pm",
                },
                {
                    "code": "TID3a",
                    "definition": "Maxillary right first molar abutment",
                    "display": "3a",
                },
                {
                    "code": "TID3i",
                    "definition": "Maxillary right first molar implant",
                    "display": "3i",
                },
                {
                    "code": "TID3p",
                    "definition": "Maxillary right first molar prosthesis",
                    "display": "3p",
                },
                {
                    "code": "TID3pd",
                    "definition": "Maxillary right first molar distal prosthesis",
                    "display": "3pd",
                },
                {
                    "code": "TID3pm",
                    "definition": "Maxillary right first molar mesial prosthesis",
                    "display": "3pm",
                },
                {
                    "code": "TID4a",
                    "definition": "Maxillary right second premolar abutment",
                    "display": "4a",
                },
                {
                    "code": "TID4i",
                    "definition": "Maxillary right second premolar implant",
                    "display": "4i",
                },
                {
                    "code": "TID4p",
                    "definition": "Maxillary right second premolar prosthesis",
                    "display": "4p",
                },
                {
                    "code": "TID4pd",
                    "definition": "Maxillary right second premolar distal prosthesis",
                    "display": "4pd",
                },
                {
                    "code": "TID4pm",
                    "definition": "Maxillary right second premolar mesial prosthesis",
                    "display": "4pm",
                },
                {
                    "code": "TID5a",
                    "definition": "Maxillary right first premolar abutment",
                    "display": "5a",
                },
                {
                    "code": "TID5i",
                    "definition": "Maxillary right first premolar implant",
                    "display": "5i",
                },
                {
                    "code": "TID5p",
                    "definition": "Maxillary right first premolar prosthesis",
                    "display": "5p",
                },
                {
                    "code": "TID5pd",
                    "definition": "Maxillary right first premolar distal prosthesis",
                    "display": "5pd",
                },
                {
                    "code": "TID5pm",
                    "definition": "Maxillary right first premolar mesial prosthesis",
                    "display": "5pm",
                },
                {
                    "code": "TID6a",
                    "definition": "Maxillary right canine abutment",
                    "display": "6a",
                },
                {
                    "code": "TID6i",
                    "definition": "Maxillary right canine implant",
                    "display": "6i",
                },
                {
                    "code": "TID6p",
                    "definition": "Maxillary right canine prosthesis",
                    "display": "6p",
                },
                {
                    "code": "TID6pd",
                    "definition": "Maxillary right canine distal prosthesis",
                    "display": "6pd",
                },
                {
                    "code": "TID6pm",
                    "definition": "Maxillary right canine mesial prosthesis",
                    "display": "6pm",
                },
                {
                    "code": "TID7a",
                    "definition": "Maxillary right lateral incisor abutment",
                    "display": "7a",
                },
                {
                    "code": "TID7i",
                    "definition": "Maxillary right lateral incisor implant",
                    "display": "7i",
                },
                {
                    "code": "TID7p",
                    "definition": "Maxillary right lateral incisor prosthesis",
                    "display": "7p",
                },
                {
                    "code": "TID7pd",
                    "definition": "Maxillary right lateral incisor distal prosthesis",
                    "display": "7pd",
                },
                {
                    "code": "TID7pm",
                    "definition": "Maxillary right lateral incisor mesial prosthesis",
                    "display": "7pm",
                },
                {
                    "code": "TID8a",
                    "definition": "Maxillary right central incisor abutment",
                    "display": "8a",
                },
                {
                    "code": "TID8i",
                    "definition": "Maxillary right central incisor implant",
                    "display": "8i",
                },
                {
                    "code": "TID8p",
                    "definition": "Maxillary right central incisor prosthesis",
                    "display": "8p",
                },
                {
                    "code": "TID8pd",
                    "definition": "Maxillary right central incisor distal prosthesis",
                    "display": "8pd",
                },
                {
                    "code": "TID8pm",
                    "definition": "Maxillary right central incisor mesial prosthesis",
                    "display": "8pm",
                },
                {
                    "code": "TID9a",
                    "definition": "Maxillary left central incisor abutment",
                    "display": "9a",
                },
                {
                    "code": "TID9i",
                    "definition": "Maxillary left central incisor implant",
                    "display": "9i",
                },
                {
                    "code": "TID9p",
                    "definition": "Maxillary left central incisor prosthesis",
                    "display": "9p",
                },
                {
                    "code": "TID9pd",
                    "definition": "Maxillary left central incisor distal prosthesis",
                    "display": "9pd",
                },
                {
                    "code": "TID9pm",
                    "definition": "Maxillary left central incisor mesial prosthesis",
                    "display": "9pm",
                },
            ],
            "definition": "Artificial dentition, artificial subsitutes for the natural dentition",
            "display": "Artificial dentition",
        }
    )
    """
    Artificial dentition

    Artificial dentition, artificial subsitutes for the natural dentition
    """

    permanent_dentition = CodeSystemConcept(
        {
            "code": "PermanentDentition",
            "concept": [
                {
                    "code": "TID1",
                    "definition": "Maxillary right third molar",
                    "display": "1",
                },
                {
                    "code": "TID10",
                    "definition": "Maxillary left lateral incisor",
                    "display": "10",
                },
                {
                    "code": "TID11",
                    "definition": "Maxillary left canine",
                    "display": "11",
                },
                {
                    "code": "TID12",
                    "definition": "Maxillary left first premolar",
                    "display": "12",
                },
                {
                    "code": "TID13",
                    "definition": "Maxillary left second premolar",
                    "display": "13",
                },
                {
                    "code": "TID14",
                    "definition": "Maxillary left first molar",
                    "display": "14",
                },
                {
                    "code": "TID15",
                    "definition": "Maxillary left second molar",
                    "display": "15",
                },
                {
                    "code": "TID16",
                    "definition": "Maxillary left third molar",
                    "display": "16",
                },
                {
                    "code": "TID17",
                    "definition": "Mandibular left third molar",
                    "display": "17",
                },
                {
                    "code": "TID17d",
                    "definition": "Mandibular left third molar distal hemisection",
                    "display": "17d",
                },
                {
                    "code": "TID17m",
                    "definition": "Mandibular left third molar mesial hemisection",
                    "display": "17m",
                },
                {
                    "code": "TID18",
                    "definition": "Mandibular left second molar",
                    "display": "18",
                },
                {
                    "code": "TID18d",
                    "definition": "Mandibular left second molar distal hemisection",
                    "display": "18d",
                },
                {
                    "code": "TID18m",
                    "definition": "Mandibular left second molar mesial hemisection",
                    "display": "18m",
                },
                {
                    "code": "TID19",
                    "definition": "Mandibular left first molar",
                    "display": "19",
                },
                {
                    "code": "TID19d",
                    "definition": "Mandibular left first molar distal hemisection",
                    "display": "19d",
                },
                {
                    "code": "TID19m",
                    "definition": "Mandibular left first molar mesial hemisection",
                    "display": "19m",
                },
                {
                    "code": "TID2",
                    "definition": "Maxillary right second molar",
                    "display": "2",
                },
                {
                    "code": "TID20",
                    "definition": "Mandibular left second premolar",
                    "display": "20",
                },
                {
                    "code": "TID21",
                    "definition": "Mandibular left first premolar",
                    "display": "21",
                },
                {
                    "code": "TID22",
                    "definition": "Mandibular left canine",
                    "display": "22",
                },
                {
                    "code": "TID23",
                    "definition": "Mandibular left lateral incisor",
                    "display": "23",
                },
                {
                    "code": "TID24",
                    "definition": "Mandibular left central incisor",
                    "display": "24",
                },
                {
                    "code": "TID25",
                    "definition": "Mandibular right central incisor",
                    "display": "25",
                },
                {
                    "code": "TID26",
                    "definition": "Mandibular right lateral incisor",
                    "display": "26",
                },
                {
                    "code": "TID27",
                    "definition": "Mandibular right canine",
                    "display": "27",
                },
                {
                    "code": "TID28",
                    "definition": "Mandibular right first premolar",
                    "display": "28",
                },
                {
                    "code": "TID29",
                    "definition": "Mandibular right second premolar",
                    "display": "29",
                },
                {
                    "code": "TID3",
                    "definition": "Maxillary right first molar",
                    "display": "3",
                },
                {
                    "code": "TID30",
                    "definition": "Mandibular right first molar",
                    "display": "30",
                },
                {
                    "code": "TID30d",
                    "definition": "Mandibular right first molar distal hemisection",
                    "display": "30d",
                },
                {
                    "code": "TID30m",
                    "definition": "Mandibular right first molar mesial hemisection",
                    "display": "30m",
                },
                {
                    "code": "TID31",
                    "definition": "Mandibular right second molar",
                    "display": "31",
                },
                {
                    "code": "TID31d",
                    "definition": "Mandibular right second molar distal hemisection",
                    "display": "31d",
                },
                {
                    "code": "TID31m",
                    "definition": "Mandibular right second molar mesial hemisection",
                    "display": "31m",
                },
                {
                    "code": "TID32",
                    "definition": "Mandibular right third molar",
                    "display": "32",
                },
                {
                    "code": "TID32d",
                    "definition": "Mandibular right third molar distal hemisection",
                    "display": "32d",
                },
                {
                    "code": "TID32m",
                    "definition": "Mandibular right third molar mesial hemisection",
                    "display": "32m",
                },
                {
                    "code": "TID4",
                    "definition": "Maxillary right second premolar",
                    "display": "4",
                },
                {
                    "code": "TID5",
                    "definition": "Maxillary right first premolar",
                    "display": "5",
                },
                {
                    "code": "TID6",
                    "definition": "Maxillary right canine",
                    "display": "6",
                },
                {
                    "code": "TID7",
                    "definition": "Maxillary right lateral incisor",
                    "display": "7",
                },
                {
                    "code": "TID8",
                    "definition": "Maxillary right central incisor",
                    "display": "8",
                },
                {
                    "code": "TID9",
                    "definition": "Maxillary left central incisor",
                    "display": "9",
                },
            ],
            "definition": "Permanent dentition, the natural teeth of adulthood that replace or are added to the deciduous teeth",
            "display": "Permanent dentition",
        }
    )
    """
    Permanent dentition

    Permanent dentition, the natural teeth of adulthood that replace or are added to the deciduous teeth
    """

    primary_dentition = CodeSystemConcept(
        {
            "code": "PrimaryDentition",
            "concept": [
                {
                    "code": "TIDA",
                    "definition": "Maxillary right second primary molar",
                    "display": "A",
                },
                {
                    "code": "TIDB",
                    "definition": "Maxillary right first primary molar",
                    "display": "B",
                },
                {
                    "code": "TIDC",
                    "definition": "Maxillary right primary canine",
                    "display": "C",
                },
                {
                    "code": "TIDD",
                    "definition": "Maxillary right lateral primary incisor",
                    "display": "D",
                },
                {
                    "code": "TIDE",
                    "definition": "Maxillary right central primary incisor",
                    "display": "E",
                },
                {
                    "code": "TIDF",
                    "definition": "Maxillary left central primary incisor",
                    "display": "F",
                },
                {
                    "code": "TIDG",
                    "definition": "Maxillary left lateral primary incisor",
                    "display": "G",
                },
                {
                    "code": "TIDH",
                    "definition": "Maxillary left primary canine",
                    "display": "H",
                },
                {
                    "code": "TIDI",
                    "definition": "Maxillary left first primary molar",
                    "display": "I",
                },
                {
                    "code": "TIDJ",
                    "definition": "Maxillary left second primary molar",
                    "display": "J",
                },
                {
                    "code": "TIDK",
                    "definition": "Mandibular left second primary molar",
                    "display": "K",
                },
                {
                    "code": "TIDL",
                    "definition": "Mandibular left first primary molar",
                    "display": "L",
                },
                {
                    "code": "TIDM",
                    "definition": "Mandibular left primary canine",
                    "display": "M",
                },
                {
                    "code": "TIDN",
                    "definition": "Mandibular left lateral primary incisor",
                    "display": "N",
                },
                {
                    "code": "TIDO",
                    "definition": "Mandibular left central primary incisor",
                    "display": "O",
                },
                {
                    "code": "TIDP",
                    "definition": "Mandibular right central primary incisor",
                    "display": "P",
                },
                {
                    "code": "TIDQ",
                    "definition": "Mandibular right lateral primary incisor",
                    "display": "Q",
                },
                {
                    "code": "TIDR",
                    "definition": "Mandibular right primary canine",
                    "display": "R",
                },
                {
                    "code": "TIDS",
                    "definition": "Mandibular right first primary molar",
                    "display": "S",
                },
                {
                    "code": "TIDT",
                    "definition": "Mandibular right second primary molar",
                    "display": "T",
                },
            ],
            "definition": "Primary dentition, the first teeth to errupt and usually replaced with permanent dentition",
            "display": "Primary dentition",
        }
    )
    """
    Primary dentition

    Primary dentition, the first teeth to errupt and usually replaced with permanent dentition
    """

    supernumerary_tooth = CodeSystemConcept(
        {
            "code": "SupernumeraryTooth",
            "concept": [
                {
                    "code": "TID10s",
                    "definition": "Supernumerary maxillary left lateral incisor",
                    "display": "10s",
                },
                {
                    "code": "TID11s",
                    "definition": "Supernumerary maxillary left canine",
                    "display": "11s",
                },
                {
                    "code": "TID12s",
                    "definition": "Supernumerary maxillary left first premolar",
                    "display": "12s",
                },
                {
                    "code": "TID13s",
                    "definition": "Supernumerary maxillary left second premolar",
                    "display": "13s",
                },
                {
                    "code": "TID14s",
                    "definition": "Supernumerary maxillary left first molar",
                    "display": "14s",
                },
                {
                    "code": "TID15s",
                    "definition": "Supernumerary maxillary left second molar",
                    "display": "15s",
                },
                {
                    "code": "TID16s",
                    "definition": "Supernumerary maxillary left third molar",
                    "display": "16s",
                },
                {
                    "code": "TID17s",
                    "definition": "Supernumerary mandibular left third molar",
                    "display": "17s",
                },
                {
                    "code": "TID18s",
                    "definition": "Supernumerary mandibular left second molar",
                    "display": "18s",
                },
                {
                    "code": "TID19s",
                    "definition": "Supernumerary mandibular left first molar",
                    "display": "19s",
                },
                {
                    "code": "TID1s",
                    "definition": "Supernumerary maxillary right third molar",
                    "display": "1s",
                },
                {
                    "code": "TID20s",
                    "definition": "Supernumerary mandibular left second premolar",
                    "display": "20s",
                },
                {
                    "code": "TID21s",
                    "definition": "Supernumerary mandibular left first premolar",
                    "display": "21s",
                },
                {
                    "code": "TID22s",
                    "definition": "Supernumerary mandibular left canine",
                    "display": "22s",
                },
                {
                    "code": "TID23s",
                    "definition": "Supernumerary mandibular left lateral incisor",
                    "display": "23s",
                },
                {
                    "code": "TID24s",
                    "definition": "Supernumerary mandibular left central incisor",
                    "display": "24s",
                },
                {
                    "code": "TID25s",
                    "definition": "Supernumerary mandibular right central incisor",
                    "display": "25s",
                },
                {
                    "code": "TID26s",
                    "definition": "Supernumerary mandibular right lateral incisor",
                    "display": "26s",
                },
                {
                    "code": "TID27s",
                    "definition": "Supernumerary mandibular right canine",
                    "display": "27s",
                },
                {
                    "code": "TID28s",
                    "definition": "Supernumerary mandibular right first premolar",
                    "display": "28s",
                },
                {
                    "code": "TID29s",
                    "definition": "Supernumerary mandibular right second premolar",
                    "display": "29s",
                },
                {
                    "code": "TID2s",
                    "definition": "Supernumerary maxillary right second molar",
                    "display": "2s",
                },
                {
                    "code": "TID30s",
                    "definition": "Supernumerary mandibular right first molar",
                    "display": "30s",
                },
                {
                    "code": "TID31s",
                    "definition": "Supernumerary mandibular right second molar",
                    "display": "31s",
                },
                {
                    "code": "TID32s",
                    "definition": "Supernumerary mandibular right third molar",
                    "display": "32s",
                },
                {
                    "code": "TID3s",
                    "definition": "Supernumerary maxillary right first molar",
                    "display": "3s",
                },
                {
                    "code": "TID4s",
                    "definition": "Supernumerary maxillary right second premolar",
                    "display": "4s",
                },
                {
                    "code": "TID5s",
                    "definition": "Supernumerary maxillary right first premolar",
                    "display": "5s",
                },
                {
                    "code": "TID6s",
                    "definition": "Supernumerary maxillary right canine",
                    "display": "6s",
                },
                {
                    "code": "TID7s",
                    "definition": "Supernumerary maxillary right lateral incisor",
                    "display": "7s",
                },
                {
                    "code": "TID8s",
                    "definition": "Supernumerary maxillary right central incisor",
                    "display": "8s",
                },
                {
                    "code": "TID9s",
                    "definition": "Supernumerary maxillary left central incisor",
                    "display": "9s",
                },
                {
                    "code": "TIDAs",
                    "definition": "Supernumerary maxillary right second primary molar",
                    "display": "As",
                },
                {
                    "code": "TIDBs",
                    "definition": "Supernumerary maxillary right first primary molar",
                    "display": "Bs",
                },
                {
                    "code": "TIDCs",
                    "definition": "Supernumerary maxillary right primary canine",
                    "display": "Cs",
                },
                {
                    "code": "TIDDs",
                    "definition": "Supernumerary maxillary right lateral primary incisor",
                    "display": "Ds",
                },
                {
                    "code": "TIDEs",
                    "definition": "Supernumerary maxillary right central primary incisor",
                    "display": "Es",
                },
                {
                    "code": "TIDFs",
                    "definition": "Supernumerary maxillary left central primary incisor",
                    "display": "Fs",
                },
                {
                    "code": "TIDGs",
                    "definition": "Supernumerary maxillary left lateral primary incisor",
                    "display": "Gs",
                },
                {
                    "code": "TIDHs",
                    "definition": "Supernumerary maxillary left primary canine",
                    "display": "Hs",
                },
                {
                    "code": "TIDIs",
                    "definition": "Supernumerary maxillary left first primary molar",
                    "display": "Is",
                },
                {
                    "code": "TIDJs",
                    "definition": "Supernumerary maxillary left second primary molar",
                    "display": "Js",
                },
                {
                    "code": "TIDKs",
                    "definition": "Supernumerary mandibular left second primary molar",
                    "display": "Ks",
                },
                {
                    "code": "TIDLs",
                    "definition": "Supernumerary mandibular left first primary molar",
                    "display": "Ls",
                },
                {
                    "code": "TIDMs",
                    "definition": "Supernumerary mandibular left primary canine",
                    "display": "Ms",
                },
                {
                    "code": "TIDNs",
                    "definition": "Supernumerary mandibular left lateral primary incisor",
                    "display": "Ns",
                },
                {
                    "code": "TIDOs",
                    "definition": "Supernumerary mandibular left central primary incisor",
                    "display": "Os",
                },
                {
                    "code": "TIDPs",
                    "definition": "Supernumerary mandibular right central primary incisor",
                    "display": "Ps",
                },
                {
                    "code": "TIDQs",
                    "definition": "Supernumerary mandibular right lateral primary incisor",
                    "display": "Qs",
                },
                {
                    "code": "TIDRs",
                    "definition": "Supernumerary mandibular right primary canine",
                    "display": "Rs",
                },
                {
                    "code": "TIDSs",
                    "definition": "Supernumerary mandibular right first primary molar",
                    "display": "Ss",
                },
                {
                    "code": "TIDTs",
                    "definition": "Supernumerary mandibular right second primary molar",
                    "display": "Ts",
                },
            ],
            "definition": "Supernumerary tooth, any tooth in addition to the normal permanent and primary dentition",
            "display": "Supernumerary Tooth",
        }
    )
    """
    Supernumerary Tooth

    Supernumerary tooth, any tooth in addition to the normal permanent and primary dentition
    """

    class Meta:
        resource = _resource
