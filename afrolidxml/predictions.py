import xmltodict


def write_predicted_languages_xml(predicted_langs, output_file):
    with open(output_file, "w") as file:
        file.write(predicted_languages_to_xml(predicted_langs))


def predicted_languages_to_xml(predicted_langs):
    # Reformat dict returned from Afrolid to make it easier to format as XML
    formatted_langs = []

    for lang_code in predicted_langs:
        predicted_langs[lang_code]["code"] = lang_code
        formatted_langs.append(predicted_langs[lang_code])

    # Format language data as XML
    languages_data = {"@sourcetool": "AfroLID", "language": formatted_langs}
    return xmltodict.unparse({"languages": languages_data}, pretty=True)
