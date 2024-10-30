# I den här uppgiften ska du implementera funktionalitet för att konvertera
# input på nedanstående format (EXAMPLE_INPUT) till HTML.
# Input består alltid av en lista av listor, där varje sublista motsvarar en paragraf.
# Varje sublista ska alltså efter konvertering omringas av <p>...</p>
# Sublistorna består av dictionaries, som alltid innehåller en "text"-key.
# Dessutom så kan de innehålla information om formattering, genom nycklarna "bold",
# "italic" och "underline".
# Denna formattering ska översättas till HTML enligt följande:
# bold -> <strong>
# italic -> <em>
# underline -> <u>

# När man kör detta skript så printas förväntad och faktisk output från de båda 
# exempel-inputsen.


EXAMPLE_INPUT_1 = [
    [
        {"text": "Hej på "},
        {"text": "dig", "bold": True},
        {"text": "!"}
    ]
]

EXAMPLE_INPUT_2 = [
    [
        {"text": "Hej p"},
        {"text": "å ", "italic": True},
        {"text": "d", "italic": True, "bold": True},
        {"text": "ig", "bold": True},
        {"text": "!"}
    ],
    [
        {"text": "Hej på "},
        {"text": "dig", "underline": True},
        {"text": "!"}
    ]
]

EXAMPLE_INPUT_3 = [
    [
        {"text": "Hej på ", "bold": True},
        {"text": "dig", "bold": True, "underline": True},
        {"text": "!", "bold": True}
    ]
]


EXPECTED_OUTPUT_1 = "<p>Hej på <strong>dig</strong>!</p>"
EXPECTED_OUTPUT_2 = "<p>Hej p<em>å <strong>d</em>ig</strong>!</p><p>Hej på <u>dig</u>!</p>"
EXPECTED_OUTPUT_3 = "<p><strong>Hej på <u>dig</u>!</strong></p>"


def convert_to_html(input):
    output = ""

    # loop each input row in the input lists
    for inputRow in input:
        # append starting p-tag on output for current list
        output += "<p>"
        # dict containing state for if the styling tag is open 
        documentFlags = {"bold": False, "underline": False, "italic": False}

        # loop trough each dictionary containing html data in the current input row (list)
        for htmlData in inputRow:
            text = htmlData.get("text")
            # dict containing info regarding styling for current html data
            stylingTags = {"bold": htmlData.get("bold"),"underline": htmlData.get("underline"), "italic": htmlData.get("italic")}

            # adds closing tag depending on if last input has opened a tag and current input does not contain tag
            output += set_closing_tag(stylingTags, documentFlags)

            # adds opening tag if needed
            output += set_opening_tags(stylingTags, documentFlags)   
            output += text

        # closes tag if on last html data and tags are still open     
        if documentFlags.get("bold"):
            output += "</strong>"
        if documentFlags.get("italic"):
            output += "</u>"
        if documentFlags.get("underline"):
            output += "</em>"

        #append closing p-tag to output string
        output += "</p>"
    
    return output

# function for setting opening tag, checks if current html input has styling tag and if the document flag for that styling is false, and sets accordingly whilst updating flags
def set_opening_tags(stylingTags, documentFlags):
    if stylingTags.get("bold") and not documentFlags.get("bold"):
        documentFlags["bold"] = True
        return "<strong>"
    if stylingTags.get("italic") and not documentFlags.get("italic"):
        documentFlags["italic"] = True
        return "<em>"
    if stylingTags.get("underline") and not documentFlags.get("underline"):
        documentFlags["underline"] = True
        return "<u>"
    return ""

# function for setting closing tag, similar to function set_opening_tags, but instead checks if the flag is true and styling for current element if false. 
def set_closing_tag(stylingTags, documentFlags):
    if documentFlags.get("bold") and not stylingTags.get("bold"):
        documentFlags["bold"] = False
        return "</strong>"
    if documentFlags.get("underline") and not stylingTags.get("underline"):
        documentFlags["underline"] = False
        return "</u>"
    if documentFlags.get("italic") and not stylingTags.get("italic"):
        documentFlags["italic"] = False
        return "</em>"
    return ""



print(f"Expected:\t{EXPECTED_OUTPUT_1}")
print(f"Actual:\t\t{convert_to_html(EXAMPLE_INPUT_1)}")

print(f"Expected:\t{EXPECTED_OUTPUT_2}")
print(f"Actual:\t\t{convert_to_html(EXAMPLE_INPUT_2)}")

print(f"Expected:\t{EXPECTED_OUTPUT_3}")
print(f"Actual:\t\t{convert_to_html(EXAMPLE_INPUT_3)}")
