from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["OperationOutcomeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class OperationOutcomeCodes:
    """
    Operation Outcome Codes

    Operation Outcome codes used by FHIR test servers (see Implementation
file translations.xml)

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/operation-outcome
    """

    delete_multiple_matches = CodeSystemConcept(
        {
            "code": "DELETE_MULTIPLE_MATCHES",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Fout: er is meer dan één resultaat voor de conditionele delete",
                }
            ],
            "display": "Error: Multiple matches exist for the conditional delete",
        }
    )
    """
    Error: Multiple matches exist for the conditional delete

    
    """

    msg_auth_required = CodeSystemConcept(
        {
            "code": "MSG_AUTH_REQUIRED",
            "designation": [
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Autenticazione richiesta prima di usare questo servizio",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Wymagana autentykacja przed użyciem tego serwisu",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Vous devez être authentifié avant de pouvoir utiliser ce service",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "U moet zich authenticeren voor gebruik van deze service",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "使用此服务前需认证",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Debe autenticarse antes de poder usar este servicio",
                },
            ],
            "display": "You must authenticate before you can use this service",
        }
    )
    """
    You must authenticate before you can use this service

    
    """

    msg_bad_format = CodeSystemConcept(
        {
            "code": "MSG_BAD_FORMAT",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Неверный синтакс: "%s" должен быть %s',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Sintassi Errata: "%s" deve essere un %s\'',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Błąd składni: "%s" powinno być %s\'',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Erreur de Syntaxe : "%s" doit être un %s',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Verkeerde syntax: "%s" moet een %s zijn',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '句法错误: "%s" 必须是一个 %s\'',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Sintaxis Incorrecta: "%s" debe de ser un %s\'',
                },
            ],
            "display": 'Bad Syntax: "%s" must be a %s\'',
        }
    )
    """
    Bad Syntax: "%s" must be a %s'

    
    """

    msg_bad_syntax = CodeSystemConcept(
        {
            "code": "MSG_BAD_SYNTAX",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Неверный синтакс: %s",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Sintassi errata in %s",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Błąd składni w %s",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Erreur de Syntaxe dans %s",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Verkeerde syntax in %s",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "%s 中句法错误",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Sintaxis Incorrecta en %s",
                },
            ],
            "display": "Bad Syntax in %s",
        }
    )
    """
    Bad Syntax in %s

    
    """

    msg_cant_parse_content = CodeSystemConcept(
        {
            "code": "MSG_CANT_PARSE_CONTENT",
            "designation": [
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Impossibile effettuare il parsing del feed (tipo del contenuto della entry = "%s")',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Błąd parsowania (typ zawartości wejściowej = "%s")',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Impossible d'analyser le flux (type de contenu de l'entrée = \"%s\")",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Kan feed niet verwerken (contenttype inhoud = "%s")',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '无法解析feed (条目的内容类型 = "%s")',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'No se pudo parsear el feed (el tipo de contenido de la entry = "%s")',
                },
            ],
            "display": 'Unable to parse feed (entry content type = "%s")',
        }
    )
    """
    Unable to parse feed (entry content type = "%s")

    
    """

    msg_cant_parse_root = CodeSystemConcept(
        {
            "code": "MSG_CANT_PARSE_ROOT",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Не удалось разобрать данные (корневой элемент = "%s")',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Impossibile effettuare il parsing del feed (nome elemento root = "%s")',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Błąd parsowania (nazwa elementu root = "%s")',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Impossible d'analyser le flux (nom de l'élément racine = \"%s\")",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Kan feed niet verwerken (rootelementnaam = "%s")',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '无法解析feed (根元素名 = "%s")',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'No se pudo parsear el feed (nombre del elemento raiz = "%s")',
                },
            ],
            "display": 'Unable to parse feed (root element name = "%s")',
        }
    )
    """
    Unable to parse feed (root element name = "%s")

    
    """

    msg_created = CodeSystemConcept(
        {
            "code": "MSG_CREATED",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Nieuwe resource gemaakt",
                }
            ],
            "display": "New resource created",
        }
    )
    """
    New resource created

    
    """

    msg_date_format = CodeSystemConcept(
        {
            "code": "MSG_DATE_FORMAT",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Значение Date %s в неверном формате (требуется Xml Date формат)",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Il valore %s per la data non è nel formato corretto (richiesto il Formato Data Xml)",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Niepoprawny format wartości daty %s (wymagany format XML)",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Le format de la date %s est incorrect (format Date Xml attendu)",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "De Datum-waarde %s heeft niet de juiste structuur (Xml Date vereist)",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "日期的值 %s 格式不正确 (要求是Xml Date格式)",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "El valor de la fecha %s no está en el formato correcto (se requiere un formato de fecha Xml)",
                },
            ],
            "display": "The Date value %s is not in the correct format (Xml Date Format required)",
        }
    )
    """
    The Date value %s is not in the correct format (Xml Date Format required)

    
    """

    msg_deleted = CodeSystemConcept(
        {
            "code": "MSG_DELETED",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Данный ресурс был удалён",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Questa risorsa è stata cancellata",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Ten zasób został usunięty",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "La ressource a été supprimée",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Deze resource is verwijderd",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "该资源已删除",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Este recurso ha sido borrado",
                },
            ],
            "display": "This resource has been deleted",
        }
    )
    """
    This resource has been deleted

    
    """

    msg_deleted_done = CodeSystemConcept(
        {
            "code": "MSG_DELETED_DONE",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Ресурс удалён",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Risorsa cancellata",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Zasób usunięto",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Ressource supprimée",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Resource verwijderd",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "资源已删除",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Recurso borrado",
                },
            ],
            "display": "Resource deleted",
        }
    )
    """
    Resource deleted

    
    """

    msg_deleted_id = CodeSystemConcept(
        {
            "code": "MSG_DELETED_ID",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Ресурс "%s" был удалён',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'La risorsa "%s" è stata eliminata',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Zasób "%s" został usunięty',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'La ressource "%s" a été supprimée',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'De resource "%s" is verwijderd',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '资源 "%s" 已被删除',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'El recurso "%s" ha sido borrado',
                },
            ],
            "display": 'The resource "%s" has been deleted',
        }
    )
    """
    The resource "%s" has been deleted

    
    """

    msg_duplicate_id = CodeSystemConcept(
        {
            "code": "MSG_DUPLICATE_ID",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Дублирующий Id %s для типа ресурса %s",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id %s duplicato per il tipo di risorsa %s",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Zdublowany identyfikator %s dla zasobu typu %s",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id %s en double pour le type de ressource %s",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Duplicaat-id %s voor resourcetype %s",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ID %s 重复（资源类型 %s）",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id %s duplicada para el recurso de tipo %s",
                },
            ],
            "display": "Duplicate Id %s for resource type %s",
        }
    )
    """
    Duplicate Id %s for resource type %s

    
    """

    msg_error_parsing = CodeSystemConcept(
        {
            "code": "MSG_ERROR_PARSING",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Ошибка синтаксического разбора ресурса Xml (%s)",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Errore nel parsing della risorsa Xml (%s)",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Błąd w trakcie parsowania zasobu XML (%s)",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Erreur d'analyse de la ressource Xml (%s)",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Fout in verwerking resource Xml (%s)",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "解析资源Xml时出错 (%s)",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Error parseando el recurso Xml (%s)",
                },
            ],
            "display": "Error parsing resource Xml (%s)",
        }
    )
    """
    Error parsing resource Xml (%s)

    
    """

    msg_id_invalid = CodeSystemConcept(
        {
            "code": "MSG_ID_INVALID",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Id "%s" содержит недопустимые символы "%s"',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'L\'\'Id "%s" ha un carattere non valido: "%s"',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Identyfikator "%s" zawiera niepoprawny znak "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Id "%s" possède un caractère invalide "%s"',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Id "%s" heeft een ongeldig teken "%s"',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'ID "%s" 带有非法字符: "%s"',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'El Id "%s" contiene el caracter inválido "%s"',
                },
            ],
            "display": 'Id "%s" has an invalid character "%s"',
        }
    )
    """
    Id "%s" has an invalid character "%s"

    
    """

    msg_id_too_long = CodeSystemConcept(
        {
            "code": "MSG_ID_TOO_LONG",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Недопустимая длина Id "%s" (ограничение 36)',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Id "%s" troppo lunga (limite di lunghezza: 36)',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Identyfikator "%s" jest zbyt długi (limit długości 36)',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Id "%s" trop long (la longueur limite est 36)',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Id "%s" te lang (max lengte 36)',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Id "%s" 过长 (长度限制: 36)',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'El Id "%s" es demasiado largo (limite de longitud: 36)',
                },
            ],
            "display": 'Id "%s" too long (length limit 36)',
        }
    )
    """
    Id "%s" too long (length limit 36)

    
    """

    msg_invalid_id = CodeSystemConcept(
        {
            "code": "MSG_INVALID_ID",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id не принято",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id non accettato",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Identyfikator nie zaakceptowany",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id non accepté",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id niet geaccepteerd",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id不被接受",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id no aceptada",
                },
            ],
            "display": "Id not accepted",
        }
    )
    """
    Id not accepted

    
    """

    msg_json_object = CodeSystemConcept(
        {
            "code": "MSG_JSON_OBJECT",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Json Source для ресурса должен начинаться с объекта",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Il sorgente Json di una risorsa dovrebbe iniziare con un oggetto",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Źródło json dla zasobu powinno rozpoczynać się od obiektu",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "La source Json pour une ressource doit commencer par un objet",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Json Source van een resource moeten beginnen met een object",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "资源的Json源应以一个object开始",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "La fuente Json para un recurso debería empezar con un objeto",
                },
            ],
            "display": "Json Source for a resource should start with an object",
        }
    )
    """
    Json Source for a resource should start with an object

    
    """

    msg_local_fail = CodeSystemConcept(
        {
            "code": "MSG_LOCAL_FAIL",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Невозможно определить локальную ссылку на ресурс %s",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Impossibile risolvere il riferimento locale alla risorsa %s",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Zasób wskazywany przez loklaną referencję %s nie został odnaleziony",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Impossible de résourdre la référence locale à la ressource %s",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "De resource met lokale referentie %s is niet gevonden",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "无法解析对资源 %s 的本地引用",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Imposible resolver la referencia al recurso %s",
                },
            ],
            "display": "Unable to resolve local reference to resource %s",
        }
    )
    """
    Unable to resolve local reference to resource %s

    
    """

    msg_no_exist = CodeSystemConcept(
        {
            "code": "MSG_NO_EXIST",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Ресурс Id "%s" не существует',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'La risorsa con Id "%s" non esiste',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Zasób o identyfikatorze "%s" nie istnieje',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "La ressource avec l'Id \"%s\" n'existe pas",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Resource-id "%s" bestaat niet',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '资源Id "%s"不存在',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'El recurso con Id "%s" no existe',
                },
            ],
            "display": 'Resource Id "%s" does not exist',
        }
    )
    """
    Resource Id "%s" does not exist

    
    """

    msg_no_match = CodeSystemConcept(
        {
            "code": "MSG_NO_MATCH",
            "designation": [
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nessuna Risorsa soddisfa la query "%s"',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Geen resource gevonden met query "%s"',
                },
            ],
            "display": 'No Resource found matching the query "%s"',
        }
    )
    """
    No Resource found matching the query "%s"

    
    """

    msg_no_module = CodeSystemConcept(
        {
            "code": "MSG_NO_MODULE",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Модуль для обработки запроса "%s" не найден',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Impossibile trovare un modulo per gestire la richiesta "%s"',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nie można odnaleźć modułu, aby obsłużyć żądanie "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Aucun module disponible pour traiter la requête "%s"',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Er kon geen module worden gevonden om verzoek "%s" te verwerken',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '无法找到处理请求"%s"的模块',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'No se encontró un modulo que gestione la petición "%s"',
                },
            ],
            "display": 'No module could be found to handle the request "%s"',
        }
    )
    """
    No module could be found to handle the request "%s"

    
    """

    msg_no_summary = CodeSystemConcept(
        {
            "code": "MSG_NO_SUMMARY",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Отсутствует Summary для данного ресурса",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Nessun riepilogo per questa risorsa",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Brak podsumowania (Summary) dla tego zasobu",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Aucun résumé disponible pour cette ressource",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Geen samenvatting voor deze resource",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "该资源无summary",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "No existe un resumen para este recurso",
                },
            ],
            "display": "No Summary for this resource",
        }
    )
    """
    No Summary for this resource

    
    """

    msg_op_not_allowed = CodeSystemConcept(
        {
            "code": "MSG_OP_NOT_ALLOWED",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Операция %s недопустима для ресурса %s (по причине локальной конфигурации)",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Operazione %s non consentita per la risorsa %s (a causa di configurazioni locali)",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Niedozwolona operacja %s dla zasobu %s (ze względu na lokalną konfigurację)",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "L'opération %s n'est pas permise pour la ressource %s (à cause de la configuration locale)",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Bewerking %s niet toegestaan voor resource %s (vanwege lokale configuratie)",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "操作 %s 不允许，对于资源 %s (由于本地配置)",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Operación %s no permitida para el recurso %s (debido a la configuración local)",
                },
            ],
            "display": "Operation %s not allowed for resource %s (due to local configuration)",
        }
    )
    """
    Operation %s not allowed for resource %s (due to local configuration)

    
    """

    msg_param_chained = CodeSystemConcept(
        {
            "code": "MSG_PARAM_CHAINED",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Неизвестое вложенное наименование параметра "%s"',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nome di parametro concatenato sconosciuto: "%s"',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nieznana nazwa parametru powiązanego "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nom du paramètre chainé inconnu : "%s"',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Onbekende geschakelde parameternaam "%s"',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '未知的链式参数名: "%s"',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nombre de parametro encadenado desconocido: "%s"',
                },
            ],
            "display": 'Unknown chained parameter name "%s"',
        }
    )
    """
    Unknown chained parameter name "%s"

    
    """

    msg_param_invalid = CodeSystemConcept(
        {
            "code": "MSG_PARAM_INVALID",
            "designation": [
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Il contenuto del Parametro "%s" non è valido',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Waarde van parameter "%s" is ongeldig',
                },
            ],
            "display": 'Parameter "%s" content is invalid',
        }
    )
    """
    Parameter "%s" content is invalid

    
    """

    msg_param_modifier_invalid = CodeSystemConcept(
        {
            "code": "MSG_PARAM_MODIFIER_INVALID",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Modifier van parameter "%s" is ongeldig',
                }
            ],
            "display": 'Parameter "%s" modifier is invalid',
        }
    )
    """
    Parameter "%s" modifier is invalid

    
    """

    msg_param_no_repeat = CodeSystemConcept(
        {
            "code": "MSG_PARAM_NO_REPEAT",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Параметр "%s" не может быть повторён',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Non � consentito ripetere il parametro "%s"',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Parametr "%s" nie może zostać powtórzony',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Le paramètre "%s" ne peut pas être répété',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Parameter "%s" mag niet herhalen',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '参数"%s"不可重复',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'No se permite la repetición del parámetro "%s"',
                },
            ],
            "display": 'Parameter "%s" is not allowed to repeat',
        }
    )
    """
    Parameter "%s" is not allowed to repeat

    
    """

    msg_param_unknown = CodeSystemConcept(
        {
            "code": "MSG_PARAM_UNKNOWN",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Параметр "%s" не понят',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Parametro "%s" non riconosciuto',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Niezrozumiały parametr "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Paramètre "%s" non reconnu',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Parameter "%s" onbekend',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '无法理解参数"%s"',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Parámetro "%s" no reconocido',
                },
            ],
            "display": 'Parameter "%s" not understood',
        }
    )
    """
    Parameter "%s" not understood

    
    """

    msg_resource_example_protected = CodeSystemConcept(
        {
            "code": "MSG_RESOURCE_EXAMPLE_PROTECTED",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Ресурс с идентификатором "example" не может быть удалён (для случаев тестирования/обучения)',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Le Risorse aventi l\'identità "example" non possono essere cancellate (per finalità di test/formazione)',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Zasoby oznaczone jako "example" nie mogą zostać usunięte (dla celów testów/szkoleń)',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Les ressources ayant l\'identité "example" ne peuvent pas être supprimées (utilisées pour les tests/formations)',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Resources met identiteit "voorbeeld" kunnen niet worden verwijderd (ten behoeve van testen/training)',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '以"example" 为ID的资源不能被删除 (用于测试/培训)',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Recursos con la identidad "example" no pueden ser borrados (son usados para pruebas/entrenamiento)',
                },
            ],
            "display": 'Resources with identity "example" cannot be deleted (for testing/training purposes)',
        }
    )
    """
    Resources with identity "example" cannot be deleted (for testing/training purposes)

    
    """

    msg_resource_id_fail = CodeSystemConcept(
        {
            "code": "MSG_RESOURCE_ID_FAIL",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "невозможно выделить идентификатор ресурса",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "impossibile allocare l''id della risorsa",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "nie można nadać identyfikatora zasobu",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "impossible d'allouer l'id de la ressource",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "kan geen resource-id reserveren",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "无法分配资源ID",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "imposible encontrar el id del recurso",
                },
            ],
            "display": "unable to allocate resource id",
        }
    )
    """
    unable to allocate resource id

    
    """

    msg_resource_id_mismatch = CodeSystemConcept(
        {
            "code": "MSG_RESOURCE_ID_MISMATCH",
            "designation": [
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Problème de correspondance d'Id de la Ressource",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Resource ID's komen niet overeen",
                },
            ],
            "display": "Resource Id Mismatch",
        }
    )
    """
    Resource Id Mismatch

    
    """

    msg_resource_id_missing = CodeSystemConcept(
        {
            "code": "MSG_RESOURCE_ID_MISSING",
            "designation": [
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id della Risorsa mancante",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Id de la Ressource manquante",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Resource ID ontbreekt",
                },
            ],
            "display": "Resource Id Missing",
        }
    )
    """
    Resource Id Missing

    
    """

    msg_resource_not_allowed = CodeSystemConcept(
        {
            "code": "MSG_RESOURCE_NOT_ALLOWED",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Для данной операции отправка ресурса недопустима",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Non è consentito sottomettere una risorsa per questa operazione",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Nie można zgłosić zasobu dla tej operacji",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Non autorisé à soumettre une ressource pour cette opération",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Niet toegestaan om een resource in te dienen voor deze bewerking",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "该操作不允许提交资源",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "No se permite el envío de un recurso para esta operación",
                },
            ],
            "display": "Not allowed to submit a resource for this operation",
        }
    )
    """
    Not allowed to submit a resource for this operation

    
    """

    msg_resource_required = CodeSystemConcept(
        {
            "code": "MSG_RESOURCE_REQUIRED",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Требуется ресурс",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "E'' richiesta una risorsa",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Zasób jest wymagany",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Une ressource est requise",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Een resource is verplicht",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "必须提供一个资源",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Se requiere un recurso",
                },
            ],
            "display": "A resource is required",
        }
    )
    """
    A resource is required

    
    """

    msg_resource_type_mismatch = CodeSystemConcept(
        {
            "code": "MSG_RESOURCE_TYPE_MISMATCH",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Несоответствие типа ресурса",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Tipo Risorsa non corrispondente",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Niepoprawny typ zasobu",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Type de ressource incorrect",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Verkeerd resourcetype",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "资源类型不匹配",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Los Tipos de los recursos no coinciden",
                },
            ],
            "display": "Resource Type Mismatch",
        }
    )
    """
    Resource Type Mismatch

    
    """

    msg_sort_unknown = CodeSystemConcept(
        {
            "code": "MSG_SORT_UNKNOWN",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Неизвестное имя параметра сортировки "%s"',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nome del parametro di ordinamento "%s" non riconosciuto',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nieznany parametr sortowania "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nom du paramètre de tri inconnu "%s"',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Onbekende parameternaam "%s" voor sortering',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '未知的排序参数名称"%s"',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nombre del parámetro de ordenación "%s" desconocido',
                },
            ],
            "display": 'Unknown sort parameter name "%s"',
        }
    )
    """
    Unknown sort parameter name "%s"

    
    """

    msg_transaction_duplicate_id = CodeSystemConcept(
        {
            "code": "MSG_TRANSACTION_DUPLICATE_ID",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Дублирующий идентификатор в транзакции: %s",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Zdublowany identyfikator w transakcji: %s",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Identifiant en double dans la transaction : %s",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Dubbele identificatie in transactie: %s",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "事务中存在重复Id: %s",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Identificador duplicado en la transacción: %s",
                },
            ],
            "display": "Duplicate Identifier in transaction: %s",
        }
    )
    """
    Duplicate Identifier in transaction: %s

    
    """

    msg_transaction_missing_id = CodeSystemConcept(
        {
            "code": "MSG_TRANSACTION_MISSING_ID",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Отсутствует идентификатор в транзакции - требуется entry.id",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Brak identyfikatora w transakcji - należy podać entry.id",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Identifiant manquant dans la transaction - un élément entry.id doit être fourni",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Ontbrekende identificatie in transactie - entry.id is verplicht",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "事务中缺少Id - 必须提供一个entry.id",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Identificador de la transacción no encontrado - se debe proporcionar un entry.id",
                },
            ],
            "display": "Missing Identifier in transaction - an entry.id must be provided",
        }
    )
    """
    Missing Identifier in transaction - an entry.id must be provided

    
    """

    msg_unhandled_node_type = CodeSystemConcept(
        {
            "code": "MSG_UNHANDLED_NODE_TYPE",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Не обработанный xml узел "%s"',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Tipo di nodo Xml non gestito "%s"',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nieobsługiwany typ węzła XML "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Type de noeud xml "%s" non traité',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Kan xml nodetype "%s" niet verwerken',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '未处理的XML节点类型"%s"',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Tipo de nodo Xml no soportado "%s"',
                },
            ],
            "display": 'Unhandled xml node type "%s"',
        }
    )
    """
    Unhandled xml node type "%s"

    
    """

    msg_unknown_content = CodeSystemConcept(
        {
            "code": "MSG_UNKNOWN_CONTENT",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Неизвестный контент (%s) в %s",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Contenuto Sconosciuto (%s) at %s",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Nieznana zawartość (%s) dla %s",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Contenu inconnu (%s) à %s",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Onbekende content (%s) at %s",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "未知内容 (%s) 位于 %s",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Contenido desconocido (%s) en %s",
                },
            ],
            "display": "Unknown Content (%s) at %s",
        }
    )
    """
    Unknown Content (%s) at %s

    
    """

    msg_unknown_operation = CodeSystemConcept(
        {
            "code": "MSG_UNKNOWN_OPERATION",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "неизвестная операция FHIR http",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "operazione http FHIR sconosciuta",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "nieznana operacja FHIR http",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "operation http FHIR inconnue",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "onbekende FHIR http operation",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "未知的FHIR HTTP操作",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Operación http FHIR desconocida",
                },
            ],
            "display": "unknown FHIR http operation",
        }
    )
    """
    unknown FHIR http operation

    
    """

    msg_unknown_type = CodeSystemConcept(
        {
            "code": "MSG_UNKNOWN_TYPE",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Тип ресурса "%s" не распознан',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Tipo di Risorsa "%s" non riconosciuto',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Nie rozpoznany typ zasobu: "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Type de ressource "%s" non reconnu',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Resourcetype "%s" niet herkend',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '资源类型"%s"未识别',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Tipo de Recurso "%s" no reconocido',
                },
            ],
            "display": 'Resource Type "%s" not recognised',
        }
    )
    """
    Resource Type "%s" not recognised

    
    """

    msg_updated = CodeSystemConcept(
        {
            "code": "MSG_UPDATED",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "существующий ресурс обновлён",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "risorsa esistente aggiornata",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "uaktualniono istniejący zasób",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "ressource existante mise à jour",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "bestaande resource updated",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "已有资源被更新",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Recurso existente actualizado",
                },
            ],
            "display": "existing resource updated",
        }
    )
    """
    existing resource updated

    
    """

    msg_version_aware = CodeSystemConcept(
        {
            "code": "MSG_VERSION_AWARE",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Для данного ресурса необходимы обновления с учётом версии",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Questa risorsa richiede aggiornamenti per versione",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Uaktualnienia zakładające wersjonowanie są wymagane dla tego zasobu",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Des mises à jour en relation avec la version sont requises pour cette ressource",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Versie-bewuste updates zijn vereist voor deze resource",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "该资源的更新必须针对版本",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Este recurso requiere actualizaciones en base a versiones",
                },
            ],
            "display": "Version aware updates are required for this resource",
        }
    )
    """
    Version aware updates are required for this resource

    
    """

    msg_version_aware_conflict = CodeSystemConcept(
        {
            "code": "MSG_VERSION_AWARE_CONFLICT",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Конфликт обновления (текущая версия сервера = "%s", указанная версия клиента = "%s")',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Conflitto nell\'\'aggiornamento (attuale = "%s", quotato = "%s")',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Konflikt podczas uaktualnienia (obecna wersja na serwerze = "%s", wersja wskazana przez klienta = "%s")',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Conflit de mise à jour (version courante du serveur = "%s", version référencée du client = "%s")',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Updateconflict (huidige serverversie = "%s", opgegeven clientversie = "%s")',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '更新冲突 (服务器当前版本 = "%s", 客户端引用的版本 = "%s")',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Conflicto de actualizaciones (versión actual del servidor = "%s", versión del cliente referenciada = "%s")',
                },
            ],
            "display": 'Update Conflict (server current version = "%s", client version referenced = "%s")',
        }
    )
    """
    Update Conflict (server current version = "%s", client version referenced = "%s")

    
    """

    msg_version_aware_url = CodeSystemConcept(
        {
            "code": "MSG_VERSION_AWARE_URL",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "URL для указанной версии не распознан",
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "URL specifico alla versione non riconosciuto",
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Nie rozpoznany URL specyficzny dla wersji",
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "URL spécifique à une version non reconnue",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Versie-specifieke URL niet herkend",
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "未识别特定版本的URL",
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "URL especifica de la versión no reconocida",
                },
            ],
            "display": "Version specific URL not recognised",
        }
    )
    """
    Version specific URL not recognised

    
    """

    msg_wrong_ns = CodeSystemConcept(
        {
            "code": "MSG_WRONG_NS",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Dit lijkt geen FHIR element of resource te zijn (verkeerde namespace "%s")',
                }
            ],
            "display": 'This does not appear to be a FHIR element or resource (wrong namespace "%s")',
        }
    )
    """
    This does not appear to be a FHIR element or resource (wrong namespace "%s")

    
    """

    search_multiple = CodeSystemConcept(
        {
            "code": "SEARCH_MULTIPLE",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Ошибка: множественные совпадения для %s с параметрами поиска "%s"',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Errore: Trovate corrispondenze multiple per %s parametri di ricerca "%s"',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Błąd: Istnieją wielokrotne dopasowania dla %s parametrów wyszukiwania "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Erreur : Plusieurs correspondances existent pour ce paramètre de recherche %s",
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Fout: er is meer dan één resultaat voor %s zoekparameters "%s"',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '错误: 对于 %s 搜索的参数 "%s"存在多个匹配',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Error: Multiples ocurrencias existen para %s parametros de búsqueda "%s"',
                },
            ],
            "display": 'Error: Multiple matches exist for %s search parameters "%s"',
        }
    )
    """
    Error: Multiple matches exist for %s search parameters "%s"

    
    """

    search_none = CodeSystemConcept(
        {
            "code": "SEARCH_NONE",
            "designation": [
                {
                    "language": "ru",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Ошибка: обрабатываемых результатов поиска для %s с параметрами поиска "%s" не найдено',
                },
                {
                    "language": "it",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Errore: non è stato trovato alcun parametro di ricerca processabile per %s parametri di ricerca "%s"',
                },
                {
                    "language": "pl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Błąd: Niewykonalne wyszukiwanie dla %s parametrów wyszukiwania "%s"',
                },
                {
                    "language": "fr",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Erreur : aucune recherche trouvée pour les paramètres %s "%s"',
                },
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Fout: geen verwerkbare zoekactie gevonden voor %s zoekparameters "%s"',
                },
                {
                    "language": "zh",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": '错误: 对%s搜索参数"%s"未找到可处理的搜索',
                },
                {
                    "language": "es",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": 'Error: no se encontro una búsqueda apropiada para %s parametros de búsqueda "%s"',
                },
            ],
            "display": 'Error: no processable search found for %s search parameters "%s"',
        }
    )
    """
    Error: no processable search found for %s search parameters "%s"

    
    """

    update_multiple_matches = CodeSystemConcept(
        {
            "code": "UPDATE_MULTIPLE_MATCHES",
            "designation": [
                {
                    "language": "nl",
                    "use": {
                        "code": "display",
                        "system": "http://terminology.hl7.org/CodeSystem/designation-usage",
                    },
                    "value": "Fout: er is meer dan één resultaat voor de conditionele update",
                }
            ],
            "display": "Error: Multiple matches exist for the conditional update",
        }
    )
    """
    Error: Multiple matches exist for the conditional update

    
    """

    class Meta:
        resource = _resource
