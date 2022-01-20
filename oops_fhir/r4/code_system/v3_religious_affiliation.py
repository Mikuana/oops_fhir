from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ReligiousAffiliation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ReligiousAffiliation:
    """
    v3 Code System ReligiousAffiliation

     Assigment of spiritual faith affiliation

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation
    """

    one001 = CodeSystemConcept(
        {"code": "1001", "definition": "Adventist", "display": "Adventist"}
    )
    """
    Adventist

    Adventist
    """

    one002 = CodeSystemConcept(
        {
            "code": "1002",
            "definition": "African Religions",
            "display": "African Religions",
        }
    )
    """
    African Religions

    African Religions
    """

    one003 = CodeSystemConcept(
        {
            "code": "1003",
            "definition": "Afro-Caribbean Religions",
            "display": "Afro-Caribbean Religions",
        }
    )
    """
    Afro-Caribbean Religions

    Afro-Caribbean Religions
    """

    one004 = CodeSystemConcept(
        {"code": "1004", "definition": "Agnosticism", "display": "Agnosticism"}
    )
    """
    Agnosticism

    Agnosticism
    """

    one005 = CodeSystemConcept(
        {"code": "1005", "definition": "Anglican", "display": "Anglican"}
    )
    """
    Anglican

    Anglican
    """

    one006 = CodeSystemConcept(
        {"code": "1006", "definition": "Animism", "display": "Animism"}
    )
    """
    Animism

    Animism
    """

    one007 = CodeSystemConcept(
        {"code": "1007", "definition": "Atheism", "display": "Atheism"}
    )
    """
    Atheism

    Atheism
    """

    one008 = CodeSystemConcept(
        {
            "code": "1008",
            "definition": "Babi & Baha'I faiths",
            "display": "Babi & Baha'I faiths",
        }
    )
    """
    Babi & Baha'I faiths

    Babi & Baha'I faiths
    """

    one009 = CodeSystemConcept(
        {"code": "1009", "definition": "Baptist", "display": "Baptist"}
    )
    """
    Baptist

    Baptist
    """

    one010 = CodeSystemConcept({"code": "1010", "definition": "Bon", "display": "Bon"})
    """
    Bon

    Bon
    """

    one011 = CodeSystemConcept(
        {"code": "1011", "definition": "Cao Dai", "display": "Cao Dai"}
    )
    """
    Cao Dai

    Cao Dai
    """

    one012 = CodeSystemConcept(
        {"code": "1012", "definition": "Celticism", "display": "Celticism"}
    )
    """
    Celticism

    Celticism
    """

    one013 = CodeSystemConcept(
        {
            "code": "1013",
            "definition": "Christian (non-Catholic, non-specific)",
            "display": "Christian (non-Catholic, non-specific)",
        }
    )
    """
    Christian (non-Catholic, non-specific)

    Christian (non-Catholic, non-specific)
    """

    one014 = CodeSystemConcept(
        {"code": "1014", "definition": "Confucianism", "display": "Confucianism"}
    )
    """
    Confucianism

    Confucianism
    """

    one015 = CodeSystemConcept(
        {
            "code": "1015",
            "definition": "Cyberculture Religions",
            "display": "Cyberculture Religions",
        }
    )
    """
    Cyberculture Religions

    Cyberculture Religions
    """

    one016 = CodeSystemConcept(
        {"code": "1016", "definition": "Divination", "display": "Divination"}
    )
    """
    Divination

    Divination
    """

    one017 = CodeSystemConcept(
        {"code": "1017", "definition": "Fourth Way", "display": "Fourth Way"}
    )
    """
    Fourth Way

    Fourth Way
    """

    one018 = CodeSystemConcept(
        {"code": "1018", "definition": "Free Daism", "display": "Free Daism"}
    )
    """
    Free Daism

    Free Daism
    """

    one019 = CodeSystemConcept(
        {"code": "1019", "definition": "Gnosis", "display": "Gnosis"}
    )
    """
    Gnosis

    Gnosis
    """

    one020 = CodeSystemConcept(
        {"code": "1020", "definition": "Hinduism", "display": "Hinduism"}
    )
    """
    Hinduism

    Hinduism
    """

    one021 = CodeSystemConcept(
        {"code": "1021", "definition": "Humanism", "display": "Humanism"}
    )
    """
    Humanism

    Humanism
    """

    one022 = CodeSystemConcept(
        {"code": "1022", "definition": "Independent", "display": "Independent"}
    )
    """
    Independent

    Independent
    """

    one023 = CodeSystemConcept(
        {"code": "1023", "definition": "Islam", "display": "Islam"}
    )
    """
    Islam

    Islam
    """

    one024 = CodeSystemConcept(
        {"code": "1024", "definition": "Jainism", "display": "Jainism"}
    )
    """
    Jainism

    Jainism
    """

    one025 = CodeSystemConcept(
        {
            "code": "1025",
            "definition": "Jehovah's Witnesses",
            "display": "Jehovah's Witnesses",
        }
    )
    """
    Jehovah's Witnesses

    Jehovah's Witnesses
    """

    one026 = CodeSystemConcept(
        {"code": "1026", "definition": "Judaism", "display": "Judaism"}
    )
    """
    Judaism

    Judaism
    """

    one027 = CodeSystemConcept(
        {
            "code": "1027",
            "definition": "Latter Day Saints",
            "display": "Latter Day Saints",
        }
    )
    """
    Latter Day Saints

    Latter Day Saints
    """

    one028 = CodeSystemConcept(
        {"code": "1028", "definition": "Lutheran", "display": "Lutheran"}
    )
    """
    Lutheran

    Lutheran
    """

    one029 = CodeSystemConcept(
        {"code": "1029", "definition": "Mahayana", "display": "Mahayana"}
    )
    """
    Mahayana

    Mahayana
    """

    one030 = CodeSystemConcept(
        {"code": "1030", "definition": "Meditation", "display": "Meditation"}
    )
    """
    Meditation

    Meditation
    """

    one031 = CodeSystemConcept(
        {
            "code": "1031",
            "definition": "Messianic Judaism",
            "display": "Messianic Judaism",
        }
    )
    """
    Messianic Judaism

    Messianic Judaism
    """

    one032 = CodeSystemConcept(
        {"code": "1032", "definition": "Mitraism", "display": "Mitraism"}
    )
    """
    Mitraism

    Mitraism
    """

    one033 = CodeSystemConcept(
        {"code": "1033", "definition": "New Age", "display": "New Age"}
    )
    """
    New Age

    New Age
    """

    one034 = CodeSystemConcept(
        {
            "code": "1034",
            "definition": "non-Roman Catholic",
            "display": "non-Roman Catholic",
        }
    )
    """
    non-Roman Catholic

    non-Roman Catholic
    """

    one035 = CodeSystemConcept(
        {"code": "1035", "definition": "Occult", "display": "Occult"}
    )
    """
    Occult

    Occult
    """

    one036 = CodeSystemConcept(
        {"code": "1036", "definition": "Orthodox", "display": "Orthodox"}
    )
    """
    Orthodox

    Orthodox
    """

    one037 = CodeSystemConcept(
        {"code": "1037", "definition": "Paganism", "display": "Paganism"}
    )
    """
    Paganism

    Paganism
    """

    one038 = CodeSystemConcept(
        {"code": "1038", "definition": "Pentecostal", "display": "Pentecostal"}
    )
    """
    Pentecostal

    Pentecostal
    """

    one039 = CodeSystemConcept(
        {"code": "1039", "definition": "Process, The", "display": "Process, The"}
    )
    """
    Process, The

    Process, The
    """

    one040 = CodeSystemConcept(
        {
            "code": "1040",
            "definition": "Reformed/Presbyterian",
            "display": "Reformed/Presbyterian",
        }
    )
    """
    Reformed/Presbyterian

    Reformed/Presbyterian
    """

    one041 = CodeSystemConcept(
        {
            "code": "1041",
            "definition": "Roman Catholic Church",
            "display": "Roman Catholic Church",
        }
    )
    """
    Roman Catholic Church

    Roman Catholic Church
    """

    one042 = CodeSystemConcept(
        {"code": "1042", "definition": "Satanism", "display": "Satanism"}
    )
    """
    Satanism

    Satanism
    """

    one043 = CodeSystemConcept(
        {"code": "1043", "definition": "Scientology", "display": "Scientology"}
    )
    """
    Scientology

    Scientology
    """

    one044 = CodeSystemConcept(
        {"code": "1044", "definition": "Shamanism", "display": "Shamanism"}
    )
    """
    Shamanism

    Shamanism
    """

    one045 = CodeSystemConcept(
        {"code": "1045", "definition": "Shiite (Islam)", "display": "Shiite (Islam)"}
    )
    """
    Shiite (Islam)

    Shiite (Islam)
    """

    one046 = CodeSystemConcept(
        {"code": "1046", "definition": "Shinto", "display": "Shinto"}
    )
    """
    Shinto

    Shinto
    """

    one047 = CodeSystemConcept(
        {"code": "1047", "definition": "Sikism", "display": "Sikism"}
    )
    """
    Sikism

    Sikism
    """

    one048 = CodeSystemConcept(
        {"code": "1048", "definition": "Spiritualism", "display": "Spiritualism"}
    )
    """
    Spiritualism

    Spiritualism
    """

    one049 = CodeSystemConcept(
        {"code": "1049", "definition": "Sunni (Islam)", "display": "Sunni (Islam)"}
    )
    """
    Sunni (Islam)

    Sunni (Islam)
    """

    one050 = CodeSystemConcept(
        {"code": "1050", "definition": "Taoism", "display": "Taoism"}
    )
    """
    Taoism

    Taoism
    """

    one051 = CodeSystemConcept(
        {"code": "1051", "definition": "Theravada", "display": "Theravada"}
    )
    """
    Theravada

    Theravada
    """

    one052 = CodeSystemConcept(
        {
            "code": "1052",
            "definition": "Unitarian-Universalism",
            "display": "Unitarian-Universalism",
        }
    )
    """
    Unitarian-Universalism

    Unitarian-Universalism
    """

    one053 = CodeSystemConcept(
        {
            "code": "1053",
            "definition": "Universal Life Church",
            "display": "Universal Life Church",
        }
    )
    """
    Universal Life Church

    Universal Life Church
    """

    one054 = CodeSystemConcept(
        {
            "code": "1054",
            "definition": "Vajrayana (Tibetan)",
            "display": "Vajrayana (Tibetan)",
        }
    )
    """
    Vajrayana (Tibetan)

    Vajrayana (Tibetan)
    """

    one055 = CodeSystemConcept(
        {"code": "1055", "definition": "Veda", "display": "Veda"}
    )
    """
    Veda

    Veda
    """

    one056 = CodeSystemConcept(
        {"code": "1056", "definition": "Voodoo", "display": "Voodoo"}
    )
    """
    Voodoo

    Voodoo
    """

    one057 = CodeSystemConcept(
        {"code": "1057", "definition": "Wicca", "display": "Wicca"}
    )
    """
    Wicca

    Wicca
    """

    one058 = CodeSystemConcept(
        {"code": "1058", "definition": "Yaohushua", "display": "Yaohushua"}
    )
    """
    Yaohushua

    Yaohushua
    """

    one059 = CodeSystemConcept(
        {"code": "1059", "definition": "Zen Buddhism", "display": "Zen Buddhism"}
    )
    """
    Zen Buddhism

    Zen Buddhism
    """

    one060 = CodeSystemConcept(
        {"code": "1060", "definition": "Zoroastrianism", "display": "Zoroastrianism"}
    )
    """
    Zoroastrianism

    Zoroastrianism
    """

    one061 = CodeSystemConcept(
        {"code": "1061", "definition": "Assembly of God", "display": "Assembly of God"}
    )
    """
    Assembly of God

    Assembly of God
    """

    one062 = CodeSystemConcept(
        {"code": "1062", "definition": "Brethren", "display": "Brethren"}
    )
    """
    Brethren

    Brethren
    """

    one063 = CodeSystemConcept(
        {
            "code": "1063",
            "definition": "Christian Scientist",
            "display": "Christian Scientist",
        }
    )
    """
    Christian Scientist

    Christian Scientist
    """

    one064 = CodeSystemConcept(
        {
            "code": "1064",
            "definition": "Church of Christ",
            "display": "Church of Christ",
        }
    )
    """
    Church of Christ

    Church of Christ
    """

    one065 = CodeSystemConcept(
        {"code": "1065", "definition": "Church of God", "display": "Church of God"}
    )
    """
    Church of God

    Church of God
    """

    one066 = CodeSystemConcept(
        {"code": "1066", "definition": "Congregational", "display": "Congregational"}
    )
    """
    Congregational

    Congregational
    """

    one067 = CodeSystemConcept(
        {
            "code": "1067",
            "definition": "Disciples of Christ",
            "display": "Disciples of Christ",
        }
    )
    """
    Disciples of Christ

    Disciples of Christ
    """

    one068 = CodeSystemConcept(
        {
            "code": "1068",
            "definition": "Eastern Orthodox",
            "display": "Eastern Orthodox",
        }
    )
    """
    Eastern Orthodox

    Eastern Orthodox
    """

    one069 = CodeSystemConcept(
        {"code": "1069", "definition": "Episcopalian", "display": "Episcopalian"}
    )
    """
    Episcopalian

    Episcopalian
    """

    one070 = CodeSystemConcept(
        {
            "code": "1070",
            "definition": "Evangelical Covenant",
            "display": "Evangelical Covenant",
        }
    )
    """
    Evangelical Covenant

    Evangelical Covenant
    """

    one071 = CodeSystemConcept(
        {"code": "1071", "definition": "Friends", "display": "Friends"}
    )
    """
    Friends

    Friends
    """

    one072 = CodeSystemConcept(
        {"code": "1072", "definition": "Full Gospel", "display": "Full Gospel"}
    )
    """
    Full Gospel

    Full Gospel
    """

    one073 = CodeSystemConcept(
        {"code": "1073", "definition": "Methodist", "display": "Methodist"}
    )
    """
    Methodist

    Methodist
    """

    one074 = CodeSystemConcept(
        {"code": "1074", "definition": "Native American", "display": "Native American"}
    )
    """
    Native American

    Native American
    """

    one075 = CodeSystemConcept(
        {"code": "1075", "definition": "Nazarene", "display": "Nazarene"}
    )
    """
    Nazarene

    Nazarene
    """

    one076 = CodeSystemConcept(
        {"code": "1076", "definition": "Presbyterian", "display": "Presbyterian"}
    )
    """
    Presbyterian

    Presbyterian
    """

    one077 = CodeSystemConcept(
        {"code": "1077", "definition": "Protestant", "display": "Protestant"}
    )
    """
    Protestant

    Protestant
    """

    one078 = CodeSystemConcept(
        {
            "code": "1078",
            "definition": "Protestant, No Denomination",
            "display": "Protestant, No Denomination",
        }
    )
    """
    Protestant, No Denomination

    Protestant, No Denomination
    """

    one079 = CodeSystemConcept(
        {"code": "1079", "definition": "Reformed", "display": "Reformed"}
    )
    """
    Reformed

    Reformed
    """

    one080 = CodeSystemConcept(
        {"code": "1080", "definition": "Salvation Army", "display": "Salvation Army"}
    )
    """
    Salvation Army

    Salvation Army
    """

    one081 = CodeSystemConcept(
        {
            "code": "1081",
            "definition": "Unitarian Universalist",
            "display": "Unitarian Universalist",
        }
    )
    """
    Unitarian Universalist

    Unitarian Universalist
    """

    one082 = CodeSystemConcept(
        {
            "code": "1082",
            "definition": "United Church of Christ",
            "display": "United Church of Christ",
        }
    )
    """
    United Church of Christ

    United Church of Christ
    """

    class Meta:
        resource = _resource
